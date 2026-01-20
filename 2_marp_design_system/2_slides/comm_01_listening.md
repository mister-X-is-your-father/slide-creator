---
marp: true
theme: default
paginate: false
style: |
  /* ================================ */
  /* コミュ力シリーズ - ポップテーマ  */
  /* ================================ */

  :root {
    --bg: #FFF9E6;
    --primary: #FF6B6B;
    --secondary: #4ECDC4;
    --accent: #FFE66D;
    --purple: #A06CD5;
    --blue: #6BC5F8;
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
    font-size: 2.5em;
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
    background: linear-gradient(135deg, var(--purple) 0%, #8E7CC3 100%);
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
    border-left: 5px solid var(--secondary);
    margin: 15px 0;
    box-shadow: 0 3px 15px rgba(0,0,0,0.05);
  }
  .point-title {
    color: var(--secondary);
    font-weight: 700;
    font-size: 1.1em;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
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
  .ng-box { background: #FFE5E5; border: 2px solid var(--primary); }
  .ok-box { background: #E5FFF9; border: 2px solid var(--secondary); }
  .ng-label, .ok-label {
    font-weight: 700;
    text-align: center;
    margin-bottom: 10px;
    font-size: 1.1em;
  }
  .ng-label { color: var(--primary); }
  .ok-label { color: #00A67E; }

  /* まとめ */
  .summary-pop {
    background: linear-gradient(135deg, var(--secondary) 0%, #45B7AA 100%);
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
    border: 3px dashed var(--purple);
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    margin-top: 20px;
  }
  .next-episode .next-label {
    color: var(--purple);
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

  /* 沈黙 */
  .silence {
    text-align: center;
    padding: 30px;
    color: var(--text-light);
    font-style: italic;
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
  .step-item:nth-child(3) .step-num { background: var(--purple); }

---

<!-- タイトル -->
<div class="title-pop">
<span class="episode">コミュ力アップ講座 #01</span>

# 🎧 聞いてるフリしてない？

<div class="subtitle">〜 後輩が話しかけてこなくなった理由 〜</div>
<span class="skill-tag">💡 今日の学び：傾聴力</span>
</div>

---

<!-- シーン1 -->

<div class="scene-box">
<div class="scene-icon">🏢</div>
<div class="scene-title">ある日のオフィス</div>
</div>

<div class="chara">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
最近、後輩の鈴木くんが全然話しかけてこないんだよね...
</div>
</div>

<div class="chara right">
<span class="chara-icon">👩‍💻</span>
<div class="chara-bubble">
<div class="chara-name">同僚（山田）</div>
えっ、前はよく相談してたじゃん。何かあった？
</div>
</div>

<div class="chara">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
いや、別に何も...<strong>俺、何かした？</strong>
</div>
</div>

---

<!-- シーン2: 回想 -->

<div class="scene-box">
<div class="scene-icon">💭</div>
<div class="scene-title">1週間前の出来事...</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
田中さん、ちょっと相談があるんですけど...
</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
うん、いいよ〜
<br><br>
（カタカタカタ...PCを見ながら）
</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
あの、クライアントへの提案なんですけど、ちょっと迷ってて...
</div>
</div>

---

<!-- シーン3 -->

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
あーはいはい、それね。<strong>Aプランでいいんじゃない？</strong>
<br><br>
（まだPC見てる）
</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
いや、実はAプランだと予算的に厳しくて、でもBプランだと...
</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
<strong>じゃあBで。</strong>大丈夫大丈夫、なんとかなるって！
</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
...あ、はい。ありがとうございます。<br>
<span style="color: #999;">（話、最後まで聞いてくれなかったな...）</span>
</div>
</div>

---

<!-- 気づき -->

<div class="chara right">
<span class="chara-icon">👩‍💻</span>
<div class="chara-bubble">
<div class="chara-name">同僚（山田）</div>
田中さん...それ、<strong>「聞いてるフリ」</strong>になってない？
</div>
</div>

<div class="chara">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
え？ちゃんと聞いてたよ！アドバイスもしたし！
</div>
</div>

<div class="chara right">
<span class="chara-icon">👩‍💻</span>
<div class="chara-bubble">
<div class="chara-name">同僚（山田）</div>
本当に？<br>
じゃあ聞くけど...<strong>鈴木くんは何に悩んでたの？</strong>
</div>
</div>

<div class="chara">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
えーっと...提案の...Aプランか...Bプランか...
<br><br>
<strong>......あれ？</strong>
</div>
</div>

---

<!-- 問題点 -->

## ❌ 田中さんの問題点

<div class="ng-ok">
<div class="ng-box">
<div class="ng-label">❌ やってしまったこと</div>

- PCを見ながら対応
- 話を最後まで聞かない
- すぐに解決策を提示
- 相手の表情を見ていない

</div>
<div class="ok-box">
<div class="ok-label">✅ 鈴木くんが欲しかったもの</div>

- 顔を見て話を聞いてほしい
- 最後まで状況を説明したい
- 一緒に考えてほしい
- 気持ちを理解してほしい

</div>
</div>

<div class="hint-pop">
<span class="hint-icon">💡</span>
<div>相談する人は「答え」より「聴いてもらうこと」を求めていることが多い！</div>
</div>

---

<!-- 傾聴とは -->

## 👂 「傾聴」ってなに？

<div class="point-box">
<div class="point-title">📖 傾聴（けいちょう）とは</div>
相手の話に<strong>心から耳を傾け</strong>、言葉だけでなく<strong>感情や意図</strong>まで理解しようとすること。
<br><br>
「聞く」= 音が耳に入る（受動的）<br>
「聴く」= 心を傾けて理解する（能動的）← こっち！
</div>

<div class="steps-pop">
<div class="step-item">
<div class="step-num">1</div>
<strong>姿勢</strong><br>
相手に体を向ける
</div>
<div class="step-item">
<div class="step-num">2</div>
<strong>反応</strong><br>
うなずき・相づち
</div>
<div class="step-item">
<div class="step-num">3</div>
<strong>確認</strong><br>
言い換えて確認
</div>
</div>

---

<!-- リベンジ -->

<div class="scene-box">
<div class="scene-icon">✨</div>
<div class="scene-title">田中さん、リベンジ！</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
田中さん、ちょっといいですか...
</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
（PCから手を離して、椅子を向ける）<br><br>
うん、どうした？<strong>座って話そうか。</strong>
</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
<span style="color: #999;">（あれ、なんか雰囲気違う...？）</span><br>
実は、新しい案件の進め方で悩んでて...
</div>
</div>

---

<!-- リベンジ2 -->

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
うんうん。<strong>どんなところが悩みどころ？</strong>
</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
クライアントは早く進めたいって言ってるんですけど、<br>
チーム内ではもう少し調査した方がいいって意見もあって...
</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
なるほど...<strong>スピードと品質のバランスで板挟みになってるんだね。</strong><br>
それは確かに悩むよね。
</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
そうなんです！<strong>わかってもらえて嬉しいです。</strong><br>
それで、自分としては...
</div>
</div>

---

<!-- 変化 -->

## ✨ 何が変わった？

<div class="ng-ok">
<div class="ng-box">
<div class="ng-label">Before 😰</div>

- 作業しながら対応
- 「Aでいいんじゃない？」
- すぐ結論を出す
- 相手の気持ち無視

→ 「もう相談したくない...」

</div>
<div class="ok-box">
<div class="ok-label">After 😊</div>

- 手を止めて向き合う
- 「どんなところが悩み？」
- 相手の言葉を言い換え
- 気持ちに共感

→ 「話を聞いてもらえた！」

</div>
</div>

---

<!-- まとめ -->

<div class="summary-pop">

## 🎧 今日の学び：傾聴力

<div class="summary-key">
「聴く」は最高の承認<br>
答えを出すより、まず受け止める
</div>

</div>

<br>

<div class="steps-pop">
<div class="step-item">
<div class="step-num">✓</div>
手を止める<br>相手に向き合う
</div>
<div class="step-item">
<div class="step-num">✓</div>
言い換える<br>「〜ってこと？」
</div>
<div class="step-item">
<div class="step-num">✓</div>
気持ちを拾う<br>「それは悩むね」
</div>
</div>

---

<!-- 次回予告 -->

<div class="title-pop" style="padding-top: 30px;">

## 🎬 To Be Continued...

</div>

<div class="next-episode">
<div class="next-label">📺 次回予告</div>
<div class="next-title">「なんで分かってくれないの？」<br>〜 伝えたつもりが伝わってない問題 〜</div>
</div>

<div class="chara" style="margin-top: 20px;">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
あの...この前お伝えした件なんですけど...
</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
え、<strong>そんなこと聞いてないけど？</strong>
</div>
</div>
