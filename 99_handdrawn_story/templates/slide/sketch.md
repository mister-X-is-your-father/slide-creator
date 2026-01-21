---
marp: true
theme: default
paginate: false
size: 16:9
style: |
  /* ================================ */
  /* スケッチ風テンプレート           */
  /* ================================ */

  @import url('https://fonts.googleapis.com/css2?family=Klee+One:wght@400;600&display=swap');

  :root {
    --paper: #FFFEF9;
    --pencil: #4A4A4A;
    --pencil-light: #9CA3AF;
    --accent: #6366F1;
  }

  section {
    background: var(--paper);
    font-family: "Klee One", sans-serif;
    color: var(--pencil);
    padding: 50px 70px;
    font-size: 24px;
    line-height: 1.9;
  }

  /* スケッチ風ボーダー */
  .sketch-border {
    border: 2px solid var(--pencil);
    border-radius: 255px 15px 225px 15px/15px 225px 15px 255px;
    padding: 20px 25px;
  }

  /* 手書き線 */
  .hand-line {
    height: 2px;
    background: linear-gradient(90deg,
      transparent 0%,
      var(--pencil-light) 10%,
      var(--pencil) 30%,
      var(--pencil) 70%,
      var(--pencil-light) 90%,
      transparent 100%
    );
    margin: 25px 0;
  }

  /* タイトル */
  h1 {
    font-weight: 600;
    font-size: 2.2em;
    color: var(--pencil);
    border-bottom: 2px solid var(--pencil-light);
    padding-bottom: 10px;
    margin-bottom: 20px;
  }

  /* 本文 */
  .sketch-text {
    font-size: 1.15em;
    line-height: 2.1;
    max-width: 850px;
  }

  /* イラストエリア */
  .illust-frame {
    border: 1px solid var(--pencil-light);
    border-radius: 3px;
    padding: 30px;
    margin: 20px auto;
    max-width: 400px;
    text-align: center;
    background: rgba(255,255,255,0.5);
  }

  .illust-frame .caption {
    font-size: 0.85em;
    color: var(--pencil-light);
    margin-top: 10px;
    font-style: italic;
  }

  /* アノテーション（注釈） */
  .annotation {
    font-size: 0.9em;
    color: var(--pencil-light);
    font-style: italic;
    margin: 15px 0;
  }

  .annotation::before {
    content: '※ ';
  }

  /* 矢印付きコメント */
  .arrow-note {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 0.95em;
    color: var(--pencil-light);
  }

  .arrow-note::before {
    content: '←';
    font-size: 1.2em;
  }

  /* ハイライト */
  .highlight {
    background: linear-gradient(transparent 50%, rgba(99, 102, 241, 0.2) 50%);
  }

  /* キャラクタースケッチ */
  .char-sketch {
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    margin: 0 15px;
  }

  .char-sketch .icon {
    width: 70px;
    height: 70px;
    border: 2px solid var(--pencil);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    font-weight: 600;
  }

  .char-sketch .name {
    font-size: 0.85em;
    margin-top: 8px;
    color: var(--pencil-light);
  }

  /* レイアウト */
  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
  }

  .center { text-align: center; }

  /* ページ番号 */
  .page-num {
    position: absolute;
    bottom: 25px;
    right: 50px;
    font-size: 0.75em;
    color: var(--pencil-light);
  }

  /* 終わり */
  .fin {
    text-align: center;
    font-size: 1.5em;
    color: var(--pencil-light);
    margin-top: 60px;
    letter-spacing: 0.5em;
  }

---

<!-- 表紙 -->
<div class="center" style="padding-top: 80px;">

<div class="illust-frame" style="max-width: 300px;">
[ メインイラスト ]
</div>

# タイトル

<div class="annotation" style="text-align: center;">
サブタイトルや説明
</div>

</div>

---

<!-- キャラクター紹介例 -->
# 登場人物

<div class="center" style="margin-top: 40px;">

<div class="char-sketch">
<div class="icon">A</div>
<div class="name">キャラA</div>
</div>

<div class="char-sketch">
<div class="icon">B</div>
<div class="name">キャラB</div>
</div>

<div class="char-sketch">
<div class="icon">C</div>
<div class="name">キャラC</div>
</div>

</div>

<div class="annotation center">
それぞれの関係性や特徴
</div>

<div class="page-num">- 1 -</div>

---

<!-- ストーリーページ例 -->
<div class="two-col">

<div>

<div class="sketch-text">
ある日のこと。

主人公は<span class="highlight">不思議なもの</span>を見つけた。

それは今まで見たことのない...
</div>

</div>

<div>

<div class="illust-frame">
[ シーンのスケッチ ]
<div class="caption">発見の瞬間</div>
</div>

</div>

</div>

<div class="page-num">- 3 -</div>

---

<!-- 解説ページ例 -->
# ポイント

<div class="hand-line"></div>

<div class="sketch-border">

**重要なこと**

ここに説明文を入れる。
スケッチ風だが、内容は明確に伝える。

</div>

<div class="arrow-note">
これが物語の核心部分
</div>

<div class="page-num">- 8 -</div>

---

<!-- エンディング例 -->
<div class="center" style="padding-top: 60px;">

<div class="illust-frame" style="max-width: 350px;">
[ 最後のイラスト ]
<div class="caption">エピローグ</div>
</div>

<div class="sketch-text center" style="margin-top: 30px;">
物語はこうして幕を閉じた。

でも、彼らの旅は続いていく...
</div>

<div class="fin">
- fin -
</div>

</div>
