---
marp: true
theme: default
paginate: false
size: 16:9
style: |
  /* ================================ */
  /* コミュ力シリーズ - ポップテーマ  */
  /* Episode 05: フィードバック力    */
  /* ================================ */
  /* レイアウト計算
   * 画面: 1280x720px (16:9)
   * パディング: 30px
   * 使用可能: 1220x660px
   */

  :root {
    --bg: #F0FFF4;
    --primary: #00B894;
    --secondary: #00CEC9;
    --accent: #FDCB6E;
    --coral: #FF7675;
    --purple: #A29BFE;
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
  .chara.right .chara-bubble { background: var(--primary); color: white; }
  .chara-name {
    font-size: 0.7em;
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 3px;
  }
  .chara.right .chara-name { color: var(--white); opacity: 0.9; }
  .chara-bubble strong { color: var(--coral); }
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
    font-size: 2.1em;
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
    background: linear-gradient(135deg, var(--primary) 0%, #00A085 100%);
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
    font-size: 0.95em;
  }
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
  .ok-box { background: #E0FFF4; border: 2px solid var(--primary); }
  .ng-box ul, .ok-box ul { margin: 5px 0; padding-left: 18px; }
  .ng-box li, .ok-box li { margin: 2px 0; }
  .ng-label, .ok-label {
    font-weight: 700;
    text-align: center;
    margin-bottom: 6px;
    font-size: 1em;
  }
  .ng-label { color: var(--coral); }
  .ok-label { color: var(--primary); }

  /* まとめ */
  .summary-pop {
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
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

  /* 完結 */
  .finale {
    background: var(--white);
    border: 2px solid var(--accent);
    border-radius: 12px;
    padding: 12px 15px;
    text-align: center;
    margin-top: 12px;
  }
  .finale .finale-label {
    color: var(--primary);
    font-size: 0.8em;
    font-weight: 700;
  }
  .finale .finale-title {
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

  /* フレームワーク */
  .framework-box {
    background: var(--white);
    border-radius: 12px;
    padding: 12px 15px;
    border: 2px solid var(--primary);
    margin: 10px 0;
  }
  .framework-title {
    text-align: center;
    font-size: 1.15em;
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 10px;
  }
  .framework-steps {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
  }
  .framework-step {
    text-align: center;
    padding: 8px;
    background: var(--bg);
    border-radius: 8px;
  }
  .framework-step .step-letter {
    font-size: 1.3em;
    font-weight: 900;
    color: var(--primary);
  }
  .framework-step .step-ja {
    font-size: 0.8em;
    font-weight: 600;
    margin-top: 3px;
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
  .step-item:nth-child(3) .step-num { background: var(--purple); }

  /* スキル一覧 */
  .skills-recap {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 8px;
    margin: 10px 0;
  }
  .skill-item {
    background: var(--white);
    border-radius: 10px;
    padding: 10px 8px;
    text-align: center;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  }
  .skill-item .skill-num {
    font-size: 0.7em;
    color: var(--text-light);
  }
  .skill-item .skill-icon {
    font-size: 1.5em;
    margin: 5px 0;
  }
  .skill-item .skill-name {
    font-size: 0.8em;
    font-weight: 600;
  }

---

<!-- タイトル -->
<div class="title-pop">
<span class="episode">コミュ力アップ講座 #05（最終回）</span>

# 🗣️ なんでできないの？
<div class="subtitle">〜 言い方ひとつで関係が壊れる問題 〜</div>
<span class="skill-tag">💡 今日の学び：フィードバック力</span>
</div>

---

<!-- シーン1 -->

<div class="scene-box">
<div class="scene-icon">📄</div>
<div class="scene-title">資料チェックにて</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
鈴木くん、この資料のミス、<strong>3回目</strong>だよね？
</div>
</div>

<div class="chara">
<span class="chara-icon">😰</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
す、すみません...
</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
<strong>なんで同じミスするの？</strong> ちゃんと確認してる？
</div>
</div>

<div class="chara">
<span class="chara-icon">😰</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
確認は...してたつもりなんですけど... <span style="color: #999;">（もう何も言えない...）</span>
</div>
</div>

---

<!-- シーン2 -->

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
「つもり」じゃダメなんだよ。 <strong>もっとちゃんとやって。</strong>
</div>
</div>

<div class="chara">
<span class="chara-icon">😢</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
はい...すみません... <span style="color: #999;">（田中さん、最近怖い...もう相談したくないな...）</span>
</div>
</div>

<div class="hint-pop">
<span class="hint-icon">😱</span>
<div>田中さんの言い方、何が問題だったか分かりますか？</div>
</div>

---

<!-- 問題点 -->

## 😰 田中さんの問題点

<div class="ng-ok">
<div class="ng-box">
<div class="ng-label">❌ 田中さんがやったこと</div>

- 「なんで？」で責める
- 過去のミスを持ち出す
- 「ちゃんとやって」と曖昧に指示
- 相手を萎縮させる

</div>
<div class="ok-box">
<div class="ok-label">💭 鈴木くんへの影響</div>

- 怖くて何も言えない
- 「どうせまた怒られる」と萎縮
- 相談・報告を避けるようになる
- 信頼関係が壊れる

</div>
</div>

<div class="point-box">
<div class="point-title">⚠️ 「なんで？」は危険ワード</div>
「なんで？」と聞かれると、人は<strong>言い訳モード</strong>になる。<br>
改善ではなく、防御に意識が向いてしまう。
</div>

---

<!-- フィードバックとは -->

## 💬 良いフィードバックとは？

<div class="framework-box">
<div class="framework-title">DESC法（デスク法）</div>
<div class="framework-steps">
<div class="framework-step">
<div class="step-letter">D</div>
<div class="step-ja">描写する</div>
<span style="font-size:0.7em;color:#666;">Describe</span>
</div>
<div class="framework-step">
<div class="step-letter">E</div>
<div class="step-ja">説明する</div>
<span style="font-size:0.7em;color:#666;">Express</span>
</div>
<div class="framework-step">
<div class="step-letter">S</div>
<div class="step-ja">提案する</div>
<span style="font-size:0.7em;color:#666;">Suggest</span>
</div>
<div class="framework-step">
<div class="step-letter">C</div>
<div class="step-ja">選択させる</div>
<span style="font-size:0.7em;color:#666;">Choose</span>
</div>
</div>
</div>

<div class="hint-pop">
<span class="hint-icon">💡</span>
<div>「人」ではなく「事実」にフォーカスする！</div>
</div>

---

<!-- リベンジ -->

<div class="scene-box">
<div class="scene-icon">✨</div>
<div class="scene-title">田中さん、リベンジ！</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
鈴木くん、ちょっといい？ <strong>この資料の数字、元データと違ってるみたいなんだけど...</strong>
</div>
</div>

<div class="chara">
<span class="chara-icon">😳</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
あ、本当ですね...すみません。
</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
似たようなミスが前にもあったから、<strong>何か確認しにくい原因があるのかなと思って。</strong>
</div>
</div>

---

<!-- リベンジ2 -->

<div class="chara">
<span class="chara-icon">🧑‍💻</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
実は...データの転記作業が複雑で、<strong>どこをチェックすればいいか迷うことがあって...</strong>
</div>
</div>

<div class="chara right">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
なるほど。じゃあ<strong>チェックリストを一緒に作ってみない？</strong> それで確認漏れを防げるかも。
</div>
</div>

<div class="chara">
<span class="chara-icon">😊</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
ぜひお願いします！ <strong>ありがとうございます！</strong>
</div>
</div>

---

<!-- DESC適用 -->

## ✅ DESC法を適用すると

<div class="ng-ok">
<div class="ng-box">
<div class="ng-label">❌ Before</div>

**D**: (なし)<br>
**E**: 「なんで？」「ちゃんとやって」<br>
**S**: (なし)<br>
**C**: (なし)

→ 責めるだけで終わり

</div>
<div class="ok-box">
<div class="ok-label">✅ After</div>

**D**: 「数字が違ってる」（事実）<br>
**E**: 「確認しにくい原因があるのかな」<br>
**S**: 「チェックリスト作ってみない？」<br>
**C**: 「どうする？」

→ 一緒に改善策を考える

</div>
</div>

---

<!-- フレーズ集 -->

## 🗣️ フィードバックフレーズ集

<div class="ng-ok">
<div class="ng-box">
<div class="ng-label">❌ 避けたい言い方</div>

「なんで？」「どうして？」<br>
「何回言ったら分かるの？」<br>
「ちゃんとやって」<br>
「前も言ったよね？」<br>
「君って〇〇だよね」（人格否定）

</div>
<div class="ok-box">
<div class="ok-label">✅ 使いたい言い方</div>

「〇〇になってるね」（事実描写）<br>
「何か困ってることある？」<br>
「〇〇してみるのはどう？」<br>
「一緒に考えよう」<br>
「〇〇すると良くなりそう」

</div>
</div>

<div class="hint-pop">
<span class="hint-icon">💡</span>
<div>「You」メッセージより「I」メッセージ！<br>「君が〜」→「私は〇〇と感じた」</div>
</div>

---

<!-- まとめ -->

<div class="summary-pop">

## 🗣️ 今日の学び：フィードバック力
<div class="summary-key">
「人」を責めず「事実」を伝える ― DESC法で建設的なフィードバックを
</div>

</div>

<div class="steps-pop">
<div class="step-item">
<div class="step-num">D</div>
<strong>描写</strong><br>
事実を伝える
</div>
<div class="step-item">
<div class="step-num">E</div>
<strong>説明</strong><br>
影響を説明
</div>
<div class="step-item">
<div class="step-num">S</div>
<strong>提案</strong><br>
改善策を提案
</div>
</div>

---

<!-- シリーズまとめ -->

## 🎓 コミュ力アップ講座 完結！

<div class="skills-recap">
<div class="skill-item">
<div class="skill-num">#01</div>
<div class="skill-icon">🎧</div>
<div class="skill-name">傾聴力</div>
</div>
<div class="skill-item">
<div class="skill-num">#02</div>
<div class="skill-icon">📢</div>
<div class="skill-name">伝える力</div>
</div>
<div class="skill-item">
<div class="skill-num">#03</div>
<div class="skill-icon">❓</div>
<div class="skill-name">質問力</div>
</div>
<div class="skill-item">
<div class="skill-num">#04</div>
<div class="skill-icon">💖</div>
<div class="skill-name">共感力</div>
</div>
<div class="skill-item">
<div class="skill-num">#05</div>
<div class="skill-icon">🗣️</div>
<div class="skill-name">フィードバック</div>
</div>
</div>

<div class="point-box">
<div class="point-title">🔑 5つのスキルの共通点</div>

**「相手の立場に立つ」** ことがすべての基本。<br>
自分が言いたいことより、相手がどう受け取るかを考える。

</div>

---

<!-- フィナーレ -->

<div class="title-pop" style="padding-top: 15px;">

## 🎬 Fin.
</div>

<div class="finale">
<div class="finale-label">📚 全5回シリーズ 完結</div>
<div class="finale-title">田中さんと鈴木くんは、最高のチームになりましたとさ。めでたしめでたし。</div>
</div>

<div class="chara" style="margin-top: 10px;">
<span class="chara-icon">👨‍💼</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
鈴木くん、成長したな〜
</div>
</div>

<div class="chara right">
<span class="chara-icon">😊</span>
<div class="chara-bubble">
<div class="chara-name">後輩（鈴木）</div>
田中さんも変わりましたよ！ <strong>最初は怖かったのに...</strong>
</div>
</div>

<div class="chara">
<span class="chara-icon">😅</span>
<div class="chara-bubble">
<div class="chara-name">先輩（田中）</div>
...(反省)
</div>
</div>
