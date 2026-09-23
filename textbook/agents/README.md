# Textbookサブエージェント定義

22のTask別ページペアと33のサービスページを安全に並列執筆するための役割と実行順を定義する。すべてのエージェントは[`textbook/AGENTS.md`](../AGENTS.md)に従う。

## 役割

| 役割 | 定義 | 主な成果物 |
|---|---|---|
| オーケストレーター | [`orchestrator.md`](orchestrator.md) | 割り当て、競合防止、進捗管理、統合判断 |
| ページペア執筆者 | [`page-pair-writer.md`](page-pair-writer.md) | 同じTaskに対応するliteral／supplimental各1ページ |
| ページペアレビュー担当 | [`page-pair-reviewer.md`](page-pair-reviewer.md) | 公式根拠、範囲、読みやすさ、相互対応の修正または指摘 |
| 昇格ページペア執筆者 | [`page-pair-writer-high.md`](page-pair-writer-high.md) | `ESCALATE`となったページペアの再検証と再構成 |
| サービスページ執筆者 | [`service-page-writer.md`](service-page-writer.md) | 1つのサービスページの公式機能、管理境界、連携、Task対応 |
| サービスページレビュー担当 | [`service-page-reviewer.md`](service-page-reviewer.md) | サービスページの公式根拠、範囲、機能体系、役割分離の修正または指摘 |
| 昇格サービスページ執筆者 | [`service-page-writer-high.md`](service-page-writer-high.md) | `ESCALATE`となったサービスページの再検証と再構成 |
| 全体整合性監査担当 | [`cross-page-auditor.md`](cross-page-auditor.md) | 全ページ横断の用語、重複、リンク、Skill網羅性の監査結果 |

## Codexカスタムエージェント

上記の役割のうち、繰り返し起動する7つをプロジェクト固有のカスタムエージェントとして定義している。

| エージェント名 | モデル／推論強度 | 設定 | 権限 |
|---|---|---|---|
| `textbook_page_pair_writer` | Sol／medium | [`.codex/agents/textbook-page-pair-writer.toml`](../../.codex/agents/textbook-page-pair-writer.toml) | 担当ページペアのみ編集 |
| `textbook_page_pair_reviewer` | Terra／high | [`.codex/agents/textbook-page-pair-reviewer.toml`](../../.codex/agents/textbook-page-pair-reviewer.toml) | 完成済みの担当ページペアのみ編集 |
| `textbook_page_pair_writer_high` | Sol／high | [`.codex/agents/textbook-page-pair-writer-high.toml`](../../.codex/agents/textbook-page-pair-writer-high.toml) | `ESCALATE`となった担当ページペアのみ編集 |
| `textbook_service_page_writer` | Sol／medium | [`.codex/agents/textbook-service-page-writer.toml`](../../.codex/agents/textbook-service-page-writer.toml) | 担当サービスページ1ファイルのみ編集 |
| `textbook_service_page_reviewer` | Terra／high | [`.codex/agents/textbook-service-page-reviewer.toml`](../../.codex/agents/textbook-service-page-reviewer.toml) | 完成済みの担当サービスページ1ファイルのみ編集 |
| `textbook_service_page_writer_high` | Sol／high | [`.codex/agents/textbook-service-page-writer-high.toml`](../../.codex/agents/textbook-service-page-writer-high.toml) | `ESCALATE`となった担当サービスページのみ編集 |
| `textbook_cross_page_auditor` | Luna／medium | [`.codex/agents/textbook-cross-page-auditor.toml`](../../.codex/agents/textbook-cross-page-auditor.toml) | 読み取り専用 |

同時に開くサブエージェントは[`.codex/config.toml`](../../.codex/config.toml)で最大5に設定する。カスタムエージェントを指定しないサブエージェントの既定値はTerra／mediumとする。オーケストレーターはセッションへ応答しているメインエージェントが担当し、作業の割り当て、レビュー判定の受領、昇格、統合判断を保持する。

## 自動昇格フロー

ページペアとサービスページは所有単位が異なるが、判定と昇格の流れは同じである。

```text
通常執筆（Sol／medium）
  └─ レビュー（Terra／high）
       ├─ PASS     → 完了
       ├─ FIX      → レビュー担当の小修正後に完了
       └─ ESCALATE → 昇格執筆（Sol／high）→ 再レビュー
                                               ├─ PASSまたはFIX → 完了
                                               └─ ESCALATE      → 自動処理を止めて報告
```

`ESCALATE`は、主要な公式根拠の不一致、Task・Skillsまたは主要機能の重大な欠落、役割境界や管理境界の大幅な崩れ、または章全体の再構成が必要な場合に限る。同じページペアまたはサービスページの昇格は1回までとし、Sol／highを通常執筆へ予防的に使わない。

## 並列化の単位

同じファイル名を持つliteral pageとsupplimental pageを1つのページペアとして扱う。執筆者を22人固定で定義するのではなく、[`assignment-template.md`](assignment-template.md)へ対象を埋め、同じ「ページペア執筆者」を必要数だけ起動する。

この方式により、各ペア内では公式内容と補足内容の境界を一人が保ちつつ、異なるTaskのページペアを並列作成できる。

サービス別は[`service-pages/README.md`](../service-pages/README.md)の予定ファイル1つを1つの所有単位とする。[`service-page-assignment-template.md`](service-page-assignment-template.md)へ対象を埋め、異なるサービスページを並列作成する。同じ1ファイルを複数エージェントへ割り当てない。

## 推奨実行順

1. オーケストレーターがTask別目次またはサービス別目次から未着手の所有単位を選ぶ
2. 同時実行枠を超えない範囲で、異なるページペアまたはサービスページの執筆者を起動する
3. 執筆完了した所有単位だけを、対応するレビュー担当へ渡す
4. `PASS`または`FIX`なら完了とし、`ESCALATE`なら対象だけを対応する昇格執筆者へ1回再割り当てする
5. 昇格後の対象を同種のレビュー担当へ戻し、再び`ESCALATE`なら自動処理を止めて未解決事項を報告する
6. Domain単位、サービス重要度の部単位、全22ペアまたは全33サービスページの完了後に全体整合性監査を行う
7. オーケストレーターだけが目次や進捗表示を更新する

執筆中のページをレビューしたり、複数エージェントへ同じページを割り当てたりしない。利用可能な同時実行数が限られる場合は、執筆とレビューを小さなBatchで交互に行う。

## エージェントへ必ず渡す情報

ページペアには次を渡す。

- Pair IDとTask ID
- 対応Skills
- literal出力パス
- supplimental出力パス
- 対象となる`docs/tasks/`の相対パス
- 目次に記載された主な公式URL
- 編集してよいファイルと、編集禁止ファイル
- 執筆かレビューか
- レビューの場合は昇格回数（`0`または`1`）
- 昇格執筆の場合は直前のレビュー報告全文
- 完了時に報告する内容

具体的な依頼文は[`assignment-template.md`](assignment-template.md)を使う。

サービスページには次を渡す。

- Page IDと重要度
- 対象サービス／機能
- 対応Task・Skillsと参照するTask文書
- 出力パス
- 目次の主要機能サブ目次
- 関連literal／supplimental page
- 主な公式URLと変更されやすい事項
- 編集してよい1ファイルと編集禁止ファイル
- 執筆かレビューか
- レビューの場合は昇格回数（`0`または`1`）
- 昇格執筆の場合は直前のレビュー報告全文

具体的な依頼文は[`service-page-assignment-template.md`](service-page-assignment-template.md)を使う。

## 競合を避ける規則

- `workspace-write`は実行環境上の権限であり、個別ファイルの所有権は割り当て指示で制限する
- 執筆者の所有範囲は2ファイルだけとする
- サービスページ執筆者の所有範囲は割り当てられた1ファイルだけとする
- レビュー担当は執筆完了の通知後に同じ2ファイルを引き継ぐ
- サービスページレビュー担当は執筆完了の通知後に同じ1ファイルを引き継ぐ
- オーケストレーターは各完了報告で変更ファイル一覧を確認し、割り当て外の変更があれば統合前に停止する
- 全体監査中は原則として本文執筆を止める
- 横断的な修正は監査担当が直接大量編集せず、修正一覧をオーケストレーターへ返す
- 目次、テンプレート、共通指示の変更はオーケストレーターへ集約する
