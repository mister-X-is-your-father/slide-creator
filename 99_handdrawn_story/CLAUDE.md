# 99_handdrawn_story - 手書き風ストーリースライド生成

プロンプト + テンプレートシステムで手書き風の物語スライドを生成。

## ディレクトリ構造

```
99_handdrawn_story/
├── prompts/
│   ├── outline/       # アウトライン生成プロンプト
│   │   ├── picturebook.md
│   │   └── horror.md
│   ├── content/       # コンテンツ詳細化プロンプト
│   │   └── detailed.md
│   └── marp/          # Marpスライド生成プロンプト
│       └── handdrawn.md
├── templates/
│   ├── style/         # スタイル設定（JSON）
│   │   ├── picturebook.json
│   │   └── notebook.json
│   └── story/         # 物語構造（JSON）
│       └── basic.json
└── output/            # 生成物
```

## 使い方

### 1. アウトライン生成

```bash
# プロンプトを確認
cat prompts/outline/picturebook.md

# Claudeに依頼
「prompts/outline/picturebook.md のプロンプトで、
トピック: 友情
ページ数: 15
のアウトラインを生成して」
```

### 2. コンテンツ詳細化

```bash
cat prompts/content/detailed.md

# 生成されたアウトラインJSONを渡して詳細化を依頼
```

### 3. Marpスライド生成

```bash
cat prompts/marp/handdrawn.md

# コンテンツJSONとスタイルテンプレートを指定してスライド生成を依頼
```

## プロンプト変数

| 変数 | 説明 |
|------|------|
| `{topic}` | テーマ |
| `{page_count}` | ページ数 |
| `{audience}` | 対象読者 |
| `{lesson}` | 教訓（任意） |
| `{style}` | スタイルID |

## ワークフロー

```
トピック入力
    ↓
prompts/outline/*.md でアウトラインJSON生成
    ↓
prompts/content/detailed.md で各ページ詳細化
    ↓
prompts/marp/handdrawn.md + templates/style/*.json でMarp生成
    ↓
output/ に出力
```
