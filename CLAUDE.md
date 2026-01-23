# Slide Creator - スライド作成システム

## 概要

テキスト/Markdownから高品質なスライドを生成するシステム。
シナリオは別で用意 → **テキストをリライトせず、配置・デザインで魅せる**。

## スキル（コマンド）

| スキル | 機能 | 主なオプション |
|--------|------|---------------|
| `/create-slide` | テキスト → Marpスライド化 | `--style`, `--characters` |
| `/build` | スライド → HTML/PDF出力 | `--format`, `--output` |
| `/export-gslides` | → Google Slides | `--mode`, `--template` |
| `/export-pptx` | → PowerPoint | `--template`, `--output` |

詳細は `.claude/commands/` 内の各ファイルを参照。

## テイスト（スタイル）

階層構造で指定。詳細は `theme/styles.json` を参照。

### business（ビジネス向け）
`default` / `modern` / `corporate` / `minimal`

### handdrawn（手書き風）
`light` / `normal` / `sketchy` / `rough` / `crayon` / `pen` / `marker`

Rough.js + roughViz による手書き風グラフィック。
- ライブラリ: `assets/js/handdrawn.js`
- デモ: `assets/js/handdrawn-example.html`

### picturebook（絵本風）
`warm` / `pastel` / `colorful` / `natural`

## ディレクトリ構成

```
slide-creator/
├── 1_input/              # 入力テキスト・下書き
├── 2_create/             # Marp形式スライド
├── 3_export/             # 出力（HTML/PDF/PPTX）
├── theme/
│   ├── styles.json       # テイスト定義
│   ├── theme.css         # 基本テーマ
│   ├── components.css    # ビジネス向けコンポーネント
│   ├── infographics.css  # グラフ・チャート
│   ├── handdrawn.css     # 手書き風テーマ
│   └── picturebook.css   # 絵本風テーマ
├── assets/
│   ├── js/
│   │   ├── handdrawn.js  # Rough.js ラッパー
│   │   └── handdrawn-example.html
│   ├── icons/            # アイコン素材
│   ├── characters/       # キャラクター素材
│   └── illustrations/    # イラスト素材
├── .claude/
│   └── commands/         # スキル定義
└── CLAUDE.md
```

## 処理ルール

### テキスト処理
- **リライトしない** - 原文をそのまま使用
- **配置は最適化** - スライド分割、レイアウト調整
- **図解は自動生成** - 内容に応じてコンポーネントを選択

### スライドルール
- タイトル: 最大30文字
- リード文: 最大2行
- 箇条書き: 1項目25文字以内、最大5項目

### 3層構造
```
タイトル（何について）
    ↓
リード文（結論・最も伝えたいこと）
    ↓
ボディ（根拠・詳細）
```

## コンポーネント一覧

### レイアウト
`title-slide` / `section-header` / `two-column` / `three-column` / `four-column`

### 図解・フロー
`flow-horizontal` / `flow-vertical` / `timeline` / `roadmap` / `gantt` / `org-chart` / `pyramid` / `funnel` / `cycle` / `matrix-2x2` / `swot`

### グラフ・チャート（infographics.css）
`pie-chart` / `donut-chart` / `bar-chart` / `radar-chart` / `skill-bars` / `animated-progress`

### 比較
`before-after` / `comparison-table` / `feature-comparison` / `pros-cons` / `vs-comparison`

### カード・ボックス
`card` / `metric-card` / `data-card` / `flip-card` / `quote-box` / `highlight-box` / `callout`

### ステップ・リスト
`steps` / `process-steps` / `arrow-steps` / `numbered-list` / `checklist` / `icon-list`

## Rough.js テイスト

`handdrawn.js` で使用可能なプリセット:

| テイスト | roughness | 用途 |
|----------|-----------|------|
| light | 0.5 | ビジネスでも使える |
| normal | 1.0 | 標準 |
| sketchy | 2.0 | 絵本向け |
| rough | 3.0 | 落書き風 |
| crayon | 2.5 | 子供向け |
| pen | 0.8 | 洗練された印象 |
| marker | 1.2 | 強調 |

カラーパレット: `warm` / `cool` / `pastel` / `earth` / `mono` / `picturebook`

## 依存ツール

- Marp CLI (`npm install -g @marp-team/marp-cli`)
- Rough.js（CDN: `https://unpkg.com/roughjs@latest/bundled/rough.cjs.js`）
- roughViz（CDN: `https://unpkg.com/rough-viz@2.0.5`）
- python-pptx（PowerPoint出力用）
- Google Slides API（要認証設定）
