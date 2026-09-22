# 学習計画

最終更新日: 2026-09-21

## 目標と前提

| 項目 | 内容 |
|---|---|
| 試験 | AWS Certified Generative AI Developer - Professional |
| 試験コード | AIP-C01 |
| 開始日 | 未設定 |
| 受験予定日 | 未設定 |
| 標準期間 | 10週間（準備週を除く） |
| 標準学習時間 | 週8時間。実際に確保できる時間が分かったら調整する |
| 現在地 | リポジトリ上は、ドメイン別ノートと間違い記録が未着手 |
| 直近の目標 | 準備週を完了し、受験予定日と週次の学習枠を確定する |

この計画の目的は、試験範囲を一度読むことではなく、要件から適切な構成を選び、その理由、トレードオフ、障害時の調査方法を説明できる状態になることである。

具体的な作業、目安時間、公式教材、成果物、完了条件は [`docs/tasks/README.md`](tasks/README.md) から開始する。実装項目は [`labs/local-genai/`](../labs/local-genai/) のAWS／ローカル統合ラボで、ローカルの再現可能な比較とAWS Managed serviceの実挙動を対応付けて学ぶ。

## 公式範囲と時間配分

[公式試験ガイド](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html)の配点を学習時間の基準にする。ただし、弱点診断後は弱い領域へ時間を移す。

| ドメイン | 配点 | 標準学習時間の目安 | 主な到達点 |
|---|---:|---:|---|
| [Domain 1: FM統合、データ管理、コンプライアンス](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html) | 31% | 25時間 | FM選定、データ処理、Vector Store、RAG、Promptを設計できる |
| [Domain 2: 実装と統合](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html) | 26% | 21時間 | API、Agent、ツール、デプロイ、企業システム統合を実装判断できる |
| [Domain 3: 安全性、セキュリティ、ガバナンス](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html) | 20% | 16時間 | 多層防御、データ保護、監査、Responsible AIを組み込める |
| [Domain 4: 運用効率と最適化](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html) | 12% | 10時間 | コスト、性能、監視のトレードオフを説明できる |
| [Domain 5: テスト、検証、トラブルシューティング](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html) | 11% | 8時間 | 評価を設計し、FM・Prompt・検索の問題を切り分けられる |

合計80時間を標準とする。これは受験に必要な時間の保証ではなく、10週間の配分を決めるための初期値である。

## 学習方針

各テーマは次の順で学ぶ。

1. 公式試験ガイドで対象TaskとSkillsを確認する
2. 公式ドキュメントを読み、選定条件と比較軸を自分の言葉で説明する
3. 小さな実装または構成図で動作と制約を確認する
4. シナリオ問題を解き、判断根拠を説明する
5. 誤答や曖昧な判断を [`questions/mistake-log.md`](../questions/mistake-log.md) に残す
6. 1週間以内に再確認し、関連する [`docs/notes/`](notes/) を更新する

すべてのサービスを同じ深さで暗記しない。[In-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/aip-01-in-scope-services.html)は範囲確認に使い、ドメインのTaskで要求される「いつ、なぜ選ぶか」を優先する。モデル開発・学習、Advanced ML、Feature Engineeringは対象候補者の職務範囲外なので、関連Taskに必要な深さを超えて追わない。

### 教材とラボの選定方針

1. AWS公式資料を一次情報とする。試験ガイド、AWS Documentation、AWS Prescriptive Guidance、AWS Well-Architected、公式コード例、Skill Builderを使う
2. Skill Builderの有料・購読対象教材は、学習効果と残予算を確認して選ぶ。購読を前提としない代替経路も残す
3. AWS実機を標準の学習経路に含める。Bedrock API、Guardrails、Knowledge Bases、IAM、CloudWatch／CloudTrailなど、Managed serviceの境界や観測結果を実際に確認する
4. AWS実機の前後にローカルの決定的なStub／Fixtureを実行し、同じ入力の差、失敗時のSignal、Managed serviceへ委譲される責務を記録する
5. 月間AWS利用料は5,000円程度までとし、計画実行枠4,000円＋安全余裕1,000円に分ける。5,000円は使い切る目標ではない
6. 50%、80%、100%のAWS Budgets通知を設定する。実績または予測が4,000円に達したら新規の有料実験を止め、請求確認と削除を優先する
7. On-demand／Serverless、少量Dataset、短時間実行を基本とし、Provisioned Throughput、常時稼働Endpoint、大規模OpenSearch／Auroraなどは、費用対効果を説明できない限り作成しない
8. 実行前に料金、対応Region、Quota、最小権限、作成Resource、削除手順、最大呼出回数を記録する。終了時は削除確認と概算・実績を成果物へ残す
9. 仕様、料金、Region、提供状況が変化し得る情報は実施日に公式資料を再確認し、ノートへ確認日と差分を残す
10. 各学習項目は目安時間、公式根拠、具体的な作業、成果物、完了条件を持つ。詳細は [`docs/tasks/README.md`](tasks/README.md) を基準にする
11. 実際の認証情報、個人情報、機密情報を教材、Fixture、Log、Commitへ含めない

## 10週間のロードマップ

日付は開始日を決めた後に記入する。週をまたいで未完了になった場合は、項目を削らず、次週の演習枠を調整する。

| 期間 | 重点 | 成果物・完了条件 |
|---|---|---|
| 準備週 | 範囲把握とベースライン | 受験予定日と週8時間の具体的な枠を決める。公式ガイドの全Taskを読む。診断問題を解き、弱点上位3つを決める |
| 第1週 | Domain 1: 要件分析とFM選定 | Task 1.1〜1.2を説明できる。ユースケース、品質、レイテンシー、コスト、可用性からFMと呼び出し方式を比較した設計メモを作る |
| 第2週 | Domain 1: データ処理とVector Store | Task 1.3〜1.4を説明できる。入力検証、前処理、Embedding、メタデータ、同期方式を含む構成図を作る |
| 第3週 | Domain 1: RAGとPrompt | Task 1.5〜1.6を説明できる。Chunking、検索、Reranking、Prompt管理を含む最小RAGを設計または実装し、評価用質問を用意する |
| 第4週 | Domain 2: FM APIとアプリ統合 | Task 2.4〜2.5を説明できる。同期・非同期・Streaming、Retry、Throttling、構造化出力を扱う最小APIを設計または実装する |
| 第5週 | Domain 2: Agent、デプロイ、企業統合 | Task 2.1〜2.3を説明できる。Tool利用、状態、停止条件、Human-in-the-loop、権限境界、CI/CDを既存構成へ追加する |
| 第6週 | Domain 3: Safetyとデータ保護 | Task 3.1〜3.2を説明できる。Guardrails、入力・出力検証、Prompt Injection対策、PII、IAM、暗号化、Private接続の多層防御を設計する |
| 第7週 | Domain 3: GovernanceとResponsible AI | Task 3.3〜3.4を説明できる。データ系譜、監査ログ、Model Card、出典、Fairness、人手レビューを含む運用ルールを作る |
| 第8週 | Domain 4: コスト、性能、監視 | Task 4.1〜4.3を説明できる。Token、品質、レイテンシー、エラー、検索性能、事業KPIの監視項目と改善判断を表にする |
| 第9週 | Domain 5: 評価と障害切り分け | Task 5.1〜5.2を説明できる。Golden Dataset、RAG・Agent評価、品質Gateを定義し、FM・Prompt・Retrieval・APIの障害切り分け表を作る |
| 第10週 | 総合演習と弱点補強 | 時間を計って総合問題を解く。誤答を公式資料で再確認する。弱点上位3つを再学習し、受験可否を判定する |

実装は週ごとに別々のサンプルを作らず、第3週の最小RAGを第4〜9週で段階的に拡張する。ローカル版を比較基準にし、AWS版では実API、IAM、Managed serviceの状態、Metric／Log、料金を観測する。予算、Region、Quotaにより実機確認できない項目は、理由と確認日を残し、構成図、擬似コード、APIリクエスト例、障害切り分け表で補う。

## マイルストーン

### M1: 学習開始可能

- [ ] 開始日、受験予定日、週の学習枠を記入した
- [ ] 公式ガイドの全20 Taskを一読した
- [ ] ベースライン問題の結果から弱点上位3つを記録した
- [ ] AWS Budgetsの通知、月4,000円の実行停止線、月5,000円の上限目安、共通Tag、削除手順を設定した

### M2: 中核設計を説明可能（第3週終了）

- [ ] 要件からFM、Embedding、Vector Store、検索方式を選べる
- [ ] RAGのデータ取り込みから回答生成までを図示できる
- [ ] PromptのVersion管理、評価、監査方法を説明できる
- [ ] [`docs/notes/domain-1-foundation-model.md`](notes/domain-1-foundation-model.md) を自分の言葉で更新した

### M3: 本番向け構成を説明可能（第7週終了）

- [ ] FM APIとAgentの失敗処理、状態管理、権限境界を説明できる
- [ ] セキュリティを入力、処理、データ、出力、監査の各層で説明できる
- [ ] CI/CD、Rollback、Human-in-the-loopを含む構成を説明できる
- [ ] Domain 2、3のノートを更新した

### M4: 運用・評価を説明可能（第9週終了）

- [ ] 品質、Safety、コスト、性能、事業価値の指標を選べる
- [ ] Model、Prompt、Retrieval、Agentを分けて評価できる
- [ ] 症状からログ、メトリクス、Trace、設定を調べる順番を説明できる
- [ ] Domain 4、5のノートを更新した

### M5: 受験準備完了（第10週終了）

- [ ] 公式の問題演習を含む総合演習で、異なる2回に80%以上正解した
- [ ] すべての誤答について、正解だけでなく他の選択肢を除外する理由を説明できる
- [ ] `questions/mistake-log.md` の「まだ説明できないテーマ」が空、または受験判断に影響しない状態になった
- [ ] 最終週に新しい教材へ広げず、弱点と間違い記録を再確認した

80%は学習上の目安であり、合格を保証する基準ではない。公式試験は100〜1,000のスケールドスコアで、合格点は750である。

## 1週間の進め方

標準の週8時間を次のように使う。弱点補強週は問題演習と復習を増やす。

| 活動 | 時間 | 実施内容 |
|---|---:|---|
| 公式資料とノート | 3時間 | 該当Taskを読み、選定条件、比較、制約を要約する |
| ハンズオン／設計 | 3時間 | 最小実装、構成図、API例、評価表のいずれかを作る |
| 問題演習 | 1時間 | シナリオ問題を時間を意識して解く |
| 復習と週次レビュー | 1時間 | 誤答の根拠確認、翌週の調整、古い情報の確認を行う |

## 完了の定義

チェックは、読んだだけでは完了にしない。各Taskについて次を満たしたときに完了とする。

- 何を解決するTaskかを2〜3文で説明できる
- 要件から主要なAWSサービスまたは方式を選び、少なくとも1つの代替案を除外できる
- Security、可用性、性能、コストの主要な注意点を説明できる
- 実装例、構成図、比較表、障害切り分け表のいずれかを残している
- 公式URLと最終確認日をノートに記録している
- 関連問題の誤答を復習し、同じ判断ミスをしない見分け方を説明できる

## 進捗記録

### 週次レビュー

```text
対象期間:
学習時間（予定 / 実績）:
対象Task:
読んだ公式資料:
作成・実装したもの:
説明できるようになったこと:
まだ説明できないこと:
問題演習（正答数 / 問題数）:
間違いの傾向:
次週に持ち越す項目:
次週の最優先事項:
```

### 計画を見直す条件

- 2週続けて予定時間の70%を下回った: 受験日または週あたりの範囲を調整する
- 同じテーマで2回以上誤答した: 次週の冒頭で公式資料と実装を再確認する
- 総合演習でドメイン正答率が70%未満: そのドメインへ追加で2〜4時間を割り当てる
- 公式試験ガイドが更新された: [`docs/links/official.md`](links/official.md) と関連ノートに差分と確認日を残す

## 次に行うこと

- [ ] 開始日と受験予定日を決める
- [ ] 1週間に確保できる曜日・時間帯を決める
- [ ] [`PREP-01`](tasks/README.md#prep-01-試験範囲と現在地を確定する1時間30分) を実施し、弱点上位3つをこのファイルへ追記する
- [ ] [`PREP-02`](tasks/README.md#prep-02-awsローカル統合ラボを準備する2時間) を実施する
- [ ] [`D1-01`](tasks/domain-1.md#d1-01-要件を分析しgenaiソリューションを設計する3時間) に着手する

## 公式根拠

- [AIP-C01 Exam Guide](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html)
- [Technologies and concepts that might appear on the exam](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-technologies-concepts.html)
- [In-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/aip-01-in-scope-services.html)
- [AWS Certification Prep](https://aws.amazon.com/certification/certification-prep/)
- [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)

公式情報の最終確認日: 2026-09-21
