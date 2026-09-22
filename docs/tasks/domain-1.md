# Domain 1 実行タスク: FM統合、データ管理、コンプライアンス

配点31%、目安25時間。公式範囲は [Content Domain 1](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html) を基準にする。

## D1-01: 要件を分析し、GenAIソリューションを設計する（3時間）

公式・無料教材:

- [Domain 1 / Task 1.1](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html)
- [AWS Well-Architected Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html)

作業:

- [ ] 30分: Task 1.1とGenerative AI Lensの設計原則を読み、機能要件と非機能要件の分類を作る
- [ ] 60分 — Skill 1.1.1: ラボの社内ヘルプデスクについて、利用者、データ、品質、レイテンシー、可用性、Security、コスト、データ所在地を `artifacts/requirements.md` に記入する
- [ ] 45分 — Skill 1.1.2: PoCで検証する仮説を3つ選び、測定指標、合格条件、停止条件を定義する
- [ ] 45分 — Skill 1.1.3: 再利用する標準部品を、認証、Model gateway、Prompt、Retrieval、Safety、Logging、Evaluationに分けて構成図へ表す

成果物: `labs/local-genai/artifacts/requirements.md` と `architecture.md`。

完了条件: 3つの要件について選択案と却下案を説明でき、PoCの成功を数値または観察可能な条件で判定できる。

## D1-02: FMを選定・設定する（4時間）

公式・無料教材:

- [Model availability and compatibility](https://docs.aws.amazon.com/bedrock/latest/userguide/models.html)
- [Inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)
- [Prompt routing](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html)
- [Custom models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html)

作業:

- [ ] 30分: Model選定軸として、Modality、Context、Tool use、Region、API互換性、価格、Throughputを抜き出す
- [ ] 45分 — Skill 1.2.1: 3種類の架空Modelを品質・レイテンシー・単価・制約で採点し、2ユースケースのModelを選ぶ
- [ ] 45分 — Skill 1.2.2: Model IDをアプリコードから分離し、設定ファイルだけでProvider／Modelを切り替える設計を書く
- [ ] 45分 — Skill 1.2.3: Throttling、Region障害、Model停止の各ケースについてRetry、Circuit breaker、Cross-Region inference、Graceful degradationを割り当てる
- [ ] 45分 — Skill 1.2.4: BedrockのModel customizationとSageMaker AI endpointを比較し、Version、評価、段階リリース、Rollback、廃止のLifecycleを作る
- [ ] 30分: `model-catalog.json` のRoutingをローカルTestした後、同じ代表PromptをBedrock On-demandの候補Modelへ上限10 Requestで実行し、品質、Latency、Token、概算費用、Response metadataを比較する

成果物: `artifacts/model-selection.md` と編集済み `config/model-catalog.json`。

完了条件: Modelの能力だけでなく、Region、データ所在地、可用性、Lifecycleを含めて選定できる。

## D1-03: FM入力用のデータ検証・処理Pipelineを実装する（4時間）

公式・無料教材:

- [Amazon Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html)
- [Multimodal Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-multimodal.html)
- [AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/data-quality-gs-studio.html)
- [Making inference requests](https://docs.aws.amazon.com/bedrock/latest/userguide/inference.html)

作業:

- [ ] 30分: Text、Image、Audio、Tabularの入力経路と、Glue Data Quality、SageMaker Processing/Data Wrangler、Transcribe、Bedrock Data Automationの役割を整理する
- [ ] 35分 — Skill 1.3.1: 必須項目、文字コード、Size、重複、欠損、更新日、PIIの検証規則と失敗時の隔離先を定義する
- [ ] 35分 — Skill 1.3.2: 4つのModalityについて、抽出、正規化、検証、保存、再処理のPipelineを図示する
- [ ] 35分 — Skill 1.3.3: `Converse`用の会話形式、構造化出力用JSON Schema、SageMaker endpoint用Payloadの違いを比較する
- [ ] 35分 — Skill 1.3.4: 空白・表記揺れの正規化、Entity抽出、Language判定、重複排除をどの段階で行うか決める
- [ ] 50分: ローカルのIngestion処理を実装し、不正な3ファイルが理由付きでRejectされることをTestする。正常な架空Data 1件だけをAWS側の入力経路へ送り、形式・Size・権限Errorのうち1つを実機で確認する
- [ ] 20分: 大量ファイル、再実行、途中失敗時のIdempotencyとMonitoringを追記する

成果物: `artifacts/data-pipeline.md`、Ingestionコード、テスト結果。

完了条件: 正常データと不正データの経路を説明でき、異なるModalityに適したAWSサービスを選べる。

## D1-04: Vector Storeを設計・実装する（4時間）

公式・無料教材:

- [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Supported vector stores](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html)
- [Metadata for Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-metadata.html)

作業:

- [ ] 30分: OpenSearch Service、Aurora PostgreSQL/pgvector、RDS、Knowledge Basesの管理範囲と選定軸を読む
- [ ] 30分 — Skill 1.4.1: データ量、Query特性、既存DB、運用負荷、可用性からVector Storeを選ぶDecision tableを作る
- [ ] 30分 — Skill 1.4.2: 文書ID、版、部門、公開範囲、作成日、有効期限、出典をMetadata schemaに定義する
- [ ] 30分 — Skill 1.4.3: Shard、Index、Dimension、Approximate search、Multi-indexの性能上のトレードオフを整理する
- [ ] 30分 — Skill 1.4.4: S3、社内Wiki、文書管理システムからのConnectorと権限境界を図示する
- [ ] 30分 — Skill 1.4.5: Full sync、Incremental update、Change detection、Tombstone、Re-index、Rollbackの運用手順を作る
- [ ] 45分: ローカルで文書とMetadataをIndex化し、部門・公開範囲・日付FilterをTestする。事前見積りが実行枠内なら、小DatasetでKnowledge Basesと対応Vector Storeを短時間作成し、同期状態、IAM、削除まで確認する
- [ ] 15分: Vector Storeが古い場合の検知Metricと再同期手順を追記する

成果物: `artifacts/vector-store-decision.md`、Metadata付きローカルIndex、同期手順。

完了条件: 少なくとも3種類のStoreを要件で比較し、削除・更新を含むIndex Lifecycleを説明できる。

## D1-05: FM拡張用のRetrievalを設計する（5時間）

公式・無料教材:

- [Configure Knowledge Base queries](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html)
- [Knowledge Base chunking and parsing](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking-parsing.html)
- [Metadata filters](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-metadata.html)

作業:

- [ ] 30分: Semantic、Keyword、Hybrid、Reranking、Metadata filterの処理順を読む
- [ ] 30分 — Skill 1.5.1: Fixed、Sentence、Semantic、Hierarchical chunkingを同じ3文書へ適用する計画を作る
- [ ] 30分 — Skill 1.5.2: EmbeddingのDimension、言語、Modality、品質、Latency、Cost、Batch処理を選定表にする
- [ ] 30分 — Skill 1.5.3: OpenSearch vector search、Aurora pgvector、Knowledge Bases managed storeの構成を比較する
- [ ] 30分 — Skill 1.5.4: SemanticとKeywordの結果を融合し、Rerankする処理とScore thresholdを定義する
- [ ] 30分 — Skill 1.5.5: Query expansion、Decomposition、Rewriteを使う条件と、変換失敗時のFallbackを定義する
- [ ] 30分 — Skill 1.5.6: RetrievalをFunction calling、REST、MCP toolとして公開するInterface schemaを作る
- [ ] 75分: ローカルRAGでChunk size、top-k、Metadata filterを変えてGolden queryのRecallとLatencyを比較する。Level 3を実施できる場合は同じ代表QueryをKnowledge BasesのRetrieveへ流し、検索結果、Citation、Latency、概算費用の差を記録する
- [ ] 15分: 結果を `retrieval-experiment.md` にまとめ、採用設定を決める

成果物: `artifacts/retrieval-decision.md`、Retrieval実装、比較結果。

完了条件: 取得失敗をEmbedding、Chunking、Query、Filter、Index freshnessに切り分けられる。

## D1-06: Prompt engineeringとGovernanceを実装する（5時間）

公式・無料教材:

- [Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html)
- [Amazon Bedrock Flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html)
- [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)

作業:

- [ ] 30分: Prompt、Variable、Variant、Version、Flow、Guardrailの関係を読む
- [ ] 30分 — Skill 1.6.1: Role、制約、Context、出力Schema、拒否条件を含むSystem prompt v1を作る
- [ ] 30分 — Skill 1.6.2: 会話履歴の保存期間、要約、User確認、Intent不明時のClarification flowを設計する
- [ ] 30分 — Skill 1.6.3: Owner、Review、Approval、Version、Audit、Rollbackを含むPrompt lifecycleを定義する
- [ ] 30分 — Skill 1.6.4: 正常、境界、Adversarial、RegressionのPrompt test caseを最低12件作る
- [ ] 30分 — Skill 1.6.5: Few-shot、明示的な構造、出力制約、Feedback loopを使い、v1からv2を作る。内部推論の開示を前提にしない
- [ ] 30分 — Skill 1.6.6: Pre-process、Prompt、Retrieval、Validation、Fallbackを条件分岐付きFlowとして図示する
- [ ] 75分: ローカルStubとBedrock On-demandでPrompt v1/v2をGolden datasetの代表Caseへ実行し、形式遵守率、根拠提示率、非決定性、Token、Latency、概算費用を比較する。AWS側は事前に最大Case数とRetry上限を固定する
- [ ] 15分: 採用版と却下版の理由を記録する

成果物: Version管理されたPrompt、Test dataset、`artifacts/prompt-evaluation.md`。

完了条件: Prompt変更を品質Gateで判定し、承認・監査・Rollbackまで説明できる。

## Domain 1 終了チェック

- [ ] Skills 1.1.1〜1.6.6の全項目を実施した
- [ ] [`docs/notes/domain-1-foundation-model.md`](../notes/domain-1-foundation-model.md) を更新した
- [ ] FM、Vector Store、Retrieval、Promptの各選定に代替案と却下理由がある
- [ ] Bedrock Runtimeの実測Evidenceと、実施できた場合はKnowledge Basesの作成・削除Evidenceがある
- [ ] Domain 1の問題演習を行い、誤答を記録した
