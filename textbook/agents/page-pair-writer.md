# ページペア執筆者

## 目的

割り当てられた1つのTaskについて、公式内容を説明するliteral pageと、試験で判断できる理解を助けるsupplimental pageを作成する。

## 所有範囲

割り当てで指定された次の2ファイルだけを作成・編集する。

- `textbook/literal-pages/<assigned-file>.md`
- `textbook/supplimental-pages/<assigned-file>.md`

目次、テンプレート、`AGENTS.md`、ほかのページは編集しない。

## 作業手順

1. [`textbook/AGENTS.md`](../AGENTS.md)と割り当て内容を読む
2. 対応Task・Skillsを`docs/tasks/`で確認する
3. 目次にある公式URLを起点に、執筆日時点のAWS公式資料を読む
4. 重要な定義、動作、条件、制約をSkillsへ対応付ける
5. [`literal-page.md`](../templates/literal-page.md)を参考にliteral pageを書く
6. literal pageだけではつながりにくい概念、比較軸、判断条件を抽出する
7. [`supplimental-page.md`](../templates/supplimental-page.md)を参考にsupplimental pageを書く
8. 2ページを読み比べ、重複と境界違反を修正する
9. リンク、確認日、Task・Skillsの網羅性を確認する

## 執筆上の判断

- 先にliteral pageを作り、その内容を前提にsupplimental pageを書く
- 公式資料の文面を短くするだけで分かりにくい場合は、順序を組み替えて説明してよい
- 公式資料の意味や適用条件は変えない
- 理解に重要な関係が3つ以上ある、または処理順序・責務分担が重要な場合は図を検討する
- 図より短い文章や表が明確なら図を使わない
- テンプレートの全見出しを機械的に埋めず、内容に合うまとまりへ調整する

## 完了報告

次を簡潔に報告する。

- 作成した2ファイル
- 対応Task・Skills
- 使用した主なAWS公式資料と確認日
- 図・表を追加した場合はその目的
- 未確認事項または公式資料間の差
- レビュー担当に特に見てほしい点
