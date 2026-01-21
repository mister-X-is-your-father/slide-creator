# プロンプトディレクトリ

手書き風ストーリー生成用のプロンプトテンプレート。

## ディレクトリ構造

```
prompts/
├── outline/          # アウトライン生成
│   ├── default.md    # 汎用
│   ├── picturebook.md # 絵本向け
│   └── horror.md     # ホラー向け
├── content/          # コンテンツ詳細化
│   └── detailed.md
└── html/             # HTML生成
    └── reveal-default.md
```

## 変数

| 変数名 | 説明 | 例 |
|--------|------|-----|
| `{topic}` | トピック | "友情" |
| `{slide_count}` | スライド数 | 10 |
| `{language}` | 言語 | "ja" |
| `{audience}` | 対象読者 | "子供向け" |
