# AWS実行Runbook

最終確認日: 2026-09-21

この文書はAWS実機Taskの共通手順である。Service固有のConsole手順を固定せず、変化しにくい安全確認とEvidenceを定義する。

## Preflight

- [ ] `aws sts get-caller-identity` で意図したAccount／Roleであることを画面上だけで確認した
- [ ] `aws configure get region` と利用Service／Modelの対応Regionが一致する
- [ ] Root userを使わず、学習に必要な最小権限のPrincipalを使う
- [ ] AWS Budgetsの通知先、月5,000円相当の予算、4,000円の停止線を確認した
- [ ] Cost ExplorerまたはBillingで当月実績と想定外Serviceがないことを確認した
- [ ] 料金ページを当日確認し、最大Request／Token／時間から最悪時概算を記録した
- [ ] 作成Resource、共通Tag、削除順、終了予定時刻を記録した
- [ ] 入力がRepository内の架空Datasetだけであることを確認した

## 推奨する最小実験

| 実験 | AWSで確認すること | コスト制御 |
|---|---|---|
| Bedrock Runtime | ConverseのRequest／Response、Usage、Latency、Validation error | On-demand、少量Prompt、`maxTokens`、最大Request数 |
| Guardrails | ApplyGuardrailまたはModel適用時のBlock／MaskとTrace | 少数の代表Case、同じCaseの再実行を避ける |
| IAM | 許可／明示的Deny、Resource／Action境界 | Policyを狭くし、不要なResourceを作らない |
| CloudWatch／CloudTrail | Metric、Event、Correlation、秘匿化 | 短いRetention、詳細Payloadを不用意にLogしない |
| Knowledge Bases | Data source同期、Metadata filter、Retrieve／RetrieveAndGenerate | 小Dataset、当日作成・削除、Vector Store料金を含めて事前見積り |

Knowledge Basesで必要になるVector Storeは、実施時点の[対応一覧](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html)と各料金を比較して選ぶ。月4,000円の実行枠で作成から削除まで完結できない場合は作成せず、ローカルRAG＋Bedrock Runtime／Guardrailsの実測へ切り替える。

## Evidenceの残し方

保存してよいもの:

- Service名、Region、Model ID、設定値、Status code、Error code
- Token usage、Latency、Guardrail action、Metric名、Sanitize済みEvent
- Resource種別と論理名、作成／削除時刻、概算／実績費用

保存しないもの:

- Access key、Secret、Session token、Cookie、署名付きURL
- Account ID、個人ARN、Email、実在の個人情報・機密情報
- Logに不要な完全Prompt／Response

## Cleanup

- [ ] Task開始時に書いたResource一覧を逆順に削除した
- [ ] Knowledge Base／Data source／Vector Store／S3 objectなど、親Resourceの削除で残るものを個別確認した
- [ ] CloudWatch Log group、Alarm、Dashboard、IAM Role／Policyなど補助Resourceを確認した
- [ ] Tagまたは命名Prefixで残存Resourceを検索した
- [ ] 削除時刻と確認方法を `artifacts/cost-log.md` に記録した
- [ ] 翌日以降、料金反映後の実績を追記した

Cleanupに失敗した場合は新規実験を止め、Error、依存Resource、次に試す削除手順を記録する。

## 公式資料

- [Making inference requests](https://docs.aws.amazon.com/bedrock/latest/userguide/inference.html)
- [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Identity and access management for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html)
- [CloudWatch metrics for Amazon Bedrock runtime](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-runtime-metrics.html)
- [CloudTrail logging for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html)
