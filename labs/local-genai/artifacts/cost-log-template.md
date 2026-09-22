# AWSラボ Cost log

対象月:
月間上限目安: 5,000円
新規有料実験の停止線: 4,000円
Budget通知: Actual 50% / 80% / 100%、Forecast 80% / 100%
通知確認日:

> このTemplateを `cost-log.md` へ複製して使う。Account ID、ARN、Credential、Emailは記録しない。

## 実験記録

| 日時 | Task | Region | Service／Model | 上限（Request・Token・時間） | 事前概算 | 実行量 | 実行直後の概算 | 後日確認した実績 | 削除確認 | 料金確認日 |
|---|---|---|---|---|---:|---|---:|---:|---|---|
|  |  |  |  |  |  |  |  |  |  |  |

## 実験前Checklist

- [ ] 仮説と合格条件を記録した
- [ ] 料金、Region、Model availability、Quotaを公式資料で当日確認した
- [ ] 当月実績＋最悪時概算が4,000円未満である
- [ ] 最大Request、Token、時間、Retry回数を決めた
- [ ] 作成Resource、Tag、削除順を記録した
- [ ] 架空Datasetだけを使う

## 作成・削除するResource

| Resource種別 | 論理名／Tag | 作成時刻 | 削除手順 | 削除時刻 | 残存確認方法 |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 差分と学び

- Local baselineとの違い:
- AWSへ委譲できた責務:
- AWSでもApplication側に残った責務:
- Cost／品質／LatencyのTrade-off:
- 見積りと実績の差、その理由:
- 次回の削減策:

## 公式根拠

- 料金URL:
- Region／Model URL:
- Service仕様URL:
- 確認日:
