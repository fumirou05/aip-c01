# AIP-C01 教科書

AWS公式資料の内容を、AIP-C01の学習順に読みやすい日本語で整理する。学習計画と実行タスクから抽出したliteral／supplimentalのページペアに加え、同じ範囲をサービス単位で体系化する。

最終抽出日: 2026-09-22

作成状況: 22ページペア中9ペアを作成・レビュー済み（PREP-01、PREP-02、D1-01〜D1-06、D2-02）。Domain 1の6ページペアは横断監査済み。サービス別は33ページの目次を作成済み、本文は未作成。

## 2種類のページ

| 種類 | 役割 | 含めるもの | 含めないもの |
|---|---|---|---|
| [`literal-pages/`](literal-pages/README.md) | 公式資料の内容を、意味を変えずに平易な日本語へ再構成する | 公式の定義、機能、制約、手順、試験Task・Skill | 独自の推奨、公式資料にない例、学習上の補足 |
| [`supplimental-pages/`](supplimental-pages/README.md) | 各literal pageの内容を、試験で選択・判断できる理解へつなぐ | 前提知識、概念間の関係、比較軸、シナリオ、設計判断、具体例 | 既存の疑問・誤答を起点にした記事、公式仕様であるかのように断定した独自解釈 |

`literal` は「逐語訳」ではない。原文の章立てや意味を尊重しつつ、不自然な直訳を避けた日本語で説明する。補足が必要な場合は本文へ混ぜず、対応する `supplimental-pages` へリンクする。

`supplimental` は既存の疑問に答えるFAQではない。対応するliteral pageとTask・Skillを先に定め、その内容について、試験のシナリオから要件を読み取り、方式を選び、他の選択肢を除外できるようにするための補助教材とする。学びログや間違い記録は復習や改善には利用できるが、補足章の収録範囲を決める根拠にはしない。

## サービス別の学習軸

[`service-pages/`](service-pages/README.md)は、Task・Skill別の2種類のページと競合する第3の本文分類ではなく、同じ試験範囲をAWSサービス別に引き直す学習軸である。公式In-Scopeのサービス／機能をA（中核）、B（重要）、C（関連）に分け、各サービスの主要機能をサブ目次として整理している。

- Taskの定義・Skillを確認する: [`literal-pages/`](literal-pages/README.md)
- 要件からの選択と除外理由を学ぶ: [`supplimental-pages/`](supplimental-pages/README.md)
- 1サービスの機能全体と連携関係を学ぶ: [`service-pages/`](service-pages/README.md)

## 目次の範囲

- 準備: 試験範囲、対象サービス、学習時のAWS利用
- Domain 1: 6 Task、28 Skills
- Domain 2: 5 Task、25 Skills
- Domain 3: 4 Task、15 Skills
- Domain 4: 3 Task、16 Skills
- Domain 5: 2 Task、14 Skills
- 補足: 上記22ページと対応し、試験で必要な比較・判断・適用を補助する22ページ
- サービス別: 公式In-Scope 106項目をA（中核）13ページ、B（重要）13ページ、C（関連）7ページへ整理する33ページ

本編20 Task・98 Skillsは [`docs/tasks/`](../docs/tasks/README.md) と一対一で追跡できるようにする。目次にないテーマは、試験ガイドの対象か、既存タスクの完了に必要かを確認してから追加する。

## 読み方

1. [`literal-pages` の目次](literal-pages/README.md)から対象Taskの公式内容を読む
2. 分かりにくい概念や選定理由を[`supplimental-pages` の目次](supplimental-pages/README.md)で補う
3. 関係するAWSサービスの機能全体を[`service-pages` の目次](service-pages/README.md)から確認する
4. [`docs/tasks/`](../docs/tasks/README.md)で演習し、結果を[`docs/notes/`](../docs/notes/README.md)へ残す
5. 判断を誤った箇所を[`questions/mistake-log.md`](../questions/mistake-log.md)へ記録する

## 本文を追加するときの共通ルール

- 各ページの冒頭に、対応Task・Skill、対象読者、前提知識を書く
- 公式URLと最終確認日をページ単位で記録する
- 料金、対応Region、Quota、Model ID、Connector、提供状況は変更され得る情報として確認日を添え、利用時に公式対応表を再確認する
- 目次で作成済みとするページは、見出しではなく実ファイルへ直接リンクする
- 類似するサービス名や機能名は管理主体と接続主体を分ける。例えば、Amazon Bedrock Managed Knowledge Baseの基盤管理とBedrock AgentCore connectorは別の責務として書く
- 原文の長い転載や逐語訳を避け、自分の言葉で要点を再構成する
- `literal-pages` では、公式資料から確認できる事実と範囲だけを書く
- `supplimental-pages` は必ず対応するliteral pageとTask・Skillを明記し、試験で必要な理解の範囲を越えて広げない
- `supplimental-pages` では、「公式情報」「概念整理」「比較・判断」「シナリオ例」を見出しで区別する
- 既存の疑問、学びログ、誤答の有無を理由に補足章を追加・削除しない
- 公式情報と既存ノートが異なる場合は公式情報を優先し、ノート側へ差分と確認日を残す
- 認定試験の非公開問題や問題文の転載は含めない

## 目次の抽出元

- [`docs/study-plan.md`](../docs/study-plan.md)
- [`docs/tasks/README.md`](../docs/tasks/README.md)
- [`docs/tasks/domain-1.md`](../docs/tasks/domain-1.md)
- [`docs/tasks/domain-2.md`](../docs/tasks/domain-2.md)
- [`docs/tasks/domain-3.md`](../docs/tasks/domain-3.md)
- [`docs/tasks/domain-4.md`](../docs/tasks/domain-4.md)
- [`docs/tasks/domain-5.md`](../docs/tasks/domain-5.md)

[`docs/notes/`](../docs/notes/README.md)、[`docs/glossary.md`](../docs/glossary.md)、[`questions/mistake-log.md`](../questions/mistake-log.md)は学習結果の記録先であり、目次の範囲を決める抽出元にはしない。

公式範囲の基準は[AIP-C01 Exam Guide](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html)とする。

## 並列執筆

- [`AGENTS.md`](AGENTS.md): textbook配下で作業する全エージェントの共通ルール
- [`agents/`](agents/README.md): ページペア執筆、レビュー、全体監査の役割定義と割り当て方法
- [`.codex/agents/`](../.codex/agents/): Codexから選択できるプロジェクト固有のカスタムエージェント
- [`templates/literal-page.md`](templates/literal-page.md): literal pageのひな形
- [`templates/supplimental-page.md`](templates/supplimental-page.md): supplimental pageのひな形
- [`templates/service-page.md`](templates/service-page.md): サービスページのひな形

テンプレートは必須項目の漏れを防ぐための出発点であり、見出しの順序や数を厳密に揃えることより、内容に合った分かりやすい構成を優先する。
