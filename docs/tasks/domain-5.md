# Domain 5 実行タスク: テスト、検証、トラブルシューティング

配点11%、目安8時間。公式範囲は [Content Domain 5](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html) を基準にする。

## D5-01: GenAI evaluation systemを実装する（5時間）

公式・無料教材:

- [Amazon Bedrock evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html)
- [RAG evaluation metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-retrieve.html)
- [LLM-as-a-judge evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html)
- [AgentCore evaluators](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/create-evaluator.html)

作業:

- [ ] 30分: Offline／Online、Automatic／Human、Reference-based／Reference-free評価を読む
- [ ] 20分 — Skill 5.1.1: Relevance、Factual accuracy、Consistency、Fluency、Safety、Format complianceのRubricを定義する
- [ ] 20分 — Skill 5.1.2: Model、Prompt、ParameterをA/B比較し、Quality、Token、Latency、Cost、Business outcomeを同時に評価する計画を作る
- [ ] 20分 — Skill 5.1.3: Rating、Free-text、Correction、EscalationからUser feedbackを収集し、Sampling biasを記録する
- [ ] 20分 — Skill 5.1.4: Unit、Golden regression、Adversarial、Canary、Continuous evaluationをRelease quality gateへ配置する
- [ ] 20分 — Skill 5.1.5: Programmatic metric、LLM-as-a-judge、Human reviewを組み合わせ、Judge biasとCalibrationを扱う
- [ ] 20分 — Skill 5.1.6: Context relevance、Context coverage、Recall@k、Retrieval latencyを測定する
- [ ] 20分 — Skill 5.1.7: Task completion、Tool selection、Tool error recovery、Step数、Human handoffをAgent metricにする
- [ ] 20分 — Skill 5.1.8: 技術者向け詳細とStakeholder向け要約を分けたReport templateを作る
- [ ] 20分 — Skill 5.1.9: Synthetic user、Semantic drift、Hallucination、ConsistencyをCanaryとRollback条件にする
- [ ] 75分: ローカル評価Runnerで全Caseを回し、層化抽出した少量CaseだけをBedrockのModel／Prompt 2版で比較する。品質、Safety、Token、Latency、概算費用とSample数の制約を同じReportへ載せる
- [ ] 15分: 総合Scoreだけでなく、Case別の失敗とConfidence interval上の制約を報告する

成果物: Evaluation plan、Golden dataset、Rubric、比較Report、Release判定。

完了条件: Modelだけでなく、Retrieval、Prompt、Agent、End-to-endを分離して評価できる。

## D5-02: GenAI applicationをTroubleshootする（3時間）

公式・無料教材:

- [Amazon Bedrock API error codes](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html)
- [Bedrock Runtime metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-runtime-metrics.html)
- [Model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html)
- [Agent tracing](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html)

作業:

- [ ] 30分: 症状をInput、API、Model、Prompt、Retrieval、Tool、Output、Infrastructureに分けるTriage順を作る
- [ ] 20分 — Skill 5.2.1: Context overflow、Truncation、Chunk不足、入力形式不正を再現し、診断Signalと修正を対応付ける
- [ ] 20分 — Skill 5.2.2: Authentication、Validation、AccessDenied、Throttling、Timeout、5xxのLogとRetry可否を対応付ける
- [ ] 20分 — Skill 5.2.3: Prompt版、Parameter、入力分布、Model版を固定して差分を切り分ける手順を作る
- [ ] 20分 — Skill 5.2.4: Embedding mismatch、Stale index、Metadata filter、Chunking、top-k、Vector search latencyの診断手順を作る
- [ ] 20分 — Skill 5.2.5: Template変数、Schema、Prompt confusion、Version driftをLog、Trace、Regression testで調べる
- [ ] 35分: ローカルの5故障Fixtureを診断する。AWSではValidation、AccessDenied、ThrottlingまたはQuota関連のうち安全に再現できる2種を確認し、Error code、Retry可否、追加Costを切り分ける
- [ ] 15分: 症状、仮説、Evidence、Root cause、修正、再発防止をIncident reportへ残す

成果物: Troubleshooting decision tree、5件の診断結果、Incident report。

完了条件: 最初からPromptを調整せず、観測Signalを使ってComponentと原因を絞り込める。

## Domain 5 終了チェック

- [ ] Skills 5.1.1〜5.2.5の全項目を実施した
- [ ] [`docs/notes/domain-5-testing-troubleshooting.md`](../notes/domain-5-testing-troubleshooting.md) を更新した
- [ ] 品質Gateに合格しない変更をRejectまたはRollbackできる
- [ ] ローカル故障とAWS Service errorのSignal差を説明できる
- [ ] Domain 5の問題演習を行い、誤答を記録した
