# Slide Creator

スライド・プレゼンテーション作成ツール集

## 構成

```
slide-creator/
├── 2_marp_design_system/   # Marp ベースのスライド作成システム
└── googleslides/           # Google Slides API 連携モジュール
```

## 1. Marp Design System (`2_marp_design_system/`)

Markdown から PDF スライドを作成する手動ワークフロー。

### 特徴
- **Marp** (Markdown Presentation Ecosystem) を使用
- 手書き風テーマ対応
- CSS アイコン（Lucide, Phosphor）内蔵

### 使い方
```bash
cd 2_marp_design_system
# Markdown を作成
vim 2_slides/my_presentation.md

# PDF に変換
npx @marp-team/marp-cli 2_slides/my_presentation.md -o 3_output/my_presentation.pdf --theme theme/handdrawn.css
```

詳細は `2_marp_design_system/CLAUDE.md` を参照。

---

## 2. Google Slides Integration (`googleslides/`)

Google Slides API を使用してプレゼンテーションを作成・アップロードするモジュール。

### セットアップ

1. [Google Cloud Console](https://console.cloud.google.com/) でプロジェクト作成
2. Google Slides API を有効化
3. OAuth 2.0 クライアント ID を作成（デスクトップアプリ）
4. `credentials.json` をダウンロードしてプロジェクトルートに配置

```bash
pip install -r googleslides/requirements.txt
```

### 使い方

```python
from googleslides import PresentationBuilder

# テンプレートを指定してビルダーを作成
builder = PresentationBuilder(
    template_name='business-proposal',
    templates_dir='path/to/templates/slides'
)

# スライドを追加
builder.add_title_slide("プロジェクト提案", "2025年度")
builder.add_section_slide("01", "はじめに", "概要説明")
builder.add_content_slide("背景", ["課題1", "課題2", "課題3"])

# プレゼンテーションを作成
presentation_id, url = builder.build("My Presentation")
print(f"作成完了: {url}")
```

### サンプルスクリプト
```bash
python -m googleslides.example
```

詳細は `googleslides/README.md` を参照。

---

## ライセンス

MIT License
