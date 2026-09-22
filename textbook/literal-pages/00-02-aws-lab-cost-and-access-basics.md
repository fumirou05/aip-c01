# AWSラボのアクセスとコスト管理の基礎

## このページの位置づけ

| 項目 | 内容 |
|---|---|
| 対応Task | [`PREP-02`](../../docs/tasks/README.md#prep-02-awsローカル統合ラボを準備する2時間) |
| 対応Skills | なし（試験学習を始めるための準備Task） |
| このページで分かること | AWSラボを始める前に確認する、短期認証情報、Region、Service Quotas、料金、予算通知、実績確認、コスト配分タグの公式な仕組み |
| 前提知識 | AWSアカウント、AWS CLI、Amazon Bedrockの基本的な用途 |
| 対応する補足ページ | [`00-02-aws-lab-cost-and-access-basics.md`](../supplimental-pages/00-02-aws-lab-cost-and-access-basics.md) |

## まず全体像

AWSラボでは、APIを呼び出せることだけでなく、誰の権限で、どのRegionのどのモデルを、どのクォータと料金条件で利用したかを確認する。利用中はAWS Budgetsで実績または予測のしきい値を監視し、利用後はCost Explorerで費用を分析する。コスト配分タグを使う場合は、リソースへのタグ付けとは別に、Billing and Cost Managementでタグを有効化する。

料金、モデルの提供状況、Region、クォータは変更され得る。このページでは固定の一覧や単価を転載せず、実験の実施日に公式ページと対象アカウントで確認する項目を整理する。

## IAM Identity Centerと短期認証情報

AWS IAMのセキュリティベストプラクティスでは、人がAWSへアクセスするとき、IDプロバイダーとのフェデレーションと一時的な認証情報を使用する。複数アカウントへのアクセスを一元管理する場合、AWSはAWS IAM Identity Centerを推奨している。

IAM Identity Centerのユーザーには、割り当てられたPermission Setに対応するIAMロールを通じて短期認証情報が与えられる。AWS CLIではSSO token provider configurationが推奨されており、`aws configure sso`でProfileを構成し、`aws sso login --profile <profile-name>`でサインインする。AWS access portalのSessionが有効な間、CLIは短期認証情報を取得し、必要に応じて更新する。Session自体が失効した場合は、再度サインインする。

短期認証情報も権限を持つ認証情報である。Permission SetまたはIAMロールには、実験に必要な最小権限を付与する。認証情報、Account ID、完全なARNなどをRepositoryや学習成果物へ保存しない。

## Region、モデル提供状況、Service Quotas

Amazon Bedrockで利用できるモデルと推論方式はRegionによって異なる。公式のRegional availabilityでは、モデルごとにIn-Region、Geographic cross-Region、Global cross-Regionの対応状況が示されている。In-Regionは指定した単一Region内で処理され、Cross-Region inferenceは対応する地理的範囲または商用Regionへリクエストをルーティングする。したがって、単に「Bedrockが利用可能なRegion」だけでなく、利用するモデル、推論方式、データ所在地の要件を合わせて確認する必要がある。

Service Quotasは、AWSアカウント、AWS Region、またはリソースに適用されるリソース数や操作数の上限である。Service Quotasコンソールでは、デフォルト値、適用済みの値、調整可能かどうかを確認できる。増加申請は承認、却下、一部承認のいずれにもなり得て、処理には時間がかかる。

Amazon Bedrockのモデル推論にはトークン使用量に関するクォータがあり、一部のモデルではトークンが異なる倍率で数えられる。Bedrockのデフォルトクォータは、Regionなどの条件により更新されることがある。実験前には対象Regionと対象アカウントで、使用するモデル・エンドポイントに対応する適用済みクォータを確認する。

## Amazon Bedrockの料金

Amazon Bedrockの料金ページは、モデル推論だけでなく、Knowledge Bases、Guardrails、Model Evaluation、Data Automationなどの機能別料金を掲載している。モデル料金はModality、Provider、Modelに依存し、Standard、Flex、Priority、Reservedなど複数のService Tierがある。モデルや方式によっては、入力・出力トークン、画像、動画、クエリ、時間、モデルユニットなど、課金単位も異なる。

料金を確認するときは、少なくとも次を一致させる。

- 利用する機能とモデルID
- RegionまたはCross-Region inferenceの方式
- On-Demand、Batch、Provisioned Throughputなどの推論方式
- 入力・出力、Cache、組み込みToolなど、利用する課金項目
- Model invocation以外に作成するストレージ、検索、ログなどのAWSリソース

単価と提供条件は変更され得るため、実験の実施日に公式料金ページで確認する。

## AWS Budgetsによる予算監視

AWS Budgetsでは、Cost budgetやUsage budgetなどを作成できる。Cost budgetには、費用発生後のActual spendと、費用発生前のForecasted spendに対する通知しきい値を設定できる。通知先にはEmail、Amazon SNS topic、またはその両方を指定できる。

AWS Budgetsの情報は1日に最大3回更新され、通常は前回更新から8〜12時間後に更新される。リソース利用から請求データへの反映にも遅延があるため、費用が通知しきい値を超えてから通知されることがあり、通知後も費用が増減する可能性がある。

予算通知は監視の仕組みであり、通知を設定しただけではAPI呼び出しやリソースを停止しない。しきい値到達時にAWS BudgetsからIAM PolicyやService Control Policy（SCP）を適用するなどの処理を行うには、Budget actionを別途構成し、自動実行または手動承認を選ぶ。

## Cost Explorerによる実績の分析

AWS Cost Explorerは、AWSの費用と使用量を表示・分析するためのToolである。ServiceやTagなどの条件でFilterまたはGroup化し、費用の傾向や内訳を調べられる。

Cost Explorerを初めて有効化すると、当月のデータは約24時間後に利用可能になり、それ以前のデータの準備にはさらに数日かかることがある。有効化後の費用データは少なくとも24時間ごとに更新されるが、上流の請求データによっては24時間より遅れる場合がある。そのため、Cost Explorerの表示は即時の課金メーターではない。

Cost ExplorerのConsole UIによる表示は無料で利用できる。Cost Explorer APIはページ分割されたリクエストごとに料金がかかる。APIを利用する場合は、呼び出し自体の料金も確認する。

## コスト配分タグ

コスト配分タグ（Cost allocation tag）は、AWSコストを詳しい単位で分類・追跡するために使う。User-defined tagは利用者が定義し、対応するAWSリソースへ付与する。費用分析へ使うには、リソースへタグを付けるだけでなく、Billing and Cost Management Consoleでコスト配分タグとして有効化する。

有効化したタグは、Cost ExplorerのFilterやコスト配分レポートで利用できる。タグがBilling and Cost Management Consoleへ表示されるまで最大24時間かかることがある。組織のManagement accountと、組織に属さない単独アカウントだけが、Billing ConsoleのCost allocation tag managerへアクセスできる。

タグへ機密情報を含めない。タグ対応とコスト配分の動作はAWSサービスごとに異なるため、対象リソースがタグ付けに対応するか、そのタグが費用へどのように反映されるかを各サービスの文書で確認する。

## 重要な条件と制約

- 長期Access keyより、フェデレーションまたはIAMロールによる短期認証情報を使う。人の集中管理にはIAM Identity Centerが推奨されている。
- Regionはモデル名だけで決めず、推論方式、データ所在地、モデル提供状況、適用済みクォータを合わせて確認する。
- AWS BudgetsとCost Explorerには請求データ反映の遅延がある。予算通知は即時停止を保証しない。
- Budget actionは通知とは別の構成であり、実行可能なActionの対象には制限がある。
- コスト配分タグは、リソースへの付与とBilling側での有効化の両方が必要である。
- Bedrockの料金、モデル、Region、クォータ、提供条件は、2026-09-21に公式資料で確認した。実験時にも再確認する。

## 用語

| 用語 | このページでの意味 |
|---|---|
| 短期認証情報 | 有効期限があり、IAMロールやIAM Identity Centerなどから取得する認証情報 |
| Permission Set | IAM Identity CenterでAWSアカウントへの権限を定義する設定。対応するIAMロールが作成される |
| Region | AWSサービスを提供する地理的な領域。サービス、モデル、料金、クォータの条件になり得る |
| Service Quota | AWSアカウント、Region、またはリソースに適用されるリソース数や操作数の上限 |
| Actual spend | すでに発生し、請求データへ反映された費用に基づく値 |
| Forecasted spend | 現在の利用傾向から見積もった将来の費用 |
| Budget action | 予算しきい値到達時に、AWS Budgetsが自動または承認後に実行する構成済みAction |
| コスト配分タグ | 費用をTagのKeyとValueで分類・追跡するために有効化したTag |

## このページの要点

- IAM Identity CenterまたはIAMロールによる短期認証情報と最小権限を使い、認証情報をRepositoryへ保存しない。
- Bedrockの利用可否は、モデル、推論方式、Region、クォータ、アクセス条件を実施日に確認する。
- Bedrock料金はモデル推論以外の機能や関連リソースも含めて確認する。
- AWS Budgetsは実績と予測を監視できるが、通知と請求データには遅延があり、通知だけでは利用を停止しない。
- Cost Explorerで費用を分析できるが、データは即時ではない。
- コスト配分タグは、対応リソースへの付与後にBilling側で有効化する。

## 公式資料

- [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) — 人のフェデレーション、短期認証情報、IAM Identity Center、最小権限
- [Getting IAM Identity Center user credentials for the AWS CLI or AWS SDKs](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html) — IAM Identity Centerの短期認証情報と自動更新
- [Configuring IAM Identity Center authentication with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) — AWS CLIの推奨SSO構成
- [Regional availability by models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html) — モデルごとのRegionと推論方式
- [What is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) — Quotaの定義、適用範囲、増加申請
- [Quotas for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html) — BedrockのToken quotaと確認方法
- [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/) — モデルと各Bedrock機能の料金
- [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) — Budget種別、実績・予測通知、更新遅延
- [Configuring budget actions](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html) — Budget actionの実行方式と対象
- [Analyzing your costs and usage with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) — Cost Explorerの機能、更新頻度、API料金
- [Organizing and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) — コスト配分タグの種類、有効化、反映時間
- [Using user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/custom-tags.html) — User-defined tagの適用条件と制約

最終確認日: 2026-09-21
