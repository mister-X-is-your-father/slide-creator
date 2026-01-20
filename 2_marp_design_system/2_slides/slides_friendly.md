---
marp: true
theme: default
paginate: true
style: |
  /* ========================================
     親しみやすいデザイン - Friendly Design
     可愛い・ポップ・シンプル・手書き風
     ======================================== */
  :root {
    /* パステルカラーパレット */
    --pink: #FFB5C5;
    --pink-light: #FFF0F5;
    --mint: #98D8C8;
    --mint-light: #E8FAF6;
    --lavender: #DDA0DD;
    --lavender-light: #F8F0FF;
    --peach: #FFDAB9;
    --peach-light: #FFF8F0;
    --sky: #87CEEB;
    --sky-light: #F0F8FF;
    --yellow: #FFE66D;
    --yellow-light: #FFFEF0;
    --coral: #FF7F7F;
    --text-dark: #5D5D5D;
    --text-light: #888888;
    --white: #FFFFFF;
    --bg-cream: #FFFAF5;
    --border-soft: #E0E0E0;
  }
  section {
    background-color: var(--bg-cream);
    color: var(--text-dark);
    font-family: 'Noto Sans CJK JP', 'Rounded Mplus 1c', sans-serif;
    padding: 40px;
  }
  h1 {
    color: var(--coral);
    border-bottom: 3px dashed var(--pink);
    padding-bottom: 0.3em;
    font-weight: bold;
  }
  h2 { color: var(--lavender); }
  h3 { color: var(--mint); }
  /* ================================
     タイトルスライド（可愛い版）
     ================================ */
  .title-cute {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    text-align: center;
    background: linear-gradient(135deg, var(--pink-light) 0%, var(--lavender-light) 50%, var(--sky-light) 100%);
    margin: -40px;
    padding: 40px;
    border-radius: 0;
  }
  .title-cute h1 {
    font-size: 2.5em;
    border-bottom: none;
    color: var(--coral);
    text-shadow: 2px 2px 0 var(--white);
  }
  .title-cute p {
    font-size: 1.3em;
    color: var(--text-light);
  }
  .title-cute .deco {
    font-size: 2em;
    margin: 0.5em 0;
  }
  /* ================================
     セクションヘッダー（ポップ版）
     ================================ */
  .section-pop {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    background: linear-gradient(135deg, var(--yellow) 0%, var(--peach) 100%);
    margin: -40px;
    padding: 40px;
    text-align: center;
  }
  .section-pop h1 {
    color: var(--white);
    border-bottom: none;
    font-size: 2.8em;
    text-shadow: 3px 3px 0 var(--coral);
  }
  .section-pop p { color: var(--text-dark); font-size: 1.2em; }
  /* ================================
     吹き出し系
     ================================ */
  /* シンプル吹き出し */
  .bubble {
    background: var(--white);
    border: 3px solid var(--pink);
    border-radius: 20px;
    padding: 1em 1.5em;
    position: relative;
    margin-bottom: 1.5em;
    box-shadow: 4px 4px 0 var(--pink-light);
  }
  .bubble::after {
    content: '▼';
    position: absolute;
    bottom: -20px;
    left: 30px;
    color: var(--pink);
    font-size: 1em;
  }
  /* モコモコ吹き出し */
  .bubble-cloud {
    background: var(--white);
    border: 3px solid var(--sky);
    border-radius: 30px 30px 30px 5px;
    padding: 1em 1.5em;
    box-shadow: 4px 4px 0 var(--sky-light);
  }
  /* 考え事吹き出し */
  .bubble-think {
    background: var(--lavender-light);
    border: 2px dashed var(--lavender);
    border-radius: 50%;
    padding: 1.5em;
    text-align: center;
    display: inline-block;
  }
  /* 会話形式 */
  .chat { display: flex; flex-direction: column; gap: 1em; }
  .chat-row { display: flex; align-items: flex-start; gap: 1em; }
  .chat-row.right { flex-direction: row-reverse; }
  .chat-icon {
    width: 50px; height: 50px; border-radius: 50%;
    display: flex; justify-content: center; align-items: center;
    font-size: 1.5em; flex-shrink: 0;
  }
  .chat-icon.a { background: var(--pink); }
  .chat-icon.b { background: var(--mint); }
  .chat-bubble {
    background: var(--white);
    border-radius: 15px;
    padding: 0.8em 1.2em;
    max-width: 70%;
    box-shadow: 2px 2px 0 var(--border-soft);
  }
  .chat-row.right .chat-bubble {
    background: var(--mint-light);
  }
  /* ================================
     リボン・ラベル
     ================================ */
  /* シンプルリボン */
  .ribbon {
    background: var(--coral);
    color: var(--white);
    padding: 0.5em 2em;
    font-weight: bold;
    display: inline-block;
    position: relative;
    margin: 0.5em 1em;
  }
  .ribbon::before, .ribbon::after {
    content: '';
    position: absolute;
    top: 0;
    border: 15px solid var(--coral);
  }
  .ribbon::before {
    left: -15px;
    border-left-color: transparent;
  }
  .ribbon::after {
    right: -15px;
    border-right-color: transparent;
  }
  /* ステッチリボン */
  .ribbon-stitch {
    background: var(--pink);
    color: var(--white);
    padding: 0.6em 1.5em;
    border-radius: 5px;
    display: inline-block;
    border: 2px dashed var(--white);
    box-shadow: 0 0 0 4px var(--pink);
    font-weight: bold;
  }
  /* タグ風ラベル */
  .tag-label {
    background: var(--yellow);
    color: var(--text-dark);
    padding: 0.4em 1em 0.4em 1.5em;
    border-radius: 0 20px 20px 0;
    display: inline-block;
    position: relative;
    font-weight: bold;
  }
  .tag-label::before {
    content: '●';
    position: absolute;
    left: 8px;
    color: var(--white);
    font-size: 0.6em;
  }
  /* ================================
     カード系（可愛い版）
     ================================ */
  .card-cute {
    background: var(--white);
    border: 3px solid var(--border-soft);
    border-radius: 20px;
    padding: 1.5em;
    text-align: center;
    box-shadow: 5px 5px 0 var(--pink-light);
    transition: transform 0.2s;
  }
  .card-cute .icon { font-size: 2.5em; margin-bottom: 0.3em; }
  .card-cute .title { font-weight: bold; color: var(--coral); margin-bottom: 0.3em; }
  .card-cute .desc { font-size: 0.9em; color: var(--text-light); }
  /* カードグリッド */
  .card-grid-cute {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5em;
  }
  /* ================================
     リスト系（手書き風）
     ================================ */
  /* チェックリスト（手書き風） */
  .check-hand {
    list-style: none;
    padding: 0;
  }
  .check-hand li {
    display: flex;
    align-items: center;
    gap: 0.8em;
    margin-bottom: 0.8em;
    padding: 0.6em 1em;
    background: var(--white);
    border-radius: 10px;
    border-left: 5px solid var(--mint);
  }
  .check-hand .mark { font-size: 1.2em; }
  .check-hand .done { color: var(--mint); }
  .check-hand .todo { color: var(--text-light); }
  /* 番号リスト（丸い） */
  .num-round {
    list-style: none;
    padding: 0;
  }
  .num-round li {
    display: flex;
    align-items: flex-start;
    gap: 1em;
    margin-bottom: 1em;
  }
  .num-round .num {
    background: linear-gradient(135deg, var(--pink) 0%, var(--coral) 100%);
    color: var(--white);
    width: 35px;
    height: 35px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    flex-shrink: 0;
    box-shadow: 2px 2px 0 var(--pink-light);
  }
  /* ================================
     ステップ系（ポップ版）
     ================================ */
  .steps-pop {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 0.5em;
  }
  .step-pop {
    background: var(--white);
    border: 3px solid var(--sky);
    border-radius: 15px;
    padding: 1em;
    text-align: center;
    min-width: 120px;
  }
  .step-pop .num {
    background: var(--sky);
    color: var(--white);
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    font-size: 1.2em;
    margin-bottom: 0.5em;
  }
  .step-pop .title { font-weight: bold; color: var(--text-dark); }
  .step-arrow { font-size: 2em; color: var(--yellow); }
  /* ================================
     フロー（丸い矢印）
     ================================ */
  .flow-round {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 0.5em;
  }
  .flow-item-round {
    background: linear-gradient(135deg, var(--mint) 0%, var(--sky) 100%);
    color: var(--white);
    padding: 1em 1.5em;
    border-radius: 25px;
    font-weight: bold;
    box-shadow: 3px 3px 0 var(--mint-light);
  }
  .flow-arrow-round {
    font-size: 1.8em;
    color: var(--coral);
  }
  /* ================================
     メトリクス（可愛い版）
     ================================ */
  .metric-cute {
    background: var(--white);
    border-radius: 20px;
    padding: 1.5em;
    text-align: center;
    border: 3px solid var(--yellow);
    box-shadow: 5px 5px 0 var(--yellow-light);
  }
  .metric-cute .number {
    font-size: 3em;
    font-weight: bold;
    color: var(--coral);
  }
  .metric-cute .label {
    color: var(--text-light);
    margin-top: 0.3em;
  }
  .metric-cute .icon { font-size: 1.5em; margin-bottom: 0.3em; }
  /* メトリックグリッド */
  .metric-grid-cute {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5em;
  }
  /* ================================
     比較系（ポップ版）
     ================================ */
  .compare-pop {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: 1em;
    align-items: center;
  }
  .compare-pop .before {
    background: var(--pink-light);
    border: 3px solid var(--pink);
    border-radius: 20px;
    padding: 1.5em;
    text-align: center;
  }
  .compare-pop .after {
    background: var(--mint-light);
    border: 3px solid var(--mint);
    border-radius: 20px;
    padding: 1.5em;
    text-align: center;
  }
  .compare-pop .arrow {
    font-size: 3em;
    color: var(--yellow);
  }
  .compare-pop h3 { margin-bottom: 0.5em; }
  /* ================================
     ボックス系（可愛い版）
     ================================ */
  /* ハイライトボックス */
  .box-highlight {
    background: linear-gradient(135deg, var(--yellow-light) 0%, var(--peach-light) 100%);
    border: 3px solid var(--yellow);
    border-radius: 15px;
    padding: 1em 1.5em;
    margin: 1em 0;
  }
  /* インフォボックス */
  .box-info {
    background: var(--sky-light);
    border-left: 5px solid var(--sky);
    border-radius: 0 15px 15px 0;
    padding: 1em 1.5em;
    margin: 1em 0;
  }
  /* 注意ボックス */
  .box-warning {
    background: var(--pink-light);
    border-left: 5px solid var(--coral);
    border-radius: 0 15px 15px 0;
    padding: 1em 1.5em;
    margin: 1em 0;
  }
  /* 引用ボックス */
  .quote-cute {
    background: var(--lavender-light);
    border-radius: 20px;
    padding: 1.5em 2em;
    position: relative;
    margin: 1em 0;
  }
  .quote-cute::before {
    content: '"';
    font-size: 4em;
    color: var(--lavender);
    position: absolute;
    top: -10px;
    left: 10px;
    opacity: 0.5;
  }
  .quote-cute p {
    font-style: italic;
    font-size: 1.1em;
    margin: 0;
  }
  .quote-cute .author {
    text-align: right;
    color: var(--text-light);
    margin-top: 0.8em;
  }
  /* ================================
     タイムライン（可愛い版）
     ================================ */
  .timeline-cute { border-collapse: collapse; }
  .timeline-cute td { padding: 0.3em 0.8em; vertical-align: top; }
  .timeline-cute .col-line { text-align: center; color: var(--pink); line-height: 1.4; width: 40px; font-size: 1.2em; }
  .timeline-cute .col-date {
    background: var(--pink);
    color: var(--white);
    padding: 0.3em 0.8em;
    border-radius: 15px;
    font-weight: bold;
    font-size: 0.85em;
    white-space: nowrap;
  }
  .timeline-cute .col-content { padding-left: 1em; }
  /* ================================
     バッジ（可愛い版）
     ================================ */
  .badge-cute {
    display: inline-block;
    padding: 0.3em 1em;
    border-radius: 20px;
    font-weight: bold;
    font-size: 0.85em;
  }
  .badge-cute.pink { background: var(--pink); color: var(--white); }
  .badge-cute.mint { background: var(--mint); color: var(--white); }
  .badge-cute.yellow { background: var(--yellow); color: var(--text-dark); }
  .badge-cute.lavender { background: var(--lavender); color: var(--white); }
  .badge-cute.sky { background: var(--sky); color: var(--white); }
  /* タグリスト */
  .tag-list-cute {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5em;
  }
  .tag-cute {
    background: var(--white);
    border: 2px solid var(--border-soft);
    border-radius: 15px;
    padding: 0.3em 0.8em;
    font-size: 0.9em;
  }
  /* ================================
     レイアウト
     ================================ */
  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 2em; }
  .three-col { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1.5em; }
  /* ================================
     装飾要素
     ================================ */
  .deco-dots {
    background-image: radial-gradient(var(--pink) 2px, transparent 2px);
    background-size: 20px 20px;
    padding: 2em;
    border-radius: 15px;
  }
  .deco-stripe {
    background: repeating-linear-gradient(
      45deg,
      var(--white),
      var(--white) 10px,
      var(--pink-light) 10px,
      var(--pink-light) 20px
    );
    padding: 2em;
    border-radius: 15px;
  }
  /* ================================
     ピラミッド（可愛い版）
     ================================ */
  .pyramid-cute {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .pyramid-cute .layer {
    display: flex;
    justify-content: center;
    align-items: center;
    color: var(--white);
    font-weight: bold;
    padding: 0.6em;
    margin-bottom: 3px;
    border-radius: 10px;
  }
  .pyramid-cute .layer-1 { width: 35%; background: var(--coral); }
  .pyramid-cute .layer-2 { width: 50%; background: var(--pink); }
  .pyramid-cute .layer-3 { width: 65%; background: var(--lavender); }
  .pyramid-cute .layer-4 { width: 80%; background: var(--sky); }
  .pyramid-cute .layer-5 { width: 95%; background: var(--mint); }
  /* ================================
     サイクル（可愛い版）
     ================================ */
  .cycle-cute {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 1em;
    max-width: 450px;
    margin: 0 auto;
  }
  .cycle-cute .item {
    background: var(--white);
    border: 3px solid var(--pink);
    border-radius: 15px;
    padding: 1em;
    text-align: center;
  }
  .cycle-cute .item .num {
    background: var(--pink);
    color: var(--white);
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    margin-bottom: 0.3em;
  }
  .cycle-cute .arrow-text { font-weight: bold; color: var(--coral); }
  /* ================================
     表（可愛い版）
     ================================ */
  table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    border-radius: 15px;
    overflow: hidden;
    border: 3px solid var(--pink);
  }
  th {
    background: var(--pink);
    color: var(--white);
    padding: 0.8em;
    font-weight: bold;
  }
  td {
    background: var(--white);
    padding: 0.8em;
    border-bottom: 1px solid var(--border-soft);
  }
  tr:last-child td { border-bottom: none; }
  .check-mark { color: var(--mint); font-size: 1.2em; }
  .cross-mark { color: var(--coral); font-size: 1.2em; }
---

<div class="title-cute">

<div class="deco">🌸 ✨ 🎀</div>

# 親しみやすいデザイン集

可愛い・ポップ・シンプル・手書き風コンポーネント

<div class="deco">💕</div>

</div>

---

<div class="section-pop">

# 吹き出しデザイン

会話風・モコモコ・考え事

</div>

---

# シンプル吹き出し

ポイントを強調

<div class="bubble">
ここがポイント！シンプルで可愛い吹き出しです。角丸と影でやわらかい印象に。
</div>

<div class="bubble-cloud">
モコモコ吹き出しは、やさしい印象を与えます。説明文に最適！
</div>

---

# 会話形式

キャラクターとの対話風

<div class="chat">
<div class="chat-row">
<div class="chat-icon a">🐱</div>
<div class="chat-bubble">こんにちは！今日のテーマは何ですか？</div>
</div>
<div class="chat-row right">
<div class="chat-icon b">🐶</div>
<div class="chat-bubble">今日は「親しみやすいデザイン」について学びましょう！</div>
</div>
<div class="chat-row">
<div class="chat-icon a">🐱</div>
<div class="chat-bubble">わぁ、楽しみです！</div>
</div>
</div>

---

# 考え事吹き出し

内面の声を表現

<div class="two-col">
<div style="text-align: center;">

<div class="bubble-think">
うーん、<br>どうしよう...🤔
</div>

悩み・迷い

</div>
<div style="text-align: center;">

<div class="bubble-think">
なるほど！<br>わかった！💡
</div>

気づき・発見

</div>
</div>

---

<div class="section-pop">

# リボン・ラベル

見出しを可愛く装飾

</div>

---

# リボンデザイン

タイトルを華やかに

<div style="text-align: center; margin: 2em 0;">

<span class="ribbon">NEW!</span>

<span class="ribbon-stitch">おすすめ</span>

<span class="tag-label">ポイント</span>

</div>

<div class="box-info">
リボンやラベルを使うと、重要な情報が目立ちます。色を変えて使い分けましょう。
</div>

---

<div class="section-pop">

# カード・リスト

情報を整理して見せる

</div>

---

# 可愛いカード

アイコン付きで親しみやすく

<div class="card-grid-cute">
<div class="card-cute">
<div class="icon">🚀</div>
<div class="title">スピード</div>
<div class="desc">高速で処理</div>
</div>
<div class="card-cute">
<div class="icon">🔒</div>
<div class="title">セキュリティ</div>
<div class="desc">安心・安全</div>
</div>
<div class="card-cute">
<div class="icon">💡</div>
<div class="title">アイデア</div>
<div class="desc">ひらめきを形に</div>
</div>
</div>

---

# チェックリスト

手書き風のやわらかさ

<ul class="check-hand">
<li><span class="mark done">✓</span>企画書を作成する</li>
<li><span class="mark done">✓</span>デザインを決める</li>
<li><span class="mark done">✓</span>レビューを受ける</li>
<li><span class="mark todo">○</span>最終調整</li>
<li><span class="mark todo">○</span>公開する</li>
</ul>

---

# 番号リスト

丸いナンバーで可愛く

<ul class="num-round">
<li><span class="num">1</span>アイデアを出す</li>
<li><span class="num">2</span>下書きを作る</li>
<li><span class="num">3</span>デザインを整える</li>
<li><span class="num">4</span>確認して完成！</li>
</ul>

---

<div class="section-pop">

# ステップ・フロー

プロセスを可愛く表現

</div>

---

# ステップ表示

ポップな段階表示

<div class="steps-pop">
<div class="step-pop">
<div class="num">1</div>
<div class="title">計画</div>
</div>
<span class="step-arrow">→</span>
<div class="step-pop">
<div class="num">2</div>
<div class="title">実行</div>
</div>
<span class="step-arrow">→</span>
<div class="step-pop">
<div class="num">3</div>
<div class="title">確認</div>
</div>
<span class="step-arrow">→</span>
<div class="step-pop">
<div class="num">4</div>
<div class="title">完了</div>
</div>
</div>

---

# フロー図

丸みのある流れ表現

<div class="flow-round">
<div class="flow-item-round">入力</div>
<span class="flow-arrow-round">→</span>
<div class="flow-item-round">処理</div>
<span class="flow-arrow-round">→</span>
<div class="flow-item-round">出力</div>
</div>

---

<div class="section-pop">

# メトリクス・数値

成果を可愛く見せる

</div>

---

# 可愛いメトリクス

数値を楽しく表示

<div class="metric-grid-cute">
<div class="metric-cute">
<div class="icon">😊</div>
<div class="number">98%</div>
<div class="label">満足度</div>
</div>
<div class="metric-cute">
<div class="icon">👥</div>
<div class="number">1,234</div>
<div class="label">ユーザー数</div>
</div>
<div class="metric-cute">
<div class="icon">⭐</div>
<div class="number">4.8</div>
<div class="label">評価</div>
</div>
</div>

---

<div class="section-pop">

# 比較・対比

Before/Afterを可愛く

</div>

---

# Before / After

変化を明るく表現

<div class="compare-pop">
<div class="before">
<h3>😢 Before</h3>

- 時間がかかる
- ミスが多い
- 大変...

</div>
<div class="arrow">✨→</div>
<div class="after">
<h3>😄 After</h3>

- サクサク！
- 正確！
- 楽ちん！

</div>
</div>

---

<div class="section-pop">

# ボックス・引用

情報を囲んで強調

</div>

---

# ハイライトボックス

重要情報を目立たせる

<div class="box-highlight">
💡 **ポイント**: パステルカラーを使うと、やわらかく親しみやすい印象になります！
</div>

<div class="box-info">
ℹ️ **補足**: 色は3色程度に抑えると、まとまりが出ます。
</div>

<div class="box-warning">
⚠️ **注意**: 文字色とのコントラストは確保しましょう。
</div>

---

# 引用ボックス

名言を可愛く表示

<div class="quote-cute">
<p>シンプルであることは、<br>複雑であることよりも難しい。</p>
<div class="author">— スティーブ・ジョブズ</div>
</div>

---

<div class="section-pop">

# タイムライン

時系列を可愛く

</div>

---

# 可愛いタイムライン

マイルストーンを楽しく表示

<table class="timeline-cute">
<tr><td class="col-line">●<br>│</td><td class="col-date">1月</td><td class="col-content">プロジェクト開始 🎉</td></tr>
<tr><td class="col-line">●<br>│</td><td class="col-date">3月</td><td class="col-content">デザイン完成 🎨</td></tr>
<tr><td class="col-line">●<br>│</td><td class="col-date">6月</td><td class="col-content">開発完了 💻</td></tr>
<tr><td class="col-line">●</td><td class="col-date">9月</td><td class="col-content">リリース！ 🚀</td></tr>
</table>

---

<div class="section-pop">

# バッジ・タグ

ラベルを可愛く

</div>

---

# バッジデザイン

状態を色で表現

<span class="badge-cute pink">NEW</span>
<span class="badge-cute mint">完了</span>
<span class="badge-cute yellow">進行中</span>
<span class="badge-cute lavender">レビュー中</span>
<span class="badge-cute sky">計画中</span>

<br><br>

**タグリスト:**

<div class="tag-list-cute">
<span class="tag-cute">デザイン</span>
<span class="tag-cute">可愛い</span>
<span class="tag-cute">ポップ</span>
<span class="tag-cute">パステル</span>
<span class="tag-cute">シンプル</span>
</div>

---

<div class="section-pop">

# 図解パターン

定番図解を可愛く

</div>

---

# ピラミッド

階層を可愛く表現

<div class="pyramid-cute">
<div class="layer layer-1">ビジョン 🌟</div>
<div class="layer layer-2">戦略</div>
<div class="layer layer-3">戦術</div>
<div class="layer layer-4">施策</div>
<div class="layer layer-5">日常業務</div>
</div>

---

# PDCAサイクル

循環を可愛く表現

<div class="cycle-cute">
<div class="item">
<div class="num">1</div>
<strong>Plan</strong><br>計画する
<div class="arrow-text">→</div>
</div>
<div class="item">
<div class="num">2</div>
<strong>Do</strong><br>実行する
<div class="arrow-text">↓</div>
</div>
<div class="item">
<div class="num">4</div>
<strong>Act</strong><br>改善する
<div class="arrow-text">↑</div>
</div>
<div class="item">
<div class="num">3</div>
<strong>Check</strong><br>確認する
<div class="arrow-text">←</div>
</div>
</div>

---

# 比較表

表を可愛く

| 機能 | プランA | プランB |
|------|:-------:|:-------:|
| 容量 | 10GB | 100GB |
| サポート | <span class="check-mark">✓</span> | <span class="check-mark">✓</span> |
| API | <span class="cross-mark">✗</span> | <span class="check-mark">✓</span> |

---

<div class="section-pop">

# 装飾パターン

背景を可愛く

</div>

---

# ドット柄背景

<div class="deco-dots">

## ポイント

ドット柄は可愛らしさを演出します。控えめな色で使うと上品に。

</div>

---

# ストライプ背景

<div class="deco-stripe">

## ポイント

斜めストライプはポップな印象。パステルカラーで優しく。

</div>

---

<div class="title-cute">

<div class="deco">🎀 ✨ 🌸</div>

# ありがとうございました

親しみやすいデザインで<br>伝わるプレゼンを！

<div class="deco">💕</div>

</div>
