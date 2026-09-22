# Domain 2 実行タスク: 実装と統合

配点26%、目安21時間。公式範囲は [Content Domain 2](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html) を基準にする。

## D2-01: Agentic AIとTool integrationを実装する（5時間）

公式・無料教材:

- [Tool use with Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html)
- [Amazon Bedrock AgentCore Developer Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
- [AWS Step Functions concepts](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- [Agent tracing](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html)

作業:

- [ ] 30分: Agent loop、Memory、State、Tool schema、Trace、停止条件を読む
- [ ] 25分 — Skill 2.1.1: Session state、短期履歴、長期Memory、Idempotency keyの保存先と有効期限を定義する
- [ ] 25分 — Skill 2.1.2: Plan→Act→Observe→Re-planのState machineを作り、最大Step数を設定する
- [ ] 25分 — Skill 2.1.3: Timeout、Budget、Tool allowlist、IAM境界、Circuit breaker、強制停止を設計する
- [ ] 25分 — Skill 2.1.4: 単一Agent、Supervisor型Multi-agent、Model ensembleを比較し、過剰設計になる条件も記す
- [ ] 25分 — Skill 2.1.5: 金額変更、個人情報参照、低信頼回答をHuman approvalへ送る規則を作る
- [ ] 25分 — Skill 2.1.6: `search_policy` と `create_ticket` のJSON Schema、Validation、Retry、Error responseを定義する
- [ ] 25分 — Skill 2.1.7: Lambda型のStateless MCP serverとECS型のStateful/long-running serverを比較する
- [ ] 80分: ローカルAgent loopへ2つのTool、停止条件、承認待ち、Traceを実装する。BedrockのTool useで正常な選択と不正引数を上限付きで試し、Application側のValidation／認可が必要なことをTraceで確認する
- [ ] 15分: Traceから失敗箇所を説明し、改善案を記録する

成果物: Agent state図、Tool schema、Agent実装、Trace 3件。

完了条件: ModelにToolを直接実行させず、Application側でValidation・認可・実行・結果返却を制御できる。

## D2-02: Model deployment strategyを実装する（3時間）

公式・無料教材:

- [Amazon Bedrock inference](https://docs.aws.amazon.com/bedrock/latest/userguide/inference.html)
- [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html)
- [Deploy models to SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html)

作業:

- [ ] 30分: On-demand、Provisioned Throughput、Batch inference、SageMaker endpointの課金と運用責任を読む
- [ ] 35分 — Skill 2.2.1: 低頻度、予測可能な高負荷、Custom modelの3ケースへLambda、Bedrock、SageMakerを割り当てる
- [ ] 35分 — Skill 2.2.2: Model load、GPU memory、Cold start、Token throughput、Container healthのLLM固有課題を一覧化する
- [ ] 35分 — Skill 2.2.3: Small model、Model cascading、Batch、Quantization/efficient servingを品質・資源の観点で比較する
- [ ] 30分: Blue/green、Canary、Quality gate、Rollbackを含むDeployment sequenceを作る
- [ ] 15分: 3つのTraffic patternについて採用案と却下案を説明する

成果物: `artifacts/deployment-strategy.md`。

完了条件: Traffic、Model customization、SLO、CostからHosting方式とDeployment方式を選べる。

## D2-03: Enterprise integration architectureを設計・実装する（5時間）

公式・無料教材:

- [Serverless agentic AI patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/)
- [Infrastructure as code for serverless AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/infrastructure-as-code.html)
- [CI/CD and automation for serverless AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/cicd-and-automation.html)

作業:

- [ ] 30分: API、Event、Batch、Workflow orchestrationの結合度と一貫性を比較する
- [ ] 35分 — Skill 2.3.1: Legacy system連携を同期API、EventBridge/SQS、定期同期の3方式で比較する
- [ ] 35分 — Skill 2.3.2: API Gateway、Lambda、EventBridge、Step Functionsを使う論理構成図を作る
- [ ] 35分 — Skill 2.3.3: User、Application、FM、Data、Toolごとに認証主体と最小権限を定義する
- [ ] 35分 — Skill 2.3.4: Cloud、On-premises、Edge間のData classification、Residency、Routing、暗号化を表にする
- [ ] 35分 — Skill 2.3.5: Code、Prompt、Evaluation data、IaCをVersion管理し、Test、Security scan、Approval、Canary、Rollbackを含むPipelineを設計する
- [ ] 80分: ローカルで同期API、非同期Queue、Dead-letter相当処理を実装する。短時間のAWS実験ではSQSなど最小のManaged componentを1つ使い、IAM、重複Message、可視性TimeoutまたはDLQの挙動を確認して削除する
- [ ] 15分: GenAI gatewayで集中管理するPolicy、Routing、Quota、Loggingを記録する

成果物: Enterprise構成図、権限表、CI/CD図、Queue統合テスト結果。

完了条件: 同期／非同期、Cloud／Hybrid、直接呼出し／Gatewayの選択理由を説明できる。

## D2-04: FM API integrationを実装する（4時間）

公式・無料教材:

- [Amazon Bedrock Runtime API](https://docs.aws.amazon.com/bedrock/latest/userguide/inference.html)
- [Converse API examples](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-examples.html)
- [Retry behavior in AWS SDKs](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html)

作業:

- [ ] 30分: Invoke、Converse、Streaming、Async/BatchのRequest/Responseと用途を読む
- [ ] 35分 — Skill 2.4.1: 同期処理、SQSを使う非同期処理、API GatewayによるValidationのSequence図を作る
- [ ] 35分 — Skill 2.4.2: Streaming、WebSocket、Server-Sent Eventsを比較し、切断・再接続時の振る舞いを定義する
- [ ] 35分 — Skill 2.4.3: Timeout、Exponential backoff＋Jitter、Throttling、Fallback、Idempotency、X-Ray traceを実装方針へ落とす
- [ ] 35分 — Skill 2.4.4: 静的Routing、内容ベースRouting、MetricベースRoutingのDecision tableを作る
- [ ] 55分: FM clientのTimeout、Retry、Rate limit、Fallback、Streaming eventを実装し、Bedrock Converse／Streamingを少量実行する。Validation errorとAccessDenied等の非Retry errorを実機または最小権限Testで確認し、Retry回数分のCostも記録する
- [ ] 15分: RetryすべきErrorとRetryしてはいけないErrorを整理する

成果物: API Sequence図、Resilience policy、Fault injection結果。

完了条件: API方式をUXと処理時間で選び、4xx・5xx・Throttling・Timeoutを別々に処理できる。

## D2-05: Application integration patternと開発Toolを実装する（4時間）

公式・無料教材:

- [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
- [Amazon Bedrock Flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html)
- [Amazon Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html)
- [AWS X-Ray Developer Guide](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)

作業:

- [ ] 30分: OpenAPI-first、Webhook、Workflow、Event-driven、No-code Flowの使い分けを読む
- [ ] 25分 — Skill 2.5.1: Streaming、Token limit、Request validation、Timeout、Retryを含むFM API契約を書く
- [ ] 25分 — Skill 2.5.2: Amplify UI、OpenAPI client、Prompt Flowの採用条件を比較する
- [ ] 25分 — Skill 2.5.3: CRM更新または文書処理を題材に、Lambda、Step Functions、Data Automationの役割を図示する
- [ ] 25分 — Skill 2.5.4: Amazon Q Developerが支援できる作業と、人がReviewすべきSecurity・Correctness項目を分ける
- [ ] 25分 — Skill 2.5.5: Prompt chaining、Agent、Step Functions orchestration、Multi-agentの境界をDecision tableにする
- [ ] 25分 — Skill 2.5.6: Logs Insights、X-Ray、Application logをCorrelation IDでつなぐ調査手順を書く
- [ ] 45分: ラボAPIのOpenAPI仕様とCorrelation ID付き構造化Logを作り、Bedrock Request 1件をApplication log、CloudWatch Metric、CloudTrail Eventの取得可能な範囲で追跡する。Prompt／Response本文を既定で記録しない
- [ ] 15分: 利用者、運用者、開発者の各Interfaceをレビューする

成果物: OpenAPI仕様、Integration decision table、End-to-end trace。

完了条件: Integration patternを、処理時間、結合度、User experience、監査性で比較できる。

## Domain 2 終了チェック

- [ ] Skills 2.1.1〜2.5.6の全項目を実施した
- [ ] [`docs/notes/domain-2-implementation.md`](../notes/domain-2-implementation.md) を更新した
- [ ] Agent、API、Queue、Toolの正常系・Timeout・不正入力を試した
- [ ] Bedrock APIまたはAWS Managed componentの実測と削除確認を残した
- [ ] Domain 2の問題演習を行い、誤答を記録した
