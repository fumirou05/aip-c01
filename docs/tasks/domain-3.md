# Domain 3 実行タスク: AI Safety、Security、Governance

配点20%、目安16時間。公式範囲は [Content Domain 3](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html) を基準にする。

## D3-01: 入出力のSafety controlを実装する（5時間）

公式・無料教材:

- [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [Prompt attack detection](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-prompt-attack.html)
- [Contextual grounding checks](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-contextual-grounding-check.html)
- [Prompt injection security](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-injection.html)

作業:

- [ ] 30分: Content filter、Denied topic、Word filter、Sensitive information、Prompt attack、Grounding checkの適用箇所を読む
- [ ] 35分 — Skill 3.1.1: Harmful input、Prompt injection、Jailbreak、Oversized inputを分類し、Pre-processing controlを割り当てる
- [ ] 35分 — Skill 3.1.2: Harmful output、PII leakage、Policy違反、Unsafe tool instructionを分類し、Post-processing controlを割り当てる
- [ ] 35分 — Skill 3.1.3: Citation、RAG grounding、Confidence、Structured output、Fact checkを使うAccuracy verification flowを作る
- [ ] 35分 — Skill 3.1.4: API Gateway、Custom validator、Guardrails、Output validatorを組み合わせたDefense-in-depth構成を作る
- [ ] 35分 — Skill 3.1.5: Adversarial dataset、Detection、Alert、Block、Review、Regression testのThreat detection loopを作る
- [ ] 80分: ローカルSafety pipelineで全Adversarial datasetを反復し、代表CaseだけをBedrock Guardrailsへ適用する。Guardrail action、False positive／negative、ローカルControlとの責任分界、概算費用を記録する
- [ ] 15分: False positiveとFalse negativeを集計し、Threshold変更の影響を記録する

成果物: Threat model、Safety pipeline、Adversarial test report。

完了条件: 1つのFilterだけに依存せず、入力、Retrieval、Tool、出力の各境界にControlを配置できる。

## D3-02: Data securityとPrivacy controlを実装する（4時間）

公式・無料教材:

- [Data protection in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)
- [Identity and access management for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html)
- [Amazon Bedrock and interface VPC endpoints](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html)
- [AWS KMS Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)

作業:

- [ ] 30分: AWS Shared Responsibility、Encryption、IAM、PrivateLink、Logging時の機密情報を読む
- [ ] 40分 — Skill 3.2.1: User、Application、Ingestion、Runtime、Operatorの最小権限とResource boundaryをIAM表として定義する
- [ ] 40分 — Skill 3.2.2: PIIを収集前、Prompt送信前、Log保存前、Output返却前に検知・Maskし、Retentionと削除を定義する
- [ ] 40分 — Skill 3.2.3: Tokenization、Pseudonymization、Anonymization、Redactionの可逆性とUtilityを比較する
- [ ] 75分: ローカルでPII redaction、Role別Metadata filter、Log sanitizationを実装する。AWSでは最小権限Roleで許可されたBedrock呼出しと明示的に拒否される操作を試し、Sanitize済みのError codeをEvidenceにする
- [ ] 15分: At-rest、In-transit、In-useのControlと未解決Riskを記録する

成果物: Data flow／Trust boundary図、IAM表、Privacy test report。

完了条件: Model providerのData取扱いだけでなく、Application、Log、Vector Store、Backupを含むData lifecycleを説明できる。

## D3-03: AI GovernanceとCompliance mechanismを実装する（4時間）

公式・無料教材:

- [CloudTrail logging for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html)
- [SageMaker Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html)
- [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)
- [Generative AI Lifecycle Operational Excellence](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/)

作業:

- [ ] 30分: Governanceの対象をData、Model、Prompt、Tool、Output、Human decision、Audit logに分ける
- [ ] 35分 — Skill 3.3.1: Model card、Data lineage、Decision log、Owner、Approval、Evidence retentionを含むControl matrixを作る
- [ ] 35分 — Skill 3.3.2: Source ID、Version、License、Owner、取得日、CitationをRetrieval結果からOutputまで追跡するSchemaを作る
- [ ] 35分 — Skill 3.3.3: Builder、Reviewer、Risk owner、Security、Legal、OperatorのRACIと例外承認Processを作る
- [ ] 35分 — Skill 3.3.4: Misuse、Drift、Bias、Policy違反をMetric→Alert→Triage→Remediation→Evidence保存につなげる
- [ ] 55分: AWS実行1 Requestについて、ApplicationのCorrelation IDからCloudTrail Event、Prompt版、Model ID、Safety判定、Output metadataまでのAudit recordを生成する。CloudTrailで確認できないData plane情報はApplication logとの境界を明記する
- [ ] 15分: Audit recordだけでは証明できない事項を列挙する

成果物: Governance control matrix、RACI、Lineage schema、Audit record。

完了条件: 「Logがある」だけでなく、誰が、何を、いつ判断し、どのEvidenceを残すか説明できる。

## D3-04: Responsible AIの原則を実装する（3時間）

公式・無料教材:

- [AWS Responsible AI](https://aws.amazon.com/ai/responsible-ai/)
- [AWS AI Service Cards](https://aws.amazon.com/ai/responsible-ai/resources/)
- [SageMaker Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-fairness-and-explainability.html)
- [Amazon Bedrock evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html)

作業:

- [ ] 30分: Fairness、Explainability、Privacy、Safety、Controllability、Veracity、Governance、Transparencyをユースケースへ対応付ける
- [ ] 35分 — Skill 3.4.1: Citation、Limitation、Confidence／Uncertainty、Human escalationをUser interfaceへ表示する仕様を書く。内部推論の開示を前提にしない
- [ ] 35分 — Skill 3.4.2: 2つの利用者Groupと2つのLanguageについて、代表性、Error rate差、拒否率差を測るFairness testを作る
- [ ] 35分 — Skill 3.4.3: Model card、Guardrail policy、Automated compliance check、例外承認をRelease gateへ組み込む
- [ ] 30分: ローカルの全評価DataとBedrockで実行した少量の代表CaseをGroup別に集計し、全体平均では見えない差とSample数の制約を報告する
- [ ] 15分: 残存RiskとHuman oversightが必要な判断を記録する

成果物: Responsible AI checklist、Group別評価表、User disclosure仕様。

完了条件: Responsible AIを理念だけでなく、測定、Release判定、User communicationへ落とし込める。

## Domain 3 終了チェック

- [ ] Skills 3.1.1〜3.4.3の全項目を実施した
- [ ] [`docs/notes/domain-3-safety-security-governance.md`](../notes/domain-3-safety-security-governance.md) を更新した
- [ ] Threat、Trust boundary、Governance owner、残存Riskを説明できる
- [ ] Guardrails、IAM、CloudTrailのうち2つ以上でAWS実測Evidenceを残した
- [ ] Domain 3の問題演習を行い、誤答を記録した
