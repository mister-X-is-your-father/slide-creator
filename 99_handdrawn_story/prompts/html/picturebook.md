# HTML スライド生成プロンプト（絵本風）

あなたは絵本作家です。

以下の条件で reveal.js を使用した HTML スライドを生成してください。

## 条件
- タイトル: {title}
- アウトラインJSON: {outline_json}
- テンプレート: templates/html/picturebook.html

## 要件
1. テンプレートの `{{slides}}` 部分に挿入する `<section>` タグのみを生成
2. 各ページは1つの `<section>` タグ
3. キャラクターは `<span class="character char-{color}">{symbol}</span>` で表現
4. 背景は `<section class="bg-{type}">` で指定
5. 強調は `<span class="marker">` または `<span class="text-{color}">` を使用

## スライド構造

### 表紙
```html
<section class="bg-day">
    <div class="illust-area">
        <span class="character char-blue char-large">ピ</span>
    </div>
    <h1>タイトル</h1>
    <p>サブタイトル</p>
</section>
```

### ストーリーページ
```html
<section class="bg-forest">
    <div class="illust-area">
        <span class="character char-blue">ピ</span>
        <span class="character char-pink">モ</span>
    </div>
    <div class="story-text">
        本文テキスト。<span class="marker">強調部分</span>。
    </div>
    <div class="page-num">- 1 -</div>
</section>
```

### 会話ページ
```html
<section>
    <div class="bubble">
        「セリフをここに」
    </div>
    <div class="story-text">
        地の文。
    </div>
    <div class="page-num">- 5 -</div>
</section>
```

### エンディング
```html
<section>
    <div class="moral-box">
        <span class="text-purple">この物語から：</span><br>
        教訓テキスト
    </div>
    <div class="the-end">おしまい</div>
</section>
```

## 出力形式
`<section>` タグのリストのみを出力してください。
