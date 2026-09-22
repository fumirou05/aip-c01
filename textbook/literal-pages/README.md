# Literal pages 目次

公式試験ガイドと、各学習タスクが参照するAWS公式資料を、意味を変えずに理解しやすい日本語へ再構成するページの作成予定一覧。

最終抽出日: 2026-09-21  
状態: 22ページ中9ページを作成・レビュー済み。Domain 1の6ページは横断監査済み。リンク付きのファイル名は本文作成済みで、コード表記のファイル名は作成予定。

本文作成時は[`templates/literal-page.md`](../templates/literal-page.md)を出発点にする。テンプレートより内容の正確さと理解しやすさを優先する。

## 章の書き方

各ページは次の順にする。

1. この章で分かること
2. 対応するTask・Skill
3. 公式資料の内容を平易に再構成した本文
4. 公式資料に明記された制約・注意点
5. 用語の短い整理
6. 公式URLと最終確認日
7. 関連する補足ページへのリンク

公式資料にない比較、例、推奨構成、演習結果はこのディレクトリへ入れない。

## 第0部: 試験範囲と学習の入口

| 予定ファイル | 対応 | 収録する要素 | 主な公式根拠 |
|---|---|---|---|
| [`00-01-exam-guide-and-scope.md`](00-01-exam-guide-and-scope.md) | [PREP-01](../../docs/tasks/README.md#prep-01-試験範囲と現在地を確定する1時間30分) | 試験の対象者、5ドメインと配点、20 Task、対象・対象外の技術と職務、試験準備リソース | [Exam Guide](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html)、[In-Scope Services](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/aip-01-in-scope-services.html)、[Technologies and Concepts](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-technologies-concepts.html) |
| [`00-02-aws-lab-cost-and-access-basics.md`](00-02-aws-lab-cost-and-access-basics.md) | [PREP-02](../../docs/tasks/README.md#prep-02-awsローカル統合ラボを準備する2時間) | IAM Identity Center／短期認証情報、Region・Quota、AWS Budgets、Bedrock料金、Cost Explorer、コスト配分Tag | [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)、[Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)、[Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) |

## 第1部: Foundation Model統合、データ管理、コンプライアンス

対応範囲: [Domain 1実行タスク](../../docs/tasks/domain-1.md)、Skills 1.1.1〜1.6.6（28 Skills）。

| 予定ファイル | 対応Task・Skills | 収録する要素 | 主な公式根拠 |
|---|---|---|---|
| [`01-01-requirements-and-solution-design.md`](01-01-requirements-and-solution-design.md) | D1-01 / 1.1.1〜1.1.3 | 機能・非機能要件、利用者・データ・品質・レイテンシー・可用性・セキュリティ・コスト・データ所在地、PoC仮説と成功条件、再利用可能な構成要素 | [Domain 1](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html)、[Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html) |
| [`01-02-foundation-model-selection-and-configuration.md`](01-02-foundation-model-selection-and-configuration.md) | D1-02 / 1.2.1〜1.2.4 | Modality、Context、Tool use、Region、互換性、価格、Throughput、Model IDの外部設定、Inference profile、Prompt routing、Customization、Lifecycle | [Models](https://docs.aws.amazon.com/bedrock/latest/userguide/models.html)、[Inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)、[Prompt routing](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html)、[Custom models](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) |
| [`01-03-data-validation-and-processing.md`](01-03-data-validation-and-processing.md) | D1-03 / 1.3.1〜1.3.4 | Text・Image・Audio・Tabular、必須項目・文字コード・サイズ・重複・欠損・更新日・PII、抽出・正規化・検証・保存・再処理、Converse形式・JSON Schema・SageMaker payload | [Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html)、[Multimodal Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-multimodal.html)、[Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/data-quality-gs-studio.html)、[Inference requests](https://docs.aws.amazon.com/bedrock/latest/userguide/inference.html) |
| [`01-04-vector-store-design.md`](01-04-vector-store-design.md) | D1-04 / 1.4.1〜1.4.5 | Vector Storeの選定、Metadata schema、Shard・Index・Dimension・近似検索・Multi-index、Connectorと権限、Full／Incremental sync、Change detection、Tombstone、Re-index、Rollback | [Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)、[Supported vector stores](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html)、[Metadata](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-metadata.html) |
| [`01-05-retrieval-for-rag.md`](01-05-retrieval-for-rag.md) | D1-05 / 1.5.1〜1.5.6 | Fixed・Sentence・Semantic・Hierarchical chunking、Embedding、OpenSearch・Aurora pgvector・Managed store、Semantic／Keyword／Hybrid検索、Reranking、Metadata filter、Query expansion・Decomposition・Rewrite、Retrieval interface | [Query configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html)、[Chunking and parsing](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking-parsing.html)、[Metadata filters](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-metadata.html) |
| [`01-06-prompt-engineering-and-governance.md`](01-06-prompt-engineering-and-governance.md) | D1-06 / 1.6.1〜1.6.6 | Role・制約・Context・出力Schema・拒否条件、会話履歴と確認Flow、PromptのOwner・Review・Approval・Version・Audit・Rollback、Prompt test、Few-shot、FlowとGuardrail | [Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html)、[Bedrock Flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html)、[Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) |

## 第2部: 実装と統合

対応範囲: [Domain 2実行タスク](../../docs/tasks/domain-2.md)、Skills 2.1.1〜2.5.6（25 Skills）。

| 予定ファイル | 対応Task・Skills | 収録する要素 | 主な公式根拠 |
|---|---|---|---|
| `02-01-agentic-ai-and-tool-integration.md` | D2-01 / 2.1.1〜2.1.7 | Agent loop、Session state、短期履歴・長期Memory、冪等性、Plan／Act／Observe／Re-plan、停止条件、単一・Multi-agent、Human approval、Tool schema、MCP server、Trace | [Tool use](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html)、[AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)、[Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)、[Agent tracing](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html) |
| [`02-02-model-deployment-strategies.md`](02-02-model-deployment-strategies.md) | D2-02 / 2.2.1〜2.2.3 | On-demand、Provisioned Throughput、Batch inference、SageMaker endpoint、Model load・GPU memory・Cold start・Token throughput・Container health、Small model・Cascading・Quantization | [Bedrock inference](https://docs.aws.amazon.com/bedrock/latest/userguide/inference.html)、[Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html)、[Deploy to SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html) |
| `02-03-enterprise-integration-architecture.md` | D2-03 / 2.3.1〜2.3.5 | 同期API・Event・Queue・Batch・Workflow、API Gateway・Lambda・EventBridge・SQS・Step Functions、認証主体と最小権限、Cloud・On-premises・Edge、Data residency、IaCとCI/CD | [Serverless agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/)、[IaC](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/infrastructure-as-code.html)、[CI/CD](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/cicd-and-automation.html) |
| `02-04-foundation-model-api-integration.md` | D2-04 / 2.4.1〜2.4.4 | Invoke・Converse・Streaming・Async／Batch、同期・非同期、WebSocket・SSE、Timeout、Backoff＋Jitter、Throttling、Fallback、Idempotency、X-Ray、Model routing | [Bedrock Runtime](https://docs.aws.amazon.com/bedrock/latest/userguide/inference.html)、[Converse examples](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-examples.html)、[SDK retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) |
| `02-05-application-integration-and-development-tools.md` | D2-05 / 2.5.1〜2.5.6 | OpenAPI-first、Webhook、Event-driven、No-code Flow、FM API契約、Amplify UI・OpenAPI client・Prompt Flow、Data Automation、Amazon Q Developer、Prompt chaining・Agent・Orchestration、Logs Insights・X-Ray | [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)、[Bedrock Flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html)、[Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html)、[X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) |

## 第3部: AI Safety、Security、Governance

対応範囲: [Domain 3実行タスク](../../docs/tasks/domain-3.md)、Skills 3.1.1〜3.4.3（15 Skills）。

| 予定ファイル | 対応Task・Skills | 収録する要素 | 主な公式根拠 |
|---|---|---|---|
| `03-01-input-output-safety-controls.md` | D3-01 / 3.1.1〜3.1.5 | Harmful input／output、Prompt injection、Jailbreak、Oversized input、PII leakage、Unsafe tool instruction、Citation・Grounding・Confidence・Structured output、Defense in depth、Threat detection loop | [Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)、[Prompt attack detection](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-prompt-attack.html)、[Grounding checks](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-contextual-grounding-check.html)、[Prompt injection security](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-injection.html) |
| `03-02-data-security-and-privacy.md` | D3-02 / 3.2.1〜3.2.3 | Shared Responsibility、IAM最小権限、Encryption、PrivateLink、PII検知・Mask・Retention・削除、Tokenization・Pseudonymization・Anonymization・Redaction | [Data protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)、[Bedrock IAM](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html)、[VPC endpoints](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html)、[KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) |
| `03-03-ai-governance-and-compliance.md` | D3-03 / 3.3.1〜3.3.4 | Data・Model・Prompt・Tool・Output・Human decision・Audit log、Model card、Data lineage、Decision log、Evidence retention、出典追跡、RACI、例外承認、Misuse・Drift・Bias・Policy違反 | [Bedrock CloudTrail logging](https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html)、[Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html)、[Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)、[Lifecycle Operational Excellence](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/) |
| `03-04-responsible-ai.md` | D3-04 / 3.4.1〜3.4.3 | Fairness、Explainability、Privacy、Safety、Controllability、Veracity、Governance、Transparency、Citation・Limitation・Uncertainty・Human escalation、Group別評価、Release gate | [AWS Responsible AI](https://aws.amazon.com/ai/responsible-ai/)、[AI Service Cards](https://aws.amazon.com/ai/responsible-ai/resources/)、[SageMaker Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-fairness-and-explainability.html)、[Bedrock evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html) |

## 第4部: 運用効率と最適化

対応範囲: [Domain 4実行タスク](../../docs/tasks/domain-4.md)、Skills 4.1.1〜4.3.6（16 Skills）。

| 予定ファイル | 対応Task・Skills | 収録する要素 | 主な公式根拠 |
|---|---|---|---|
| `04-01-cost-and-resource-efficiency.md` | D4-01 / 4.1.1〜4.1.4 | Input／Output token、Context圧縮・剪定、Response limit、Model routing、Batch・Concurrency・Capacity・Auto Scaling・Provisioned Throughput、Exact・Semantic・Edge・Prompt caching | [Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)、[Prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)、[Cost attribution](https://docs.aws.amazon.com/bedrock/latest/userguide/cost-mgmt-application-inference-profiles.html)、[Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) |
| `04-02-application-performance.md` | D4-02 / 4.2.1〜4.2.6 | Gateway・Retrieval・Model queue・TTFT・Generation・ToolのLatency、Pre-compute・Parallel・Streaming、検索設定、Throughput、Temperature・top-p・top-k・max tokens、Capacity planning、Profiling | [Runtime metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-runtime-metrics.html)、[Prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)、[KB query configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html) |
| `04-03-monitoring-and-observability.md` | D4-03 / 4.3.1〜4.3.6 | Metric・Log・Trace、Availability・Latency・Error・Token・Quality・Feedback・Business KPI、Alert、Request ID、Agent・Tool指標、Vector検索・Index freshness・Ingestion、Golden dataset・Output diff | [Runtime metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-runtime-metrics.html)、[Invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html)、[Advanced operations](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/prod-monitoring-advanced-operations.html) |

## 第5部: テスト、検証、トラブルシューティング

対応範囲: [Domain 5実行タスク](../../docs/tasks/domain-5.md)、Skills 5.1.1〜5.2.5（14 Skills）。

| 予定ファイル | 対応Task・Skills | 収録する要素 | 主な公式根拠 |
|---|---|---|---|
| `05-01-genai-evaluation.md` | D5-01 / 5.1.1〜5.1.9 | Offline／Online、Automatic／Human、Reference-based／free、評価Rubric、A/B比較、User feedback、Regression・Adversarial・Canary・Continuous evaluation、LLM-as-a-judge、RAG・Agent指標、Report、Rollback条件 | [Bedrock evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html)、[RAG metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-retrieve.html)、[LLM-as-a-judge](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html)、[AgentCore evaluators](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/create-evaluator.html) |
| `05-02-troubleshooting.md` | D5-02 / 5.2.1〜5.2.5 | Input・API・Model・Prompt・Retrieval・Tool・Output・InfrastructureのTriage、Context overflow・Truncation、API errorとRetry、版・Parameter・入力分布の固定、Embedding・Index・Filter・Chunk・top-k、Template・Schema・Version drift | [API error codes](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html)、[Runtime metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-runtime-metrics.html)、[Invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html)、[Agent tracing](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html) |

## 網羅性の確認

| 対象 | Task数 | Skill数 | 予定ページ数 |
|---|---:|---:|---:|
| 準備 | 2 | - | 2 |
| Domain 1 | 6 | 28 | 6 |
| Domain 2 | 5 | 25 | 5 |
| Domain 3 | 4 | 15 | 4 |
| Domain 4 | 3 | 16 | 3 |
| Domain 5 | 2 | 14 | 2 |
| 合計 | 22 | 98 | 22 |
