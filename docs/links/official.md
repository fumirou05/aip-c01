# 公式リンク集

URLをブックマークとして残すだけでなく、対象・用途・最終確認日も記録する。

最終確認日: 2026-09-21

## 試験・認定

| 分類 | リンク | 用途 |
|---|---|---|
| 試験ページ | [AWS Certified Generative AI Developer - Professional](https://aws.amazon.com/certification/certified-generative-ai-developer-professional/) | 試験概要・受験要件・公式Prep Plan |
| 試験ガイド | [AIP-C01 Exam Guide（PDF）](https://docs.aws.amazon.com/pdfs/aws-certification/latest/ai-professional-01/ai-professional-01.pdf) | 試験目的・ドメイン・技術・サービス範囲 |
| ドメイン1 | [Foundation Model Integration, Data Management, and Compliance](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html) | FM、データ、RAG、プロンプト |
| ドメイン2 | [Implementation and Integration](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html) | Agent、API、デプロイ、統合 |
| ドメイン3 | [AI Safety, Security, and Governance](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html) | 安全性、セキュリティ、ガバナンス |
| ドメイン4 | [Operational Efficiency and Optimization](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html) | 運用、性能、コスト |
| ドメイン5 | [Testing, Validation, and Troubleshooting](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html) | 評価、検証、トラブルシュート |
| 対象サービス | [In-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/aip-01-in-scope-services.html) | 試験範囲に含まれるサービス |
| 技術・概念 | [Technologies and Concepts](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-technologies-concepts.html) | RAG、Agent、IaC、CI/CDなど |
| 範囲外 | [Out-of-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/aip-01-out-of-scope-services.html) | 優先度を下げる判断材料 |

## AWS公式学習資料

| 分類 | リンク | 用途 |
|---|---|---|
| 公式対策 | [AWS Certification Prep](https://aws.amazon.com/certification/certification-prep/) | 公式問題セット・試験準備コース |
| AIP-C01対策 | [AIP-C01 Exam Prep Plan](https://skillbuilder.aws/category/exam-prep/generative-ai-developer-professional-AIP-C01) | 登録済み。無料対象のOfficial Practice Question Setを確認。Subscription表示の教材は必須経路から除外する |
| Skill Builder | [AWS Skill Builder](https://skillbuilder.aws/) | コース・Builder Labs・演習 |
| 無料デジタル学習 | [AWS Training and Certification](https://aws.amazon.com/training/) | 無料デジタルコースの入口。購読限定ラボとは区別する |
| AWSドキュメント | [AWS Documentation](https://docs.aws.amazon.com/) | サービス仕様・API・手順 |
| Step Functions | [Handling errors in Step Functions workflows](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html) | `Retry`、`Catch`、エラー処理 |
| Step Functions設計例 | [Using the circuit breaker pattern with AWS Step Functions and Amazon DynamoDB](https://aws.amazon.com/blogs/compute/using-the-circuit-breaker-pattern-with-aws-step-functions-and-amazon-dynamodb/) | サーキットブレーカーパターンの実装例 |
| Agent／Tool連携 | [Tool-based agents for calling functions](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/tool-based-agents-for-calling-functions.html) | FMによるTool選択と実行結果のループ |
| Agent／Workflow連携 | [Workflow orchestration agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/workflow-orchestration-agents.html) | Step FunctionsによるAgent・Workflowのオーケストレーション |
| Graceful degradation | [Definitions - Agentic AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/definitions.html) | 障害時に部分機能を維持する考え方 |
| フォレンジック | [Validating CloudTrail log file integrity](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html) | 証拠ログの完全性検証 |
| ポストモーテム | [Performing a post-incident analysis in Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/analysis.html) | blamelessな事後分析と改善アクション |
| OpenSearchシャーディング | [Choosing the number of shards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/bp-sharding.html) | シャード数・サイズの設計 |
| OpenSearchベクトル検索 | [Vector search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vector-search.html) | k-NN、Embedding、RAG |
| Aurora PostgreSQL／pgvector | [Using Aurora PostgreSQL as a Knowledge Base for Amazon Bedrock](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.VectorDB.html) | PostgreSQLをVector Storeとして使う構成 |
| ベクトル埋め込み | [Getting started with Amazon Titan Text Embeddings in Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/getting-started-with-amazon-titan-text-embeddings/) | Embedding、意味検索、RAG |
| Bedrock | [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/) | FM、Knowledge Bases、Agentsなど |
| Bedrock料金 | [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/) | Model、Guardrails、Knowledge Basesなどの実施日前の料金確認 |
| 料金見積り | [AWS Pricing Calculator](https://calculator.aws/) | 作成前の概算と構成比較 |
| 予算管理 | [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) | 月次予算、実績・予測通知の設定 |
| Cost Explorer | [Analyzing your costs with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) | Service／Tag別の実績確認 |
| コスト配分Tag | [Organizing and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) | ラボ費用の識別と集計 |
| SageMaker AI | [Amazon SageMaker AI Documentation](https://docs.aws.amazon.com/sagemaker/) | ML開発・評価・運用 |
| Well-Architected | [Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html) | 生成AIワークロードの設計原則 |
| Well-Architected | [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) | セキュリティ、信頼性、コストなど |
| 設計・運用 | [Generative AI Lifecycle Operational Excellence](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/) | PoCから本番運用までの設計・評価・監視 |
| Agent設計 | [Building serverless architectures for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/) | Agent、IaC、CI/CD、運用Pattern |

Skill Builderのデジタル教材には無料対象と購読限定項目が混在する。公式Workshop、AWS Samples、User Guideの手順も、AWSへDeploy・Invokeすると料金が発生し得る。学習タスクでは無料教材を優先しつつ、AWS実機でしか確認しにくい項目は月額方針の範囲で [`labs/local-genai/`](../../labs/local-genai/) に組み込む。単価、Free Tier、Credit、Region、Quotaは実施日に各公式ページで再確認する。

## リンク確認メモ

リンク先の内容が変わった場合は、行の用途を修正し、関連ノートの確認日も更新する。
