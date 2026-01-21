# プロンプトディレクトリ

手書き風ストーリースライド生成用のプロンプトテンプレート。

## ディレクトリ構造

```
prompts/
├── outline/          # アウトライン生成用
│   ├── picturebook.md   # 絵本風
│   └── horror.md        # ホラー・ノート風
├── content/          # コンテンツ詳細化用
│   └── detailed.md
└── marp/             # Marpスライド生成用
    └── handdrawn.md
```

## 使い方

### Claudeに依頼する例

```
prompts/outline/picturebook.md のプロンプトを使って、
以下の条件でアウトラインを生成してください：

- トピック: 友情の大切さ
- ページ数: 15
- 対象読者: 子供向け
- 教訓: 助け合うことの喜び
```

## プロンプト変数

| 変数 | 説明 | 例 |
|------|------|-----|
| `{topic}` | テーマ | 友情、勇気 |
| `{page_count}` | ページ数 | 15 |
| `{audience}` | 対象読者 | 子供向け |
| `{lesson}` | 教訓 | 助け合いの大切さ |
| `{style}` | スタイルID | picturebook |
| `{fear_level}` | 恐怖レベル | light/medium/heavy |
