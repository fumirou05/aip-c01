# AWS／ローカル GenAI統合ラボ

最終確認日: 2026-09-21

## 目的

AIP-C01の判断力を、ローカルの再現可能な実験とAWS Managed serviceの実挙動を往復して身につける。架空企業「Example Commerce」の社内ヘルプデスクを段階的に構築し、単にAPIを成功させるのではなく、要件、IAM、失敗処理、Safety、観測性、評価、コスト、削除までを1つのLifecycleとして扱う。

```text
                         +-- CloudWatch / CloudTrail / Cost --+
                         |                                     |
User -> API -> Safety -> Router -> Retrieval -> Amazon Bedrock +-> Validation
                  |          |          |             |
                  +---------- Local deterministic baseline ----+
                                      |
                                  Evaluation
```

ローカル版は大量の異常系、回帰Test、原因切り分けを安価に反復する比較基準である。AWS版ではModel responseの揺らぎ、IAM評価、Service error、Region／Quota、Metric／Log、従量料金など、Stubでは再現できない境界を観測する。AWSサービスをローカルへ再実装することは目的にしない。

## 前提

- Python 3.10以上、標準ライブラリ
- AWSアカウントとAWS CLI
- IAM Identity Centerまたは短期Credentialを優先し、Access keyをRepositoryへ保存しない
- Bedrockを利用できるRegionと、利用予定ModelへのAccessを実施日に確認する
- Datasetはすべて架空。実在する個人情報、機密情報、顧客Dataを送信しない

## コストガードレール

月間AWS利用料は**5,000円程度まで**を上限目安とする。これは使い切る目標ではない。

| 枠 | 金額 | 運用 |
|---|---:|---|
| 計画実行枠 | 4,000円 | Model invocation、Guardrails、短時間のKnowledge Bases、Log／評価など |
| 安全余裕 | 1,000円 | 料金反映の遅延、為替・税、削除漏れ、見積り差へのReserve |

開始前に次を満たす。

- AWS Budgetsへ月5,000円相当のCost budgetを作り、Actualの50%・80%・100%とForecastの80%・100%を通知する
- 4,000円到達または到達予測を新規有料実験の停止線にする。Budget通知だけではResourceやAPI呼出しが停止しない前提で運用する
- 当日の[Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)、各Service料金、Region、Model availability、Quota、Free Tier／Credit条件を確認する
- 実験ごとに最大Request数、最大Token、最大実行時間、作成Resource、削除手順、最悪時概算を先に `artifacts/cost-log.md` へ書く
- 全Resourceに `Project=aip-c01-lab`、`Purpose=study`、`ExpiresOn=YYYY-MM-DD` を付ける。Tag非対応Resourceは同じ識別子を名前へ含める
- On-demand／Serverless、少量Dataset、短時間実行を優先する

次のいずれかで有料実験を止め、Cost Explorer／BillingとResource一覧を確認する。

- 実績または予測が4,000円へ到達した
- 見積りにないService／Resourceの料金が発生した
- Resourceを削除できない、または削除済みと確認できない
- Request数、Token数、実行時間の上限を超えた

Provisioned Throughput、常時稼働SageMaker endpoint、NAT Gateway、大きなOpenSearch／Aurora構成は、この予算内で必要性と削除まで説明できない限り作成しない。AWS Budgets、料金表、Cost Explorerの更新には時間差があり得るため、安全余裕を使って追加実験を正当化しない。

## 学習Level

各Taskで必要な最小Levelまで進める。Level 0だけでTaskを完了せず、全Domainを通してLevel 1以上のEvidenceを残す。

| Level | 実行場所 | 学ぶこと | Evidence |
|---|---|---|---|
| 0: Baseline | ローカル | Interface、決定的Test、異常系、評価式 | Test結果、期待値、Trace |
| 1: Runtime | AWS | Bedrock Converse／Invoke、Model parameter、Service error、Usage | Sanitized request、Response metadata、呼出回数、概算 |
| 2: Managed controls | AWS | Guardrails、IAM、CloudWatch／CloudTrail、Prompt管理 | Policy、Block結果、Metric／Event、権限Error |
| 3: Managed RAG | AWS | S3 Data source、Knowledge Bases、同期、検索、Citation | Resource構成、同期結果、検索評価、削除確認 |
| 4: Operations | ローカル＋AWS | 評価、障害注入、Cost／Latency／品質のTrade-off | 比較Report、Runbook、Cost log |

Level 3はVector Storeなどの料金を当日見積り、4,000円の実行枠内で作成から削除まで完結できる場合に実施する。条件を満たせない場合はLevel 1・2の実測とローカルRAGを組み合わせ、未確認事項を明記する。

## 最初の確認

Repository rootで実行する。

```bash
python3 labs/local-genai/scripts/check_setup.py
python3 -m unittest discover -s labs/local-genai/tests -v
aws sts get-caller-identity
aws configure get region
```

`aws sts get-caller-identity` の出力は成果物へ貼らない。Account、ARNなどをEvidenceに残す場合はMaskする。続いて [`aws/README.md`](aws/README.md) のPreflightを完了し、`artifacts/cost-log-template.md` を `artifacts/cost-log.md` として使う。

## 用意されているもの

| Path | 内容 | 主に使うTask |
|---|---|---|
| `config/model-catalog.json` | 能力、Latency、Costが異なる架空Model | D1-02、D4-01 |
| `data/knowledge-base/` | Helpdesk用の架空規程とMetadata | D1-03〜D1-05 |
| `data/evaluation/golden.jsonl` | Question、期待Fact、期待Source | D1-06、D5-01 |
| `data/security/adversarial.jsonl` | Prompt attack、PII、権限越境Test | D3-01、D3-02 |
| `data/faults/scenarios.json` | 診断対象の5故障 | D2-04、D4-03、D5-02 |
| `prompts/system-v1.txt` | 改善前のSystem prompt | D1-06 |
| `schemas/tools.json` | Tool schemaの出発点 | D2-01 |
| `aws/README.md` | AWS実行RunbookとResource選定 | 全Domain |
| `artifacts/_template.md` | 設計・実験成果物の共通Template | 全Domain |
| `artifacts/cost-log-template.md` | 見積り、実績、削除確認 | AWS実機Task |
| `artifacts/incident-report-template.md` | 障害記録Template | D5-02 |

## 段階的に作る構成

| 段階 | ローカル | AWS | 主な学習 |
|---|---|---|---|
| FM選定 | Model catalog、Stub | Bedrock On-demand inference | Model ID、parameter、Token、Latency、Error |
| RAG | Chunking、簡易検索 | S3＋Knowledge Bases（予算条件付き） | Data source、IAM、同期、検索、Citation |
| Safety | 決定的Filter | Bedrock Guardrails | Block／Mask、False positive、Layering |
| Integration | API／QueueのSimulation | 必要最小限のLambda／SQS等 | Retry、Idempotency、DLQ、権限境界 |
| Observability | 構造化Log、Metric集計 | CloudWatch／CloudTrail | Correlation、監査、Sensitive data抑制 |
| Evaluation | Golden／Adversarial runner | 少量の実Model比較 | 品質、Safety、Latency、CostのTrade-off |

## 実装するModule

各Moduleは対応Taskで作成し、AWS SDK／CLIを直接呼ぶ部分とDomain logicを分離する。これにより同じTest caseをLocal adapterとAWS adapterへ流せる。

| 推奨Path | 責務 | 対応Task |
|---|---|---|
| `src/ingest.py` | Validation、Normalization、Chunking、Index更新 | D1-03、D1-04 |
| `src/retrieval.py` | Keyword／Vector検索、Filter、Ranking | D1-05 |
| `src/prompting.py` | Prompt version、変数、出力Schema | D1-06 |
| `src/model_router.py` | 要件別Model選択、Fallback | D1-02、D2-04 |
| `src/bedrock_adapter.py` | Converse／Invoke、Timeout、Retry、Usage抽出 | D1-02、D2-04 |
| `src/agent.py` | State、Tool loop、停止条件、Approval | D2-01 |
| `src/api.py` | 同期／Streaming、Validation、Retry | D2-04、D2-05 |
| `src/safety.py` | 入出力Filter、PII redaction、Policy | D3-01、D3-02 |
| `src/telemetry.py` | Metric、構造化Log、Trace | D3-03、D4-03 |
| `src/evaluate.py` | Golden、RAG、Agent、Safety評価 | D5-01 |

ローカルのVector相当検索は、標準ライブラリで実装できるTF-IDFまたはToken overlapでよい。Embedding品質を再現しないため、AWSで少量の実検索を行い差を測る。Local Model responseはFixtureまたは決定的なStubとし、回帰Testを安定させる。

## 1回のAWS実験手順

1. **Plan**: 仮説、合格条件、最大Request／Token／時間、見積り、対象Region、Resource、削除手順を書く
2. **Preflight**: Caller identity、Region、残予算、料金、Quota、最小権限、Datasetが架空であることを確認する
3. **Deploy**: 共通TagとExpiryを付け、最小構成だけを作る
4. **Exercise**: 正常系1件、異常系2件を上限内で実行し、秘密・PIIを除いたEvidenceを保存する
5. **Compare**: Local baselineと品質、Latency、Error、観測性、責任分界を比較する
6. **Destroy**: 作成一覧と逆順に削除し、Console／CLIで残存Resourceがないことを確認する
7. **Record**: 概算、Cost Explorerで後日確認した実績、差分、削除時刻、次回改善をCost logへ追記する

## 実装規約

- 1つの変更につき正常系1件、異常系2件以上のTestを追加する
- Random値を使う場合はSeedを固定する。実Modelの非決定性は複数回測定と許容範囲で扱う
- Logへ生のPII、秘密、完全なPrompt／Response、Account ID、Credentialを出さない
- Timeout、Retry上限、Agent step上限、Token上限、AWS Request上限を必ず設定する
- Retryで課金が増えることをCost modelへ含め、無制限Retryを禁止する
- Test fixtureと評価Datasetを同じ目的で使い回さない
- 成果物には公式URL、確認日、採用案、却下案、制約、AWS実測、概算／実績、削除確認を残す

## 公式根拠

- [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)
- [Model support by AWS Region](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html)
- [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [Analyzing your costs with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
- [Data protection in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)
- [CloudTrail logging for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html)

料金、Region、Model、Quota、Free Tier／Creditの公式情報は実施日に再確認する。
