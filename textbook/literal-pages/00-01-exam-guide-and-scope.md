# AIP-C01試験ガイドと出題範囲

## このページの位置づけ

| 項目 | 内容 |
|---|---|
| 対応Task | `PREP-01` |
| 対応Skills | なし（準備タスク。本編20 Task・98 Skillsの構造と範囲を扱う） |
| 対象読者 | AIP-C01の学習を始める人、または最新の公式範囲を確認したい人 |
| このページで分かること | 対象者、試験構成、5ドメインと20 Task、出題され得る技術・概念、対象・対象外サービス、公式準備リソース |
| 前提知識 | AWSの基本的なサービス分類と、生成AIアプリケーションの概要 |
| 対応する補足ページ | [`00-01-exam-guide-and-scope.md`](../supplimental-pages/00-01-exam-guide-and-scope.md) |

## まず全体像

AWS Certified Generative AI Developer - Professional（AIP-C01）は、Foundation Model（FM）をアプリケーションや業務ワークフローへ統合し、AWS上の本番環境へ生成AIソリューションを実装する能力を確認する試験である。

公式試験ガイドは、出題範囲を5つのContent Domainに分け、各DomainをTaskとSkillへ展開している。技術・概念およびAWSサービスの一覧も示されるが、いずれも非網羅的で、変更される可能性がある。試験ガイド自体も、試験内容の完全な一覧ではないと明記している。

## 対象者と確認される能力

対象者には、AWSまたはオープンソース技術を使った本番品質のアプリケーション構築経験が2年以上、一般的なAI／機械学習またはデータエンジニアリングの経験、生成AIソリューションを実装した実務経験が1年あることが想定されている。

推奨されるAWS知識は次のとおりである。

- Compute、Storage、Networkingサービスの利用経験
- AWSのセキュリティベストプラクティスとIdentity管理の理解
- DeploymentとInfrastructure as Code（IaC）ツールの利用経験
- MonitoringとObservabilityサービスへの習熟
- AWSのコスト最適化原則の理解

試験では、主に次の能力が確認される。

- Vector Store、Retrieval Augmented Generation（RAG）、Knowledge Baseなどを使った生成AIアーキテクチャの設計と実装
- FMとアプリケーション／業務ワークフローの統合
- Prompt EngineeringとPrompt Management
- Agentic AIソリューションの実装
- コスト、性能、事業価値に対する生成AIアプリケーションの最適化
- Security、Governance、Responsible AIの実装
- 生成AIアプリケーションのTroubleshooting、Monitoring、Optimization
- FMの品質と責任ある利用に関する評価

一方、対象者が遂行できることを期待されない職務として、次が明記されている。この一覧も非網羅的である。

- モデルの開発と学習
- 高度な機械学習手法
- データエンジニアリングとFeature Engineering

## 現行の試験構成

2026-09-21時点の公式情報では、試験構成は次のとおりである。

| 項目 | 公式情報 |
|---|---|
| 試験時間 | 180分 |
| 問題数 | 75問 |
| 採点対象 | 65問 |
| 採点対象外 | 10問。将来の採点問題として評価するために使われ、受験者には識別されない |
| 問題形式 | Multiple choice（4選択肢から1つ）とMultiple response（5つ以上の選択肢から2つ以上） |
| 採点 | 100〜1,000のScaled score。合格点は750 |
| 合否判定 | 全体スコアで判定するCompensatory scoring。各Domainで個別に合格する必要はない |
| 受験方法 | Pearson VUEテストセンターまたはオンライン監督付き試験 |
| 提供言語 | 英語、日本語、韓国語、中国語（簡体字） |
| 受験料 | 300 USD。為替などの追加情報は公式Exam pricingを確認する |

未回答は不正解として扱われるが、推測回答に対する減点はない。受験料、提供方法、言語などは変更され得るため、申込時にも公式認定ページを確認する必要がある。

## 5ドメイン、配点、20 Task

配点は採点対象問題に対する比率である。

| Domain | 配点 | Task |
|---|---:|---|
| 1: Foundation Model Integration, Data Management, and Compliance | 31% | 1.1 要件分析と生成AIソリューション設計<br>1.2 FMの選定と設定<br>1.3 FM向けデータ検証・処理Pipelineの実装<br>1.4 Vector Storeソリューションの設計・実装<br>1.5 FM拡張のためのRetrieval機構の設計<br>1.6 FMとの対話に対するPrompt EngineeringとGovernanceの実装 |
| 2: Implementation and Integration | 26% | 2.1 Agentic AIソリューションとTool Integrationの実装<br>2.2 Model Deployment戦略の実装<br>2.3 Enterprise Integration Architectureの設計・実装<br>2.4 FM API Integrationの実装<br>2.5 Application Integration Patternと開発ツールの実装 |
| 3: AI Safety, Security, and Governance | 20% | 3.1 入力・出力Safety Controlの実装<br>3.2 Data SecurityとPrivacy Controlの実装<br>3.3 AI GovernanceとCompliance機構の実装<br>3.4 Responsible AI原則の実装 |
| 4: Operational Efficiency and Optimization for GenAI Applications | 12% | 4.1 コスト最適化とResource Efficiency戦略の実装<br>4.2 Application Performanceの最適化<br>4.3 生成AIアプリケーションのMonitoring Systemの実装 |
| 5: Testing, Validation, and Troubleshooting | 11% | 5.1 生成AIのEvaluation Systemの実装<br>5.2 生成AIアプリケーションのTroubleshooting |

5つの配点は合計100%であり、Taskは合計20である。各Taskの下には、試験で求められる具体的なSkillと実装例が定義されている。

## 出題され得る技術と概念

公式試験ガイドは、次の技術と概念を挙げている。これは非網羅的で変更され得る一覧であり、掲載順や配置は出題比率や重要度を表さない。

- Retrieval Augmented Generation（RAG）
- Vector DatabaseとEmbedding
- Prompt EngineeringとManagement
- Foundation Model（FM）Integration
- Agentic AI System
- Responsible AI Practice
- Content SafetyとModeration
- Model EvaluationとValidation
- AI WorkloadのCost Optimization
- AI ApplicationのPerformance Tuning
- AI SystemのMonitoringとObservability
- AI ApplicationのSecurityとGovernance
- API DesignとIntegration Pattern
- Event-driven Architecture
- Serverless Computing
- Container Orchestration
- Infrastructure as Code（IaC）
- AI Application向けCI/CD
- Hybrid Cloud Architecture
- Enterprise System Integration

## 対象となるAWSサービスと機能

In-Scope AWS Servicesは、主な機能別カテゴリに整理されている。公式一覧は非網羅的で変更され得る。

| カテゴリ | 対象サービス／機能 |
|---|---|
| Analytics | Amazon Athena、Amazon EMR、AWS Glue、Amazon Kinesis、Amazon OpenSearch Service、Amazon Quick Sight、Amazon Managed Streaming for Apache Kafka（Amazon MSK） |
| Application Integration | Amazon AppFlow、AWS AppConfig、Amazon EventBridge、Amazon SNS、Amazon SQS、AWS Step Functions |
| Compute | AWS App Runner、Amazon EC2、AWS Lambda、AWS Lambda@Edge、AWS Outposts、AWS Wavelength |
| Containers | Amazon ECR、Amazon ECS、Amazon EKS、AWS Fargate |
| Customer Engagement | Amazon Connect |
| Database | Amazon Aurora、Amazon DocumentDB、Amazon DynamoDB、Amazon DynamoDB Streams、Amazon ElastiCache、Amazon Neptune、Amazon RDS |
| Developer Tools | AWS Amplify、AWS CDK、AWS CLI、AWS CloudFormation、AWS CodeArtifact、AWS CodeBuild、AWS CodeDeploy、AWS CodePipeline、Kiro、AWS Tools and SDKs、AWS X-Ray |
| Machine Learning | Amazon Augmented AI、Amazon Bedrock、Amazon Bedrock AgentCore、Amazon Bedrock Knowledge Bases、Amazon Bedrock Prompt Management、Amazon Bedrock Prompt Flows、Amazon Comprehend、Amazon Kendra、Amazon Lex、Amazon Q Business、Amazon Q Business Apps、Amazon Q Developer、Amazon Quick、Amazon Rekognition、Amazon SageMaker AI、Amazon SageMaker Clarify、Amazon SageMaker Data Wrangler、Amazon SageMaker Ground Truth、Amazon SageMaker JumpStart、Amazon SageMaker Model Monitor、Amazon SageMaker Model Registry、Amazon SageMaker Neo、Amazon SageMaker Processing、Amazon SageMaker Unified Studio、Amazon Textract、Amazon Titan、Amazon Transcribe |
| Management and Governance | AWS Auto Scaling、AWS Chatbot、AWS CloudTrail、Amazon CloudWatch、Amazon CloudWatch Logs、Amazon CloudWatch Synthetics、AWS Cost Anomaly Detection、AWS Cost Explorer、Amazon Managed Grafana、AWS Service Catalog、AWS Systems Manager、AWS Well-Architected Tool |
| Migration and Transfer | AWS DataSync、AWS Transfer Family |
| Networking and Content Delivery | Amazon API Gateway、AWS AppSync、Amazon CloudFront、Elastic Load Balancing（ELB）、AWS Global Accelerator、AWS PrivateLink、Amazon Route 53、Amazon VPC |
| Security, Identity, and Compliance | Amazon Cognito、AWS Encryption SDK、IAM、IAM Access Analyzer、IAM Identity Center、AWS KMS、Amazon Macie、AWS Secrets Manager、AWS WAF |
| Storage | Amazon EBS、Amazon EFS、Amazon S3、Amazon S3 Intelligent-Tiering、Amazon S3 Lifecycle policies、Amazon S3 Cross-Region Replication |

試験では、よく知られたサービスの正式名称に略称や括弧書きが含まれる場合、公式の短縮名が使われる。各問題のHelpから、対象となる短縮名と正式名の一覧を参照できる。ただし、すべての略語が展開されるわけではなく、対象者が知っていることを期待される略語もある。

## 対象外となるAWSサービスと機能

Out-of-Scope AWS Servicesも非網羅的で、変更される可能性がある。対象職務とまったく関係しないAWSサービスは、この対象外一覧自体からも省略されている。

| カテゴリ | 対象外サービス／機能 |
|---|---|
| Application Integration | Amazon MQ |
| Analytics | AWS Clean Rooms、AWS Data Exchange、Amazon DataZone、Amazon FinSpace |
| Blockchain | Amazon Managed Blockchain（AMB） |
| Business Applications | Alexa for Business、Amazon Chime、AWS Wickr、Amazon WorkDocs、Amazon WorkMail |
| Cloud Financial Management | AWS Budgets、AWS Cost and Usage Report、Reserved Instance reports、AWS Savings Plans |
| Compute | AWS Batch、Amazon EC2 Image Builder、Amazon ECS Anywhere、Amazon EKS Anywhere、AWS Elastic Beanstalk、Amazon Lightsail、AWS Local Zones、AWS Serverless Application Repository |
| Containers | AWS App2Container、AWS Copilot、Red Hat OpenShift Service on AWS（ROSA） |
| Customer Engagement | Amazon SES |
| Database | Amazon Keyspaces、Amazon Quantum Ledger Database（Amazon QLDB）、Amazon Redshift、Amazon Timestream |
| Developer Tools | AWS Cloud9、AWS CloudShell、Amazon CodeGuru、AWS CodeStar、Amazon Corretto |
| End User Computing | Amazon AppStream 2.0、Amazon WorkLink、Amazon WorkSpaces、Amazon WorkSpaces Web |
| Frontend Web and Mobile | AWS Device Farm、Amazon Location Service、Amazon Pinpoint |
| Game Development | Amazon GameLift、Amazon Lumberyard |
| Internet of Things（IoT） | AWS IoT 1-Click、AWS IoT Analytics、AWS IoT Button、AWS IoT Core、AWS IoT Device Defender、AWS IoT Device Management、AWS IoT Events、AWS IoT FleetWise、AWS IoT Greengrass、AWS IoT SiteWise、AWS IoT TwinMaker |
| Management and Governance | AWS Console Mobile Application、AWS Health Dashboard、AWS License Manager、AWS Proton、AWS Trusted Advisor |
| Machine Learning | AWS DeepComposer、AWS DeepRacer、Amazon DevOps Guru、Amazon Forecast、Amazon Fraud Detector、Amazon HealthLake、Amazon Lookout for Equipment、Amazon Lookout for Metrics、Amazon Lookout for Vision、Amazon Monitron、AWS Panorama |
| Media Services | Amazon Elastic Transcoder、AWS Elemental MediaConnect、AWS Elemental MediaConvert、AWS Elemental MediaLive、AWS Elemental MediaPackage、AWS Elemental MediaStore、AWS Elemental MediaTailor、Amazon Interactive Video Service、Amazon Kinesis Video Streams、Amazon Nimble Studio |
| Migration and Transfer | AWS Application Discovery Service、AWS Application Migration Service、CloudEndure Migration、AWS Migration Hub、AWS Snow Family |
| Networking and Content Delivery | AWS App Mesh、AWS Cloud Map、AWS Direct Connect、AWS Private 5G、AWS Transit Gateway、AWS VPN |
| Quantum Technologies | Amazon Braket |
| Robotics | AWS RoboMaker |
| Satellite | AWS Ground Station |

## 公式の試験準備リソース

AWS認定ページは、AWS Skill Builder上のAIP-C01 Exam Prep Planを公式準備経路として案内している。このPlanは4段階で構成され、認定ページからOfficial Practice Question Setを使って試験形式の問題を確認するよう案内されている。

AWS Certification exam preparationページでは、Official Practice Question SetsとExam Prep Coursesを無料コンテンツとして案内している。一方、Official Practice Exams、Lab、追加のPractice QuestionなどはSubscription対象になり得る。無料／有料の区分や個別教材の提供状況は変更され得るため、利用時にSkill Builder上の表示を確認する必要がある。

## 重要な条件と制約

- 試験ガイドのDomain、Task、Skill、技術・概念、サービス一覧は、試験内容の完全な一覧ではない。
- 技術・概念、In-Scope Services、Out-of-Scope Servicesはいずれも非網羅的で、変更される可能性がある。
- In-Scope Servicesのカテゴリは主な機能に基づく分類である。
- 技術・概念一覧の順序は、出題比率や重要度を示さない。
- Domainの配点は採点対象問題に対する比率であり、各Domainを個別に合格する方式ではない。
- 受験料、受験方法、対応言語、Skill Builder教材の提供条件は変更され得るため、申込時・利用時に再確認する。

## 用語

| 用語 | このページでの意味 |
|---|---|
| Domain | 試験内容を大きな責務領域に分けた単位。配点が設定される |
| Task | Domain内で対象者が実行できることを求められる仕事の単位 |
| Skill | Taskを遂行するために必要な具体的能力。公式ガイドでは例示技術も伴う |
| Scored content | 合否に使われる採点対象問題 |
| Unscored content | 将来の利用評価のための採点対象外問題。受験中には識別できない |
| In-Scope | 公式ガイドが出題範囲として挙げるサービス／機能。ただし一覧は非網羅的 |
| Out-of-Scope | 公式ガイドが出題範囲外として挙げるサービス／機能。ただし一覧は非網羅的 |

## このページの要点

- AIP-C01は、本番品質の生成AIアプリケーションをAWSで設計、統合、保護、運用、評価する開発者の能力を確認する。
- 出題構造の中核は、配点を持つ5 Domainと、その下の20 Taskおよび98 Skillsである。
- 技術・概念とサービスの一覧は範囲確認に使えるが、非網羅的で変更され得る。
- モデル開発・学習、高度な機械学習、データ／Feature Engineeringは対象職務外である。
- 公式準備経路にはAIP-C01 Exam Prep PlanとOfficial Practice Question Setがあるが、教材の提供条件は利用時に再確認する。

## 公式資料

- [AIP-C01 Exam Guide](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html) — 対象者、対象外職務、問題形式、採点、Domain配点
- [Domain 1](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html) — Task 1.1〜1.6
- [Domain 2](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html) — Task 2.1〜2.5
- [Domain 3](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html) — Task 3.1〜3.4
- [Domain 4](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html) — Task 4.1〜4.3
- [Domain 5](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html) — Task 5.1〜5.2
- [Technologies and concepts](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-technologies-concepts.html) — 出題され得る技術と概念
- [Mentions of AWS services on the exam](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-service-mentions.html) — サービス短縮名とHelpの扱い
- [In-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/aip-01-in-scope-services.html) — 対象サービスと機能
- [Out-of-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/aip-01-out-of-scope-services.html) — 対象外サービスと機能
- [AWS Certified Generative AI Developer - Professional](https://aws.amazon.com/certification/certified-generative-ai-developer-professional/) — 試験時間、問題数、受験料、受験方法、言語、AIP-C01準備経路
- [AWS Certification exam preparation](https://aws.amazon.com/certification/certification-prep/) — 無料コンテンツとSubscription対象の区分
- [AIP-C01 Exam Prep Plan](https://skillbuilder.aws/category/exam-prep/generative-ai-developer-professional-AIP-C01) — AWS Skill Builder上の公式準備Plan

最終確認日: 2026-09-21
