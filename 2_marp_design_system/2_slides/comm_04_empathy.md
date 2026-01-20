---
marp: true
theme: default
paginate: false
style: |
  /* ================================ */
  /* コミュ力シリーズ - ポップテーマ  */
  /* ================================ */

  :root {
    --bg: #FFF0F6;
    --primary: #F368E0;
    --secondary: #FF6B81;
    --accent: #FFC048;
    --mint: #00D2D3;
    --blue: #54A0FF;
    --text: #2D3436;
    --text-light: #636E72;
    --white: #FFFFFF;
  }

  section {
    background: var(--bg);
    font-family: "Hiragino Maru Gothic Pro", "Noto Sans JP", sans-serif;
    color: var(--text);
    padding: 35px 45px;
  }

  h1 { color: var(--primary); font-size: 1.9em; }
  h2 { color: var(--text); font-size: 1.4em; }

  /* キャラクター */
  .chara {
    display: flex;
    align-items: flex-start;
    gap: 15px;
    margin: 12px 0;
  }
  .chara.right { flex-direction: row-reverse; }
  .chara-icon { font-size: 2.8em; flex-shrink: 0; }
  .chara-bubble {
    background: var(--white);
    border-radius: 20px;
    padding: 15px 20px;
    max-width: 80%;
    box-shadow: 0 3px 15px rgba(0,0,0,0.08);
    position: relative;
    line-height: 1.7;
  }
  .chara.right .chara-bubble { background: var(--secondary); color: white; }
  .chara-name {
    font-size: 0.7em;
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 5px;
  }
  .chara.right .chara-name { color: var(--white); opacity: 0.9; }
  .chara-bubble strong { color: var(--primary); }
  .chara.right .chara-bubble strong { color: var(--accent); }

  /* タイトル */
  .title-pop {
    text-align: center;
    padding-top: 50px;
  }
  .title-pop .episode {
    background: var(--primary);
    color: white;
    padding: 5px 20px;
    border-radius: 20px;
    font-size: 0.9em;
    display: inline-block;
    margin-bottom: 15px;
  }
  .title-pop h1 {
    font-size: 2.3em;
    margin: 0;
    color: var(--text);
  }
  .title-pop .subtitle {
    color: var(--text-light);
    margin-top: 15px;
    font-size: 1.1em;
  }
  .title-pop .skill-tag {
    background: var(--accent);
    color: var(--text);
    padding: 8px 25px;
    border-radius: 25px;
    font-weight: 700;
    display: inline-block;
    margin-top: 20px;
  }

  /* シーン説明 */
  .scene-box {
    background: linear-gradient(135deg, var(--primary) 0%, #D847C0 100%);
    color: white;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    margin: 20px 0;
  }
  .scene-box .scene-icon { font-size: 2em; margin-bottom: 10px; }
  .scene-box .scene-title { font-weight: 700; font-size: 1.1em; }

  /* ポイントボックス */
  .point-box {
    background: var(--white);
    border-radius: 15px;
    padding: 20px;
    border-left: 5px solid var(--mint);
    margin: 15px 0;
    box-shadow: 0 3px 15px rgba(0,0,0,0.05);
  }
  .point-title {
    color: var(--mint);
    font-weight: 700;
    font-size: 1.1em;
    margin-bottom: 10px;
  }

  /* NGとOK */
  .ng-ok {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
    margin: 15px 0;
  }
  .ng-box, .ok-box {
    border-radius: 15px;
    padding: 15px;
  }
  .ng-box { background: #FFE5E5; border: 2px solid var(--secondary); }
  .ok-box { background: #E0FFFF; border: 2px solid var(--mint); }
  .ng-label, .ok-label {
    font-weight: 700;
    text-align: center;
    margin-bottom: 10px;
    font-size: 1.1em;
  }
  .ng-label { color: var(--secondary); }
  .ok-label { color: #00A67E; }

  /* まとめ */
  .summary-pop {
    background: linear-gradient(135deg, var(--mint) 0%, #00B5B5 100%);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    color: white;
  }
  .summary-pop h2 { color: white; margin: 0 0 15px; }
  .summary-key {
    background: rgba(255,255,255,0.2);
    border-radius: 10px;
    padding: 15px;
    font-size: 1.3em;
    font-weight: 700;
  }

  /* 次回予告 */
  .next-episode {
    background: var(--white);
    border: 3px dashed var(--primary);
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    margin-top: 20px;
  }
  .next-episode .next-label {
    color: var(--primary);
    font-size: 0.85em;
    font-weight: 700;
  }
  .next-episode .next-title {
    font-size: 1.2em;
    font-weight: 700;
    margin-top: 8px;
    color: var(--text);
  }

  /* ヒント */
  .hint-pop {
    background: var(--accent);
    border-radius: 12px;
    padding: 15px;
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 15px 0;
  }
  .hint-icon { font-size: 1.8em; }

  /* 感情カード */
  .emotion-cards {
    display: flex;
    gap: 15px;
    margin: 15px 0;
  }
  .emotion-card {
    flex: 1;
    background: var(--white);
    border-radius: 15px;
    padding: 15px;
    text-align: center;
    box-shadow: 0 3px 10px rgba(0,0,0,0.08);
  }
  .emotion-icon { font-size: 2.5em; margin-bottom: 10px; }
  .emotion-label { font-weight: 600; }
  .emotion-hidden {
    font-size: 0.85em;
    color: var(--text-light);
    margin-top: 5px;
  }

  /* ステップ */
  .steps-pop {
    display: flex;
    gap: 15px;
    margin: 15px 0;
  }
  .step-item {
    flex: 1;
    background: var(--white);
    border-radius: 15px;
    padding: 15px;
    text-align: center;
    box-shadow: 0 3px 10px rgba(0,0,0,0.08);
  }
  .step-num {
    background: var(--primary);
    color: white;
    width: 35px;
    height: 35px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 10px;
    font-weight: 700;
  }
  .step-item:nth-child(2) .step-num { background: var(--secondary); }
  .step-item:nth-child(3) .step-num { background: var(--mint); }

  /* 共感フレーズ */
  .empathy-phrases {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin: 15px 0;
  }
  .empathy-phrase {
    background: var(--white);
    border-radius: 10px;
    padding: 12px 15px;
    border-left: 4px solid var(--primary);
    font-size: 0.95em;
  }

---

<!-- タイトル -->
<div class="title-pop">
<span class="episode">コミュ力アップ講座 #04</span>

# 💭 そういうことじゃないんだけど...

<div class="subtitle">〜 相手の気持ちが分からない問題 〜</div>
<span class="skill-tag">💡 今日の学び：共感力</span>
</div>

---

<!-- シーン1 -->

<div class="scene-box">
<div class="scene-icon">☕</div>
<div class="scene-title">休憩室にて</div>
</div>

<div class="chara">
<span class="chara-icon">😢</span>
<div class="chara-bubble">
<div class="chara-name">同僚（山田）</div>
最近、仕事がうまくいかなくて...<br>
クライアントからの要望も増えて、正直しんどいんだよね...
</div>
</div>

<div class="chara right">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
<strong>じゃあ、タスク管理ツールを使ったらどうですか？</strong><br>
僕これ使ってるんですけど、めっちゃ便利ですよ！
</div>
</div>

<div class="chara">
<span class="chara-icon">😢</span>
<div class="chara-bubble">
<div class="chara-name">同僚（山田）</div>
...うん...<span style="color: #999;">（そういうことじゃないんだけど...）</span>
</div>
</div>

---

<!-- シーン2 -->

<div class="chara right">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
あと、朝早く来て作業するとはかどりますよ！<br>
<strong>僕なんか毎日6時起きですから！</strong>
</div>
</div>

<div class="chara">
<span class="chara-icon">😢</span>
<div class="chara-bubble">
<div class="chara-name">同僚（山田）</div>
あ、そうなんだ...<br>
<span style="color: #999;">（私の話、全然聞いてない...）</span>
</div>
</div>

<div class="chara right">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
大丈夫ですよ！<strong>頑張ればなんとかなりますって！</strong>
</div>
</div>

<div class="chara">
<span class="chara-icon">😢</span>
<div class="chara-bubble">
<div class="chara-name">同僚（山田）</div>
...うん、ありがとう...<br>
<span style="color: #999;">（もういいや...）</span>
</div>
</div>

---

<!-- 問題点 -->

## 😰 鈴木くんの問題点

<div class="ng-ok">
<div class="ng-box">
<div class="ng-label">❌ 鈴木くんがやったこと</div>

- いきなり解決策を提示
- 自分の成功談を語る
- 「大丈夫」「頑張れ」で片付ける
- 相手の気持ちをスルー

</div>
<div class="ok-box">
<div class="ok-label">💭 山田さんが欲しかったもの</div>

- 話を聞いてほしい
- 気持ちをわかってほしい
- 「つらいね」と言ってほしい
- 一緒に考えてほしい

</div>
</div>

<div class="hint-pop">
<span class="hint-icon">💡</span>
<div>相談は「解決してほしい」より「聞いてほしい」が多い！</div>
</div>

---

<!-- 共感とは -->

## 💖 「共感」ってなに？

<div class="point-box">
<div class="point-title">📖 共感（Empathy）とは</div>
相手の<strong>感情</strong>を理解し、それを<strong>受け止める</strong>こと。<br><br>
「同情」との違い：<br>
・同情 = 「かわいそう」（上から目線）<br>
・共感 = 「つらいよね」（同じ目線）
</div>

<div class="emotion-cards">
<div class="emotion-card">
<div class="emotion-icon">😤</div>
<div class="emotion-label">怒り</div>
<div class="emotion-hidden">の裏には「悲しみ」</div>
</div>
<div class="emotion-card">
<div class="emotion-icon">😰</div>
<div class="emotion-label">不安</div>
<div class="emotion-hidden">の裏には「期待」</div>
</div>
<div class="emotion-card">
<div class="emotion-icon">😢</div>
<div class="emotion-label">悲しみ</div>
<div class="emotion-hidden">の裏には「願い」</div>
</div>
</div>

---

<!-- 共感のステップ -->

## 🎯 共感の3ステップ

<div class="steps-pop">
<div class="step-item">
<div class="step-num">1</div>
<strong>聴く</strong><br>
最後まで聴く<br>
（解決策は後！）
</div>
<div class="step-item">
<div class="step-num">2</div>
<strong>受け止める</strong><br>
気持ちを言葉にする<br>
「〜って感じてるんだね」
</div>
<div class="step-item">
<div class="step-num">3</div>
<strong>寄り添う</strong><br>
味方でいることを伝える<br>
「話してくれてありがとう」
</div>
</div>

<div class="hint-pop">
<span class="hint-icon">⚠️</span>
<div>アドバイスは「相手が求めたとき」だけ！いきなりはNG</div>
</div>

---

<!-- リベンジ -->

<div class="scene-box">
<div class="scene-icon">✨</div>
<div class="scene-title">鈴木くん、リベンジ！</div>
</div>

<div class="chara">
<span class="chara-icon">😢</span>
<div class="chara-bubble">
<div class="chara-name">同僚（山田）</div>
最近、仕事がうまくいかなくて...
</div>
</div>

<div class="chara right">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
そうなんですか...<strong>何があったんですか？</strong>
</div>
</div>

<div class="chara">
<span class="chara-icon">😢</span>
<div class="chara-bubble">
<div class="chara-name">同僚（山田）</div>
クライアントからの要望がどんどん増えて、<br>
全然追いつかないんだよね...
</div>
</div>

---

<!-- リベンジ2 -->

<div class="chara right">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
それは<strong>大変ですね...</strong><br>
要望が増え続けるのって、終わりが見えなくてしんどいですよね。
</div>
</div>

<div class="chara">
<span class="chara-icon">😢</span>
<div class="chara-bubble">
<div class="chara-name">同僚（山田）</div>
そうなの！<strong>わかってくれる？</strong><br>
なんか、頑張っても頑張っても終わらない感じで...
</div>
</div>

<div class="chara right">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
うんうん...<strong>話してくれてありがとうございます。</strong><br>
僕にできることあったら言ってくださいね。
</div>
</div>

<div class="chara">
<span class="chara-icon">😊</span>
<div class="chara-bubble">
<div class="chara-name">同僚（山田）</div>
ありがとう...聞いてもらえて<strong>ちょっと楽になった。</strong>
</div>
</div>

---

<!-- 使えるフレーズ -->

## 🗣️ 共感フレーズ集

<div class="empathy-phrases">
<div class="empathy-phrase">「それは<strong>大変でしたね</strong>」</div>
<div class="empathy-phrase">「<strong>つらかった</strong>ですよね」</div>
<div class="empathy-phrase">「そう感じるの、<strong>わかります</strong>」</div>
<div class="empathy-phrase">「それは<strong>モヤモヤ</strong>しますね」</div>
<div class="empathy-phrase">「話してくれて<strong>ありがとう</strong>」</div>
<div class="empathy-phrase">「<strong>味方</strong>だからね」</div>
</div>

<div class="ng-ok">
<div class="ng-box">
<div class="ng-label">❌ 避けたい言葉</div>

「でも」「だって」<br>
「そんなことで？」<br>
「もっと頑張れば」<br>
「私なんてもっと...」

</div>
<div class="ok-box">
<div class="ok-label">✅ 意識したい姿勢</div>

まず聴く<br>
感情を言葉にする<br>
アドバイスは後で<br>
味方でいることを伝える

</div>
</div>

---

<!-- まとめ -->

<div class="summary-pop">

## 💖 今日の学び：共感力

<div class="summary-key">
相談は「解決」より「理解」を求めている<br>
まず気持ちを受け止める
</div>

</div>

<br>

<div class="steps-pop">
<div class="step-item">
<div class="step-num">1</div>
<strong>聴く</strong><br>
解決策は後
</div>
<div class="step-item">
<div class="step-num">2</div>
<strong>受け止める</strong><br>
「つらいよね」
</div>
<div class="step-item">
<div class="step-num">3</div>
<strong>寄り添う</strong><br>
「味方だよ」
</div>
</div>

---

<!-- 次回予告 -->

<div class="title-pop" style="padding-top: 30px;">

## 🎬 To Be Continued...

</div>

<div class="next-episode">
<div class="next-label">📺 次回予告</div>
<div class="next-title">「なんでできないの？」<br>〜 言い方ひとつで関係が壊れる問題 〜</div>
</div>

<div class="chara" style="margin-top: 20px;">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
鈴木くん、このミス<strong>3回目</strong>だよね？
</div>
</div>

<div class="chara right">
<span class="chara-icon">😰</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
す、すみません...<span style="color: #999;">（怖い...）</span>
</div>
</div>
