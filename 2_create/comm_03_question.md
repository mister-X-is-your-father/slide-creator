---
marp: true
theme: default
paginate: false
size: 16:9
style: |
  /* ================================ */
  /* コミュ力シリーズ - ポップテーマ  */
  /* Episode 03: 質問力              */
  /* ================================ */
  /* レイアウト計算
   * 画面: 1280x720px (16:9)
   * パディング: 30px
   * 使用可能: 1220x660px
   */

  :root {
    --bg: #FFF5F5;
    --primary: #E056FD;
    --secondary: #686DE0;
    --accent: #FFBE76;
    --mint: #55E6C1;
    --coral: #FF7675;
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

  h1 { color: var(--primary); font-size: 1.7em; margin: 0 0 10px; }
  h2 { color: var(--text); font-size: 1.25em; margin: 0 0 10px; }

  /* キャラクター */
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
    max-width: 85%;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    position: relative;
    line-height: 1.5;
    font-size: 0.95em;
  }
  .chara.right .chara-bubble { background: var(--secondary); color: white; }
  .chara-name {
    font-size: 0.7em;
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
    padding-top: 40px;
  }
  .title-pop .episode {
    background: var(--primary);
    color: white;
    padding: 4px 16px;
    border-radius: 15px;
    font-size: 0.85em;
    display: inline-block;
    margin-bottom: 10px;
  }
  .title-pop h1 {
    font-size: 2.2em;
    margin: 0;
    color: var(--text);
  }
  .title-pop .subtitle {
    color: var(--text-light);
    margin-top: 10px;
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

  /* シーン説明 */
  .scene-box {
    background: linear-gradient(135deg, var(--primary) 0%, #C44BD9 100%);
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
  .scene-box .scene-icon { font-size: 1.5em; }
  .scene-box .scene-title { font-weight: 700; font-size: 1em; }

  /* ポイントボックス */
  .point-box {
    background: var(--white);
    border-radius: 12px;
    padding: 12px 15px;
    border-left: 4px solid var(--secondary);
    margin: 10px 0;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  }
  .point-box ul { margin: 5px 0; padding-left: 20px; }
  .point-box li { margin: 3px 0; }
  .point-title {
    color: var(--secondary);
    font-weight: 700;
    font-size: 1em;
    margin-bottom: 8px;
  }

  /* NGとOK */
  .ng-ok {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 10px 0;
  }
  .ng-box, .ok-box {
    border-radius: 12px;
    padding: 10px 12px;
    font-size: 0.9em;
  }
  .ng-box { background: #FFE5E5; border: 2px solid var(--coral); }
  .ok-box { background: #E5FFF4; border: 2px solid var(--mint); }
  .ng-box ul, .ok-box ul { margin: 5px 0; padding-left: 18px; }
  .ng-box li, .ok-box li { margin: 2px 0; }
  .ng-label, .ok-label {
    font-weight: 700;
    text-align: center;
    margin-bottom: 6px;
    font-size: 1em;
  }
  .ng-label { color: var(--coral); }
  .ok-label { color: #00A67E; }

  /* まとめ */
  .summary-pop {
    background: linear-gradient(135deg, var(--secondary) 0%, #5758BB 100%);
    border-radius: 15px;
    padding: 18px;
    text-align: center;
    color: white;
  }
  .summary-pop h2 { color: white; margin: 0 0 10px; font-size: 1.2em; }
  .summary-key {
    background: rgba(255,255,255,0.2);
    border-radius: 8px;
    padding: 12px;
    font-size: 1.15em;
    font-weight: 700;
  }

  /* 次回予告 */
  .next-episode {
    background: var(--white);
    border: 2px dashed var(--primary);
    border-radius: 12px;
    padding: 12px 15px;
    text-align: center;
    margin-top: 12px;
  }
  .next-episode .next-label {
    color: var(--primary);
    font-size: 0.8em;
    font-weight: 700;
  }
  .next-episode .next-title {
    font-size: 1.05em;
    font-weight: 700;
    margin-top: 5px;
    color: var(--text);
  }

  /* ヒント */
  .hint-pop {
    background: var(--accent);
    border-radius: 10px;
    padding: 10px 14px;
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 10px 0;
    font-size: 0.95em;
  }
  .hint-icon { font-size: 1.5em; }

  /* 思考プロセス */
  .think-process {
    display: flex;
    align-items: center;
    gap: 8px;
    margin: 10px 0;
    flex-wrap: wrap;
  }
  .think-step {
    background: var(--white);
    border-radius: 8px;
    padding: 8px 12px;
    border: 2px solid var(--secondary);
    font-size: 0.85em;
  }
  .think-arrow {
    color: var(--secondary);
    font-size: 1.1em;
  }

  /* 質問タイプ */
  .question-types {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 10px 0;
  }
  .q-type {
    background: var(--white);
    border-radius: 12px;
    padding: 10px 12px;
    border: 2px solid var(--primary);
    font-size: 0.9em;
  }
  .q-type-title {
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 5px;
  }
  .q-type-example {
    font-size: 0.85em;
    color: var(--text-light);
    font-style: italic;
  }

  /* ステップ */
  .steps-pop {
    display: flex;
    gap: 12px;
    margin: 10px 0;
  }
  .step-item {
    flex: 1;
    background: var(--white);
    border-radius: 12px;
    padding: 12px 10px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    font-size: 0.9em;
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
    margin: 0 auto 8px;
    font-weight: 700;
    font-size: 0.9em;
  }
  .step-item:nth-child(2) .step-num { background: var(--secondary); }
  .step-item:nth-child(3) .step-num { background: var(--mint); }

---

<!-- タイトル -->
<div class="title-pop">
<span class="episode">コミュ力アップ講座 #03</span>

# ❓ 質問されると固まる問題
<div class="subtitle">〜 で、結局どうしたいの？ 〜</div>
<span class="skill-tag">💡 今日の学び：質問力</span>
</div>

---

<!-- シーン1 -->

<div class="scene-box">
<div class="scene-icon">🏢</div>
<div class="scene-title">企画会議にて</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
鈴木くん、この企画どう思う？
</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
え、えーっと...<strong>いいと思います。</strong>
</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
...どこが？
</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
えっと...全体的に...<span style="color: #999;">（やばい、何も考えてなかった）</span>
</div>
</div>

---

<!-- シーン2 -->

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
鈴木くんは、<strong>この企画の課題</strong>は何だと思う？
</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
課題...ですか... <strong>うーん...特に思いつかないです...</strong>
</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
じゃあ逆に、<strong>この企画を成功させるには何が必要？</strong>
</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
...必要なこと... <span style="color: #999;">（頭が真っ白...）</span>
</div>
</div>

---

<!-- 問題 -->

## 😰 なぜ固まってしまうのか？

<div class="ng-ok">
<div class="ng-box">
<div class="ng-label">🧠 鈴木くんの頭の中</div>

- 「正解」を探してしまう
- 間違ったら恥ずかしい
- 何を聞かれてるか分からない
- 考えがまとまってない

</div>
<div class="ok-box">
<div class="ok-label">💡 実は...</div>

- ビジネスに「正解」はない
- 意見を求められている
- 考えるプロセスを見せればOK
- 「分からない」も答えの一つ

</div>
</div>

<div class="hint-pop">
<span class="hint-icon">💡</span>
<div>質問への回答は「正解」じゃなく「意見」でいい！</div>
</div>

---

<!-- 思考プロセス -->

## 🧠 質問に答える「型」

<div class="point-box">
<div class="point-title">📝 「意見」を作る3ステップ</div>

**質問：「この企画どう思う？」**

</div>

<div class="think-process">
<div class="think-step">①<strong>観点</strong>を決める<br><span style="font-size:0.8em;color:#666;">→ターゲット視点で見ると</span></div>
<span class="think-arrow">→</span>
<div class="think-step">②<strong>評価</strong>を述べる<br><span style="font-size:0.8em;color:#666;">→ニーズと合ってると思う</span></div>
<span class="think-arrow">→</span>
<div class="think-step">③<strong>理由</strong>を添える<br><span style="font-size:0.8em;color:#666;">→なぜなら〜だから</span></div>
</div>

<div class="chara">
<span class="chara-icon">✨</span>
<div class="chara-bubble">
<strong>例）</strong>「ターゲット視点で見ると、ニーズに合っていると思います。<br>
なぜなら、20代は○○を重視する傾向があるからです。」
</div>
</div>

---

<!-- リベンジ -->

<div class="scene-box">
<div class="scene-icon">✨</div>
<div class="scene-title">鈴木くん、リベンジ！</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
鈴木くん、この企画どう思う？
</div>
</div>

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
<strong>コスト面で見ると</strong>、少し気になる点があります。広告費が想定より高めに見えるんですが、<strong>これはテスト期間を含めた数字ですか？</strong>
</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
お、いい視点だね！実はそこまだ詰められてなくて...<strong>一緒に考えてくれる？</strong>
</div>
</div>

---

<!-- 質問力 -->

## 🎯 「質問する力」も大事

<div class="question-types">
<div class="q-type">
<div class="q-type-title">🔓 オープン質問</div>
答えが自由な質問<br>
<div class="q-type-example">「どう思いますか？」<br>「何が課題ですか？」</div>
</div>
<div class="q-type">
<div class="q-type-title">🔒 クローズド質問</div>
Yes/Noで答える質問<br>
<div class="q-type-example">「これでいいですか？」<br>「〇〇で合ってます？」</div>
</div>
</div>

<div class="point-box">
<div class="point-title">💎 良い質問のコツ</div>

- **曖昧なら確認する**：「〇〇という理解で合ってますか？」
- **深掘りする**：「具体的にはどういうことですか？」
- **仮説を持つ**：「〇〇が原因かと思うのですが、どうでしょう？」

</div>

---

<!-- 使えるフレーズ -->

## 🗣️ 今日から使えるフレーズ集

<div class="ng-ok">
<div class="ng-box">
<div class="ng-label">❌ 固まるパターン</div>

「えーっと...」<br>
「特にないです...」<br>
「分かりません...」<br>
（沈黙）

</div>
<div class="ok-box">
<div class="ok-label">✅ 切り抜けるフレーズ</div>

「〇〇の観点で言うと...」<br>
「まだ整理できてないんですが...」<br>
「確認なんですが、〇〇ということですか？」<br>
「少し考える時間をもらえますか？」

</div>
</div>

<div class="hint-pop">
<span class="hint-icon">💡</span>
<div>「考え中」も立派な回答！沈黙より「考えています」と言おう</div>
</div>

---

<!-- まとめ -->

<div class="summary-pop">

## ❓ 今日の学び：質問力
<div class="summary-key">
「正解」より「意見」を言う ― 観点 → 評価 → 理由 の型で話す
</div>

</div>

<div class="steps-pop">
<div class="step-item">
<div class="step-num">1</div>
<strong>観点を決める</strong><br>
何の視点で見るか
</div>
<div class="step-item">
<div class="step-num">2</div>
<strong>評価を述べる</strong><br>
良い/課題がある
</div>
<div class="step-item">
<div class="step-num">3</div>
<strong>理由を添える</strong><br>
なぜそう思うか
</div>
</div>

---

<!-- 次回予告 -->

<div class="title-pop" style="padding-top: 20px;">

## 🎬 To Be Continued...
</div>

<div class="next-episode">
<div class="next-label">📺 次回予告</div>
<div class="next-title">「そういうことじゃないんだけど...」〜 相手の気持ちが分からない問題 〜</div>
</div>

<div class="chara" style="margin-top: 10px;">
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
<strong>じゃあ、こうすればいいんじゃないですか？</strong>
</div>
</div>

<div class="chara">
<span class="chara-icon">😢</span>
<div class="chara-bubble">
<div class="chara-name">同僚（山田）</div>
...そういうことじゃないんだけど...
</div>
</div>
