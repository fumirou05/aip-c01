# 気軽な学びログ

問題演習の誤答ではない、調べて分かったことや気になった設計パターンを短く残すためのノート。誤答の理由や再確認事項は [`questions/mistake-log.md`](../../questions/mistake-log.md) に記録する。

## 2026-09-21: AWS Step Functions サーキットブレーカーパターンって何？

### ひとことで

障害中のサービスへリクエストを送り続けて障害を広げないために、失敗が続いたら呼び出しを一時的に「遮断」し、時間を置いてから少数の試行で復旧を確認するパターン。電気のブレーカーと同じく、呼び出し元を守る。

Step Functions に「サーキットブレーカー」という専用状態があるわけではない。Step Functions の状態遷移、`Retry`、`Catch`、`Choice`、`Wait` と、実行をまたいで状態を保存する DynamoDB などを組み合わせて実装する。

### 典型的な流れ

```text
状態を確認
  ├─ OPEN かつ有効期限内 → すぐ失敗／フォールバック（対象サービスを呼ばない）
  └─ CLOSED または期限切れ → 対象サービスを呼ぶ
                              ├─ 成功 → 成功
                              └─ 失敗 → 限定回数 Retry（指数バックオフ）
                                         ├─ 成功 → 成功
                                         └─ 失敗 → OPEN を保存して失敗／フォールバック
```

一般的な名前では、通常時が `CLOSED`、遮断中が `OPEN`、復旧確認の試行中が `HALF_OPEN`。AWS公式の実装例では、DynamoDBのレコードに有効期限を持たせ、期限切れ後の次の呼び出しを復旧確認として扱うため、`HALF_OPEN` 相当の動きになる。

### 何がうれしいか

- タイムアウトする呼び出しを大量に重ねず、呼び出し元の待ち時間・同時実行数・コストの増加を抑えられる
- 障害中の下流サービスに負荷をかけ続けず、カスケード障害を防ぎやすい
- 失敗時にキャッシュ、キュー、簡略応答、人手確認などのフォールバックへ切り替えられる

### Step Functions での設計メモ

- `Retry` は「この実行中に何回再試行するか」を定義する機能。これだけでは、別の実行が同じ障害中サービスを呼ぶことを止められない
- 実行をまたぐ `OPEN` 状態は DynamoDB などに保存する。AWS公式例では、対象サービスごとの状態を DynamoDB に保存し、Step Functions が最初に確認する
- `Retry` は対象エラー、`MaxAttempts`、`BackoffRate` を絞る。副作用のある処理では、再試行による二重実行に備えて冪等性を設計する
- `TimeoutSeconds` で呼び出しの上限時間を決め、`Catch` で状態を `OPEN` にする処理やフォールバックへ遷移させる
- DynamoDB TTL の削除は期限ちょうどに起きる保証がない。判定はTTL削除の完了ではなく、レコード内の有効期限を見て行う
- 複数の実行が同時に復旧確認を行うと、`HALF_OPEN` のつもりが大量呼び出しになる可能性がある。条件付き書き込みなどで試行数を制御する必要がある

### 生成AIアプリケーションでの使いどころ

外部のFM API、検索基盤、企業内APIなど、遅延や一時障害が起こり得る依存先を呼ぶワークフローに適用できる。ただし、常に失敗を隠すのではなく、品質・安全性・データの鮮度に問題がないフォールバックだけを選ぶ。

### 公式資料

- [Using the circuit breaker pattern with AWS Step Functions and Amazon DynamoDB](https://aws.amazon.com/blogs/compute/using-the-circuit-breaker-pattern-with-aws-step-functions-and-amazon-dynamodb/) — AWS公式の実装例
- [Handling errors in Step Functions workflows](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html) — `Retry`、`Catch`、エラー種別
- [Best practices for Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/sfn-best-practices.html) — Lambda例外などのエラー処理

最終確認日: 2026-09-21

## 2026-09-21: ベクトル埋め込み

### ひとことで

ベクトル埋め込み（Embedding）は、文章・画像・音声などのデータを、意味や特徴を表す数値の配列（ベクトル）へ変換すること。意味が近いデータほど、選んだ距離尺度上で近くなるように表現し、意味検索・推薦・分類・クラスタリング・RAGに利用する。

Embeddingは回答を生成する処理ではない。検索対象と質問を同じ意味空間へ写像し、近いデータを探すための前処理・検索処理である。

### RAGでの使われ方

```text
取り込み時
文書 → Chunk分割 → Embeddingモデル → 文書ベクトル + 原文 + Metadataを保存

検索時
質問 → 同じEmbeddingモデル → 質問ベクトル
     → Vector Storeで類似度検索
     → 上位ChunkをFMのContextへ追加
     → FMが回答を生成
```

Amazon Bedrock Knowledge Basesでも、データをChunkに分割してEmbeddingへ変換し、元の文書との対応を保ったままVector Storeへ保存する。検索時は質問もEmbeddingに変換して、文書ベクトルと類似度を比較する。

### 設計で揃えるもの

- **Embeddingモデル**: 言語、Modality、ドメイン、検索品質、レイテンシー、料金、Batch対応を要件で選ぶ
- **ベクトル次元数**: Vector Storeのスキーマ／マッピングとモデルの出力次元を一致させる
- **距離尺度**: コサイン距離、ユークリッド距離、内積などから、モデルと検索エンジンが想定する方式を選ぶ
- **入力処理**: Chunk size、重複、表や画像の扱い、正規化、Metadata付与を決める
- **Version管理**: 文書、Embeddingモデル、モデル設定、Chunking、距離尺度、Indexを同じ変更単位で記録する

Embeddingモデルや次元数を変更する場合、既存ベクトルと新しい質問ベクトルを同じ空間で比較できなくなる可能性がある。原文とMetadataを残し、全件または影響範囲を再Embeddingして新しいIndexへ切り替える計画を持つ。

### 品質の見方

「ベクトルが作れた」だけでは成功ではない。Golden queryに対するRecall@k、Precision、MRR／nDCG、Retrieval latency、Index freshness、Token costを測る。検索結果が悪いときは、Embeddingモデルだけでなく、Chunking、Query rewrite、Metadata filter、top-k、距離尺度、Index更新遅延も切り分ける。

Embeddingは元データから作られた派生データであり、機密情報の意味を含む可能性がある。元文書と同じようにアクセス制御、暗号化、保持期間、削除・再生成の手順を考える。Embeddingを返しただけで元データへのアクセス権を与えないよう、検索結果の認可も別に実施する。

### よくある混同

| 混同 | 整理 |
|---|---|
| EmbeddingとFMの回答生成 | Embeddingは意味検索用の数値表現。回答生成は別のText／Multimodal FMが行う |
| Embeddingと暗号化 | Embeddingは復号鍵なしに戻せる暗号文ではなく、意味を持つ特徴表現。秘匿化の代わりにはならない |
| 次元数が大きいほど高品質 | 次元数だけでは品質は決まらない。モデル、データ、Chunking、Index、評価セットで比較する |
| 検索結果が悪いのでtop-kだけ増やす | Contextが増えればLatency、Token、ノイズも増える。Recall、Relevance、回答品質を一緒に評価する |

### OpenSearch／pgvectorとの関係

Embeddingモデルはベクトルを作る側、OpenSearchやpgvectorはベクトルを保存・検索する側。役割が異なるため、同じEmbeddingモデルの出力をどちらに保存するかは、既存DBとの統合、全文検索、Filter、規模、Latency、運用負荷で決める。

### 公式資料

- [Getting started with Amazon Titan Text Embeddings in Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/getting-started-with-amazon-titan-text-embeddings/) — Embeddingの意味と検索・RAGでの利用
- [Prerequisites for using a vector store you created for a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html) — EmbeddingモデルとVector Storeの次元数を一致させる考え方
- [Using models with Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/foundation-models-reference.html) — FMによるEmbedding推論
- [Protect sensitive data in RAG applications with Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/protect-sensitive-data-in-rag-applications-with-amazon-bedrock/) — RAGの取り込み・検索・データ保護

最終確認日: 2026-09-21

## 2026-09-21: フォレンジック／ポストモーテム

### ひとことで

似ているが目的が違う。

- **フォレンジック（Forensics）**: インシデント中または直後に、何が起きたか、いつ起きたか、どこまで影響したか、誰または何が操作したかを、証拠を保全しながら調査する活動
- **ポストモーテム（Postmortem）**: サービスを安定化した後に、根本原因と寄与要因、検知・判断・復旧の問題を振り返り、再発防止のアクションへつなげる活動

フォレンジックは「事実を確定する」こと、ポストモーテムは「次に同じ失敗を減らす」ことが中心。

### 流れ

```text
検知
  → 封じ込め・影響最小化
  → 証拠を保全してフォレンジック調査
  → 復旧・利用者への説明
  → ポストモーテム
       ├─ タイムラインと影響
       ├─ 根本原因・寄与要因
       ├─ 検知・対応で良かった点／不足した点
       └─ Ownerと期限付きの再発防止アクション
```

### 生成AIアプリケーションで残す証拠

- Request ID、Correlation ID、User／Tenant、発生時刻（UTC）、リージョン、環境、デプロイ版
- Step FunctionsのExecution ARN、State名、状態遷移、入力・出力、Retry、Timeout、Catch、Fallback先
- FMのモデルID／バージョン、Inference profile、Prompt templateの版、Parameter、Guardrail結果
- Tool名、引数の検証結果、呼び出し先、HTTP status、レイテンシー、外部システムのRequest ID
- RetrievalのIndex／Embeddingモデル／Chunk／Metadata filter／top-k／結果文書の版と鮮度
- CloudTrail、CloudWatch Logs、メトリクス、X-Ray、API Gateway、Lambda、BedrockのInvocation loggingやTrace
- IAMポリシー、設定変更、デプロイ、Feature flag、インデックス更新など、障害直前の変更履歴

プロンプト、検索文書、FM出力には個人情報・機密情報が含まれ得る。必要な証拠を定義したうえで、アクセス制御、暗号化、保存期間、マスキング、削除手順を決める。調査用にログを増やすこと自体が新しい情報漏えいリスクにならないようにする。

### フォレンジックの注意点

- まず対象時間、対象アカウント、リージョン、リソース、Request IDを固定する
- 元のログやオブジェクトを直接編集せず、読み取り専用の保管先へコピーして分析する
- 取得者、取得時刻、取得方法、ハッシュ、保管場所、アクセス履歴を残し、証拠のChain of Custody（保全経路）を説明できるようにする
- CloudTrailのログ完全性検証を有効にしている場合は、digestとハッシュで改変・削除の有無を確認する
- CloudTrailはAPIイベントの履歴であり、アプリケーションの完全な処理順序やFMの内部推論を表すものではない。アプリケーションログ、Step Functions実行履歴、メトリクス、TraceをCorrelation IDで関連付ける

### ポストモーテムの項目

```text
概要・影響:
検知時刻／影響開始／緩和／復旧時刻:
影響を受けた利用者・データ・機能:
事実ベースのタイムライン:
根本原因:
寄与要因（監視、設定、依存先、手順、容量など）:
検知・対応で良かったこと:
改善できること:
再発防止アクション（Owner / 期限 / 完了条件）:
検証方法:
```

責任者探しや個人の評価に使わず、「その時点で得られた情報と制約の中で、なぜその判断になったか」を扱う。AWS公式のIncident Managerも、ポストインシデント分析をblameless（個人を責めない）にし、根本原因と改善アクションを整理する形式を取っている。

### Step Functions／GenAIでの再発防止例

- `Timeout`やThrottlingを検知できるMetricとAlertを追加する
- 失敗したExecutionの入力・出力・エラー種別を、機密情報を除いて再現Fixtureにする
- Toolの不正引数、無限Loop、Fallback連鎖、重複実行をテストケースに追加する
- Prompt、Model、Embedding、Index、Guardrailの版をリリース時に記録する
- Fallbackへ切り替わった割合、回答品質、鮮度、Human handoff、再処理成功率をDashboard化する
- Action itemは「監視を改善する」ではなく、「○月○日までに○メトリクスのAlertとRunbookを追加し、Fault injectionで検証する」のように検証可能にする

### 似た言葉との違い

| 用語 | 主な問い | 成果物 |
|---|---|---|
| Troubleshooting | 今この症状をどう直すか | 切り分け、暫定対応、復旧手順 |
| フォレンジック | 何が起き、影響と証拠は何か | 保全された証拠、タイムライン、影響範囲、分析結果 |
| ポストモーテム | 次に同じ事故をどう減らすか | 根本原因、学び、Owner・期限付きアクション |
| Audit | ルールや統制を満たしているか | 証跡、評価結果、是正計画 |

### 公式資料

- [Collect and analyze forensic evidence - AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.pdf) — 証拠収集、完全性、Chain of Custody
- [Validating CloudTrail log file integrity](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html) — CloudTrailログの改変・削除検証
- [Performing a post-incident analysis in Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/analysis.html) — blamelessな事後分析と改善アクション
- [Stage 3: Inspect, adapt and iterate](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerate-observability-outcomes/inspect-adapt-iterate.html) — 事後インシデントレビューとObservability改善

最終確認日: 2026-09-21

## 2026-09-21: グレースフルデグラデーション

### ひとことで

グレースフルデグラデーション（Graceful Degradation）は、依存サービスの障害や性能低下が起きても、アプリケーション全体を一気に停止せず、機能・品質・速度を意図的に下げた状態で重要な処理を継続する設計パターン。

重要なのは「何でも成功したように見せる」ことではない。利用者へ制限を伝え、許容できる範囲の代替処理へ切り替え、データ破損や危険な副作用は発生させない。

### 生成AIアプリケーションの例

```text
通常: 高性能FM + RAG + Tool実行
  ↓ FM／Retrievalの遅延・障害
代替1: 小さいFM、別のFM、別Regionの推論
  ↓ まだ利用できない
代替2: キャッシュ済み回答、静的FAQ、Keyword検索
  ↓ 最新情報や回答生成が必要
代替3: 受付だけ行いQueueへ保存、人手対応へ引き継ぐ
  ↓ 認証・権限・支払い・削除など高リスク処理
安全側で停止し、再試行または人手承認
```

例えばRAG基盤が停止したとき、古いキャッシュを「最新情報」と表示して返すのは危険。キャッシュの取得日時を明示する、一般的な案内だけ返す、問い合わせを人へ渡すなど、回答の鮮度と安全性を考えたFallbackを選ぶ。

### Step Functionsでの実装イメージ

```text
PrimaryTask（FM／Retrieval／Tool）
  ├─ 成功 → 通常の次の状態
  └─ Timeout／Throttling／ServiceFailure
       → Retry（対象エラー・回数・Backoffを限定）
       → Catch
           ├─ 軽い代替FM／別Region
           ├─ Cache／StaticResponse
           ├─ Queue／HumanHandoff
           └─ 安全にFail
```

Step Functionsでは、`Retry`、`Catch`、`Choice`、`Wait`、Task統合を使って、障害の種類と重要度に応じたFallbackを状態機械として明示できる。サーキットブレーカーと組み合わせれば、障害中の依存先を呼び続けず、Fallbackへ早く切り替えられる。

### 設計時のチェックポイント

- **重要度を分ける**: 検索の補助機能は落としても注文確定などの中核処理は継続する、といった優先順位を決める
- **品質を下げる境界を決める**: 正確性、鮮度、言語、応答速度、機能範囲のどれをどこまで許容するかを定義する
- **高リスク操作はFail Safe**: 更新、送信、削除、決済、権限変更は、依存先や検証が不完全なときに実行しない。必要なら人手承認へ送る
- **Fallback自体を監視する**: 発生回数、切替理由、代替経路の成功率、回答品質、復旧後の再処理件数を記録する
- **復旧後の整合性を考える**: Queueへ退避した処理の重複、順序、期限、再実行、冪等性を設計する
- **利用者へ伝える**: 「簡易回答」「情報が古い可能性」「人が確認中」など、機能低下と制約を明示する

### 似た考え方との違い

| パターン | 主な目的 | 動き |
|---|---|---|
| Retry | 一時的な失敗から復旧する | 同じ処理を限定回数だけ再試行する |
| Circuit Breaker | 障害中の依存先を保護する | 呼び出しを遮断し、復旧確認までFail Fastする |
| Graceful Degradation | 利用可能な価値を残す | 代替経路や縮退機能へ切り替えて継続する |
| Fail Safe | 危険な結果を防ぐ | 不確かなときは副作用のある処理を実行しない |

### AIP-C01での覚え方

要件から「何を守るために、どの機能を、どの品質レベルまで落とせるか」を決める。単に「別のFMへ切り替える」だけでなく、データ所在地、権限、回答の鮮度、コスト、監査、再処理まで含めてFallbackを設計する。

### 公式資料

- [Definitions - Agentic AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/definitions.html) — Graceful degradationの定義
- [Common mitigation strategies - AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-analysis-framework/mitigation-strategies.html) — 単一障害点・カスケード障害への緩和策
- [Handling errors in Step Functions workflows](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html) — `Retry`、`Catch`、エラー処理
- [AIP-C01 Domain 1: Foundation Model Integration, Data Management, and Compliance](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html) — FM選定、可用性、Graceful degradationの試験範囲

最終確認日: 2026-09-21

## 2026-09-21: Step Functionsを使用したReActパターン

### ひとことで

ReAct（Reasoning and Acting）は、FMがタスクを一度に回答し切るのではなく、状況を見て次の行動を選び、ツールを実行し、その結果（Observation）を受け取って次の行動を決めるループ型のAgentパターン。

Step Functionsを組み合わせる場合、FM／Agentが「次にどのツールを使うか」を動的に判断し、Step Functionsがツール実行、分岐、Retry、Timeout、状態管理、停止条件を管理する。Step Functions自体が推論するわけではない。

### 典型的な流れ

```text
ユーザー要求
  → FMに現在の状態と利用可能なTool schemaを渡す
  → FMが構造化された次のActionを返す
       ├─ FINAL → 最終回答を返す
       └─ TOOL_CALL → 許可・引数・予算を検証
                         → Lambda／API／検索基盤などを実行
                         → 結果をObservationとして状態へ追加
                         → FMの判断へ戻る
```

Amazon States Languageでは、概ね次のような状態になる。

```text
Initialize
  → InvokeModelForNextAction
  → ValidateAction
  → Choice(ActionType)
      ├─ FINAL → ReturnAnswer
      ├─ TOOL_CALL → ExecuteTool → AppendObservation → Loop
      └─ INVALID → HumanFallback／Fail
```

### Step Functionsを使うメリット

- ツール呼び出しをLambda、API Gateway、ECS、SageMakerなどのTaskとして分離できる
- `Choice`でActionの種類を検証し、許可したツールだけを実行できる
- ツールごとに`Retry`、`Catch`、`TimeoutSeconds`、Circuit Breakerやフォールバックを設定できる
- 実行履歴、入力・出力、失敗経路を追跡しやすい
- 長い処理、承認待ち、非同期処理、複数Agentの連携を状態機械として管理できる

### 実装時の重要な制御

- **Actionを自由なコードとして実行しない**: FMの出力はJSON Schemaや許可リストで検証し、ツール名、引数、対象リソース、呼び出し元の権限を確認する
- **ループ上限を持つ**: 最大Step数、最大経過時間、最大Tool call数、Token予算、金額上限を設定し、無限ループやコスト増加を防ぐ
- **副作用を分離する**: 読み取り系Toolと更新・送信・削除系Toolを区別し、後者は人手承認や冪等性キーを要求する
- **失敗をObservationとして扱う**: エラーをそのままFMへ返すのではなく、機密情報を除いた構造化エラーに変換し、再試行可能か、別Toolへ切り替えるか、終了するかを判断させる
- **観測可能性を確保する**: Request ID、Agent実行ID、Step名、Tool名、Latency、Retry回数、結果種別を記録する。内部の逐語的な推論を監査ログへ無制限に保存せず、判断結果・根拠データ・実行結果を構造化して残す

### 他のパターンとの違い

| パターン | 次の処理の決め方 | Step Functionsとの関係 |
|---|---|---|
| Prompt chaining | 開発者が決めた固定順序 | 固定されたTask列の実装に向く |
| ReAct | FMがObservationを見て次のActionを選ぶ | Step Functionsがループ、Tool実行、制御を担当する |
| Workflow orchestration | ルールや状態機械で処理順序を管理 | Step Functionsが中心。必要な箇所だけFMの判断を組み込む |

ReActは柔軟だが、動作が非決定的で、Tool call数や品質が入力によって変わる。企業ワークフローでは、FMにすべてを任せず、Step Functions側に安全境界、停止条件、承認、Fallbackを置くのが重要。

### AIP-C01での見方

「Step Functionsを使用したReAct」は、次の責務分担として説明すると整理しやすい。

```text
FM／Agent       : 状況理解、Tool選択、次のActionの提案
Step Functions  : 状態、分岐、Tool実行、Retry、Timeout、停止条件
Lambda／API     : 実際の業務処理・外部システム呼び出し
DynamoDB等      : 会話状態、Observation、冪等性、長期Memory
IAM／Guardrail  : 実行可能なToolとデータの境界
```

### 公式資料

- [Tool-based agents for calling functions - AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/tool-based-agents-for-calling-functions.html) — FMによるTool選択と実行結果を使ったループ
- [Workflow orchestration agents - AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/workflow-orchestration-agents.html) — Step Functionsを使ったAgent・Workflowのオーケストレーション
- [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) — 状態機械、Task、Choice、Retryなどの基本
- [AIP-C01 Domain 2: Implementation and Integration](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html) — Agent、Tool、アプリケーション統合の試験範囲

最終確認日: 2026-09-21

## 2026-09-21: pgvectorとは？

### ひとことで

`pgvector` は PostgreSQL にベクトル型とベクトル類似検索の機能を追加するオープンソース拡張。文章や画像などをEmbeddingして得たベクトルを、通常のテーブルの列として保存し、SQLでメタデータ条件と組み合わせて検索できる。

つまり、独立したAWSサービス名や専用データベースではなく、PostgreSQLをVector Storeとして使うための拡張である。Amazon Aurora PostgreSQL-Compatible EditionやAmazon RDS for PostgreSQLで利用できる。

### RAGでの流れ

```text
文書をChunk分割
  → Embeddingモデルでベクトル化
  → PostgreSQLのvector列へ保存

質問
  → 質問も同じEmbeddingモデルでベクトル化
  → pgvectorで類似ベクトルを検索
  → SQLのMetadata filterやJOINを適用
  → 取得した文脈をFMへ渡して回答生成
```

例えば、文書のEmbeddingと一緒に`department`、`visibility`、`updated_at`を同じテーブルへ保存すれば、「営業部が閲覧でき、公開期限内で、質問に意味が近い文書」のような検索をSQLで表現できる。

### 主な機能

- `vector`データ型でEmbeddingを保存する
- ユークリッド距離、内積、コサイン距離などで類似度を計算する
- 全件を比較する正確な最近傍検索（KNN）と、検索対象を絞って高速化する近似最近傍検索（ANN）を選べる
- `HNSW`や`IVFFlat`などのインデックス方式を利用できる
- PostgreSQLのトランザクション、SQL、JOIN、既存の認可・業務データと組み合わせられる

### HNSWとIVFFlatのざっくり比較

| 方式 | 特徴 | 注意点 |
|---|---|---|
| HNSW | ベクトル間の近さをグラフ構造で管理し、高品質・低レイテンシーの検索を狙いやすい | インデックス構築・更新時のメモリやコスト、パラメータ調整を確認する |
| IVFFlat | ベクトルを複数のリストに分け、近いリストを中心に検索する | リスト数や検索対象リスト数の調整で、Recallと速度のバランスを取る |

どちらが常に優れているわけではない。データ量、更新頻度、同時実行数、許容Recall、メモリに収まるかを実データで測定する。

### OpenSearchとの使い分け

- **pgvectorを選びやすい場合**: 既存のPostgreSQLを使っている、ベクトル検索と業務データのJOIN・トランザクション・SQLフィルターを一体で扱いたい、データ規模と検索負荷がDB設計の範囲に収まる
- **OpenSearchを選びやすい場合**: 検索専用基盤として全文検索・ベクトル検索を大規模に分散したい、検索ワークロードを業務DBから分離したい、OpenSearchの運用基盤が既にある

pgvectorはOpenSearchのprimary shardを使う方式ではない。PostgreSQL側のテーブル、インデックス、パーティション、Auroraのインスタンス・リードレプリカなどを別の軸で設計する。大規模化したときの検索レイテンシー、Recall、インデックス構築時間、メモリ、接続数を測定して判断する。

### Amazon Bedrock Knowledge Basesとの関係

Aurora PostgreSQLをAmazon Bedrock Knowledge BasesのVector Storeとして使う構成もある。この場合、Aurora側で`pgvector`拡張を有効化し、Embedding、テキストChunk、Metadataを保存する。AWS公式手順では、利用するAuroraのDBエンジンバージョン、`pgvector`バージョン、Data API、Secrets Manager、必要なインデックスを事前に確認する。

サービスの対応バージョン、リージョン、料金、Knowledge Basesの要件は更新されるため、実装時に公式ドキュメントを再確認する。

### 公式資料

- [Using Aurora PostgreSQL as a Knowledge Base for Amazon Bedrock](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.VectorDB.html) — Aurora PostgreSQLをBedrock Knowledge BaseのVector Storeにする手順
- [The role of vector databases in generative AI applications](https://aws.amazon.com/blogs/database/the-role-of-vector-datastores-in-generative-ai-applications/) — pgvector、HNSW、IVFFlatの概要と選定観点
- [Accelerate HNSW indexing and searching with pgvector on Amazon Aurora PostgreSQL-compatible edition and Amazon RDS for PostgreSQL](https://aws.amazon.com/blogs/database/accelerate-hnsw-indexing-and-searching-with-pgvector-on-amazon-aurora-postgresql-compatible-edition-and-amazon-rds-for-postgresql/) — Aurora／RDSでのHNSW検索

最終確認日: 2026-09-21

## 2026-09-21: OpenSearch シャーディング戦略とは？

### ひとことで

OpenSearchのインデックスを複数の論理的な分割単位（`primary shard`）に分け、データノードへ分散する設計方針。各primary shardのコピーである`replica shard`の数も決める。目的は、データ量・検索／書き込み性能・可用性・コストのバランスを取ること。

「シャードを増やせば速くなる」という意味ではない。シャードが少なすぎると一つのシャードやノードがボトルネックになり、多すぎると1回の検索が多くのシャードへ広がる（fan-out）うえ、CPU・メモリ・JVMヒープを余分に使う。

### 検索と書き込みの動き

```text
書き込み
  → primary shard に書く
  → replica shard にも複製する

検索
  → coordinator が各primary shardのいずれか（primaryまたはreplica）へ問い合わせる
  → 各shardの結果をcoordinatorがまとめて返す
```

そのため、1つのインデックスにprimary shardが5個あると、検索は基本的に5個のシャードを対象にする。replicaは検索の読み取り容量や冗長性を増やせるが、データのコピーなのでストレージと書き込み負荷も増える。

### シャード数を決めるときの軸

- **データ量と成長率**: AWS公式の一般的な目安は、検索中心で1シャードあたり10〜30 GiB、書き込み中心で30〜50 GiB。将来の増加分を見込むが、現在のデータが極端に小さいのに将来分だけで大量のシャードを作らない
- **データノード数**: primary shard数をデータノード数の倍数にすると、ノード間へ均等に配置しやすく、hot nodeやstorage skewを避けやすい。ただし、最優先はシャードサイズであり、小さなインデックスなら1シャードでよい場合もある
- **レプリカ数**: 少なくとも1つを基本にし、障害時の可用性と読み取り容量が必要なら増やす。増やすほどストレージと複製コストが増える
- **ワークロード**: RAGの検索では検索レイテンシー、top-k、フィルター、同時実行数、インデックス更新頻度を実データで測る。ログのような大量書き込みとは、適切なサイズやインデックス分割の考え方が異なる
- **運用方法**: 時系列データではrolloverやIndex State Managementでインデックスを分割し、1インデックスの肥大化を防ぐ。一方、インデックスを細かく作りすぎると小さなシャードが大量に生まれるため注意する

AWS公式の概算式は次のとおり。

```text
(元データ量 + 成長見込み) × (1 + インデックスオーバーヘッド)
÷ 目標シャードサイズ ≒ primary shard数
```

これは初期値であり、最終的には本番に近いデータと検索・書き込みパターンで負荷試験し、CPU、JVMメモリ、ディスク、キュー、レイテンシーを見て調整する。

### ベクトル検索・RAGでの注意

ベクトル検索では、Embeddingの次元数や使用する検索方式、メタデータフィルター、top-k、同時実行数が検索性能と品質に影響する。シャード数だけでRecallやレイテンシーを決められないため、同じEmbeddingモデル・同じデータ分布・同じクエリ集合で比較する。

Embeddingモデルや次元数が異なるデータを同じ検索インデックスへ混在させると、マッピングや検索条件の設計が複雑になる。モデルやドメイン、テナント、更新ライフサイクルごとにインデックスを分ける（multi-index）案もあるが、インデックス数とシャード数の増加による運用負荷と比較して決める。

### 試験での覚え方

「シャーディング戦略」は、単なるスケールアウトではなく、次の設計判断の組み合わせ。

```text
データ量・成長率
  + 検索／書き込み特性
  + データノード数
  + replicaによる可用性・読み取り容量
  + ベクトル検索の品質・レイテンシー
  → primary shard数、replica数、index分割、運用方式を決める
```

### 公式資料

- [Choosing the number of shards - Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/bp-sharding.html) — シャードサイズとprimary shard数の考え方
- [Operational best practices for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/bp.html) — ノード分散、replica、シャード数、storage skew
- [Vector search - Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vector-search.html) — `knn_vector`、k-NN、RAG

最終確認日: 2026-09-21
