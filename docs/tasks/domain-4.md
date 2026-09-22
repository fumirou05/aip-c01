# Domain 4 実行タスク: 運用効率と最適化

配点12%、目安10時間。公式範囲は [Content Domain 4](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html) を基準にする。

## D4-01: Cost optimizationとResource efficiencyを実装する（3時間）

公式・無料教材:

- [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)
- [Prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)
- [Application inference profiles and cost attribution](https://docs.aws.amazon.com/bedrock/latest/userguide/cost-mgmt-application-inference-profiles.html)
- [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html)

作業:

- [ ] 30分: On-demand、Batch、Provisioned Throughput、CachingのCost driverを読む。単価は実施日に再確認する
- [ ] 25分 — Skill 4.1.1: Input/output token、Context、Prompt compression、Response limit、Context pruningの削減策を優先順位付けする
- [ ] 25分 — Skill 4.1.2: Query complexityに応じたSmall／Large modelのRoutingとQuality floorを定義する
- [ ] 25分 — Skill 4.1.3: Batch、Concurrency、Capacity、Auto scaling、Provisioned Throughputの採用条件を表にする
- [ ] 25分 — Skill 4.1.4: Exact、Semantic、Edge、Prompt cachingのKey、TTL、Invalidation、Privacy riskを定義する
- [ ] 35分: ローカルTraffic logとBedrock ResponseのUsageからRequest当たりToken、Model別概算Costを計算し、3つの改善案を比較する。Cost Explorerの後日実績との差も記録する
- [ ] 15分: Cost削減で悪化し得る品質・Latency・Freshnessを記録する

成果物: Cost model、Caching policy、改善前後の比較表。

完了条件: 単価だけでなく、Token量、再利用率、Trafficの安定性、品質を含めて最適化できる。

## D4-02: Application performanceを最適化する（3時間）

公式・無料教材:

- [CloudWatch metrics for Amazon Bedrock runtime](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-runtime-metrics.html)
- [Prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)
- [Knowledge Base query configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html)

作業:

- [ ] 30分: End-to-end latencyをGateway、Retrieval、Model queue、Time to first token、Generation、Toolへ分解する
- [ ] 15分 — Skill 4.2.1: Pre-compute、Parallel call、Streaming、Latency-optimized inferenceをUX要件へ割り当てる
- [ ] 15分 — Skill 4.2.2: Index、top-k、Filter、Hybrid search、RerankingのLatency／Relevance trade-offを定義する
- [ ] 15分 — Skill 4.2.3: Batch、Concurrency limit、Token processing、QuotaのThroughput計画を作る
- [ ] 15分 — Skill 4.2.4: Temperature、top-p、top-k、max tokensの変更仮説と評価指標を定義する
- [ ] 15分 — Skill 4.2.5: Peak request、Token/minute、Concurrency、HeadroomからCapacity planを作る
- [ ] 15分 — Skill 4.2.6: API、Retrieval、Model、ToolごとのProfiling pointとBudgetを設定する
- [ ] 45分: ローカルで逐次／並列、Cacheなし／あり、top-k 3値をBenchmarkする。AWS側は小SampleでBedrockのTime to first token／総Latencyを測り、p50/p95を計算するにはSample不足ならその制約を明記する
- [ ] 15分: 採用設定と、品質またはCost上の代償を記録する

成果物: Latency budget、Capacity plan、Benchmark結果。

完了条件: 遅いという症状をComponent別に分解し、Metricに基づいて改善案を選べる。

## D4-03: GenAI applicationのMonitoringを実装する（4時間）

公式・無料教材:

- [Bedrock Runtime CloudWatch metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-runtime-metrics.html)
- [Model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html)
- [Advanced operations for GenAI applications](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/prod-monitoring-advanced-operations.html)

作業:

- [ ] 30分: Metric、Log、Traceと、Performance、Cost、Quality、Business KPIの関係を読む
- [ ] 20分 — Skill 4.3.1: Availability、Latency、Error、Token、Quality、User feedback、Business outcomeのDashboardを設計する
- [ ] 20分 — Skill 4.3.2: Token burst、Hallucination、Response drift、Cost anomaly、Invocation logging failureのAlertを定義する
- [ ] 20分 — Skill 4.3.3: Request IDでUser interaction、Compliance log、Business eventを関連付けるSchemaを作る
- [ ] 20分 — Skill 4.3.4: Tool call数、成功率、Latency、Retry、Agent handoff、Loop回数のBaselineを定義する
- [ ] 20分 — Skill 4.3.5: Vector query latency、Index freshness、Ingestion failure、Recall sampleの監視とRunbookを作る
- [ ] 20分 — Skill 4.3.6: Golden dataset、Output diff、Traceを使うGenAI固有Troubleshooting flowを作る
- [ ] 75分: ローカルで構造化LogとMetric集計を実装し、AWSではBedrock Runtime MetricとSanitize済みApplication logを確認する。Latency／Token異常のAlert案を作り、常時課金が生じる構成は残さず削除する
- [ ] 15分: Prompt／ResponseをLogするPrivacy riskとRedaction方針を追記する

成果物: Dashboard仕様、Alert一覧、3件のRunbook、Anomaly detection結果。

完了条件: Infra healthだけでなく、品質、Retrieval、Tool、Cost、Business valueを同じRequest単位で追跡できる。

## Domain 4 終了チェック

- [ ] Skills 4.1.1〜4.3.6の全項目を実施した
- [ ] [`docs/notes/domain-4-operations-optimization.md`](../notes/domain-4-operations-optimization.md) を更新した
- [ ] Cost、Latency、品質のどれを優先した最適化か説明できる
- [ ] Bedrock Usage、実行直後の概算、後日確認したCostの差を説明できる
- [ ] Domain 4の問題演習を行い、誤答を記録した
