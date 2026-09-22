# Foundation Modelを選定・設定する

## このページの位置づけ

| 項目 | 内容 |
|---|---|
| 対応Task | `D1-02`: FMを選定・設定する |
| 対応Skills | `1.2.1〜1.2.4` |
| このページで分かること | ユースケースと技術要件に合うFoundation Model（FM）の選定軸、コードを変えずにモデルを切り替える構成、障害時の継続方法、カスタマイズしたモデルのデプロイとライフサイクルを、AWS公式資料の範囲で整理する。 |
| 前提知識 | 生成AIアプリケーションがモデルへ入力を渡し、推論結果を受け取ること |
| 対応する補足ページ | [`01-02-foundation-model-selection-and-configuration.md`](../supplimental-pages/01-02-foundation-model-selection-and-configuration.md) |

## まず全体像

Task 1.2は、モデルの品質だけでなく、用途に必要な能力、制約、運用方法まで含めてFMを選定・設定することを求めている。選定後もモデル識別子をアプリケーションコードへ固定せず、障害やモデル廃止に対応できる切替経路を用意する。用途固有の性能が必要ならモデルをカスタマイズし、版管理、評価、展開、Rollback、廃止まで管理する。

Amazon Bedrockのモデルカタログは継続して変わる。モデルごとの能力、API、Region、Inference profile、カスタマイズ対応、ライフサイクルは、利用時点のモデルカードと関連する対応表で確認する。

## Skill 1.2.1: ユースケースと技術要件に合うFMを選ぶ

公式試験ガイドは、性能ベンチマーク、能力分析、制限の評価によって、事業ユースケースと技術要件に合うFMを選ぶことを求めている。Amazon Bedrockのモデル選択では、少なくとも次の項目を確認する。

| 選定軸 | 公式資料で確認する内容 |
|---|---|
| Modality | Text、Image、Audio、Video、Embeddingなど、受け取れる入力と生成できる出力 |
| Context | 1回の推論で扱える入力・会話履歴・出力の上限。正確な上限は各モデルカードで確認する |
| Tool use | Converseなどを介したTool useまたはFunction callingへの対応 |
| 品質と制限 | 対象業務を代表するデータで測った応答品質と、言語、用途、入出力などの制限 |
| レイテンシー | 応答開始までと応答完了までの時間。Streaming対応も用途に応じて確認する |
| Region | 使用するRegionでの単一Region推論、地理別またはGlobalのCross-Region inferenceへの対応 |
| EndpointとAPI互換性 | `bedrock-runtime`または`bedrock-mantle`の対応と、Invoke、Converse、OpenAI互換、Messagesの各APIへの対応 |
| 価格 | 入出力Token、画像などの単位、On-demand、Batch、Provisioned Throughput、カスタマイズや保存に関する価格 |
| Throughput | On-demandで必要な呼出量を扱えるか、固定容量のProvisioned Throughputが必要か、対象モデルとRegionが対応するか |

Amazon Bedrockは、用途の異なる4系統のRuntime APIを提供する。

- Invoke系は、同期応答、Response stream、双方向Streaming、非同期実行を用途に応じて使う。
- Converse系は、対応モデルに共通するモデル非依存の会話インターフェースを提供する。
- OpenAI互換系は、Chat CompletionsまたはResponsesのインターフェースを提供する。
- Messages系は、`bedrock-mantle` endpointでAnthropic Messages互換のインターフェースを提供する。

すべてのモデルがすべてのAPIへ対応するわけではない。モデル選定時は、モデル名だけでなく、使用するEndpointとAPIの組み合わせを互換性表で確認する。

Provisioned Throughputは、指定モデルに対して固定費で高い推論処理能力を確保する仕組みである。Model Unit（MU）は、1分間に処理できる入力Tokenと生成できる出力Tokenの水準を表す。契約期間は無契約、1か月、6か月から選び、契約が長いほど時間単価の割引が大きくなる。

カスタマイズしたモデルの推論方式には資料間で適用範囲の差がある。Provisioned Throughputの概要はCustom modelの推論にProvisioned Throughputが必要と説明する一方、より新しいCustom model deploymentの資料は、2025-07-16以降にCustomizeした一部のAmazon NovaおよびMeta Llamaモデルを`us-east-1`または`us-west-2`へDeployし、On-demandで推論できると説明している。2026-09-22時点では、対象Base model、Customization実施日、RegionをOn-demand対応表で確認し、対象外ならProvisioned Throughputの対応表を確認する。

## Skill 1.2.2: モデル選択をコードから分離する

公式試験ガイドは、コード変更なしで動的なモデル選択とProvider切替を行える柔軟な構成を求め、AWS Lambda、Amazon API Gateway、AWS AppConfigを例示している。

AWS AppConfigは、Feature flagまたはFree-form configurationによって、コードを再デプロイせずにアプリケーションの動作を変更できる。Model ID、Provider、Region、Inference profile IDまたはPrompt router ARNのような変化する値を構成データとして扱い、アプリケーションは起動時または実行中にその構成を取得できる。AppConfigはValidator、段階的なDeployment strategy、CloudWatch Alarmに基づく自動Rollbackも提供する。

呼出し先を外部設定にしても、モデル間のRequest・Response形式の差は残る。Converseのような共通APIを使用できる候補では共通形式を利用できる。固有APIが必要な候補では、Providerごとの差を変換する層をアプリケーション側に置く。外部設定は切替値を分離する仕組みであり、互換性のないモデルを自動的に互換にするものではない。

## Skill 1.2.3: 障害中も動作を継続できる構成を作る

公式試験ガイドは、サービス中断時にも継続して動作するAIシステムを設計することを求め、Step FunctionsのCircuit breaker、Regionが限られるモデルに対するAmazon Bedrock Cross-Region Inference、Cross-Regionのモデル展開、Graceful degradationを例示している。

| 障害または制約 | 公式資料で示される仕組み |
|---|---|
| 一時的な失敗やThrottling | Retryは、再試行可能な失敗に対して待機時間を設けて再実行する。無制限の即時再試行は行わない |
| 失敗が継続している依存先 | Circuit breakerは、失敗が閾値へ達した経路への呼出しを一時的に止め、回復確認後に再開する |
| 単一Regionの容量制約または中断 | 対応モデルではCross-Region inference profileを指定し、定義された複数Regionの計算資源へBedrockがRequestをRoutingする |
| 主モデルまたは高度機能を利用できない | Graceful degradationにより、代替モデル、機能を限定した応答、非生成の経路など、事前に定めた縮退動作へ切り替える |

Inference profileは、一つのモデルとRequestの送信先になり得る一つ以上のRegionを定義するBedrock Resourceである。次の2種類がある。

- Cross Region（system-defined）Inference profileはBedrockが事前定義し、一つのモデルと複数の送信先Regionを含む。
- Application inference profileは利用者が作成し、利用量・コストを追跡する。単一RegionのFoundation Model、またはCross-Region inference profileを参照できる。

Cross-Region inferenceには、US、EU、APACなど地理的境界内でRoutingする地理別Profileと、対応する商用RegionへRoutingするGlobal Profileがある。地理別Profileはデータ所在地要件を満たす場合に使い、Global Profileは地理的制限がない場合に対象となる。RequestはProfileに含まれる送信先RegionのいずれかへRoutingされる。地理別Profileでは、Service Control Policy（SCP）で一つでも必要な送信先Regionを拒否するとRequestは失敗する。Global ProfileのSCPでは、送信先Regionの列挙ではなく`aws:RequestedRegion`を`unspecified`として許可する要件を確認する。CloudTrailはSource Regionにイベントを記録し、`additionalEventData.inferenceRegion`で処理Regionを確認できる。

Cross-Region inferenceは、Profileの外にある任意のモデルへのFailoverではない。また、Inference profileはProvisioned Throughputをサポートしない。対応モデル、Source Region、Destination Region、Profile IDはモデルカードで確認する。

## Intelligent prompt routing

Amazon Bedrock Intelligent prompt routingは、一つのServerless Endpointで、同じModel familyに属する2モデルの間へRequestを振り分ける。Requestごとに各モデルの応答品質を予測し、品質とコストを考慮して使用モデルを選ぶ。処理結果には実際に使用したモデルの情報が含まれる。

Bedrockが用意するDefault prompt routerと、利用者がモデル、Fallback model、Routing criteriaを設定するConfigured prompt routerがある。Configured routerの`responseQualityDifference`は、Fallback modelともう一方のモデルの予測品質差を基準に切替を決める。Fallback modelは信頼できる基準となり、条件を満たさない場合に使われる。

2026-09-22時点の主な制約は次のとおりである。

- 同じModel familyから、ちょうど2モデルを選ぶ。
- 英語Promptだけに最適化されている。
- アプリケーション固有の性能データに基づいてRouting判断や応答を調整することはできない。
- 特殊な用途では最適なRoutingにならない場合があり、効果は初期Training dataに依存する。
- 対応モデルとRegionは限定され、単一RegionまたはCross-Region inference profileの対応表を確認する必要がある。

Prompt routingはRequest内容に基づくモデル選択であり、Cross-Region inferenceは同じモデルの処理Regionを選ぶ仕組みである。目的は異なる。

## Skill 1.2.4: カスタマイズとライフサイクルを管理する

Amazon BedrockのModel customizationは、用途固有のTraining dataを提供してモデルの性能を改善する。2026-09-22時点の公式資料は次の方式を掲載している。

| 方式 | Training signalと動作 |
|---|---|
| Supervised fine-tuning | Label付きのInput・Output例を与え、対象Taskで期待するOutputとの対応を学習させる |
| Reinforcement fine-tuning | 応答品質を評価するReward functionを定義し、そのFeedback scoreから反復学習させる |
| Distillation | 大きいTeacher modelのResponseを使い、小さく高速で費用効率のよいStudent modelをFine-tuningする |

対応方式、Base model、Regionは方式ごとに異なる。たとえばFine-tuningの対応表にはAmazon、Anthropic、Metaの一部モデルだけが掲載されている。実施前に対応表、Training data形式、Hyperparameter、Quota、価格を確認する。

公式試験ガイドは、Amazon SageMaker AIでDomain-specific fine-tuned modelをデプロイすること、Low-Rank Adaptation（LoRA）やAdapterのようなParameter-efficient adaptation、SageMaker Model RegistryでのVersion管理とデプロイ、自動Deployment pipeline、失敗時のRollback、モデルの廃止と置換もSkill 1.2.4に含めている。

SageMaker Model Registryは、Modelを本番用Catalogへ登録し、Version、Training metricなどのMetadata、Lineage、Stage、Approval statusを管理できる。登録したModelはProductionへDeployでき、CI/CDによる自動Deployにもつなげられる。SageMaker AI Inferenceには、低レイテンシーのReal-time endpoint、Idle期間を持つWorkload向けServerless endpoint、大きいPayloadや長時間処理向けAsynchronous endpointなどがある。

### Amazon BedrockのModel lifecycle

2026-09-07以降にAmazon BedrockでLaunchされたモデルには、次の3状態がある。Console、`GetFoundationModel`、`ListFoundationModels`の`modelLifecycle` fieldで状態を確認できる。2026-09-07より前にLaunchされたモデルにはLegacy版Lifecycle policyが適用される。

| 状態 | 公式資料で定義される動作 |
|---|---|
| Active | ProviderがこのVersionへActiveに取り組んでいる状態 |
| Legacy | 廃止予定。EOL日が通知される。継続利用できるが、EOL前にActive modelへ移行する。新規顧客は採用できず、既存顧客も15日間利用がないとAccessを失う場合がある。新しいProvisioned Throughputは作成できない |
| End-of-Life（EOL） | 原則として全Regionから削除され、そのModelへのRequestは失敗する。Active modelへのMigrationは自動では行われない |

各モデルカードには、EOLがそれより前にはならない日と、原則6か月または45日のLegacy期間が示される。Legacyへ入るとEOL日がモデルカードへ追加される。Bedrock上のLifecycle日はProviderが公開する日付と異なる場合があり、Bedrockでの利用にはモデルカードの日付を使う。

Base modelがLegacyへ移行すると、新しいFine-tuning jobと新しいProvisioned Throughputは作成できない。Legacy前に作成済みのCustomized modelについては、On-demandのCustom model deploymentを新規作成でき、既存のOn-demand deploymentと既存Provisioned Throughputも継続利用できる。ただしEOL前の移行が推奨される。

## 重要な条件と制約

- モデル一覧、Region、API、Inference profile、Prompt router、Customization対応、価格は変わり得る。2026-09-22時点で公式資料を確認したが、実装時にはモデルカードと価格ページを再確認する。
- Model IDを外部設定にしても、Modality、Context、Tool use、Request schema、Response schemaの互換性確認は必要である。
- Cross-Region inferenceでは、Profileに含まれるすべてのDestination Regionをデータ所在地、SCP、IAMの条件と照合する。
- Global inference profileのDestination RegionはAWSが商用Regionを追加すると変わり得る。US、EU、APACなど地理別ProfileのDestination Region一覧は変更されず、新しいRegionを含む場合は別Profileが作成される。
- モデルの移行は自動ではない。候補Versionの評価、段階展開、Rollback経路、EOL前の廃止を利用者側で管理する。

## 用語

| 用語 | このページでの意味 |
|---|---|
| Model ID | 推論で使用するFoundation ModelまたはそのVersionを識別する値 |
| Inference profile | 一つのモデルと、推論RequestをRoutingできる一つ以上のRegionを定義するBedrock Resource |
| Cross-Region inference | 同じモデルのRequestをProfileに定義された複数Regionの計算資源へRoutingする仕組み |
| Intelligent prompt routing | Promptごとの予測品質に基づき、同じFamilyの2モデルから使用モデルを選ぶ仕組み |
| Provisioned Throughput | Model Unit単位で固定の推論処理能力を確保するBedrockの購入方式 |
| Graceful degradation | 障害時に全機能を停止せず、限定機能や代替経路へ縮退する設計 |
| EOL | End-of-Life。モデルがBedrockから削除され、通常のRequestが失敗する段階 |

## このページの要点

- Skill 1.2.1では、Modality、Context、Tool use、品質、制限、Latency、Region、API互換性、価格、Throughputを同じユースケースで評価する。
- Skill 1.2.2では、Model IDなどをAppConfigのような外部設定へ分離し、共通APIまたはProvider変換層と組み合わせる。
- Skill 1.2.3では、Retry、Circuit breaker、Cross-Region inference、Graceful degradationを障害の種類に応じて組み合わせる。
- Skill 1.2.4では、BedrockまたはSageMaker AIでカスタマイズしたモデルを扱い、Version、評価、承認、段階展開、Rollback、Legacy、EOLまで管理する。

## 公式資料

- [AIP-C01 Content Domain 1](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html) — Task 1.2とSkills 1.2.1〜1.2.4
- [Model availability and compatibility](https://docs.aws.amazon.com/bedrock/latest/userguide/models.html) — モデル選定軸、Endpoint、API、Region、Lifecycleへの入口
- [Models at a glance](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html) — 現行モデル、個別の能力、Region、Inference profile、Lifecycle情報
- [API compatibility](https://docs.aws.amazon.com/bedrock/latest/userguide/models-api-compatibility.html) — Runtime APIの種類とモデル別対応
- [Inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html) — Inference profileの種類、用途、対応機能
- [Supported Regions and models for inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html) — 現行のCross-Region/Application inference profile対応
- [Cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) — 地理別・Global Profile、Routing、SCP、監査、制約
- [Intelligent prompt routing](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html) — Prompt routerの動作、対応モデル・Region、制約
- [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) — MU、契約期間、課金、Custom modelの推論
- [Deploy a custom model for on-demand inference](https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-custom-model-on-demand.html) — On-demand対応Base model、Customization実施日、Region、Deployment ARN
- [Customize your model](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) — Fine-tuning、Reinforcement fine-tuning、Distillation
- [Fine-tuning supported models and Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html) — 現行の対応Base modelとRegion
- [Model lifecycle](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html) — Active、Legacy、EOL、Customized modelの扱い
- [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) — 外部設定、Validator、段階展開、自動Rollback
- [Handling errors in Step Functions workflows](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html) — 上限、Backoff、Jitterを持つRetryとCatchによるFallback
- [Definitions - Agentic AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/definitions.html) — Circuit breakerとGraceful degradationの定義
- [Deploy models for inference in SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html) — Endpoint方式とDeployment選択肢
- [SageMaker Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) — Version、Metadata、Lineage、Approval、CI/CD
- [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/) — 利用方式別の現行価格

最終確認日: 2026-09-22
