---
marp: true
theme: default
paginate: false
size: 16:9
style: |
  /* ================================ */
  /* 絵本風デザイン                   */
  /* 物語：さいごの夢をみる魚         */
  /* ================================ */

  @import url('https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@400;700&family=Hachi+Maru+Pop&display=swap');

  :root {
    --cream: #FFF8E7;
    --brown: #5D4037;
    --orange: #FF8A65;
    --blue: #64B5F6;
    --green: #81C784;
    --pink: #F48FB1;
    --purple: #B39DDB;
    --yellow: #FFD54F;
  }

  section {
    background: var(--cream);
    font-family: "Zen Maru Gothic", "Hachi Maru Pop", "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", sans-serif;
    color: var(--brown);
    padding: 40px 60px;
    font-size: 26px;
    line-height: 2;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  /* 絵文字用 */
  .illust, .illust-small, .dialogue-char {
    font-family: "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", sans-serif;
  }

  /* 絵本タイトル */
  .book-title {
    text-align: center;
    padding-top: 30px;
  }

  .book-title h1 {
    font-size: 2.5em;
    color: var(--blue);
    margin: 0;
    text-shadow: 3px 3px 0 rgba(0,0,0,0.1);
  }

  .book-title .author {
    margin-top: 30px;
    font-size: 0.9em;
    color: var(--brown);
    opacity: 0.7;
  }

  /* イラストエリア */
  .illust {
    text-align: center;
    font-size: 4em;
    margin: 20px 0;
    line-height: 1.3;
  }

  .illust-small {
    text-align: center;
    font-size: 2.5em;
    margin: 15px 0;
  }

  /* 本文 */
  .story-text {
    text-align: center;
    font-size: 1.3em;
    line-height: 2.2;
    max-width: 800px;
    margin: 0 auto;
  }

  /* 強調 */
  .em-blue { color: var(--blue); font-weight: 700; }
  .em-orange { color: var(--orange); font-weight: 700; }
  .em-pink { color: var(--pink); font-weight: 700; }
  .em-green { color: var(--green); font-weight: 700; }
  .em-purple { color: var(--purple); font-weight: 700; }

  /* 場面転換 */
  .scene-change {
    text-align: center;
    font-size: 1.5em;
    color: var(--purple);
    margin: 30px 0;
    letter-spacing: 1em;
  }

  /* 会話 */
  .dialogue {
    background: white;
    border-radius: 30px;
    padding: 20px 30px;
    margin: 15px auto;
    max-width: 700px;
    box-shadow: 4px 4px 0 rgba(0,0,0,0.1);
    text-align: center;
  }

  .dialogue-char {
    font-size: 2em;
    margin-right: 10px;
  }

  /* 波模様の背景 */
  .sea-bg {
    background: linear-gradient(180deg,
      #E3F2FD 0%,
      #BBDEFB 30%,
      #90CAF9 60%,
      #64B5F6 100%);
  }

  /* 夜空背景 */
  .night-bg {
    background: linear-gradient(180deg,
      #1A237E 0%,
      #283593 50%,
      #3949AB 100%);
    color: white;
  }

  .night-bg .story-text {
    color: white;
  }

  /* 朝焼け背景 */
  .dawn-bg {
    background: linear-gradient(180deg,
      #FFE0B2 0%,
      #FFCC80 30%,
      #FFB74D 60%,
      #FF9800 100%);
  }

  /* キラキラ */
  .sparkle {
    animation: sparkle 1.5s infinite;
  }

  /* ページ番号風 */
  .page-num {
    position: absolute;
    bottom: 30px;
    right: 50px;
    font-size: 0.8em;
    color: var(--brown);
    opacity: 0.5;
  }

  /* 終わり */
  .the-end {
    text-align: center;
    font-size: 2em;
    color: var(--purple);
    margin-top: 50px;
    letter-spacing: 0.3em;
  }

  /* 教訓ボックス */
  .moral {
    background: rgba(255,255,255,0.7);
    border: 3px dashed var(--orange);
    border-radius: 20px;
    padding: 20px 30px;
    margin: 20px auto;
    max-width: 600px;
    text-align: center;
  }

---

<!-- 表紙 -->
<div class="book-title">

<div class="illust">🐟✨🌊</div>

# さいごの夢をみる魚

<div class="author">
ある海の、ある物語
</div>

</div>

---

<!-- 1 -->
<div class="illust">🌊🐟🌊</div>

<div class="story-text">
むかしむかし、<span class="em-blue">深い深い海の底</span>に、

一匹の小さな魚が住んでいました。
</div>

<div class="page-num">- 1 -</div>

---

<!-- 2 -->
<section class="sea-bg">

<div class="illust">🐟💭❓</div>

<div class="story-text">
その魚には、<span class="em-purple">不思議な力</span>がありました。

<span class="em-orange">他の魚の夢の中に入る</span>ことができたのです。
</div>

<div class="page-num">- 2 -</div>

</section>

---

<!-- 3 -->
<div class="illust">🐟👀💭🐠💭🐡</div>

<div class="story-text">
魚は毎晩、誰かの夢に遊びに行きました。

楽しい夢、悲しい夢、不思議な夢。

<span class="em-green">どんな夢も、魚にとっては宝物</span>でした。
</div>

<div class="page-num">- 3 -</div>

---

<!-- 4 -->
<div class="illust">🐟💭🦈</div>

<div class="story-text">
ある日、魚は気づきました。

海の仲間たちの夢が、

<span class="em-pink">だんだん暗くなっている</span>ことに。
</div>

<div class="page-num">- 4 -</div>

---

<!-- 5 -->
<div class="dialogue">
<span class="dialogue-char">🐠</span>
「最近、怖い夢ばかり見るんだ...」
</div>

<div class="dialogue">
<span class="dialogue-char">🐡</span>
「私も...海が暗くなる夢...」
</div>

<div class="dialogue">
<span class="dialogue-char">🦀</span>
「みんな、何かを恐れている」
</div>

<div class="page-num">- 5 -</div>

---

<!-- 6 -->
<div class="illust">🐟❗🌑</div>

<div class="story-text">
魚は決心しました。

<span class="em-blue">「みんなの怖い夢を、僕が食べよう」</span>

そうすれば、みんな安心して眠れるから。
</div>

<div class="page-num">- 6 -</div>

---

<!-- 7 -->
<section class="night-bg">

<div class="illust">🐟😤🌑🌑🌑</div>

<div class="story-text">
その夜から、魚は<span class="em-orange">悪い夢を食べ始めました</span>。

真っ黒な夢。冷たい夢。悲しい夢。

全部、全部、飲み込みました。
</div>

<div class="page-num">- 7 -</div>

</section>

---

<!-- 8 -->
<div class="illust">🐠😊🐡😊🦀😊</div>

<div class="story-text">
すると、海の仲間たちは<span class="em-pink">笑顔を取り戻しました</span>。

<span class="em-green">「最近、いい夢ばかり見るよ！」</span>

みんな、とても幸せそうでした。
</div>

<div class="page-num">- 8 -</div>

---

<!-- 9 -->
<div class="illust">🐟😔🌑</div>

<div class="story-text">
でも、魚は気づきました。

食べた悪い夢は、消えたんじゃない。

<span class="em-purple">自分の中に、溜まっていたのです。</span>
</div>

<div class="page-num">- 9 -</div>

---

<!-- 10 -->
<section class="night-bg">

<div class="illust">🐟🖤🖤🖤</div>

<div class="story-text">
魚の体は、<span class="em-orange">だんだん重くなりました</span>。

泳ぐことも、息をすることも、辛くなりました。

それでも魚は、<span style="color: #FFD54F;">悪い夢を食べ続けました</span>。
</div>

<div class="page-num">- 10 -</div>

</section>

---

<!-- 11 -->
<div class="dialogue">
<span class="dialogue-char">🐢</span>
「おや、小さな魚よ。どうしたんだい？」
</div>

<div class="illust-small">🐢 🐟</div>

<div class="story-text">
古い亀が、魚に声をかけました。
</div>

<div class="page-num">- 11 -</div>

---

<!-- 12 -->
<div class="dialogue">
<span class="dialogue-char">🐟</span>
「僕は...みんなの悪い夢を食べているんです。<br>
でも、もう体が限界で...」
</div>

<div class="dialogue">
<span class="dialogue-char">🐢</span>
「なぜ、そんなことを？」
</div>

<div class="dialogue">
<span class="dialogue-char">🐟</span>
「<span class="em-blue">みんなに、幸せでいてほしいから</span>」
</div>

<div class="page-num">- 12 -</div>

---

<!-- 13 -->
<div class="illust-small">🐢</div>

<div class="dialogue">
<span class="dialogue-char">🐢</span>
「小さな魚よ。<br>
<span class="em-purple">悪い夢は、悪いものじゃないんだよ</span>」
</div>

<div class="story-text">
魚は驚きました。
</div>

<div class="page-num">- 13 -</div>

---

<!-- 14 -->
<div class="illust-small">🐢✨</div>

<div class="dialogue">
<span class="dialogue-char">🐢</span>
「怖い夢を見るから、勇気が生まれる。<br>
悲しい夢を見るから、優しさを知る。<br>
<span class="em-orange">夢は、心が成長するための栄養なんだ</span>」
</div>

<div class="page-num">- 14 -</div>

---

<!-- 15 -->
<div class="illust">🐟💭💡</div>

<div class="story-text">
魚は、ハッとしました。

<span class="em-pink">僕は、みんなから大切なものを奪っていた</span>のかもしれない。
</div>

<div class="page-num">- 15 -</div>

---

<!-- 16 -->
<div class="dialogue">
<span class="dialogue-char">🐢</span>
「まだ間に合うよ。<br>
<span class="em-green">夢は、返すことができる</span>んだ」
</div>

<div class="dialogue">
<span class="dialogue-char">🐟</span>
「どうすれば...？」
</div>

<div class="dialogue">
<span class="dialogue-char">🐢</span>
「お前自身が、<span class="em-blue">最後の夢を見るんだ</span>」
</div>

<div class="page-num">- 16 -</div>

---

<!-- 17 -->
<section class="night-bg">

<div class="illust">🐟💤✨🌙✨</div>

<div class="story-text">
その夜、魚は目を閉じました。

<span style="color: #FFD54F;">生まれて初めて、自分のための夢を見ました。</span>
</div>

<div class="page-num">- 17 -</div>

</section>

---

<!-- 18 -->
<section class="night-bg">

<div class="illust">💫🐟💫</div>

<div class="story-text">
夢の中で、魚の体から<span style="color: #FFD54F;">光が溢れ出しました</span>。

黒い夢たちが、<span style="color: #F48FB1;">色とりどりの光</span>に変わって、

<span style="color: #81C784;">海中に散らばっていきました</span>。
</div>

<div class="page-num">- 18 -</div>

</section>

---

<!-- 19 -->
<section class="dawn-bg">

<div class="illust">🌅🐠💭✨🐡💭✨🦀💭✨</div>

<div class="story-text">
朝が来ると、海の仲間たちは<span class="em-purple">不思議な夢</span>を見たと話しました。

<span class="em-blue">「怖かったけど、なんだか勇気が出た」</span>

<span class="em-pink">「悲しかったけど、温かい気持ちになった」</span>
</div>

<div class="page-num">- 19 -</div>

</section>

---

<!-- 20 -->
<div class="illust">🐟😊✨</div>

<div class="story-text">
魚の体は、<span class="em-green">すっかり軽くなっていました</span>。

もう、悪い夢を食べる必要はありません。

だって、<span class="em-orange">悪い夢なんて、最初からなかった</span>のですから。
</div>

<div class="page-num">- 20 -</div>

---

<!-- 21 -->
<div class="illust">🐟🐠🐡🦀🐢🌊</div>

<div class="story-text">
それからも、魚は夢の中を旅しました。

でも今度は、<span class="em-blue">夢を食べるためじゃなく</span>、

<span class="em-pink">一緒に夢を見るために</span>。
</div>

<div class="page-num">- 21 -</div>

---

<!-- エピローグ -->
<div class="moral">
<span class="em-purple">どんな夢も、あなたの心の一部です。</span>

怖い夢も、悲しい夢も、

<span class="em-orange">あなたを強くするために来てくれた</span>のかもしれません。
</div>

<div class="the-end">
おしまい
</div>

<div class="illust-small">🐟✨📖</div>

---

<!-- 裏表紙 -->
<div class="book-title" style="padding-top: 100px;">

<div class="illust">🌊💭✨</div>

<div style="font-size: 1.2em; color: var(--brown); margin-top: 30px;">
今夜、どんな夢を見ますか？
</div>

<div style="margin-top: 80px; font-size: 0.8em; color: var(--brown); opacity: 0.6;">
- さいごの夢をみる魚 -
</div>

</div>

