---
marp: true
theme: default
paginate: false
size: 16:9
style: |
  /* ================================ */
  /* 絵本風デザイン                   */
  /* 物語：沈黙を聴くひと             */
  /* シンプルアイコン版               */
  /* ================================ */

  @import url('https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@400;700&family=Klee+One&display=swap');

  :root {
    --paper: #FAF8F5;
    --ink: #3E2723;
    --ink-light: #6D4C41;
    --gold: #D4AF37;
    --deep-blue: #1A237E;
    --soft-blue: #90CAF9;
    --rose: #E91E63;
    --forest: #2E7D32;
    --sunset: #FF7043;
    --lavender: #B39DDB;
    --night: #0D1B2A;
  }

  section {
    background: var(--paper);
    font-family: "Klee One", "Zen Maru Gothic", sans-serif;
    color: var(--ink);
    padding: 40px 60px;
    font-size: 24px;
    line-height: 2;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  /* シンプルアイコン */
  .icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    font-size: 24px;
    font-weight: bold;
    margin: 0 8px;
  }

  .icon-girl {
    background: #FCE4EC;
    border: 3px solid var(--rose);
    color: var(--rose);
  }

  .icon-old {
    background: #FFF8E1;
    border: 3px solid var(--gold);
    color: var(--gold);
  }

  .icon-boy {
    background: #E3F2FD;
    border: 3px solid var(--deep-blue);
    color: var(--deep-blue);
  }

  .icon-sm {
    width: 45px;
    height: 45px;
    font-size: 18px;
  }

  /* イラストエリア */
  .illust {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    margin: 20px 0;
  }

  .illust-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
  }

  .illust-label {
    font-size: 0.7em;
    color: var(--ink-light);
  }

  /* シンボル */
  .symbol {
    font-size: 3em;
    text-align: center;
    margin: 15px 0;
    color: var(--deep-blue);
  }

  .symbol-sm {
    font-size: 2em;
  }

  /* 本文 */
  .story {
    text-align: center;
    font-size: 1.2em;
    line-height: 2.3;
    max-width: 850px;
    margin: 0 auto;
  }

  /* 強調 */
  .gold { color: var(--gold); font-weight: 700; }
  .blue { color: var(--deep-blue); font-weight: 700; }
  .rose { color: var(--rose); font-weight: 700; }
  .forest { color: var(--forest); font-weight: 700; }
  .sunset { color: var(--sunset); font-weight: 700; }

  /* セリフ */
  .dialogue {
    background: white;
    border-radius: 25px;
    padding: 18px 28px;
    margin: 12px auto;
    max-width: 750px;
    box-shadow: 3px 3px 0 rgba(0,0,0,0.08);
    display: flex;
    align-items: center;
    gap: 15px;
  }

  .dialogue-text {
    flex: 1;
    text-align: left;
    font-size: 1.05em;
  }

  .dialogue-thought {
    background: linear-gradient(135deg, #E8EAF6 0%, #C5CAE9 100%);
    border-radius: 25px;
    padding: 18px 28px;
    margin: 12px auto;
    max-width: 750px;
    text-align: center;
    font-style: italic;
    color: var(--ink-light);
  }

  /* 背景バリエーション */
  .bg-forest {
    background: linear-gradient(180deg, #E8F5E9 0%, #C8E6C9 50%, #A5D6A7 100%);
  }

  .bg-night {
    background: linear-gradient(180deg, #1A237E 0%, #283593 40%, #3949AB 100%);
    color: #E8EAF6;
  }
  .bg-night .story { color: #E8EAF6; }
  .bg-night .dialogue { background: rgba(255,255,255,0.95); color: var(--ink); }
  .bg-night .symbol { color: #FFD54F; }

  .bg-dawn {
    background: linear-gradient(180deg, #FFF3E0 0%, #FFE0B2 40%, #FFCC80 100%);
  }

  .bg-sunset {
    background: linear-gradient(180deg, #FFCCBC 0%, #FFAB91 40%, #FF8A65 100%);
  }

  .bg-rain {
    background: linear-gradient(180deg, #ECEFF1 0%, #CFD8DC 50%, #B0BEC5 100%);
  }

  .bg-spring {
    background: linear-gradient(180deg, #FCE4EC 0%, #F8BBD9 50%, #F48FB1 100%);
  }

  .bg-deep {
    background: linear-gradient(180deg, #212121 0%, #424242 100%);
    color: #FAFAFA;
  }
  .bg-deep .story { color: #FAFAFA; }

  /* 章タイトル */
  .chapter {
    text-align: center;
    font-size: 1.4em;
    color: var(--gold);
    margin-bottom: 20px;
    letter-spacing: 0.2em;
  }

  /* タイトル */
  .book-cover {
    text-align: center;
    padding-top: 20px;
  }

  .book-cover h1 {
    font-size: 2.8em;
    color: var(--deep-blue);
    margin: 20px 0;
    letter-spacing: 0.1em;
  }

  .book-cover .subtitle {
    font-size: 1.1em;
    color: var(--ink-light);
    margin-top: 10px;
  }

  /* ページ番号 */
  .page {
    position: absolute;
    bottom: 25px;
    right: 50px;
    font-size: 0.75em;
    color: var(--ink-light);
    opacity: 0.6;
  }

  /* 教訓 */
  .lesson-box {
    background: linear-gradient(135deg, #FFF8E1 0%, #FFECB3 100%);
    border: 3px solid var(--gold);
    border-radius: 20px;
    padding: 25px 35px;
    margin: 20px auto;
    max-width: 700px;
    text-align: center;
  }

  .lesson-title {
    color: var(--gold);
    font-size: 1.1em;
    font-weight: 700;
    margin-bottom: 15px;
  }

  .lesson-text {
    font-size: 1.2em;
    color: var(--ink);
    line-height: 1.8;
  }

  /* 終わり */
  .the-end {
    text-align: center;
    font-size: 1.8em;
    color: var(--deep-blue);
    margin-top: 40px;
    letter-spacing: 0.5em;
  }

  /* 装飾シンボル */
  .deco {
    text-align: center;
    font-size: 2em;
    color: var(--gold);
    letter-spacing: 0.5em;
  }

---

<!-- 表紙 -->
<div class="book-cover">

<div class="deco">* * *</div>

<div class="symbol">((( ♪ )))</div>

# 沈黙を聴くひと

<div class="subtitle">
〜 言葉にならない声を聴く物語 〜
</div>

<div style="margin-top: 40px; font-size: 0.9em; color: var(--ink-light);">
コミュニケーションの本質を知る、ある少女の旅
</div>

</div>

---

<!-- 序章 -->
<section class="bg-forest">

<div class="chapter">― 序章 ―</div>

<div class="symbol symbol-sm">▲ 🌲 ⌂ 🌲 ▲</div>

<div class="story">
山あいの小さな村に、<span class="blue">ユイ</span>という少女が暮らしていました。

ユイには誰にも言えない秘密がありました。

それは、<span class="gold">「人の心の声」が聞こえる</span>ということ。
</div>

<div class="page">- 1 -</div>

</section>

---

<!-- 2 -->
<div class="illust">
<div class="icon icon-girl">ユ</div>
<div style="font-size: 2em; color: var(--lavender);">♪ ～ ？</div>
</div>

<div class="story">
言葉にならない声。

口には出さない本当の気持ち。

ユイには、それが<span class="rose">小さなささやき</span>のように聞こえるのです。
</div>

<div class="dialogue-thought">
「お母さんの『大丈夫』の裏には、いつも疲れた声が聞こえる」
</div>

<div class="page">- 2 -</div>

---

<!-- 3 -->
<div class="illust">
<div class="illust-box">
<div class="icon icon-sm" style="background:#E8F5E9; border-color:var(--forest); color:var(--forest);">A</div>
<div class="illust-label">笑顔</div>
</div>
<div style="font-size: 1.5em;">→</div>
<div class="illust-box">
<div class="icon icon-sm" style="background:#E3F2FD; border-color:var(--deep-blue); color:var(--deep-blue);">...</div>
<div class="illust-label">本音は悲しみ</div>
</div>
</div>

<div class="story">
笑っている人の心から、<span class="blue">悲しみ</span>が聞こえる。

怒っている人の心から、<span class="rose">寂しさ</span>が聞こえる。

ユイは、その声を聞くたびに苦しくなりました。
</div>

<div class="page">- 3 -</div>

---

<!-- 4 -->
<section class="bg-rain">

<div class="illust">
<div class="icon icon-girl">ユ</div>
<div style="font-size: 2em; color: var(--ink-light);">／ ／ ／</div>
</div>

<div class="story">
<span class="blue">「私は、みんなの悲しみを聞くためだけに生まれたの？」</span>

ユイは誰にも話せず、一人で抱え込んでいました。

この力は、<span class="sunset">呪い</span>だと思っていたのです。
</div>

<div class="page">- 4 -</div>

</section>

---

<!-- 5 - 章 -->
<section class="bg-dawn">

<div class="chapter">― 第一章　出会い ―</div>

<div class="symbol symbol-sm">☀ ～～～</div>

<div class="story">
ユイが12歳の春。

村に、一人の<span class="gold">老人</span>がやってきました。

白い髭をたくわえ、穏やかな目をした旅人でした。
</div>

<div class="page">- 5 -</div>

</section>

---

<!-- 6 -->
<div class="illust">
<div class="icon icon-old">翁</div>
</div>

<div class="story">
老人は村のはずれに小さな小屋を建て、

<span class="forest">「話を聴く仕事」</span>を始めました。

村人たちは不思議に思いましたが、

やがて一人、また一人と老人を訪ねるようになりました。
</div>

<div class="page">- 6 -</div>

---

<!-- 7 -->
<div class="dialogue">
<div class="icon icon-sm" style="background:#E8F5E9; border-color:var(--forest); color:var(--forest);">村</div>
<div class="dialogue-text">「あの方に話を聴いてもらうと、なぜか心が軽くなるの」</div>
</div>

<div class="dialogue">
<div class="icon icon-sm" style="background:#ECEFF1; border-color:#607D8B; color:#607D8B;">村</div>
<div class="dialogue-text">「不思議だ。何もアドバイスしないのに、元気が出る」</div>
</div>

<div class="story">
ユイは、とても不思議に思いました。
</div>

<div class="page">- 7 -</div>

---

<!-- 8 -->
<div class="illust">
<div class="icon icon-girl">ユ</div>
<div style="font-size: 1.5em; color: var(--ink-light);">?</div>
<div class="icon icon-old">翁</div>
</div>

<div class="story">
ある日、ユイはこっそり老人の小屋を覗きました。

村の女性が、泣きながら話していました。

でも老人は、<span class="blue">ただ静かに聴いているだけ</span>。

何も言わない。ただ、聴いている。
</div>

<div class="page">- 8 -</div>

---

<!-- 9 -->
<section class="bg-forest">

<div class="illust">
<div class="icon icon-girl">ユ</div>
<div style="font-size: 2em; color: var(--gold);">！</div>
</div>

<div class="story">
その時、ユイは<span class="gold">信じられないもの</span>を見ました。

女性の心から聞こえていた<span class="rose">悲しみの声</span>が、

少しずつ、少しずつ、<span class="forest">静かになっていく</span>のです。
</div>

<div class="dialogue-thought">
「どうして...？ 何もしていないのに...」
</div>

<div class="page">- 9 -</div>

</section>

---

<!-- 10 -->
<div class="illust">
<div class="icon icon-girl">ユ</div>
<div style="font-size: 1.5em;">→</div>
<div class="icon icon-old">翁</div>
</div>

<div class="story">
ユイは思い切って、老人を訪ねました。
</div>

<div class="dialogue">
<div class="icon icon-sm icon-girl">ユ</div>
<div class="dialogue-text">「あの...私、人の<span class="blue">心の声</span>が聞こえるんです。でも、それが苦しくて...」</div>
</div>

<div class="story">
初めて誰かに打ち明けた秘密でした。
</div>

<div class="page">- 10 -</div>

---

<!-- 11 -->
<div class="illust">
<div class="icon icon-old">翁</div>
</div>

<div class="story">
老人は驚きませんでした。

むしろ、<span class="gold">懐かしそうに微笑んで</span>言いました。
</div>

<div class="dialogue">
<div class="icon icon-sm icon-old">翁</div>
<div class="dialogue-text">「そうか。君も<span class="blue">『沈黙を聴くひと』</span>なんだね」</div>
</div>

<div class="page">- 11 -</div>

---

<!-- 12 -->
<div class="dialogue">
<div class="icon icon-sm icon-girl">ユ</div>
<div class="dialogue-text">「沈黙を...聴く？」</div>
</div>

<div class="dialogue">
<div class="icon icon-sm icon-old">翁</div>
<div class="dialogue-text">「人は言葉を話す。でも、<span class="rose">本当に伝えたいこと</span>は、<br>言葉と言葉の<span class="gold">あいだ</span>にあるんだよ」</div>
</div>

<div class="story">
老人もまた、同じ力を持っていたのです。
</div>

<div class="page">- 12 -</div>

---

<!-- 13 - 章 -->
<section class="bg-night">

<div class="chapter" style="color: #FFD54F;">― 第二章　修行 ―</div>

<div class="symbol">☽ ✦ ✦ ✦</div>

<div class="story">
その日から、ユイは老人のもとで学び始めました。

<span style="color: #FFD54F;">「聴く」とは何か。</span>

<span style="color: #90CAF9;">「沈黙」にどう応えるのか。</span>
</div>

<div class="page">- 13 -</div>

</section>

---

<!-- 14 -->
<div class="dialogue">
<div class="icon icon-sm icon-old">翁</div>
<div class="dialogue-text">「ユイ、誰かの話を聴くとき、何を考えている？」</div>
</div>

<div class="dialogue">
<div class="icon icon-sm icon-girl">ユ</div>
<div class="dialogue-text">「えっと...『どうしてあげよう』とか、『何て言えばいいんだろう』とか...」</div>
</div>

<div class="dialogue">
<div class="icon icon-sm icon-old">翁</div>
<div class="dialogue-text">「それが<span class="rose">最初の間違い</span>なんだよ」</div>
</div>

<div class="page">- 14 -</div>

---

<!-- 15 -->
<div class="illust">
<div class="icon icon-old">翁</div>
</div>

<div class="dialogue">
<div class="icon icon-sm icon-old">翁</div>
<div class="dialogue-text">「聴いている時に『次に何を言おう』と考えたら、<br>もう<span class="blue">聴いていない</span>んだ」</div>
</div>

<div class="dialogue">
<div class="icon icon-sm icon-old">翁</div>
<div class="dialogue-text">「相手の言葉を、<span class="gold">ただ受け止める</span>。<br>それだけでいいんだよ」</div>
</div>

<div class="page">- 15 -</div>

---

<!-- 16 -->
<section class="bg-forest">

<div class="illust">
<div class="icon icon-girl">ユ</div>
<div style="font-size: 1.5em; color: var(--ink-light);">?</div>
</div>

<div class="dialogue">
<div class="icon icon-sm icon-girl">ユ</div>
<div class="dialogue-text">「でも、何も言わないと、相手は不安になりませんか？」</div>
</div>

<div class="dialogue">
<div class="icon icon-sm icon-old">翁</div>
<div class="dialogue-text">「言葉は必要ない。大切なのは...<br><span class="forest">『あなたの気持ち、ちゃんと聴こえているよ』</span><br>と、態度で伝えることなんだ」</div>
</div>

<div class="page">- 16 -</div>

</section>

---

<!-- 17 -->
<div class="illust">
<div class="icon icon-girl">ユ</div>
<div style="font-size: 2em; color: var(--gold);">！</div>
</div>

<div class="story">
ユイは少しずつ理解し始めました。

人が本当に求めているのは、<span class="sunset">アドバイス</span>じゃない。

<span class="gold">「わかってもらえた」</span>という感覚なのだと。
</div>

<div class="page">- 17 -</div>

---

<!-- 18 -->
<div class="dialogue">
<div class="icon icon-sm icon-old">翁</div>
<div class="dialogue-text">「人は誰かに話を聴いてもらうとき、<br>実は<span class="blue">自分自身の声を聴いている</span>んだよ」</div>
</div>

<div class="dialogue">
<div class="icon icon-sm icon-old">翁</div>
<div class="dialogue-text">「だから、聴き手は<span class="gold">鏡</span>になればいい。<br>相手が自分の心を映せる、静かな鏡に」</div>
</div>

<div class="page">- 18 -</div>

---

<!-- 19 - 章 -->
<section class="bg-sunset">

<div class="chapter">― 第三章　試練 ―</div>

<div class="symbol symbol-sm">◐ ～～～</div>

<div class="story">
一年が過ぎた頃、老人が言いました。
</div>

<div class="dialogue">
<div class="icon icon-sm icon-old">翁</div>
<div class="dialogue-text">「ユイ、そろそろ<span class="sunset">本当の修行</span>の時間だ」</div>
</div>

<div class="page">- 19 -</div>

</section>

---

<!-- 20 -->
<div class="illust">
<div class="icon icon-old">翁</div>
<div style="font-size: 1.5em;">→</div>
<div class="icon icon-boy">?</div>
</div>

<div class="dialogue">
<div class="icon icon-sm icon-old">翁</div>
<div class="dialogue-text">「村の東に住むタケルという男の子がいる。<br>彼は一年前に母親を亡くしてから、<span class="blue">誰とも話さなくなった</span>」</div>
</div>

<div class="dialogue">
<div class="icon icon-sm icon-old">翁</div>
<div class="dialogue-text">「彼の<span class="rose">沈黙の声</span>を聴いてごらん」</div>
</div>

<div class="page">- 20 -</div>

---

<!-- 21 -->
<section class="bg-rain">

<div class="illust">
<div class="icon icon-boy">タ</div>
<div style="font-size: 1.5em; color: var(--ink-light);">...</div>
</div>

<div class="story">
タケルは13歳。

一人で古い家に住み、誰とも目を合わせず、

<span class="blue">一言も話さない</span>少年でした。

村人たちは遠巻きに見るだけで、誰も近づきませんでした。
</div>

<div class="page">- 21 -</div>

</section>

---

<!-- 22 -->
<div class="illust">
<div class="icon icon-girl">ユ</div>
<div style="font-size: 1.5em;">→</div>
<div class="icon icon-boy">タ</div>
</div>

<div class="story">
ユイはタケルの家を訪ねました。

タケルは無表情でユイを見ましたが、

追い返しはしませんでした。
</div>

<div class="story">
ユイは<span class="gold">何も言わず、ただそばに座りました</span>。
</div>

<div class="page">- 22 -</div>

---

<!-- 23 -->
<section class="bg-deep">

<div class="illust">
<div class="icon icon-boy" style="border-color: #424242; background: #212121;">タ</div>
<div style="font-size: 1.5em; color: #FF5252;">■ ■ ■</div>
</div>

<div class="story">
タケルの心から聞こえてきたのは、

今まで聴いたことのないほど<span style="color: #FF5252;">深い悲しみ</span>でした。

<span style="color: #90CAF9;">「どうして僕を置いていったの」</span>

<span style="color: #FFD54F;">「最後に『ありがとう』も言えなかった」</span>
</div>

<div class="page">- 23 -</div>

</section>

---

<!-- 24 -->
<div class="illust">
<div class="icon icon-girl">ユ</div>
</div>

<div class="story">
ユイは泣きそうになりました。

でも、老人の言葉を思い出しました。

<span class="gold">「聴くとは、相手の感情を背負うことじゃない」</span>

<span class="blue">「ただ、『ここにいるよ』と伝えることだ」</span>
</div>

<div class="page">- 24 -</div>

---

<!-- 25 -->
<div class="illust">
<div class="icon icon-girl">ユ</div>
<div style="font-size: 1.5em; color: var(--gold);">～</div>
<div class="icon icon-boy">タ</div>
</div>

<div class="story">
ユイは毎日、タケルのもとを訪れました。

何も言わず、ただそばにいる。

時には一緒に空を眺め、時には一緒に黙って座る。

<span class="forest">一週間、二週間、一ヶ月...</span>
</div>

<div class="page">- 25 -</div>

---

<!-- 26 -->
<section class="bg-spring">

<div class="symbol symbol-sm">❀ ～ ❀ ～ ❀</div>

<div class="story">
春が来た頃、タケルが初めて口を開きました。
</div>

<div class="dialogue">
<div class="icon icon-sm icon-boy">タ</div>
<div class="dialogue-text">「...なんで、毎日来るの？」</div>
</div>

<div class="story">
ユイは静かに答えました。
</div>

<div class="dialogue">
<div class="icon icon-sm icon-girl">ユ</div>
<div class="dialogue-text">「<span class="rose">あなたの声が、聴こえたから</span>」</div>
</div>

<div class="page">- 26 -</div>

</section>

---

<!-- 27 -->
<div class="dialogue">
<div class="icon icon-sm icon-boy">タ</div>
<div class="dialogue-text">「...俺、何も話してないよ」</div>
</div>

<div class="dialogue">
<div class="icon icon-sm icon-girl">ユ</div>
<div class="dialogue-text">「うん。でも、<span class="blue">声は聴こえた</span>。<br>すごく悲しくて、すごく寂しい声」</div>
</div>

<div class="story">
タケルの目から、涙がこぼれました。

一年間、誰にも見せなかった涙でした。
</div>

<div class="page">- 27 -</div>

---

<!-- 28 -->
<div class="illust">
<div class="icon icon-boy" style="border-color: var(--soft-blue);">タ</div>
<div style="font-size: 1.5em; color: var(--rose);">～</div>
<div class="icon icon-girl">ユ</div>
</div>

<div class="dialogue">
<div class="icon icon-sm icon-boy">タ</div>
<div class="dialogue-text">「誰も...わかってくれないと思ってた...<br><span class="rose">僕の気持ちなんて、誰にも...</span>」</div>
</div>

<div class="story">
ユイはタケルの手をそっと握りました。

言葉はいらなかった。

<span class="gold">「聴こえているよ」</span>

その気持ちが、伝わればよかったから。
</div>

<div class="page">- 28 -</div>

---

<!-- 29 - 章 -->
<section class="bg-dawn">

<div class="chapter">― 終章　継承 ―</div>

<div class="illust">
<div class="icon icon-old">翁</div>
<div style="font-size: 1.5em; color: var(--gold);">～</div>
<div class="icon icon-girl">ユ</div>
</div>

<div class="story">
ユイが老人のもとに戻ると、

老人は優しく微笑んでいました。
</div>

<div class="dialogue">
<div class="icon icon-sm icon-old">翁</div>
<div class="dialogue-text">「よくやったね、ユイ」</div>
</div>

<div class="page">- 29 -</div>

</section>

---

<!-- 30 -->
<div class="dialogue">
<div class="icon icon-sm icon-girl">ユ</div>
<div class="dialogue-text">「おじいさん、私わかりました。<br>この力は<span class="rose">呪い</span>じゃなかった」</div>
</div>

<div class="dialogue">
<div class="icon icon-sm icon-girl">ユ</div>
<div class="dialogue-text">「<span class="gold">聴こえるからこそ、寄り添える</span>んですね。<br>言葉にできない苦しみを抱えた人に」</div>
</div>

<div class="page">- 30 -</div>

---

<!-- 31 -->
<div class="illust">
<div class="icon icon-old">翁</div>
</div>

<div class="dialogue">
<div class="icon icon-sm icon-old">翁</div>
<div class="dialogue-text">「その通りだよ、ユイ。<br>人は<span class="blue">『聴いてもらえた』と感じた時</span>、<br>初めて自分の心と向き合える」</div>
</div>

<div class="dialogue">
<div class="icon icon-sm icon-old">翁</div>
<div class="dialogue-text">「君はこれから、たくさんの人の<br><span class="gold">沈黙を聴く</span>ことになるだろう」</div>
</div>

<div class="page">- 31 -</div>

---

<!-- 32 -->
<section class="bg-forest">

<div class="symbol symbol-sm">→ → →</div>

<div class="illust">
<div class="icon icon-girl">ユ</div>
</div>

<div class="story">
数年後、ユイは村を出て旅に出ました。

<span class="forest">「沈黙を聴くひと」</span>として、

言葉にならない声を抱えた人々のもとへ。
</div>

<div class="page">- 32 -</div>

</section>

---

<!-- 33 -->
<div class="illust">
<div class="icon icon-girl" style="width:80px; height:80px; font-size:32px;">ユ</div>
</div>

<div class="story">
ユイは気づいていました。

特別な力がなくても、<span class="gold">誰にでもできる</span>ことがあると。

それは、<span class="rose">「ただ、聴く」</span>ということ。

相手の言葉の<span class="blue">裏にある気持ち</span>を、

想像しながら、心を傾けること。
</div>

<div class="page">- 33 -</div>

---

<!-- 教訓ページ -->
<div class="lesson-box">
<div class="lesson-title">* この物語があなたに伝えたいこと *</div>
<div class="lesson-text">
<span class="blue">相手の言葉の裏にある感情に気づくこと。</span>

人は「大丈夫」と言いながら、助けを求めていることがある。<br>
「怒り」の裏には、「悲しみ」が隠れていることがある。

<span class="gold">言葉だけでなく、その奥にある気持ちに耳を傾けてみてください。</span>
</div>
</div>

<div class="page">- 34 -</div>

---

<!-- 最終ページ -->
<div class="the-end">おしまい</div>

<div class="symbol" style="margin-top: 30px;">((( ♡ )))</div>

<div style="text-align: center; margin-top: 40px; color: var(--ink-light); font-size: 0.95em;">
今日、誰かの「沈黙」に気づけますように。
</div>

---

<!-- 裏表紙 -->
<div class="book-cover" style="padding-top: 80px;">

<div class="deco">~ ~ ~</div>

<div style="font-size: 1.3em; margin-top: 30px; color: var(--deep-blue);">
聴くことは、愛することの始まり。
</div>

<div style="margin-top: 60px; font-size: 0.9em; color: var(--ink-light);">
― 沈黙を聴くひと ―
</div>

</div>

