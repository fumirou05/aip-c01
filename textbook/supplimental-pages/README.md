# Supplimental pages 目次

各literal pageの公式内容を、AIP-C01の試験で要件から方式を選び、その理由とトレードオフを説明できる理解へつなぐ補助教材の作成予定一覧。

最終見直し日: 2026-09-22  
状態: 22ページ中9ページを作成・レビュー済み。Domain 1の6ページは横断監査済み。リンク付きのファイル名は本文作成済みで、コード表記のファイル名は作成予定。

本文作成時は[`templates/supplimental-page.md`](../templates/supplimental-page.md)を出発点にする。テンプレートより内容の正確さと理解しやすさを優先する。

## 方針

補足章は、既存の疑問、学びログ、誤答を集めたFAQではない。次の順序で範囲を決める。

1. 対応するliteral pageを定める
2. そのliteral pageが扱う公式Task・Skillを確認する
3. 試験で必要な「概念の関係」「比較軸」「要件からの選択」「不適切な選択肢を除外する理由」を抽出する
4. 公式説明を変更しない範囲で、図、たとえ、比較表、短いシナリオを加える

既存のノート、学びログ、間違い記録は、理解度の確認や本文公開後の改善には利用できる。ただし、それらに記録された疑問の有無によって章の追加・削除や収録範囲を決めない。

## 章の書き方

各ページは次の順にする。

1. 対応するliteral page、Task・Skill
2. この補足で身につける試験上の判断
3. 前提となる概念と、概念同士の関係
4. 要件から方式を選ぶための比較軸
5. 短い試験シナリオと判断過程
6. 他の方式を選ばない条件
7. セキュリティ、可用性、性能、コストの注意点
8. 公式根拠と、補助的な説明の区別

個別の疑問への回答、ラボ手順、個人の学習履歴は本文の中心にしない。試験範囲外の一般論は、Task・Skillの理解に必要な最小限にする。

## 第0部: 試験範囲と学習の入口

| 予定ファイル | 対応するliteral page | 試験理解を補助する要素 | 対応Task |
|---|---|---|---|
| [`00-01-exam-guide-and-scope.md`](00-01-exam-guide-and-scope.md) | [`00-01-exam-guide-and-scope.md`](../literal-pages/00-01-exam-guide-and-scope.md) | Domain、Task、Skill、対象サービスの関係、範囲内／範囲外を見分ける考え方、サービス名暗記ではなくTaskから学ぶ方法 | PREP-01 |
| [`00-02-aws-lab-cost-and-access-basics.md`](00-02-aws-lab-cost-and-access-basics.md) | [`00-02-aws-lab-cost-and-access-basics.md`](../literal-pages/00-02-aws-lab-cost-and-access-basics.md) | 認証情報・Region・Quota・料金・予算・削除を一つの実験計画として捉える方法、実機確認が必要な事項と設計比較でよい事項 | PREP-02 |

## 第1部: Foundation Model統合、データ管理、コンプライアンス

| 予定ファイル | 対応するliteral page | 試験理解を補助する要素 | 対応Task・Skills |
|---|---|---|---|
| [`01-01-requirements-and-solution-design.md`](01-01-requirements-and-solution-design.md) | [`01-01-requirements-and-solution-design.md`](../literal-pages/01-01-requirements-and-solution-design.md) | 機能・非機能要件の読み分け、品質・Latency・Security・Costの衝突、PoC仮説と測定可能な成功条件、標準部品化する範囲 | D1-01 / 1.1.1〜1.1.3 |
| [`01-02-foundation-model-selection-and-configuration.md`](01-02-foundation-model-selection-and-configuration.md) | [`01-02-foundation-model-selection-and-configuration.md`](../literal-pages/01-02-foundation-model-selection-and-configuration.md) | Use caseからModality・Context・Tool use・Region・Costを優先順位付けする方法、Model routing、Cross-Region、CustomizationとSageMaker endpointの選択境界 | D1-02 / 1.2.1〜1.2.4 |
| [`01-03-data-validation-and-processing.md`](01-03-data-validation-and-processing.md) | [`01-03-data-validation-and-processing.md`](../literal-pages/01-03-data-validation-and-processing.md) | Modality別Pipelineの共通点と差、検証・正規化・隔離・再処理の順序、Converse・JSON Schema・Endpoint payloadを選ぶ条件 | D1-03 / 1.3.1〜1.3.4 |
| [`01-04-vector-store-design.md`](01-04-vector-store-design.md) | [`01-04-vector-store-design.md`](../literal-pages/01-04-vector-store-design.md) | OpenSearch・Aurora PostgreSQL／pgvector・Managed storeの比較軸、Metadataと認可、近似検索のTrade-off、同期・再Index・Rollbackを含むLifecycle | D1-04 / 1.4.1〜1.4.5 |
| [`01-05-retrieval-for-rag.md`](01-05-retrieval-for-rag.md) | [`01-05-retrieval-for-rag.md`](../literal-pages/01-05-retrieval-for-rag.md) | RAG全体でのChunking・Embedding・検索・Filter・Rerankingの関係、検索方式とQuery変換の選択、検索不良の原因分離 | D1-05 / 1.5.1〜1.5.6 |
| [`01-06-prompt-engineering-and-governance.md`](01-06-prompt-engineering-and-governance.md) | [`01-06-prompt-engineering-and-governance.md`](../literal-pages/01-06-prompt-engineering-and-governance.md) | Promptの構造、会話状態、Few-shot、構造化出力の使い分け、Version・評価・承認・監査・Rollbackを一つのLifecycleとして判断する方法 | D1-06 / 1.6.1〜1.6.6 |

## 第2部: 実装と統合

| 予定ファイル | 対応するliteral page | 試験理解を補助する要素 | 対応Task・Skills |
|---|---|---|---|
| `02-01-agentic-ai-and-tool-integration.md` | [`02-01-agentic-ai-and-tool-integration.md`](../literal-pages/README.md#第2部-実装と統合) | Agent loopでのFM・Application・Toolの責務、State・Memory・冪等性、停止条件、単一／Multi-agent、Human approval、MCP serverを選ぶ条件 | D2-01 / 2.1.1〜2.1.7 |
| [`02-02-model-deployment-strategies.md`](02-02-model-deployment-strategies.md) | [`02-02-model-deployment-strategies.md`](../literal-pages/02-02-model-deployment-strategies.md) | Traffic・Customization・SLO・CostからOn-demand・Provisioned・Batch・Endpointを選ぶ方法、LLM固有のResource制約、段階リリース | D2-02 / 2.2.1〜2.2.3 |
| `02-03-enterprise-integration-architecture.md` | [`02-03-enterprise-integration-architecture.md`](../literal-pages/README.md#第2部-実装と統合) | 同期・非同期・Event・Batch・Workflowの結合度と一貫性、Cloud／Hybridのデータ境界、Gateway、最小権限、IaC・CI/CDの判断 | D2-03 / 2.3.1〜2.3.5 |
| `02-04-foundation-model-api-integration.md` | [`02-04-foundation-model-api-integration.md`](../literal-pages/README.md#第2部-実装と統合) | UXと処理時間から同期・Streaming・非同期を選ぶ方法、4xx・5xx・Throttling・Timeoutの扱い、Retry・Idempotency・Fallback・Routing | D2-04 / 2.4.1〜2.4.4 |
| `02-05-application-integration-and-development-tools.md` | [`02-05-application-integration-and-development-tools.md`](../literal-pages/README.md#第2部-実装と統合) | OpenAPI・Webhook・Event・Flow・Agent・Prompt chaining・Orchestrationの境界、開発支援Toolの責任範囲、End-to-end traceの読み方 | D2-05 / 2.5.1〜2.5.6 |

## 第3部: AI Safety、Security、Governance

| 予定ファイル | 対応するliteral page | 試験理解を補助する要素 | 対応Task・Skills |
|---|---|---|---|
| `03-01-input-output-safety-controls.md` | [`03-01-input-output-safety-controls.md`](../literal-pages/README.md#第3部-ai-safetysecuritygovernance) | 入力・Retrieval・Tool・出力の各境界へControlを置く理由、GuardrailとApplication validationの責任分担、False positive／negative、検知から回帰試験までのLoop | D3-01 / 3.1.1〜3.1.5 |
| `03-02-data-security-and-privacy.md` | [`03-02-data-security-and-privacy.md`](../literal-pages/README.md#第3部-ai-safetysecuritygovernance) | User・Application・Ingestion・Runtime・OperatorのTrust boundary、PIIを処理する時点、Tokenization・Pseudonymization・Anonymization・Redactionの選択 | D3-02 / 3.2.1〜3.2.3 |
| `03-03-ai-governance-and-compliance.md` | [`03-03-ai-governance-and-compliance.md`](../literal-pages/README.md#第3部-ai-safetysecuritygovernance) | Policy・Owner・Approval・Lineage・Audit evidenceの関係、RACI、CloudTrailとApplication logで証明できる範囲、違反検知後の是正 | D3-03 / 3.3.1〜3.3.4 |
| `03-04-responsible-ai.md` | [`03-04-responsible-ai.md`](../literal-pages/README.md#第3部-ai-safetysecuritygovernance) | Responsible AIの各原則をUI、Group別評価、Human oversight、Release gateへ具体化する方法、全体平均だけでは見えない差 | D3-04 / 3.4.1〜3.4.3 |

## 第4部: 運用効率と最適化

| 予定ファイル | 対応するliteral page | 試験理解を補助する要素 | 対応Task・Skills |
|---|---|---|---|
| `04-01-cost-and-resource-efficiency.md` | [`04-01-cost-and-resource-efficiency.md`](../literal-pages/README.md#第4部-運用効率と最適化) | Token・Model・Capacity・CacheをCost driverとして分解する方法、On-demand・Batch・Provisionedの選択、削減で悪化する品質・Latency・Freshness | D4-01 / 4.1.1〜4.1.4 |
| `04-02-application-performance.md` | [`04-02-application-performance.md`](../literal-pages/README.md#第4部-運用効率と最適化) | End-to-end latencyをComponentへ分解する方法、検索設定・生成Parameter・Concurrency・CapacityのTrade-off、局所最適を避ける判断 | D4-02 / 4.2.1〜4.2.6 |
| `04-03-monitoring-and-observability.md` | [`04-03-monitoring-and-observability.md`](../literal-pages/README.md#第4部-運用効率と最適化) | Infra・Model・Retrieval・Agent・Quality・Cost・Business KPIの関係、Metric・Log・Traceの使い分け、AlertからRunbookへつなぐ方法 | D4-03 / 4.3.1〜4.3.6 |

## 第5部: テスト、検証、トラブルシューティング

| 予定ファイル | 対応するliteral page | 試験理解を補助する要素 | 対応Task・Skills |
|---|---|---|---|
| `05-01-genai-evaluation.md` | [`05-01-genai-evaluation.md`](../literal-pages/README.md#第5部-テスト検証トラブルシューティング) | Model・Prompt・Retrieval・Agent・End-to-endを分ける評価設計、Automatic・Judge・Humanの組み合わせ、Bias・Sample数、Release／Rollback判定 | D5-01 / 5.1.1〜5.1.9 |
| `05-02-troubleshooting.md` | [`05-02-troubleshooting.md`](../literal-pages/README.md#第5部-テスト検証トラブルシューティング) | 症状からInput・API・Model・Prompt・Retrieval・Tool・Output・Infrastructureを順に絞る方法、Signal・仮説・Root cause・再発防止の関係 | D5-02 / 5.2.1〜5.2.5 |

## 対応関係の確認

| 対象 | literal pages | supplimental pages | 対応方針 |
|---|---:|---:|---|
| 準備 | 2 | 2 | 1対1 |
| Domain 1 | 6 | 6 | 1対1 |
| Domain 2 | 5 | 5 | 1対1 |
| Domain 3 | 4 | 4 | 1対1 |
| Domain 4 | 3 | 3 | 1対1 |
| Domain 5 | 2 | 2 | 1対1 |
| 合計 | 22 | 22 | 全ページ対応 |

## 作成順

[`docs/study-plan.md`](../../docs/study-plan.md)の学習順に、対応するliteral pageとsupplimental pageを対で作成する。個別の疑問や誤答の多さによって章の順番や範囲は変更しない。理解度に応じた復習順の変更は、教科書の目次ではなく学習計画側で管理する。
