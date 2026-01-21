# Slide Creator

Marp を使用したスライド作成ワークフロー

## ディレクトリ構成

```
slide-creator/
├── 1_input/      # 入力（テキスト、アイデア、ストーリー）
├── 2_create/     # 作成（Marp Markdown スライド）
├── 3_export/     # 出力（PDF, Google Slides）
│   └── googleslides/   # Google Slides API 連携
├── theme/        # CSS テーマ
└── assets/       # アイコン・素材
```

## ワークフロー

### 1. 入力 (`1_input/`)

物語やアイデアをテキストファイルで保存:
```
1_input/my_story.txt
```

### 2. 作成 (`2_create/`)

Marp 形式の Markdown でスライドを作成:
```markdown
---
marp: true
theme: handdrawn
---

# タイトル

内容...
```

### 3. 出力 (`3_export/`)

#### PDF に出力（Marp CLI）
```bash
npx @marp-team/marp-cli 2_create/my_slides.md -o 3_export/my_slides.pdf --theme theme/handdrawn.css
```

#### Google Slides に出力
```python
from googleslides import PresentationBuilder

builder = PresentationBuilder(template_name='default')
builder.add_title_slide("タイトル")
presentation_id, url = builder.build("My Presentation")
```

## テーマ

`theme/` に CSS テーマファイルを配置:
- `handdrawn.css` - 手書き風テーマ

## 素材

`assets/` にアイコン・画像を配置:
- `icons/lucide/` - Lucide アイコン
- `icons/phosphor/` - Phosphor アイコン

## セットアップ

### Marp CLI
```bash
npm install -g @marp-team/marp-cli
```

### Google Slides（オプション）
```bash
pip install -r 3_export/googleslides/requirements.txt
```

詳細は `CLAUDE.md` を参照。
