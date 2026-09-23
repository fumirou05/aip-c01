# <AWSサービス名>

最終確認日: YYYY-MM-DD

| 項目 | 内容 |
|---|---|
| 重要度 | A: 中核 / B: 重要 / C: 関連 |
| 対象サービス／機能 | 公式表記で記載 |
| 対応Task・Skills | Task X.X / Skill X.X.X〜X.X.X |
| このページで分かること | サービスの役割、主要機能、管理境界、主要な連携を2〜3文で記載 |

## 全体像

サービスが解決すること、AWSが管理する範囲、利用者が管理する範囲を先に説明する。

処理順序や責務分担が複雑な場合だけ、Mermaid図または表を置く。図の意味は本文でも説明する。

## 主要機能

`service-pages/README.md`で指定された主要機能サブ目次を、内容に合う見出しへ展開する。

各機能について、必要な範囲で次を説明する。

- 入力
- 処理または保持する状態
- 出力
- AWSと利用者の管理境界
- 代表的な連携先
- 公式の適用条件と制約

## API、Event、Dataの入出力

主要なControl plane／Data plane API、Event、Data formatを試験範囲に必要な深さで整理する。

## SecurityとData保護

IAM、暗号化、Network、機密情報、監査に関係する事項を整理する。

## 可観測性と運用

Metric、Log、Trace、可用性、Scaling、Quota、料金要因を整理する。変化し得る値は固定値として暗記させず、確認先と確認日を示す。

## AIP-C01との対応

| Task・Skill | このサービスが担う役割 | 関連ページ |
|---|---|---|
| Task X.X / Skill X.X.X | 役割を記載 | [literal](../literal-pages/<file>.md) / [supplimental](../supplimental-pages/<file>.md) |

## 重要な制約と確認事項

- Region、Quota、対応Model、API、Engine／Runtime version、提供状況など
- 公式資料で確認できない事項は「未確認」と記載する

## 用語

| 用語 | このページでの意味 |
|---|---|
| 用語 | 短い説明 |

## 公式資料

- [公式資料名](https://docs.aws.amazon.com/...) — 本文で根拠にした内容

## 関連ページ

- [サービス別目次](../service-pages/README.md)
- [関連literal page](../literal-pages/<file>.md)
- [関連supplimental page](../supplimental-pages/<file>.md)
