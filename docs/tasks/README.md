# 実行用学習タスク

最終確認日: 2026-09-21

## 使い方

このディレクトリは、[`docs/study-plan.md`](../study-plan.md) の10週間ロードマップを、1回30〜90分で着手できる作業へ分解したものである。公式試験ガイドの全20 Task・全98 Skillsを、各ドメイン文書のチェック項目へ割り当てている。

教材・演習は次の順で組み合わせる。

1. **公式資料**: AWS公式ドキュメント、AWS Prescriptive Guidance、AWS Well-Architected、AWS公式コード例で仕様と選定条件を確認する
2. **ローカル基準線**: [`labs/local-genai/`](../../labs/local-genai/) のFixtureとStubで正常系・異常系を安価かつ反復可能にする
3. **AWS実機**: 同じシナリオをBedrock、IAM、CloudWatch／CloudTrailなどで実行し、Response、権限、Metric、Log、料金を観測する
4. **比較と片付け**: ローカルとの差、Managed serviceへ委譲された責務、概算・実績費用、削除確認を成果物へ残す

Amazon Bedrockのモデル呼び出し、Guardrails、Knowledge Bases、評価Jobなどは料金が発生し得る。月間上限目安は5,000円、通常の実行停止線は4,000円とする。AWS Budgetsの通知は支出を物理的に止める仕組みではないため、実行前の上限設定、少量実行、終了時削除を併用する。詳細は[ラボのコスト・安全ルール](../../labs/local-genai/README.md#コストガードレール)に従う。

## 時間とタスク一覧

| 区分 | Task | 時間 | 実行文書 |
|---|---:|---:|---|
| 準備 | 2 | 3時間30分 | この文書 |
| Domain 1 | 6 | 25時間 | [FM統合、データ管理、コンプライアンス](domain-1.md) |
| Domain 2 | 5 | 21時間 | [実装と統合](domain-2.md) |
| Domain 3 | 4 | 16時間 | [安全性、セキュリティ、ガバナンス](domain-3.md) |
| Domain 4 | 3 | 10時間 | [運用効率と最適化](domain-4.md) |
| Domain 5 | 2 | 8時間 | [テスト、検証、トラブルシューティング](domain-5.md) |
| **合計** | **22** | **83時間30分** | 準備3時間30分＋本編80時間 |

目安時間には、公式資料の読解、成果物作成、ローカル／AWSラボ、振り返りを含む。問題演習と週次レビューは各Task内へ組み込んでいる。AWSのConsole表示やResource作成待ち時間は含めない。

## 最初に実施する準備タスク

### PREP-01: 試験範囲と現在地を確定する（1時間30分）

教材:

- [AIP-C01公式試験ガイド](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html)
- [公式Exam Prep Plan](https://skillbuilder.aws/category/exam-prep/generative-ai-developer-professional-AIP-C01)（Skill Builderへの無料登録が必要。購読限定項目は使わない）
- [AWS認定試験ページ](https://aws.amazon.com/certification/certified-generative-ai-developer-professional/)

作業:

- [x] 20分: 5ドメインの配点と全20 Taskを一読する
- [x] 20分: Target candidateとOut-of-scope job tasksを確認する
- [x] 20分: Skill Builderへ登録し、無料で利用できるExam Prep PlanとOfficial Practice Question Setの有無を確認する（2026-09-21完了）
- [ ] 20分: 無料で利用できる公式問題を解き、Domain別の正答数を記録する。提供されていなければ、各Taskを0〜2で自己評価する
- [ ] 10分: 弱点上位3つを [`docs/study-plan.md`](../study-plan.md) に追記する

確認結果（2026-09-21）: AIP-C01 Exam Prep Planへ登録済み。Plan内に無料対象の `Official Practice Question Set: AWS Certified Generative AI Developer - Professional (AIP-C01 - English)` があることを確認した。`Domain Practice` と `AWS SimuLearn` には `Subscription` 表示があるため、必須の無料経路には含めない。提供条件は変更され得るため、問題演習の実施時にも表示を再確認する。

完了条件: 弱点上位3つ、開始日、受験予定日、週の学習枠が記録されている。

### PREP-02: AWS／ローカル統合ラボを準備する（2時間）

前提: Python 3.10以上、AWSアカウント、AWS CLI。認証情報はRepositoryへ保存せず、IAM Identity Centerまたは短期Credentialを優先する。外部Model API keyと追加Python packageは不要。

作業:

- [ ] 15分: [`labs/local-genai/README.md`](../../labs/local-genai/README.md) のシナリオ、実行Level、停止条件を読む
- [ ] 15分: `python3 labs/local-genai/scripts/check_setup.py` と初期Testを実行する
- [ ] 20分: `data/knowledge-base/`、`data/evaluation/`、`data/security/` と `artifacts/` のTemplateを確認する
- [ ] 15分: AWS CLIでCaller identityとRegionを確認する。Account IDやCredentialを成果物・Logへ転記しない
- [ ] 25分: AWS Budgetsに月5,000円相当の予算と50%・80%・100%通知を設定し、4,000円で有料実験を止める運用を `artifacts/cost-log.md` に記録する
- [ ] 15分: `Project=aip-c01-lab`、`Purpose=study`、`ExpiresOn=YYYY-MM-DD` の共通Tagと、作成予定Resource／削除手順を決める
- [ ] 15分: 当日のBedrock料金、利用Region、利用予定Model、Quotaを公式ページで確認する

完了条件: Setup checkと初期Testが成功し、AWSのCaller identity／Region、予算通知、停止線、共通Tag、最初の実験の削除手順を確認できる。

## 各Taskの進め方

1. Task冒頭の公式資料を読む
2. Skill番号付きチェック項目を上から実施する
3. 指定された成果物を `labs/local-genai/artifacts/` または対応する `docs/notes/` に残す
4. AWS実機を使うTaskでは実行前後のResource一覧、呼出回数、概算／実績、削除確認を `artifacts/cost-log.md` に追記する
5. 完了条件を満たしたらTask見出し横に完了日を追記する
6. 確信を持てなかった判断を [`questions/mistake-log.md`](../../questions/mistake-log.md) に記録する

成果物は答えの丸写しではなく、次を含める。

- 選択した方式と要件
- 除外した方式と理由
- Security、可用性、性能、コストの注意点
- 公式根拠URLと確認日
- ローカルとAWS実機の観測差
- 実験結果、費用、削除確認、または確認できなかった事項

## 共通の完了判定

各Domainの最終Taskを完了する前に、次を確認する。

- [ ] 対象TaskのすべてのSkill番号がチェック済み
- [ ] 少なくとも1つの比較表または構成図がある
- [ ] 少なくとも1つの正常系と2つの異常系を試した
- [ ] AWS実機を少なくとも1回使い、Request／Response、IAM、MetricまたはLogのいずれかをEvidenceとして残した
- [ ] サービス名の暗記ではなく、要件から選ぶ理由を説明できる
- [ ] 公式URLと確認日をノートへ記録した
- [ ] 誤答・迷いを間違い記録へ反映した

## 教材・AWS利用上の注意

- AWS Skill Builderには無料デジタル教材と購読限定のラボが混在する。利用前に料金と残予算を確認する
- AWS公式WorkshopやAWS Samplesでも、デプロイ先のAWSリソースには料金が発生し得る
- 料金、対応Region、Model ID、Quota、Free Tier／Credit条件は変更される。実施日に公式ページを再確認する
- Provisioned Throughput、常時稼働SageMaker endpoint、NAT Gateway、大きなOpenSearch／Aurora構成はこの予算では原則作成せず、設計比較で学ぶ
- Budget通知は料金発生を即時停止しない。4,000円到達／予測、想定外Resource、削除失敗のいずれかで新規実験を止める
- Amazon Bedrock Agents Classicなど提供状況が変化する機能は現行試験ガイドを基準にし、実装時は現行の一般的なTool-use／AgentCore／ローカル比較を使う

公式情報の最終確認日: 2026-09-21
