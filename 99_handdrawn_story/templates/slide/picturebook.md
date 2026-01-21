---
marp: true
theme: default
paginate: false
size: 16:9
style: |
  /* ================================ */
  /* 絵本風テンプレート               */
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

  /* キャラクターアイコン */
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

  /* テキスト */
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

  /* 強調 */
  .marker { background: linear-gradient(transparent 60%, var(--yellow) 60%); }
  .marker-pink { background: linear-gradient(transparent 60%, var(--pink) 60%); }
  .marker-blue { background: linear-gradient(transparent 60%, var(--blue) 60%); }
  .text-blue { color: var(--blue); font-weight: 700; }
  .text-pink { color: var(--pink); font-weight: 700; }
  .text-green { color: var(--green); font-weight: 700; }
  .text-orange { color: #E65100; font-weight: 700; }
  .text-purple { color: #7B1FA2; font-weight: 700; }

  /* 吹き出し */
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

  /* 区切り */
  .divider { text-align: center; margin: 20px 0; font-size: 1.5em; color: var(--gray); letter-spacing: 0.5em; }

  /* 背景 */
  .bg-day { background: linear-gradient(180deg, #87CEEB 0%, #E0F7FA 100%); }
  .bg-sunset { background: linear-gradient(180deg, #FFCC80 0%, #FF8A65 50%, #E57373 100%); }
  .bg-night { background: linear-gradient(180deg, #1A237E 0%, #283593 50%, #3949AB 100%); color: white; }
  .bg-forest { background: linear-gradient(180deg, #C8E6C9 0%, #A5D6A7 50%, #81C784 100%); }
  .bg-sea { background: linear-gradient(180deg, #E3F2FD 0%, #BBDEFB 30%, #90CAF9 60%, #64B5F6 100%); }

  /* ページ番号 */
  .page-num {
    position: absolute;
    bottom: 30px;
    right: 50px;
    font-size: 0.8em;
    color: var(--brown);
    opacity: 0.5;
  }

  /* 教訓・終わり */
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
<!-- イラスト用アイコンをここに -->
</div>

# タイトル

<div style="margin-top: 20px; color: var(--gray);">
サブタイトル
</div>

</div>

---

<!-- ストーリーページ例 -->
<div class="illust-area">
<span class="character char-blue">A</span>
<span class="character char-pink">B</span>
</div>

<div class="story-text">
むかしむかし、ある場所に...

<span class="marker">大切なこと</span>がありました。
</div>

<div class="page-num">- 1 -</div>

---

<!-- 会話ページ例 -->
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

<div class="page-num">- 2 -</div>

---

<!-- エンディング例 -->
<div class="moral-box">
<span class="text-purple">物語から学べること：</span>

ここに教訓を書く
</div>

<div class="the-end">
おしまい
</div>

<div class="illust-area">
<span class="character char-blue">A</span>
<span class="character char-pink">B</span>
</div>
