# 5_html_direct - HTML直接生成

## 概要

Marpを使わず、HTML/CSSでスライドを直接生成するアプローチ。
HTML/CSSの知識があれば専門ツールの学習不要。

## ディレクトリ構成

```
5_html_direct/
├── 1_input/
│   └── slides.md        # 入力（Markdown形式）
├── 2_artifacts/
│   ├── slides.yaml      # 中間形式（構造化データ）
│   └── slides.html      # 生成されたHTML
├── 3_output/
│   └── slides.pdf       # 最終出力
├── scripts/
│   └── html-to-pdf.js   # PDF変換スクリプト
├── fig/                 # 画像リソース
├── .claude/
│   └── commands/
│       └── update-slide.md
└── CLAUDE.md            # 本ファイル
```

## ワークフロー

```
1_input/slides.md
    ↓
/update-slide コマンド
    ↓
2_artifacts/slides.yaml（構造化）
    ↓
2_artifacts/slides.html（HTML生成）
    ↓
scripts/html-to-pdf.js
    ↓
3_output/slides.pdf
```

## HTML構造

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>プレゼンテーション</title>
  <style>
    /* スライドCSS */
  </style>
</head>
<body>
  <div class="slide" id="slide-1">
    <h1>タイトル</h1>
    <p>内容</p>
  </div>
  <div class="slide" id="slide-2">
    ...
  </div>
</body>
</html>
```

## CSS基本設計

```css
/* スライド基本 */
.slide {
  width: 1280px;
  height: 720px;
  padding: 60px;
  page-break-after: always;
  box-sizing: border-box;
}

/* 印刷用 */
@media print {
  .slide {
    page-break-after: always;
  }
}
```

## カラーパレット

```css
:root {
  --primary: #2563eb;
  --secondary: #64748b;
  --accent: #f59e0b;
  --background: #ffffff;
  --text: #1e293b;
}
```

## メリット

- 専門ツール学習不要
- 自由度が高い
- CSS調整で全ページ一括変更
- GitHubで全アセット管理

## デメリット

- ページ管理が煩雑
- レスポンシブ対応は自前

## 依存ツール

- Node.js
- Puppeteer (`npm install puppeteer`)
