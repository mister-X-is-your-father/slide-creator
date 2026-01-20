---
marp: true
theme: default
paginate: false
style: |
  /* ================================ */
  /* コミュ力シリーズ - ポップテーマ  */
  /* ================================ */

  :root {
    --bg: #F0F8FF;
    --primary: #FF8C42;
    --secondary: #5D9CEC;
    --accent: #FFCD38;
    --purple: #A06CD5;
    --mint: #26D9A0;
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
    background: linear-gradient(135deg, var(--secondary) 0%, #4A8AD4 100%);
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
  .ng-box { background: #FFE5E5; border: 2px solid #FF6B6B; }
  .ok-box { background: #E5FFF4; border: 2px solid var(--mint); }
  .ng-label, .ok-label {
    font-weight: 700;
    text-align: center;
    margin-bottom: 10px;
    font-size: 1.1em;
  }
  .ng-label { color: #FF6B6B; }
  .ok-label { color: #00A67E; }

  /* まとめ */
  .summary-pop {
    background: linear-gradient(135deg, var(--primary) 0%, #E67932 100%);
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

  /* フレームワーク */
  .framework-box {
    background: var(--white);
    border-radius: 15px;
    padding: 20px;
    border: 3px solid var(--secondary);
    margin: 15px 0;
  }
  .framework-title {
    text-align: center;
    font-size: 1.3em;
    font-weight: 700;
    color: var(--secondary);
    margin-bottom: 15px;
  }
  .framework-steps {
    display: flex;
    gap: 10px;
  }
  .framework-step {
    flex: 1;
    text-align: center;
    padding: 10px;
    background: var(--bg);
    border-radius: 10px;
  }
  .framework-step .step-letter {
    font-size: 1.5em;
    font-weight: 900;
    color: var(--secondary);
  }
  .framework-step .step-word {
    font-size: 0.75em;
    color: var(--text-light);
  }
  .framework-step .step-ja {
    font-weight: 600;
    margin-top: 5px;
  }

  /* メッセージボックス */
  .message-box {
    background: #F8F9FA;
    border: 1px solid #DEE2E6;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
    font-family: monospace;
  }
  .message-header {
    font-size: 0.8em;
    color: var(--text-light);
    margin-bottom: 8px;
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

---

<!-- タイトル -->
<div class="title-pop">
<span class="episode">コミュ力アップ講座 #02</span>

# 📢 伝えたつもり症候群

<div class="subtitle">〜 なんで分かってくれないの？ 〜</div>
<span class="skill-tag">💡 今日の学び：伝える力</span>
</div>

---

<!-- シーン1 -->

<div class="scene-box">
<div class="scene-icon">💬</div>
<div class="scene-title">Slackでのやり取り</div>
</div>

<div class="message-box">
<div class="message-header">📩 鈴木 → 田中さん（3日前）</div>
田中さん、先日の件ですが、クライアントから連絡があって、来週中にミーティングできるか確認してほしいとのことでした。可能でしょうか？
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
ちゃんと連絡したのに...<strong>なんで伝わってないの？</strong>
</div>
</div>

---

<!-- シーン2 -->

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
え、そんなメッセージ来てた？<br>
<strong>「先日の件」って何の件？</strong>
</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
ABC社の提案の件ですよ！<br>
前に話したじゃないですか...
</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
ABC社...？ 俺、今5社くらい並行で見てるから...<br>
あと「来週中」っていつの来週？<strong>3日前の来週ってもう今週では？</strong>
</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
あっ......<span style="color: #999;">（やばい）</span>
</div>
</div>

---

<!-- 問題分析 -->

## 🔍 何が問題だった？

<div class="message-box">
<div class="message-header">❌ 鈴木くんのメッセージ（問題点付き）</div>
田中さん、<span style="color: red;">先日の件</span>ですが、クライアントから連絡があって、<span style="color: red;">来週中</span>にミーティングできるか確認してほしいとのことでした。<span style="color: red;">可能でしょうか？</span>
</div>

<div class="ng-ok">
<div class="ng-box">
<div class="ng-label">❌ 問題点</div>

- **先日の件** → 何の件か不明
- **来週中** → 具体的な日付なし
- **可能でしょうか？** → 何をしてほしいか曖昧

</div>
<div class="ok-box">
<div class="ok-label">📌 相手の状況</div>

- 複数案件を並行対応中
- メッセージは流し読み
- 「後で対応しよう」で忘れる

</div>
</div>

---

<!-- 気づき -->

<div class="chara right">
<span class="chara-icon">👩‍💻</span>
<div class="chara-bubble">
<div class="chara-name">同僚（山田）</div>
鈴木くん、それ<strong>「伝えたつもり症候群」</strong>だね。
</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
伝えたつもり...症候群？
</div>
</div>

<div class="chara right">
<span class="chara-icon">👩‍💻</span>
<div class="chara-bubble">
<div class="chara-name">同僚（山田）</div>
自分は「伝えた」と思ってるけど、<br>
相手には「伝わってない」状態のこと。<br><br>
<strong>伝える ≠ 伝わる</strong> なんだよね。
</div>
</div>

<div class="hint-pop">
<span class="hint-icon">💡</span>
<div>コミュニケーションの責任は「発信者」にある！</div>
</div>

---

<!-- フレームワーク -->

## 🛠️ 伝わるメッセージの型

<div class="framework-box">
<div class="framework-title">PREP法</div>
<div class="framework-steps">
<div class="framework-step">
<div class="step-letter">P</div>
<div class="step-word">Point</div>
<div class="step-ja">結論</div>
</div>
<div class="framework-step">
<div class="step-letter">R</div>
<div class="step-word">Reason</div>
<div class="step-ja">理由</div>
</div>
<div class="framework-step">
<div class="step-letter">E</div>
<div class="step-word">Example</div>
<div class="step-ja">具体例</div>
</div>
<div class="framework-step">
<div class="step-letter">P</div>
<div class="step-word">Point</div>
<div class="step-ja">結論</div>
</div>
</div>
</div>

<div class="point-box">
<div class="point-title">✨ ビジネスメッセージの鉄則</div>

1. **結論ファースト** - 最初に要点を伝える
2. **5W1H** - いつ・どこで・誰が・何を・なぜ・どうやって
3. **アクション明確** - 相手に何をしてほしいか

</div>

---

<!-- リベンジ -->

<div class="scene-box">
<div class="scene-icon">✨</div>
<div class="scene-title">鈴木くん、リベンジ！</div>
</div>

<div class="message-box">
<div class="message-header">✅ 改善後のメッセージ</div>
<strong>【要確認】ABC社MTG日程の件</strong><br><br>
田中さん<br><br>
<strong>ABC社の提案MTG</strong>について、日程調整をお願いしたいです。<br><br>
■ 依頼内容<br>
<strong>1/25(木)〜1/31(水)</strong>の間で、1時間のMTG可能な日時を教えてください。<br><br>
■ 背景<br>
先方担当の佐藤様より「来週中に一度打ち合わせしたい」とご連絡がありました。<br><br>
<strong>1/23(火) 18:00まで</strong>にご回答いただけると助かります。
</div>

---

<!-- 変化 -->

## ✨ 何が変わった？

<div class="ng-ok">
<div class="ng-box">
<div class="ng-label">Before 😰</div>

- 件名なし
- 「先日の件」（曖昧）
- 「来週中」（いつ？）
- 「可能でしょうか？」（何を？）
- 回答期限なし

</div>
<div class="ok-box">
<div class="ok-label">After 😊</div>

- 件名で要件がわかる
- 案件名を明記
- 具体的な日付範囲
- アクションが明確
- 回答期限あり

</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
お、これなら<strong>5秒で理解できる</strong>し、すぐ返信できるわ。<br>
1/26と1/30なら空いてるよ！
</div>
</div>

---

<!-- まとめ -->

<div class="summary-pop">

## 📢 今日の学び：伝える力

<div class="summary-key">
「伝えた」と「伝わった」は違う<br>
相手が5秒で理解できるか？
</div>

</div>

<br>

<div class="steps-pop">
<div class="step-item">
<div class="step-num">1</div>
<strong>結論ファースト</strong><br>
最初に要点を
</div>
<div class="step-item">
<div class="step-num">2</div>
<strong>具体的に</strong><br>
5W1Hを明確に
</div>
<div class="step-item">
<div class="step-num">3</div>
<strong>アクション</strong><br>
何をいつまでに
</div>
</div>

---

<!-- 次回予告 -->

<div class="title-pop" style="padding-top: 30px;">

## 🎬 To Be Continued...

</div>

<div class="next-episode">
<div class="next-label">📺 次回予告</div>
<div class="next-title">「で、結局どうしたいの？」<br>〜 質問されると固まる問題 〜</div>
</div>

<div class="chara" style="margin-top: 20px;">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
鈴木くん、この案件どう思う？
</div>
</div>

<div class="chara right">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
え、えーっと...<strong>どう、と言われましても...</strong>
</div>
</div>
