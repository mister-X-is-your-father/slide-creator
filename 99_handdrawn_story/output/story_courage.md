---
marp: true
theme: default
paginate: false
size: 16:9
style: |
  /* ================================ */
  /* 絵本：声をなくしたことり         */
  /* テーマ：小さな勇気               */
  /* ================================ */

  @import url('https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@400;500;700&display=swap');

  :root {
    --cream: #FFF8E7;
    --brown: #5D4037;
    --blue: #64B5F6;
    --pink: #F48FB1;
    --green: #81C784;
    --orange: #FFB74D;
    --purple: #B39DDB;
    --yellow: #FFD54F;
    --gray: #9E9E9E;
  }

  section {
    background: var(--cream);
    font-family: "Zen Maru Gothic", sans-serif;
    color: var(--brown);
    padding: 40px 60px;
    font-size: 26px;
    line-height: 2;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .character {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    font-size: 24px;
    font-weight: bold;
    margin: 0 8px;
    border: 3px solid;
  }

  .char-blue { background: #E3F2FD; border-color: var(--blue); color: var(--blue); }
  .char-pink { background: #FCE4EC; border-color: var(--pink); color: #C2185B; }
  .char-green { background: #E8F5E9; border-color: var(--green); color: #388E3C; }
  .char-orange { background: #FFF3E0; border-color: var(--orange); color: #E65100; }
  .char-purple { background: #EDE7F6; border-color: var(--purple); color: #7B1FA2; }

  .char-small { width: 45px; height: 45px; font-size: 18px; }

  .story-text {
    text-align: center;
    font-size: 1.3em;
    line-height: 2.2;
    max-width: 800px;
    margin: 0 auto;
  }

  .text-center { text-align: center; }
  .illust-area { text-align: center; padding: 20px; margin: 20px 0; }
  .text-icon { font-size: 3em; line-height: 1.3; text-align: center; }

  .marker { background: linear-gradient(transparent 60%, var(--yellow) 60%); }
  .marker-pink { background: linear-gradient(transparent 60%, rgba(244,143,177,0.4) 60%); }
  .marker-blue { background: linear-gradient(transparent 60%, rgba(100,181,246,0.4) 60%); }
  .text-blue { color: var(--blue); font-weight: 700; }
  .text-pink { color: #C2185B; font-weight: 700; }
  .text-green { color: #388E3C; font-weight: 700; }
  .text-orange { color: #E65100; font-weight: 700; }
  .text-purple { color: #7B1FA2; font-weight: 700; }

  .bubble {
    background: white;
    border: 2px solid var(--brown);
    border-radius: 20px;
    padding: 15px 25px;
    margin: 10px auto;
    max-width: 600px;
    text-align: center;
  }

  .dialogue-row {
    display: flex;
    align-items: flex-start;
    gap: 15px;
    margin: 15px 0;
  }

  .dialogue-row-right { flex-direction: row-reverse; }

  .dialogue-content {
    background: white;
    border: 2px solid var(--brown);
    border-radius: 15px;
    padding: 10px 15px;
    max-width: 70%;
  }

  .divider { text-align: center; margin: 20px 0; font-size: 1.5em; color: var(--gray); letter-spacing: 0.5em; }

  .bg-day { background: linear-gradient(180deg, #87CEEB 0%, #E0F7FA 100%); }
  .bg-sunset { background: linear-gradient(180deg, #FFCC80 0%, #FF8A65 50%, #E57373 100%); }
  .bg-night { background: linear-gradient(180deg, #1A237E 0%, #283593 50%, #3949AB 100%); color: white; }
  .bg-forest { background: linear-gradient(180deg, #C8E6C9 0%, #A5D6A7 50%, #81C784 100%); }
  .bg-morning { background: linear-gradient(180deg, #FFF8E1 0%, #FFECB3 50%, #FFE082 100%); }

  .page-num {
    position: absolute;
    bottom: 30px;
    right: 50px;
    font-size: 0.8em;
    color: var(--brown);
    opacity: 0.5;
  }

  .moral-box {
    background: rgba(255,255,255,0.8);
    border: 3px dashed var(--orange);
    border-radius: 20px;
    padding: 20px 30px;
    margin: 20px auto;
    max-width: 600px;
    text-align: center;
  }

  .the-end {
    text-align: center;
    font-size: 2em;
    color: var(--purple);
    margin-top: 50px;
    letter-spacing: 0.3em;
  }

---

<!-- 表紙 -->
<div class="text-center">

<div class="text-icon">
<span class="character char-blue" style="width:80px;height:80px;font-size:32px;">pi</span>
</div>

# 声をなくしたことり

<div style="margin-top: 20px; color: var(--gray);">
〜 小さな勇気のものがたり 〜
</div>

</div>

---

<!-- 1 -->
<div class="illust-area">
<span class="character char-blue">pi</span>
</div>

<div class="story-text">
森の奥に、<span class="text-blue">ピピ</span>という小さなことりがいました。

ピピは歌うことが大好きでした。
</div>

<div class="page-num">- 1 -</div>

---

<!-- 2 -->
<section class="bg-forest">

<div class="illust-area">
<span class="character char-blue">pi</span>
<span class="character char-green char-small">mo</span>
<span class="character char-orange char-small">ri</span>
<span class="character char-pink char-small">ha</span>
</div>

<div class="story-text">
でも、ピピには<span class="marker">困っていること</span>がありました。

他の鳥たちの前だと、声が出なくなってしまうのです。
</div>

<div class="page-num">- 2 -</div>

</section>

---

<!-- 3 -->
<div class="dialogue-row">
<span class="character char-green">mo</span>
<div class="dialogue-content">
「ピピ、一緒に歌おうよ！」
</div>
</div>

<div class="dialogue-row dialogue-row-right">
<span class="character char-blue">pi</span>
<div class="dialogue-content">
「......」
</div>
</div>

<div class="story-text" style="margin-top:20px;">
ピピは口を開けても、<span class="text-pink">声が喉の奥で固まって</span>しまいます。
</div>

<div class="page-num">- 3 -</div>

---

<!-- 4 -->
<div class="illust-area">
<span class="character char-blue">pi</span>
</div>

<div class="story-text">
「どうして僕は、みんなの前だと歌えないんだろう...」

ひとりぼっちの夜、ピピは泣きました。
</div>

<div class="page-num">- 4 -</div>

---

<!-- 5 -->
<div class="divider">* * *</div>

<div class="illust-area">
<span class="character char-blue">pi</span>
<span class="character char-purple">fu</span>
</div>

<div class="story-text">
ある日、森に<span class="text-purple">年老いたふくろう</span>がやってきました。

「おや、泣いているのかい？」
</div>

<div class="page-num">- 5 -</div>

---

<!-- 6 -->
<div class="dialogue-row">
<span class="character char-blue">pi</span>
<div class="dialogue-content">
「僕、みんなの前だと声が出ないんです...」
</div>
</div>

<div class="dialogue-row dialogue-row-right">
<span class="character char-purple">fu</span>
<div class="dialogue-content">
「ほう。それは<span class="text-orange">声</span>をなくしたのではないよ」
</div>
</div>

<div class="page-num">- 6 -</div>

---

<!-- 7 -->
<div class="illust-area">
<span class="character char-purple">fu</span>
</div>

<div class="story-text">
「お前さんは、<span class="marker">勇気を眠らせている</span>だけじゃ」

ふくろうは静かに言いました。
</div>

<div class="page-num">- 7 -</div>

---

<!-- 8 -->
<div class="dialogue-row dialogue-row-right">
<span class="character char-purple">fu</span>
<div class="dialogue-content">
「完璧に歌おうとしなくていい。<br>
<span class="text-blue">最初の一音</span>だけ出してごらん」
</div>
</div>

<div class="story-text" style="margin-top:20px;">
「最初の...一音...?」
</div>

<div class="page-num">- 8 -</div>

---

<!-- 9 -->
<section class="bg-morning">

<div class="divider">* * *</div>

<div class="illust-area">
<span class="character char-blue">pi</span>
<span class="character char-green char-small">mo</span>
<span class="character char-orange char-small">ri</span>
</div>

<div class="story-text">
次の朝、仲間たちが集まりました。

「今日も一緒に歌おう！」
</div>

<div class="page-num">- 9 -</div>

</section>

---

<!-- 10 -->
<div class="illust-area">
<span class="character char-blue">pi</span>
</div>

<div class="story-text">
ピピの心臓がドキドキします。

でも、ふくろうの言葉を思い出しました。

<span class="marker-blue">「最初の一音だけ...」</span>
</div>

<div class="page-num">- 10 -</div>

---

<!-- 11 -->
<div class="story-text" style="font-size:1.5em;">
ピピは目を閉じて、

小さく息を吸いました。
</div>

<div class="text-center" style="font-size:2em; margin-top:30px;">
<span class="text-blue">「ピ...」</span>
</div>

<div class="page-num">- 11 -</div>

---

<!-- 12 -->
<div class="illust-area">
<span class="character char-blue">pi</span>
</div>

<div class="story-text">
小さな、小さな声。

でも、<span class="marker">確かに声が出ました</span>。
</div>

<div class="page-num">- 12 -</div>

---

<!-- 13 -->
<div class="dialogue-row">
<span class="character char-green">mo</span>
<div class="dialogue-content">
「ピピ！聞こえたよ！」
</div>
</div>

<div class="dialogue-row dialogue-row-right">
<span class="character char-orange">ri</span>
<div class="dialogue-content">
「もっと聞かせて！」
</div>
</div>

<div class="page-num">- 13 -</div>

---

<!-- 14 -->
<section class="bg-day">

<div class="illust-area">
<span class="character char-blue">pi</span>
<span class="character char-green char-small">mo</span>
<span class="character char-orange char-small">ri</span>
<span class="character char-pink char-small">ha</span>
</div>

<div class="story-text">
ピピは気づきました。

<span class="text-purple">完璧じゃなくても、伝わるんだ。</span>
</div>

<div class="page-num">- 14 -</div>

</section>

---

<!-- 15 -->
<div class="story-text">
それから、ピピは<span class="marker-pink">少しずつ歌えるように</span>なりました。

まだ緊張するけれど、

<span class="text-blue">「最初の一音」</span>を出す勇気があれば大丈夫。
</div>

<div class="page-num">- 15 -</div>

---

<!-- 16 -->
<div class="moral-box">
<span class="text-purple">この物語から：</span>

<span class="text-orange">完璧を目指さなくていい。</span>

小さな一歩を踏み出す勇気が、すべてを変える。
</div>

<div class="the-end">
おしまい
</div>

---

<!-- 裏表紙 -->
<div class="text-center" style="padding-top:80px;">

<div class="illust-area">
<span class="character char-blue" style="width:80px;height:80px;font-size:32px;">pi</span>
</div>

<div style="font-size:1.2em; margin-top:30px;">
今日、あなたの「最初の一音」は何ですか？
</div>

<div style="margin-top:60px; font-size:0.8em; color:var(--gray);">
- 声をなくしたことり -
</div>

</div>
