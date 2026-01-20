# update-slide

1_input/slides.md から HTML/PDF を生成する一連の処理。

## 手順

1. `1_input/slides.md` を読み込む
2. YAML形式に構造化 → `2_artifacts/slides.yaml`
3. HTMLを生成 → `2_artifacts/slides.html`
4. PDFを生成 → `3_output/slides.pdf`

## YAML構造

```yaml
title: プレゼンテーションタイトル
author: 発表者名
date: 2024-01-01
slides:
  - type: title
    title: メインタイトル
    subtitle: サブタイトル

  - type: content
    title: スライドタイトル
    bullets:
      - ポイント1
      - ポイント2

  - type: image
    title: 画像スライド
    image: fig/image.png
    caption: キャプション
```

## HTML生成テンプレート

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>{{title}}</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    .slide {
      width: 1280px;
      height: 720px;
      padding: 60px;
      page-break-after: always;
      font-family: 'Noto Sans JP', sans-serif;
      background: #fff;
      color: #1e293b;
    }

    .slide h1 {
      color: #2563eb;
      font-size: 2.5em;
      margin-bottom: 0.5em;
      border-bottom: 3px solid #2563eb;
      padding-bottom: 0.3em;
    }

    .slide ul {
      font-size: 1.4em;
      line-height: 1.8;
      margin-left: 1.5em;
    }

    .slide.title-slide {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
    }

    .slide.title-slide h1 {
      border-bottom: none;
      font-size: 3em;
    }

    @media print {
      .slide { page-break-after: always; }
    }
  </style>
</head>
<body>
  {{#each slides}}
  <div class="slide {{type}}-slide" id="slide-{{@index}}">
    <h1>{{title}}</h1>
    {{#if bullets}}
    <ul>
      {{#each bullets}}
      <li>{{this}}</li>
      {{/each}}
    </ul>
    {{/if}}
  </div>
  {{/each}}
</body>
</html>
```

## PDF変換

```bash
cd 5_html_direct
node scripts/html-to-pdf.js 2_artifacts/slides.html 3_output/slides.pdf
```

## 依存

- Node.js
- Puppeteer (`npm install puppeteer`)
