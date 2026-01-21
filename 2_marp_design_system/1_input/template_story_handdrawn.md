# 手書き風ストーリーテンプレート

物語スライド作成用テンプレート。handdrawn.css を使用。

---

## 基本構造

```markdown
---
marp: true
theme: default
paginate: false
size: 16:9
style: |
  /* handdrawn.css の内容をここにコピー、またはインポート */
  @import url('https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@400;500;700&family=Yomogi&display=swap');

  section {
    background: #FFF8E7;  /* paper-cream */
    font-family: "Zen Maru Gothic", sans-serif;
    color: #5D4037;  /* ink-brown */
    padding: 40px 60px;
    font-size: 26px;
    line-height: 2;
  }
---
```

---

## スタイル選択

| スタイル | クラス | 用途 |
|----------|--------|------|
| 絵本風 | `.style-picturebook` | 子供向け、温かい物語 |
| ノート風 | `.style-notebook` | ホラー、日常、リアル系 |
| スケッチ風 | `.style-sketch` | アート系、おしゃれ |
| コミック風 | `.style-comic` | アクション、コメディ |
| 日記風 | `.style-diary` | 回想、エモーショナル |

---

## キャラクター定義例

```css
/* 主人公 */
.icon-hero {
  background: #E3F2FD;
  border: 3px solid #64B5F6;
  color: #64B5F6;
}

/* サブキャラ */
.icon-sub {
  background: #FCE4EC;
  border: 3px solid #F48FB1;
  color: #F48FB1;
}

/* 敵/障害 */
.icon-enemy {
  background: #FFEBEE;
  border: 3px solid #E57373;
  color: #E57373;
}
```

---

## 表紙テンプレート

```markdown
---

<div class="book-title text-center">

<div class="text-icon">
[ イラスト or アイコン ]
</div>

# タイトル

<div class="author mt-2">
サブタイトル or 作者名
</div>

</div>
```

---

## 本文ページテンプレート

```markdown
---

<div class="illust-area">
<span class="character char-blue">A</span>
<span class="character char-pink">B</span>
</div>

<div class="story-text">
物語の本文をここに。

<span class="underline-marker">強調したい部分</span>はマーカーで。
</div>

<div class="page-num">- 1 -</div>
```

---

## 会話シーンテンプレート

```markdown
---

<div class="dialogue-row">
<span class="character char-blue">A</span>
<div class="dialogue-content">
「セリフをここに」
</div>
</div>

<div class="dialogue-row dialogue-row-right">
<span class="character char-pink">B</span>
<div class="dialogue-content">
「返答をここに」
</div>
</div>

<div class="page-num">- 5 -</div>
```

---

## 吹き出しバリエーション

```markdown
<!-- 通常 -->
<div class="bubble">普通のセリフ</div>

<!-- 思考 -->
<div class="bubble-think">心の声...</div>

<!-- 叫び -->
<div class="bubble-shout">叫び！</div>
```

---

## 装飾・区切り

```markdown
<!-- ドット区切り -->
<div class="divider-dots">・ ・ ・</div>

<!-- 波線区切り -->
<div class="divider-wave">～ ～ ～</div>

<!-- 星区切り -->
<div class="divider-stars">* * *</div>

<!-- 章区切り -->
<div class="chapter">
<div class="chapter-number">第一章</div>
<div class="chapter-title">出会い</div>
</div>
```

---

## 背景バリエーション

```markdown
<!-- 昼間シーン -->
<section class="bg-day">

<!-- 夕方シーン -->
<section class="bg-sunset">

<!-- 夜シーン -->
<section class="bg-night">

<!-- 森シーン -->
<section class="bg-forest">

<!-- 海シーン -->
<section class="bg-sea">

<!-- 雨シーン -->
<section class="bg-rain">
```

---

## 教訓・終わり

```markdown
---

<div class="moral-box">
物語から学べること：

<span class="text-orange bold">ここに教訓を書く</span>
</div>

<div class="the-end">
おしまい
</div>
```

---

## 物語構成例

1. **表紙** - タイトル、雰囲気設定
2. **導入** (2-3ページ) - 主人公紹介、日常
3. **事件** (1-2ページ) - 問題発生
4. **展開** (5-10ページ) - 冒険、試練
5. **クライマックス** (2-3ページ) - 最大の困難
6. **解決** (2-3ページ) - 成長、変化
7. **エンディング** (1-2ページ) - 教訓、余韻
8. **裏表紙** - 締め

---

## Tips

- 1ページの文字数は100字以内
- キャラクターは3人以内が読みやすい
- 背景色変更で場面転換を表現
- 区切り線で時間経過を表現
- 最後に教訓を入れると締まる
