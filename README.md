# AWS Certified Generative AI Developer - Professional

AWS Certified Generative AI Developer - Professional（試験コード: **AIP-C01**）の学習用リポジトリです。

## 入口

- [学習計画](docs/study-plan.md)
- [実行用学習タスク](docs/tasks/README.md)
- [理解しやすい日本語の教科書](textbook/README.md)
- [AWS／ローカル統合ラボ](labs/local-genai/README.md)
- [公式リンク集](docs/links/official.md)
- [ドメイン別ノート](docs/notes/)
- [気軽な学びログ](docs/notes/learning-log.md)
- [用語集](docs/glossary.md)
- [間違い記録](questions/mistake-log.md)

## 試験ドメイン

- [ ] Domain 1: Foundation Model Integration, Data Management, and Compliance
- [ ] Domain 2: Implementation and Integration
- [ ] Domain 3: AI Safety, Security, and Governance
- [ ] Domain 4: Operational Efficiency and Optimization for GenAI Applications
- [ ] Domain 5: Testing, Validation, and Troubleshooting

公式の試験範囲は変更される可能性があるため、詳細は[公式試験ガイド](https://docs.aws.amazon.com/pdfs/aws-certification/latest/ai-professional-01/ai-professional-01.pdf)を基準にします。

## 学習の進め方

1. 試験ガイドで対象ドメイン・サービスを確認する
2. 公式ドキュメントを読み、`docs/notes/` に自分の言葉で要約する
3. 実装・設計上の判断理由をコード例や図で残す
4. 問題演習で迷った点を `questions/mistake-log.md` に記録する
5. 公式リンクの更新や試験ガイドの改訂を定期的に確認する

## AWS利用料金の方針

- AWS実機でしか得にくいIAM、API、監視、障害対応の経験を重視し、ラボでAWS環境を利用する
- 不必要な常時稼働リソースは避け、月間のAWS利用料は**5,000円程度まで**を上限目安とする
- ラボ実行枠は月4,000円、残り1,000円は料金反映の遅延、為替・税、削除漏れに備える安全余裕とする
- 実行前に料金・Region・Quotaを公式情報で確認し、AWS Budgetsの通知、共通Tag、終了時削除、利用記録を必須とする
- 5,000円は利用を推奨する目標額ではない。無料枠やCreditを含め、同じ学習効果なら低コストな方法を選ぶ

詳細なガードレールとAWS実機／ローカルの使い分けは [`labs/local-genai/README.md`](labs/local-genai/README.md) を基準にします。

## ノートのルール

- 外部情報は、タイトル・URL・最終確認日を残す
- AWS公式資料と自分の解釈を見出しで分ける
- 「なぜそのサービス／設計を選ぶのか」を書く
- 試験問題の転載や、認定試験の非公開情報は保存しない
- AWSアカウント情報、認証情報、個人情報はコミットしない
