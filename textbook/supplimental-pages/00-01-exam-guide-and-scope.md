# AIP-C01試験ガイドと出題範囲: 理解と判断の補足

## このページの位置づけ

| 項目 | 内容 |
|---|---|
| 対応Task | `PREP-01` |
| 対応Skills | なし（準備タスク。本編20 Task・98 Skillsの学習優先度を決める） |
| 対応する公式解説 | [`00-01-exam-guide-and-scope.md`](../literal-pages/00-01-exam-guide-and-scope.md) |
| この補足で身につける判断 | Domain、Task、Skill、技術・概念、サービス一覧の役割を区別し、Taskを起点に学ぶ範囲と深さを決められるようにする |

## まず全体像

AIP-C01の学習では、サービス名の一覧を起点にすると学ぶ深さを決めにくい。先に「対象者が何を遂行する試験か」を確認し、`Domain → Task → Skill`の順で要求能力を具体化してから、その実現手段として技術・概念とAWSサービスを結び付ける。

この関係は、次のように整理できる。

```text
対象職務
  └─ Domain（責務領域・配点）
       └─ Task（遂行する仕事）
            └─ Skill（必要な具体的能力）
                 ├─ 技術・概念
                 └─ AWSサービス／機能
```

この図の要点は、AWSサービスが最下層の実現手段であり、Taskそのものではないことである。同じサービスが複数Taskを支え、1つのTaskが複数サービスを組み合わせることもある。

## 5種類の情報を混同しない

| 情報 | 答える問い | 学習での使い方 | 単独では判断できないこと |
|---|---|---|---|
| Domainと配点 | どの責務領域がどの比率で採点されるか | 学習時間の大枠を配分する | 個々のサービスをどこまで深く学ぶか |
| Task | 対象者がどの仕事を遂行するか | 章・演習・到達目標の単位にする | 実装に使う具体的な方式 |
| Skill | Task遂行に必要な能力は何か | 要件、実装、評価、運用などの確認項目にする | 例示されたサービスだけが唯一の正解か |
| 技術・概念一覧 | どの横断概念が現れ得るか | Taskをまたぐ用語の漏れを確認する | 掲載順から重要度や配点を推定すること |
| 対象サービス一覧 | どのAWSサービス／機能が現れ得るか | Task・Skillを実現する候補を確認する | サービス名だけから出題文脈や学習深度を決めること |

たとえばAmazon Bedrockは、FM呼び出しだけでなく、Knowledge Bases、Prompt Management、Guardrails、Evaluationなどを通じて複数Domainに関係する。「Amazon Bedrockを学ぶ」という広い目標より、「Task 1.5で検索精度を改善する」「Task 3.1で入力・出力を制御する」のようにTaskへ戻すと、必要な機能と判断軸が明確になる。

## 範囲内／範囲外を見分ける

試験ガイドの一覧は非網羅的である。そのため、掲載の有無だけで未知の項目を機械的に判定せず、次の順で確認する。

1. 最新のDomain文書で、該当するTask・Skillが明記されているかを確認する。
2. Skillが求める能力に、その技術やサービスが直接必要かを確認する。
3. Technologies and concepts、In-Scope Services、Out-of-Scope Servicesで明示的な位置づけを確認する。
4. 明示されない場合は、Task遂行に必要な一般概念なのか、単なる関連知識なのかを分ける。
5. 公式資料で根拠が取れない事項は、試験範囲だと断定しない。

| 状況 | 学習上の扱い | 理由 | 避ける判断 |
|---|---|---|---|
| Task／Skillに直接書かれている | 最優先で学ぶ | 対象者に求められる能力が明示されている | サービス名だけ覚えて、要件・制約・除外理由を省く |
| In-Scope ServicesにあるがTaskとの接点が曖昧 | 関連Taskを特定してから深さを決める | 一覧は非網羅的で、サービスごとの出題比率を示さない | 全機能を同じ深さで暗記する |
| Out-of-Scope Servicesにある | 試験対策の優先度を下げる | 公式に範囲外と示されている | 似た名前の対象サービスまで一緒に除外する |
| 一覧にないがSkillの遂行に必要な一般概念 | Taskに必要な深さで確認する | 試験ガイドは完全な一覧ではない | 「一覧にないから絶対に出ない」と断定する |
| 対象職務外のモデル学習や高度なML | 関連Taskの理解に必要な境界だけ押さえる | 試験対象は生成AIソリューションの本番統合である | 学習アルゴリズムの詳細へ学習時間を広げる |
| 試験範囲外だが学習環境の運用に必要 | 試験知識と運用手順を分けて扱う | 安全な学習には範囲外サービスが必要な場合もある | ラボで使うことを理由に試験範囲だとみなす |

最後の行は特に重要である。たとえばAWS Budgetsは2026-09-21時点のOut-of-Scope Servicesに含まれるが、学習用AWSアカウントの費用管理には有用である。「試験に出るか」と「安全に学習するために使うか」は別の判断である。

## サービス名ではなくTaskから学ぶ

1つのTaskを学ぶときは、次の順で整理する。

1. **仕事を一文にする**: Taskの動詞と目的語を使い、「何をできる必要があるか」を表す。
2. **Skillを判断項目へ変える**: 各Skillについて、要件、選択肢、制約、失敗時の扱いを確認する。
3. **技術・概念を結び付ける**: RAG、Agent、Observabilityなど、判断に必要な原理を押さえる。
4. **サービスを候補として比較する**: 各サービスがどの要件を満たし、どの条件では外れるかを説明する。
5. **運用まで確認する**: Security、Availability、Performance、Cost、EvaluationがTaskにどう関わるかを見る。

### Task起点の学習記録

| 記録項目 | 書く内容 |
|---|---|
| Task | 対象者が遂行する仕事 |
| 要件 | 機能要件と非機能要件 |
| 関連Skills | 判断または実装できる必要がある項目 |
| 技術・概念 | 方式が成立する原理と用語 |
| 候補サービス | 要件を満たし得るAWSサービス／機能 |
| 選択条件 | 候補を採用する条件 |
| 除外条件 | ほかの候補を選ばない条件 |
| 公式根拠 | 最新のTask文書とサービス文書 |

この形なら、サービスが改称・追加されても、Taskと要件を基準に知識を更新できる。

## 配点の使い方

Domain配点は学習時間の初期配分には使えるが、問題数を正確に逆算するための値ではない。採点対象65問に比率を掛けても端数が生じ、10問の採点対象外問題は受験中に識別できない。また、Compensatory scoringなので、各Domainに独立した合格点があるわけではない。

したがって、配点が高いDomainを優先しつつも、低配点Domainを捨てる根拠にはしない。Task間の依存も考慮する。たとえばMonitoringとTroubleshootingは別Domainだが、障害を切り分けるには観測情報が必要であり、学習上は結び付けて理解する。

## 理解用シナリオ

> これは理解のために作成した例であり、実際の認定試験問題ではない。

学習者がIn-Scope Services一覧を見て、Amazon OpenSearch Serviceの全機能を最初から暗記しようとしている。一方、まだTask 1.4（Vector Store）、Task 1.5（Retrieval）、Task 4.2（Performance）、Task 4.3（Monitoring）のSkillを読んでいない。

### 判断

まず4つのTaskを読み、Amazon OpenSearch Serviceが各Taskで果たす役割を分ける。Vector StoreではIndexやScale、RetrievalではSemantic／Hybrid Search、PerformanceではQueryとIndexの最適化、Monitoringでは検索性能とデータ品質が判断軸になる。

サービスの全機能を均等に暗記する方法は選ばない。公式一覧は、そのサービスの全機能が同じ深さで出題されることを示していないからである。各Taskの要件に関連する機能、制約、代替案との比較へ学習範囲を絞る。

## 範囲変更へ追随する

試験ガイドは更新され得るため、古い学習資料のサービス名だけを信頼しない。確認順は次のとおりである。

1. AIP-C01 Exam Guideの対象者、Domain配点、問題構成
2. 各DomainのTaskとSkill
3. Technologies and concepts
4. In-Scope／Out-of-Scope Services
5. AWS認定ページとSkill Builderの準備リソース

変更を見つけたら、サービス一覧だけでなく、そのサービスが関係するTask・Skillと学習成果物も見直す。名称変更の場合は単なる表記差か、機能・責務の変更かを公式サービス文書で確認する。

## 理解を確認する

- Domain、Task、Skill、技術・概念、対象サービスの役割を、それぞれ一文で区別できるか。
- In-Scope Servicesに掲載されたサービスの全機能を暗記する必要がない理由を説明できるか。
- 一覧にない技術を「必ず範囲外」と断定できない理由を説明できるか。
- 対象職務外のModel Trainingと、対象範囲のFM Customization／Deploymentの境界をTaskから確認できるか。
- AWS Budgetsのように、試験範囲外でも学習環境の運用に使うサービスを区別できるか。
- 1つのTaskについて、候補サービスの採用条件と除外条件を公式根拠付きで説明できるか。

## 根拠と補足の区別

- 公式情報: 対象職務、5 Domainと配点、20 TaskとSkills、技術・概念、対象／対象外サービス、試験構成、公式準備リソース。
- 補助的な整理: 階層図、5種類の情報の比較、範囲判定手順、Task起点の学習順、学習記録表、理解用シナリオ。

## 公式資料

- [AIP-C01 Exam Guide](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html) — 試験の対象職務、構造、配点、非網羅性
- [Technologies and concepts](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-technologies-concepts.html) — 技術・概念一覧の位置づけ
- [In-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/aip-01-in-scope-services.html) — 対象サービス一覧と非網羅性
- [Out-of-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/aip-01-out-of-scope-services.html) — 対象外サービス一覧と非網羅性
- [AWS Certified Generative AI Developer - Professional](https://aws.amazon.com/certification/certified-generative-ai-developer-professional/) — 現行の試験構成とAIP-C01準備経路
- [AWS Certification exam preparation](https://aws.amazon.com/certification/certification-prep/) — 無料／Subscription準備リソースの区分

最終確認日: 2026-09-21
