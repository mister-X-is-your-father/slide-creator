---
marp: true
theme: default
size: 16:9
paginate: false
style: |
  /* ================================ */
  /* レイアウト計算                    */
  /* 画面: 1280x720px                  */
  /* パディング: 30px                  */
  /* 使用可能: 1220x660px              */
  /* ================================ */

  :root {
    --bg: #FFF9E6;
    --primary: #FF6B6B;
    --secondary: #4ECDC4;
    --accent: #FFE66D;
    --purple: #A06CD5;
    --text: #2D3436;
    --text-light: #636E72;
    --white: #FFFFFF;
  }

  section {
    background: var(--bg);
    font-family: "Hiragino Maru Gothic Pro", "Noto Sans JP", sans-serif;
    color: var(--text);
    padding: 30px 40px;
    font-size: 18px;
    line-height: 1.5;
  }

  h1 { color: var(--primary); font-size: 1.6em; margin: 0 0 15px 0; }
  h2 { color: var(--text); font-size: 1.3em; margin: 0 0 12px 0; }

  /* キャラクター - コンパクト版 */
  .chara {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    margin: 8px 0;
  }
  .chara.right { flex-direction: row-reverse; }
  .chara-icon { font-size: 2.2em; flex-shrink: 0; }
  .chara-bubble {
    background: var(--white);
    border-radius: 15px;
    padding: 10px 14px;
    max-width: 80%;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    font-size: 0.95em;
    line-height: 1.5;
  }
  .chara.right .chara-bubble { background: var(--secondary); color: white; }
  .chara-name {
    font-size: 0.65em;
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 3px;
  }
  .chara.right .chara-name { color: var(--white); opacity: 0.9; }
  .chara-bubble strong { color: var(--primary); }
  .chara.right .chara-bubble strong { color: var(--accent); }

  /* タイトル */
  .title-pop {
    text-align: center;
    padding-top: 80px;
  }
  .title-pop .episode {
    background: var(--primary);
    color: white;
    padding: 4px 16px;
    border-radius: 15px;
    font-size: 0.85em;
    display: inline-block;
    margin-bottom: 12px;
  }
  .title-pop h1 {
    font-size: 2.2em;
    margin: 0;
    color: var(--text);
  }
  .title-pop .subtitle {
    color: var(--text-light);
    margin-top: 12px;
    font-size: 1em;
  }
  .title-pop .skill-tag {
    background: var(--accent);
    color: var(--text);
    padding: 6px 20px;
    border-radius: 20px;
    font-weight: 700;
    display: inline-block;
    margin-top: 15px;
    font-size: 0.95em;
  }

  /* シーン説明 - コンパクト */
  .scene-box {
    background: linear-gradient(135deg, var(--purple) 0%, #8E7CC3 100%);
    color: white;
    border-radius: 12px;
    padding: 12px 20px;
    text-align: center;
    margin: 10px 0;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
  }
  .scene-box .scene-icon { font-size: 1.4em; }
  .scene-box .scene-title { font-weight: 700; font-size: 1em; }

  /* ポイントボックス - コンパクト */
  .point-box {
    background: var(--white);
    border-radius: 12px;
    padding: 12px 16px;
    border-left: 4px solid var(--secondary);
    margin: 10px 0;
    font-size: 0.9em;
  }
  .point-title {
    color: var(--secondary);
    font-weight: 700;
    font-size: 1em;
    margin-bottom: 6px;
  }

  /* NGとOK - コンパクト */
  .ng-ok {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 10px 0;
  }
  .ng-box, .ok-box {
    border-radius: 12px;
    padding: 10px 12px;
    font-size: 0.85em;
  }
  .ng-box { background: #FFE5E5; border: 2px solid var(--primary); }
  .ok-box { background: #E5FFF9; border: 2px solid var(--secondary); }
  .ng-label, .ok-label {
    font-weight: 700;
    text-align: center;
    margin-bottom: 6px;
    font-size: 1em;
  }
  .ng-label { color: var(--primary); }
  .ok-label { color: #00A67E; }
  .ng-box ul, .ok-box ul { margin: 0; padding-left: 1.2em; }
  .ng-box li, .ok-box li { margin: 2px 0; }

  /* まとめ - コンパクト */
  .summary-pop {
    background: linear-gradient(135deg, var(--secondary) 0%, #45B7AA 100%);
    border-radius: 15px;
    padding: 15px 20px;
    text-align: center;
    color: white;
  }
  .summary-pop h2 { color: white; margin: 0 0 10px; font-size: 1.2em; }
  .summary-key {
    background: rgba(255,255,255,0.2);
    border-radius: 8px;
    padding: 10px;
    font-size: 1.1em;
    font-weight: 700;
  }

  /* 次回予告 - コンパクト */
  .next-episode {
    background: var(--white);
    border: 2px dashed var(--purple);
    border-radius: 12px;
    padding: 12px 16px;
    text-align: center;
    margin-top: 12px;
  }
  .next-episode .next-label {
    color: var(--purple);
    font-size: 0.8em;
    font-weight: 700;
  }
  .next-episode .next-title {
    font-size: 1em;
    font-weight: 700;
    margin-top: 5px;
    color: var(--text);
  }

  /* ヒント - コンパクト */
  .hint-pop {
    background: var(--accent);
    border-radius: 10px;
    padding: 10px 14px;
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 10px 0;
    font-size: 0.9em;
  }
  .hint-icon { font-size: 1.4em; }

  /* ステップ - コンパクト */
  .steps-pop {
    display: flex;
    gap: 10px;
    margin: 10px 0;
  }
  .step-item {
    flex: 1;
    background: var(--white);
    border-radius: 10px;
    padding: 10px;
    text-align: center;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    font-size: 0.85em;
  }
  .step-num {
    background: var(--primary);
    color: white;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 6px;
    font-weight: 700;
    font-size: 0.9em;
  }
  .step-item:nth-child(2) .step-num { background: var(--secondary); }
  .step-item:nth-child(3) .step-num { background: var(--purple); }

---

<!-- スライド1: タイトル -->
<div class="title-pop">
<span class="episode">コミュ力アップ講座 #01</span>

# 🎧 聞いてるフリしてない？

<div class="subtitle">〜 後輩が話しかけてこなくなった理由 〜</div>
<span class="skill-tag">💡 今日の学び：傾聴力</span>
</div>

---

<!-- スライド2: シーン1 -->

<div class="scene-box">
<span class="scene-icon">🏢</span>
<span class="scene-title">ある日のオフィス</span>
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

<!-- スライド3: 回想1 -->

<div class="scene-box">
<span class="scene-icon">💭</span>
<span class="scene-title">1週間前の出来事...</span>
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
うん、いいよ〜（カタカタカタ...PCを見ながら）
</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
クライアントへの提案なんですけど、AプランかBプランで迷ってて...
</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
あーはいはい。<strong>Aでいいんじゃない？</strong>（まだPC見てる）
</div>
</div>

---

<!-- スライド4: 回想2 -->

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
...あ、はい。ありがとうございます。<span style="color: #999; font-size: 0.9em;">（話、最後まで聞いてくれなかったな...）</span>
</div>
</div>

<div class="hint-pop">
<span class="hint-icon">🤔</span>
<div>田中さんの問題点、わかりますか？</div>
</div>

---

<!-- スライド5: 気づき -->

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
じゃあ聞くけど...<strong>鈴木くんは何に悩んでたの？</strong>
</div>
</div>

<div class="chara">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
えーっと...Aプランか...Bプランか...<strong>......あれ？</strong>
</div>
</div>

---

<!-- スライド6: 問題点 -->

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

<!-- スライド7: 傾聴とは -->

## 👂 「傾聴」ってなに？

<div class="point-box">
<div class="point-title">📖 傾聴（けいちょう）とは</div>
相手の話に<strong>心から耳を傾け</strong>、言葉だけでなく<strong>感情や意図</strong>まで理解しようとすること。<br>
「聞く」= 音が耳に入る（受動的）→「聴く」= 心を傾けて理解する（能動的）
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

<!-- スライド8: リベンジ1 -->

<div class="scene-box">
<span class="scene-icon">✨</span>
<span class="scene-title">田中さん、リベンジ！</span>
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
（PCから手を離して、椅子を向ける）<br>
うん、どうした？<strong>座って話そうか。</strong>
</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
<span style="color: #999; font-size: 0.9em;">（あれ、なんか雰囲気違う...？）</span>
新しい案件の進め方で悩んでて...
</div>
</div>

---

<!-- スライド9: リベンジ2 -->

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
クライアントは早く進めたいって言ってるんですけど、チーム内ではもう少し調査した方がいいって意見もあって...
</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
なるほど...<strong>スピードと品質のバランスで板挟みになってるんだね。</strong>それは確かに悩むよね。
</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
そうなんです！<strong>わかってもらえて嬉しいです。</strong>それで、自分としては...
</div>
</div>

---

<!-- スライド10: 変化 -->

## ✨ 何が変わった？

<div class="ng-ok">
<div class="ng-box">
<div class="ng-label">Before 😰</div>

- 作業しながら対応
- 「Aでいいんじゃない？」
- すぐ結論を出す
- 相手の気持ち無視

→「もう相談したくない...」

</div>
<div class="ok-box">
<div class="ok-label">After 😊</div>

- 手を止めて向き合う
- 「どんなところが悩み？」
- 相手の言葉を言い換え
- 気持ちに共感

→「話を聞いてもらえた！」

</div>
</div>

---

<!-- スライド11: まとめ -->

<div class="summary-pop">

## 🎧 今日の学び：傾聴力

<div class="summary-key">
「聴く」は最高の承認 ─ 答えを出すより、まず受け止める
</div>

</div>

<div class="steps-pop">
<div class="step-item">
<div class="step-num">✓</div>
<strong>手を止める</strong><br>相手に向き合う
</div>
<div class="step-item">
<div class="step-num">✓</div>
<strong>言い換える</strong><br>「〜ってこと？」
</div>
<div class="step-item">
<div class="step-num">✓</div>
<strong>気持ちを拾う</strong><br>「それは悩むね」
</div>
</div>

---

<!-- スライド12: 次回予告 -->

<div class="title-pop" style="padding-top: 20px;">

## 🎬 To Be Continued...

</div>

<div class="next-episode">
<div class="next-label">📺 次回予告</div>
<div class="next-title">「なんで分かってくれないの？」〜 伝えたつもりが伝わってない問題 〜</div>
</div>

<div class="chara" style="margin-top: 12px;">
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
