# AWSサービス別ページ 目次

AIP-C01のTask・Skillを横断して、各AWSサービスが「何を管理し、どの主要機能を持ち、ほかのサービスとどこで接続するか」を体系的に学ぶためのページ作成予定一覧。

最終抽出日: 2026-09-22  
状態: 目次作成済み、本文33ページは未作成

## この目次の位置づけ

[`literal-pages/`](../literal-pages/README.md)と[`supplimental-pages/`](../supplimental-pages/README.md)は、公式試験ガイドのTask・Skillを学習単位にしている。このディレクトリは同じ範囲をサービス単位で引き直す。

- Taskから学ぶときは、従来どおりliteral／supplimentalのページペアを読む。
- サービスの全体像や機能間の関係を確認するときは、この目次から該当サービスを読む。
- サービス別ページには公式の機能、管理境界、主要な連携、試験Taskとの対応を書く。
- 要件からの選択、他方式を除外する理由、架空シナリオは対応するsupplimental pageへリンクし、サービス別ページでは重複して展開しない。
- 公式In-Scope一覧は非網羅的で変更され得る。掲載順は重要度や出題比率を示さない。

## 重要度の定義

この重要度はAWS公式が公表したサービス別配点ではない。公式Task・Skillで担う役割の広さと、ほかのサービスを理解する前提になる度合いから、この教科書内の学習深度を決めたものである。

| 重要度 | この目次での意味 | 本文で扱う深さ |
|---|---|---|
| A: 中核 | 複数Domain／Taskで主要な実装・選定対象になる、またはGenAIアプリケーションの中心的な実行基盤になる | 単独またはサービスファミリー単位で、主要機能、管理境界、API、セキュリティ、可観測性、料金要因、関連Taskまで説明する |
| B: 重要 | 特定Taskの主要な実装選択肢、連携先、データ基盤、セキュリティ／運用Controlになる | 試験範囲に関係する機能、Aサービスとの接続点、選択時に確認する制約を説明する |
| C: 関連 | 公式In-Scopeだが、Taskでの役割が限定的または特定シナリオ向けである | 何をするサービスか、どの構成で接続するか、A／Bサービスとの境界を識別できる深さにする |

同じサービスでもTaskによって重要度は変わり得る。例えばAmazon S3はRAGのデータソース、Prompt repository、Log保存先、Lifecycle controlとして複数Taskに関係するためAとする。一方、Amazon EBSは特定のCompute構成で必要になるが、AIP-C01のTaskから直接問われる機能範囲は狭いためCとする。

## ページ共通のサブ目次

各本文は、サービス固有の主要機能サブ目次に加えて次の共通項目を持つ。

1. サービスの役割と利用者が管理する範囲
2. 主要機能と処理の流れ
3. API、Event、Dataの入出力
4. IAM、暗号化、Network、Data保護
5. Metric、Log、Trace、監査
6. 可用性、Scaling、Quota、料金要因
7. AIP-C01の対応Task・Skill
8. 関連するliteral／supplimental page
9. 公式URLと最終確認日

## 第1部: A — 中核サービス

最初に読む13ページ。Bedrockを中心に、実行、データ、Orchestration、API、Security、Observabilityの骨格を作る。

| 予定ファイル | 対象サービス／機能 | 主な対応Task | サービス固有の主要機能サブ目次 |
|---|---|---|---|
| `01-01-amazon-bedrock.md` | Amazon Bedrock、Amazon Titan | 1.1〜1.3、1.5〜1.6、2.2、2.4〜2.5、3.1〜3.4、4.1〜4.3、5.1〜5.2 | 1. Model catalog・Model card・Amazon Titan<br>2. Bedrock Runtime endpointとConverse／Invoke／Responses／Chat Completions<br>3. Streaming・Async／Batch inference<br>4. On-demand・Provisioned Throughput・Service tier<br>5. Inference profile・Cross-Region inference・Prompt routing<br>6. Model customization・Custom model import・Model lifecycle<br>7. Structured outputs・Tool use・Prompt caching<br>8. Guardrails・Model Evaluation・Data Automation<br>9. Model Invocation Logging・CloudWatch metrics・CloudTrail<br>10. Region・Quota・料金・Data protection |
| `01-02-bedrock-knowledge-bases.md` | Amazon Bedrock Knowledge Bases | 1.4〜1.5、3.1、4.2〜4.3、5.1〜5.2 | 1. Managed／Customer-managed Knowledge Base<br>2. Data source・Connector・ACL<br>3. Parsing・Chunking・Embedding<br>4. Vector Store・Index・Metadata<br>5. Data ingestion・Sync・削除<br>6. Semantic／Hybrid search・Metadata filter<br>7. Reranking・Query decomposition・Agentic retrieval<br>8. Retrieve／RetrieveAndGenerate・Citation<br>9. Multimodal retrieval<br>10. Evaluation・Trace・運用Metric |
| `01-03-bedrock-agentcore.md` | Amazon Bedrock AgentCore | 2.1、2.5、3.1〜3.2、4.3、5.1 | 1. AgentCore全体とFramework／Model非依存性<br>2. HarnessとRuntime<br>3. Memory<br>4. Gateway・MCP・Tool schema<br>5. Identity<br>6. Browser・Code Interpreter<br>7. Observability・OpenTelemetry<br>8. Evaluations・Optimization<br>9. Policy・Registry<br>10. Session isolation・権限境界・料金要因 |
| `01-04-bedrock-prompt-management-and-flows.md` | Amazon Bedrock Prompt Management、Amazon Bedrock Prompt Flows | 1.6、2.5、3.4、5.2 | 1. Prompt・Variable・Variant<br>2. Test・Version・Lifecycle<br>3. FM／Inference configuration・Guardrailとの関連付け<br>4. Flow nodeと型<br>5. Condition・Iterator・Collector<br>6. Lambda・Knowledge Base・Prompt node<br>7. Test・Version・Alias<br>8. Trace・権限・Quota |
| `01-05-amazon-sagemaker-ai.md` | Amazon SageMaker AI、Clarify、Data Wrangler、Ground Truth、JumpStart、Model Monitor、Model Registry、Neo、Processing、Unified Studio | 1.2〜1.3、2.2、3.3〜3.4、4.1〜4.3、5.1 | 1. SageMaker AIと統合SageMakerの境界<br>2. Data Wrangler・ProcessingによるFM入力前処理<br>3. JumpStartとModel artifact<br>4. Endpoint・Inference option・Auto Scaling<br>5. Model Registry・Model Cards・Deployment guardrail<br>6. Clarify・Ground Truth・Augmented AI<br>7. Model Monitor<br>8. Neoと推論最適化<br>9. Unified Studio・Security・MLOps<br>10. AIP-C01で対象外となるModel開発・Trainingとの境界 |
| `01-06-aws-lambda.md` | AWS Lambda | 1.2〜1.5、2.1〜2.5、3.1〜3.4、5.2 | 1. Function・Runtime・Execution environment<br>2. Sync／Async invocation・Event source mapping<br>3. Version・Alias・Layer<br>4. Concurrency・Scaling・Timeout<br>5. Retry・DLQ／Destination・冪等性<br>6. Function URL・Streaming response<br>7. IAM execution role・VPC接続・Secrets<br>8. Log・Metric・Trace<br>9. FM前後処理・Tool／MCP実装 |
| `01-07-aws-step-functions.md` | AWS Step Functions | 1.2、1.5〜1.6、2.1、2.3〜2.5、3.1、5.1 | 1. Standard／Express Workflow<br>2. State・Input／Output processing<br>3. AWS SDK／Optimized service integration<br>4. Choice・Map・Parallel・Wait<br>5. Retry・Catch・Timeout<br>6. Callback・Human approval<br>7. Agent loop・停止条件・Circuit breaker<br>8. Execution history・Logging・Tracing<br>9. Version・Alias・Distributed Map |
| `01-08-amazon-api-gateway.md` | Amazon API Gateway | 1.2、2.1、2.3〜2.5、3.1、5.2 | 1. REST／HTTP／WebSocket API<br>2. Route・Method・Integration<br>3. Request／Response transformation・Validation<br>4. AuthN／AuthZ・Resource policy<br>5. Throttling・Quota・Usage plan<br>6. Streaming／SSE／WebSocketの境界<br>7. Cache・Stage・Deployment<br>8. Access log・Execution log・X-Ray<br>9. Private API・VPC link・WAF |
| `01-09-amazon-s3.md` | Amazon S3、S3 Intelligent-Tiering、S3 Lifecycle policies、S3 Cross-Region Replication | 1.3〜1.6、2.2、3.2〜3.3、4.1 | 1. Bucket・Object・Key・Metadata・Tag<br>2. Storage class・Intelligent-Tiering<br>3. Versioning・Object Lock<br>4. Lifecycle・Retention・削除<br>5. Event notification<br>6. Replication・Cross-Region Replication<br>7. Encryption・Bucket policy・Access Point<br>8. RAG data source・Model artifact・Prompt／Log repository<br>9. Consistency・Transfer・料金要因 |
| `01-10-amazon-opensearch-service.md` | Amazon OpenSearch Service | 1.4〜1.5、4.2〜4.3、5.2 | 1. Managed domain／Serverless collection<br>2. Document・Index・Mapping<br>3. Vector engine・k-NN・Dimension<br>4. Neural search・Embedding integration<br>5. Keyword／Semantic／Hybrid search<br>6. Filter・Scoring・Rerankingとの境界<br>7. Shard・Replica・Multi-index<br>8. Security・Network・Fine-grained access control<br>9. Ingestion・Index lifecycle・Snapshot<br>10. Query／Cluster metricと性能調整 |
| `01-11-amazon-cloudwatch.md` | Amazon CloudWatch、CloudWatch Logs、CloudWatch Synthetics | 1.3、1.6、3.2〜3.4、4.1〜4.3、5.2 | 1. Metric・Namespace・Dimension<br>2. Alarm・Composite alarm・Anomaly detection<br>3. Log group／Stream・Retention<br>4. Logs Insights<br>5. Dashboard<br>6. Synthetics Canary<br>7. Embedded Metric Format・Application signal<br>8. Bedrock runtime metric・Invocation log<br>9. Quality／Token／Cost／Business KPI<br>10. Redaction・Access control・料金要因 |
| `01-12-aws-iam.md` | IAM、IAM Access Analyzer、IAM Identity Center | 2.1、2.3、3.1〜3.3 | 1. Principal・User・Role・Session<br>2. Identity／Resource-based policy<br>3. Policy evaluation・Explicit deny<br>4. Temporary credential・STS・Federation<br>5. Service role・Service-linked role・PassRole<br>6. Condition key・Tag・Permission boundary<br>7. Cross-account access<br>8. Access Analyzer<br>9. IAM Identity Center<br>10. Bedrock・Data・Toolの最小権限 |
| `01-13-aws-glue.md` | AWS Glue | 1.3、3.2〜3.3 | 1. Data Catalog・Database・Table<br>2. Crawler・Classifier<br>3. ETL Job・Trigger・Workflow<br>4. Glue Studio<br>5. Data QualityとRuleset<br>6. Schema Registry<br>7. Data lineage・Source attribution<br>8. IAM・Encryption・Network<br>9. Metric・Log・Cost |

## 第2部: B — 重要な連携・基盤サービス

Aのサービスと組み合わせて設計判断に使う13ページ。ページ内では、近い責務を持つサービスの違いも整理する。

| 予定ファイル | 対象サービス／機能 | 主な対応Task | サービス固有の主要機能サブ目次 |
|---|---|---|---|
| `02-01-amazon-rds-and-aurora.md` | Amazon RDS、Amazon Aurora | 1.4〜1.5、3.2、4.2〜4.3 | 1. RDSとAuroraの管理境界<br>2. DB instance／Cluster・Storage<br>3. PostgreSQLとpgvector<br>4. Vector index・Metadata・Hybrid search<br>5. Data API・Connection management<br>6. Backup・Replica・Failover<br>7. IAM DB認証・Secrets・Encryption・Network<br>8. Metric・Log・Scaling・料金要因 |
| `02-02-amazon-dynamodb.md` | Amazon DynamoDB、DynamoDB Streams | 1.4、1.6、2.1、4.1 | 1. Table・Item・Primary key・Secondary index<br>2. Eventually／Strongly consistent read<br>3. On-demand／Provisioned capacity<br>4. Conditional write・Transaction・Idempotency<br>5. TTL<br>6. Streams・Change data capture<br>7. Global Tables・Backup<br>8. Session／Conversation state・Metadata<br>9. IAM・Encryption・Metric |
| `02-03-event-and-message-integration.md` | Amazon EventBridge、Amazon SQS、Amazon SNS、AWS AppConfig | 1.2、2.3〜2.4、4.1 | 1. EventBridge Bus・Rule・Target・Schema<br>2. Scheduler・Archive・Replay<br>3. SQS Standard／FIFO・Visibility timeout・DLQ<br>4. SNS Topic・Subscription・Fan-out<br>5. Event／Queue／Pub-Subの責務分担<br>6. AppConfig configuration・Environment・Deployment strategy<br>7. Retry・Ordering・Deduplication・Idempotency<br>8. Encryption・Policy・Monitoring |
| `02-04-compute-and-containers.md` | Amazon EC2、AWS App Runner、Amazon ECR、Amazon ECS、Amazon EKS、AWS Fargate | 2.1〜2.3、4.1〜4.2 | 1. VM／Managed web service／Container orchestrationの境界<br>2. EC2 instance・AMI・GPU・Auto Scaling<br>3. ECR repository・Image scan・Lifecycle<br>4. ECS Task／Service・Cluster<br>5. EKS Pod／Node／Managed control plane<br>6. Fargate serverless compute<br>7. App Runner source-to-service<br>8. MCP server・Custom model hosting<br>9. IAM role・Network・Log・Scaling・Cost |
| `02-05-iac-and-cicd.md` | AWS CDK、AWS CloudFormation、AWS CodeArtifact、AWS CodeBuild、AWS CodeDeploy、AWS CodePipeline | 1.2、2.3、3.3、5.1 | 1. CloudFormation Stack・Change set・Drift<br>2. CDK Construct・Synthesis・Bootstrap<br>3. CodeArtifact repository・Package policy<br>4. CodeBuild project・Buildspec・Artifact<br>5. CodeDeploy strategy・Rollback<br>6. CodePipeline Stage・Action・Approval<br>7. Prompt／Model／InfrastructureのVersion連携<br>8. Security scan・Quality gate・Canary |
| `02-06-developer-tools.md` | AWS CLI、AWS Tools and SDKs、Kiro、Amazon Q Developer | 1.3、2.4〜2.5、5.2 | 1. CLI profile・Credential chain・Output<br>2. SDK client・Request／Response・Paginator<br>3. Retry mode・Timeout・Backoff／Jitter<br>4. Waiter・Idempotency token<br>5. Kiroの仕様駆動開発支援<br>6. Q DeveloperのCode生成・Refactor・Test・Troubleshooting<br>7. Telemetry・権限・生成物Review |
| `02-07-amazon-comprehend.md` | Amazon Comprehend | 1.3、1.6、3.1〜3.2 | 1. Entity・Key phrase・Language・Sentiment<br>2. Syntax・Topic・Classification<br>3. PII detection・Redaction<br>4. Sync／Async analysis<br>5. Custom classification／Entity recognition<br>6. FM前処理・Intent補助・Safety filter<br>7. IAM・Encryption・Quota・料金要因 |
| `02-08-multimodal-ai-services.md` | Amazon Textract、Amazon Transcribe、Amazon Rekognition | 1.3、2.5、3.2 | 1. Textract OCR・Form・Table・Query・Expense／ID<br>2. Transcribe Batch／Streaming・Speaker・Vocabulary<br>3. Rekognition Image／Video・Label・Text・Moderation<br>4. Sync／Async処理とJob lifecycle<br>5. S3／EventBridge／Lambda連携<br>6. Bedrock Data Automationとの責務境界<br>7. PII・Encryption・Region・Cost |
| `02-09-data-protection-services.md` | AWS KMS、AWS Encryption SDK、AWS Secrets Manager、Amazon Macie | 3.1〜3.3 | 1. KMS key・Data key・Envelope encryption<br>2. Key policy・Grant・Rotation・Multi-Region key<br>3. Encryption SDKとEncryption context<br>4. Secrets Manager secret・Version・Rotation<br>5. Macie sensitive data discovery・Finding<br>6. Prompt／Log／S3／Vector StoreのData保護<br>7. Audit・Alert・料金要因 |
| `02-10-network-and-hybrid-connectivity.md` | Amazon VPC、AWS PrivateLink、AWS Outposts、AWS Wavelength | 1.2、2.3、3.2 | 1. VPC・Subnet・Route・Security group・NACL<br>2. Internet／NAT／Private accessの経路<br>3. Interface VPC endpoint・PrivateLink<br>4. Bedrock／SageMaker／Data serviceのPrivate接続<br>5. DNSとEndpoint policy<br>6. OutpostsのOn-premises実行境界<br>7. WavelengthのEdge実行境界<br>8. Data residency・Latency・可用性 |
| `02-11-frontend-identity-and-graphql.md` | AWS Amplify、Amazon Cognito、AWS AppSync | 2.3、2.5、3.2 | 1. Amplify hosting・Build・Backend連携<br>2. UI componentとGenAI interface<br>3. Cognito User Pool／Identity Pool<br>4. Federation・Token・Group<br>5. AppSync GraphQL schema・Resolver・Subscription<br>6. Real-time update・Offline access<br>7. API Gatewayとの境界<br>8. AuthN／AuthZ・Log・Cost |
| `02-12-audit-and-distributed-tracing.md` | AWS CloudTrail、AWS X-Ray | 1.6、2.4〜2.5、3.3〜3.4、4.3、5.2 | 1. CloudTrail Management／Data event<br>2. Event history・Trail・Event data store<br>3. Log file validation<br>4. X-Ray Trace・Segment・Subsegment<br>5. Sampling・Annotation・Service map<br>6. Request／Correlation ID<br>7. Bedrock control plane・Application log・Traceの境界<br>8. Forensics・Retention・料金要因 |
| `02-13-cost-and-architecture-governance.md` | AWS Cost Explorer、AWS Cost Anomaly Detection、AWS Auto Scaling、AWS Well-Architected Tool | 1.1、2.2〜2.3、4.1〜4.3 | 1. Cost ExplorerのDimension・Filter・Forecast<br>2. Cost allocation tag<br>3. Cost Anomaly monitor・Subscription<br>4. Auto Scaling policy・Metric・Cooldown<br>5. Well-Architected review・Lens・Milestone<br>6. Generative AI Lens<br>7. Token／Capacity／QualityのCost driver<br>8. Alert・改善記録・料金確認 |

## 第3部: C — 関連サービスの概要

公式In-Scopeを漏らさず、特定シナリオでの役割とA／Bサービスとの接続点を確認する7ページ。各サービスの全機能は対象にしない。

| 予定ファイル | 対象サービス／機能 | 関係する主な領域 | サービス固有の主要機能サブ目次 |
|---|---|---|---|
| `03-01-analytics-streaming-and-visualization.md` | Amazon Athena、Amazon EMR、Amazon Kinesis、Amazon MSK、Amazon Quick Sight、Amazon Managed Grafana | Data処理、Streaming、評価Report、Dashboard | 1. Athena SQL queryとS3<br>2. EMR cluster／Serverlessと分散処理<br>3. Kinesis Stream・Shard・Consumer<br>4. MSK Broker・Topic・Consumer group<br>5. Quick Sight Dataset・Dashboard<br>6. Managed Grafana Datasource・Dashboard<br>7. Glue／S3／CloudWatchとの接続 |
| `03-02-enterprise-data-transfer.md` | Amazon AppFlow、AWS DataSync、AWS Transfer Family | Enterprise data integration、RAG ingestion | 1. AppFlow Connection・Flow・Trigger・Mapping<br>2. DataSync Agent・Location・Task<br>3. Transfer Family Endpoint・Protocol・Identity provider<br>4. Full／Incremental transfer<br>5. S3／EFSとの接続<br>6. Encryption・Network・Monitoring |
| `03-03-business-ai-applications.md` | Amazon Connect、Amazon Kendra、Amazon Lex、Amazon Q Business、Amazon Q Business Apps、Amazon Quick | Customer／Employee interface、Enterprise search | 1. Connect Contact flow・Channel・Analytics<br>2. Kendra Index・Datasource・Query<br>3. Lex Bot・Intent・Slot・Fulfillment<br>4. Q Business Application・Index・Retriever・Plugin<br>5. Q Business Apps<br>6. Amazon Quick<br>7. Bedrock／Lambda／Identityとの境界 |
| `03-04-document-cache-and-graph-databases.md` | Amazon DocumentDB、Amazon ElastiCache、Amazon Neptune | State、Cache、Graph／Vector retrieval | 1. DocumentDB Document model・Cluster<br>2. ElastiCache Redis／Valkey／MemcachedとCaching<br>3. Neptune Graph model・Query・Analytics<br>4. Session／Semantic cache／Knowledge graph<br>5. Bedrock Knowledge Basesとの接続<br>6. Security・Scaling・Monitoring |
| `03-05-edge-and-content-delivery.md` | AWS Lambda@Edge、Amazon CloudFront、Elastic Load Balancing、AWS Global Accelerator、Amazon Route 53、AWS WAF | Edge delivery、Global availability、API protection | 1. CloudFront Distribution・Origin・Cache behavior<br>2. Lambda@Edge event<br>3. ELB ALB／NLBとTarget<br>4. Global Accelerator Endpoint group<br>5. Route 53 Routing policy・Health check<br>6. WAF Web ACL・Rule・Rate control<br>7. Streaming・Cache・Failover・Security |
| `03-06-block-and-file-storage.md` | Amazon EBS、Amazon EFS | Custom hosting、Container／Endpoint storage | 1. EBS Volume・Snapshot・Performance<br>2. EFS File system・Mount target・Access point<br>3. EC2／ECS／EKS／SageMakerとの接続<br>4. Encryption・Backup・Lifecycle<br>5. Throughput・Availability・Cost |
| `03-07-operations-and-platform-governance.md` | AWS Chatbot、AWS Service Catalog、AWS Systems Manager | Alert、Approved environment、Operations | 1. Chat notificationとChatOps<br>2. Service Catalog Portfolio・Product・Constraint<br>3. Systems Manager Parameter Store・Run Command・Automation<br>4. Approved GenAI componentの配布<br>5. Incident response・Secretとの境界<br>6. IAM・Audit・Monitoring |

## 公式In-Scope一覧との対応

2026-09-22時点の公式一覧にある106項目を、上記33ページへ次のように収録する。公式一覧はサービスとサービス内機能を別項目として含むため、項目数はサービス数と同義ではない。

| 公式カテゴリ | 公式In-Scope項目 → 収録予定ページ |
|---|---|
| Analytics | Amazon Athena → `03-01`、Amazon EMR → `03-01`、AWS Glue → `01-13`、Amazon Kinesis → `03-01`、Amazon OpenSearch Service → `01-10`、Amazon Quick Sight → `03-01`、Amazon MSK → `03-01` |
| Application Integration | Amazon AppFlow → `03-02`、AWS AppConfig → `02-03`、Amazon EventBridge → `02-03`、Amazon SNS → `02-03`、Amazon SQS → `02-03`、AWS Step Functions → `01-07` |
| Compute | AWS App Runner → `02-04`、Amazon EC2 → `02-04`、AWS Lambda → `01-06`、AWS Lambda@Edge → `03-05`、AWS Outposts → `02-10`、AWS Wavelength → `02-10` |
| Containers | Amazon ECR → `02-04`、Amazon ECS → `02-04`、Amazon EKS → `02-04`、AWS Fargate → `02-04` |
| Customer Engagement | Amazon Connect → `03-03` |
| Database | Amazon Aurora → `02-01`、Amazon DocumentDB → `03-04`、Amazon DynamoDB → `02-02`、Amazon DynamoDB Streams → `02-02`、Amazon ElastiCache → `03-04`、Amazon Neptune → `03-04`、Amazon RDS → `02-01` |
| Developer Tools | AWS Amplify → `02-11`、AWS CDK → `02-05`、AWS CLI → `02-06`、AWS CloudFormation → `02-05`、AWS CodeArtifact → `02-05`、AWS CodeBuild → `02-05`、AWS CodeDeploy → `02-05`、AWS CodePipeline → `02-05`、Kiro → `02-06`、AWS Tools and SDKs → `02-06`、AWS X-Ray → `02-12` |
| Machine Learning | Amazon Augmented AI → `01-05`、Amazon Bedrock → `01-01`、Amazon Bedrock AgentCore → `01-03`、Amazon Bedrock Knowledge Bases → `01-02`、Amazon Bedrock Prompt Management → `01-04`、Amazon Bedrock Prompt Flows → `01-04`、Amazon Comprehend → `02-07`、Amazon Kendra → `03-03`、Amazon Lex → `03-03`、Amazon Q Business → `03-03`、Amazon Q Business Apps → `03-03`、Amazon Q Developer → `02-06`、Amazon Quick → `03-03`、Amazon Rekognition → `02-08`、Amazon SageMaker AI → `01-05`、Amazon SageMaker Clarify → `01-05`、Amazon SageMaker Data Wrangler → `01-05`、Amazon SageMaker Ground Truth → `01-05`、Amazon SageMaker JumpStart → `01-05`、Amazon SageMaker Model Monitor → `01-05`、Amazon SageMaker Model Registry → `01-05`、Amazon SageMaker Neo → `01-05`、Amazon SageMaker Processing → `01-05`、Amazon SageMaker Unified Studio → `01-05`、Amazon Textract → `02-08`、Amazon Titan → `01-01`、Amazon Transcribe → `02-08` |
| Management and Governance | AWS Auto Scaling → `02-13`、AWS Chatbot → `03-07`、AWS CloudTrail → `02-12`、Amazon CloudWatch → `01-11`、Amazon CloudWatch Logs → `01-11`、Amazon CloudWatch Synthetics → `01-11`、AWS Cost Anomaly Detection → `02-13`、AWS Cost Explorer → `02-13`、Amazon Managed Grafana → `03-01`、AWS Service Catalog → `03-07`、AWS Systems Manager → `03-07`、AWS Well-Architected Tool → `02-13` |
| Migration and Transfer | AWS DataSync → `03-02`、AWS Transfer Family → `03-02` |
| Networking and Content Delivery | Amazon API Gateway → `01-08`、AWS AppSync → `02-11`、Amazon CloudFront → `03-05`、Elastic Load Balancing（ELB）→ `03-05`、AWS Global Accelerator → `03-05`、AWS PrivateLink → `02-10`、Amazon Route 53 → `03-05`、Amazon VPC → `02-10` |
| Security, Identity, and Compliance | Amazon Cognito → `02-11`、AWS Encryption SDK → `02-09`、IAM → `01-12`、IAM Access Analyzer → `01-12`、IAM Identity Center → `01-12`、AWS KMS → `02-09`、Amazon Macie → `02-09`、AWS Secrets Manager → `02-09`、AWS WAF → `03-05` |
| Storage | Amazon EBS → `03-06`、Amazon EFS → `03-06`、Amazon S3 → `01-09`、Amazon S3 Intelligent-Tiering → `01-09`、Amazon S3 Lifecycle policies → `01-09`、Amazon S3 Cross-Region Replication → `01-09` |

## 推奨する作成順

1. 第1部の`01-01`〜`01-04`でBedrock familyを作る。
2. `01-06`〜`01-12`で実行、Orchestration、API、Data、Observability、Identityの基本経路を作る。
3. `01-05`と`01-13`でSageMaker AIとData processingを補う。
4. 第2部を、対応するliteral pageの作成順に合わせて追加する。
5. 第3部はA／Bページから実際に参照する接続点を確認しながら追加する。

## 執筆・レビューの運用

- 通常執筆: [`textbook_service_page_writer`](../agents/service-page-writer.md)（Sol／medium）
- レビュー: [`textbook_service_page_reviewer`](../agents/service-page-reviewer.md)（Terra／high）
- `ESCALATE`時の再構成: [`textbook_service_page_writer_high`](../agents/service-page-writer-high.md)（Sol／high、1ページにつき1回まで）
- 割り当て: [`service-page-assignment-template.md`](../agents/service-page-assignment-template.md)
- 本文の出発点: [`service-page.md`](../templates/service-page.md)
- 横断監査: [`textbook_cross_page_auditor`](../agents/cross-page-auditor.md)（Luna／medium、読み取り専用）

同じサービスページの通常執筆、レビュー、昇格執筆を同時に実行しない。目次、状態、共通テンプレートはオーケストレーターだけが更新する。

本文作成後は、サービス名や機能名の一致だけで完了としない。各サブ目次について「入力」「処理」「出力」「利用者が管理する範囲」「代表的な連携先」を説明できることを確認する。

Bedrockの対応API、AgentCoreの構成要素、Knowledge Basesの検索機能、OpenSearchのNeural／Vector機能、Aurora Data API、LambdaのResponse streaming、CloudWatchで扱うGenAI指標、ECRのImage scanningなどは提供状況や適用条件が変わり得る。本文作成時に公式の対応Region、API、Engine／Runtime version、統合条件を再確認し、確認日を記録する。

## 公式根拠

- [AIP-C01 Exam Guide](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html) — Domain、Task、Skill
- [In-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/aip-01-in-scope-services.html) — 公式対象サービス／機能一覧
- [Domain 1](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html) — FM統合、Data、RAG、Prompt
- [Domain 2](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html) — Agent、Deployment、Integration、API
- [Domain 3](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html) — Safety、Security、Governance
- [Domain 4](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html) — Cost、Performance、Monitoring
- [Domain 5](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html) — Evaluation、Troubleshooting
- [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/) — Bedrock familyの機能構成
- [Amazon Bedrock AgentCore Developer Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) — AgentCoreの構成要素
- [Amazon SageMaker AI documentation](https://docs.aws.amazon.com/sagemaker/) — SageMaker AI familyの機能構成

公式情報の最終確認日: 2026-09-22
