---
marp: true
theme: default
paginate: false
style: |
  /* ================================ */
  /* ミステリー会話スライド           */
  /* ================================ */

  :root {
    --bg-dark: #1a1a2e;
    --bg-card: #16213e;
    --accent: #e94560;
    --accent2: #0f3460;
    --gold: #f1c40f;
    --text: #eaeaea;
    --text-dim: #a0a0a0;
    --success: #2ecc71;
    --warning: #f39c12;
  }

  section {
    background: var(--bg-dark);
    color: var(--text);
    font-family: "Noto Sans JP", sans-serif;
    padding: 30px 40px;
  }

  h1, h2 { color: var(--gold); }

  /* ================================ */
  /* タイトルスライド                 */
  /* ================================ */

  .title-mystery {
    text-align: center;
    padding-top: 60px;
  }
  .title-mystery h1 {
    font-size: 2.5em;
    color: var(--accent);
    text-shadow: 0 0 20px var(--accent);
    margin-bottom: 0.3em;
  }
  .title-mystery .subtitle {
    font-size: 1.2em;
    color: var(--gold);
    margin-bottom: 1.5em;
  }
  .title-mystery .tagline {
    font-size: 0.95em;
    color: var(--text-dim);
  }

  /* ================================ */
  /* キャラクター定義                 */
  /* ================================ */

  .character-intro {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: 20px;
  }
  .character-card {
    background: var(--bg-card);
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    border: 2px solid var(--accent2);
  }
  .character-card.detective { border-color: var(--gold); }
  .character-card.victim { border-color: var(--accent); }
  .character-icon { font-size: 3em; margin-bottom: 10px; }
  .character-name { font-weight: 700; font-size: 1.1em; color: var(--gold); }
  .character-role { font-size: 0.85em; color: var(--text-dim); margin-top: 5px; }

  /* ================================ */
  /* 会話バブル                       */
  /* ================================ */

  .dialogue {
    display: flex;
    align-items: flex-start;
    gap: 15px;
    margin: 15px 0;
  }
  .dialogue.right {
    flex-direction: row-reverse;
  }
  .speaker-icon {
    font-size: 2.5em;
    flex-shrink: 0;
    filter: drop-shadow(0 0 10px rgba(255,255,255,0.3));
  }
  .speech-bubble {
    background: var(--bg-card);
    border-radius: 15px;
    padding: 15px 20px;
    max-width: 75%;
    position: relative;
    border: 1px solid var(--accent2);
    line-height: 1.6;
  }
  .dialogue.right .speech-bubble {
    background: var(--accent2);
  }
  .speaker-name {
    font-size: 0.75em;
    color: var(--gold);
    margin-bottom: 5px;
    font-weight: 600;
  }
  .speech-bubble strong {
    color: var(--accent);
  }
  .speech-bubble em {
    color: var(--gold);
    font-style: normal;
  }

  /* ================================ */
  /* 証拠カード                       */
  /* ================================ */

  .evidence-card {
    background: var(--bg-card);
    border: 2px solid var(--gold);
    border-radius: 12px;
    padding: 20px;
    margin: 15px 0;
    position: relative;
  }
  .evidence-card::before {
    content: "EVIDENCE";
    position: absolute;
    top: -12px;
    left: 20px;
    background: var(--gold);
    color: var(--bg-dark);
    padding: 2px 12px;
    border-radius: 4px;
    font-size: 0.75em;
    font-weight: 700;
  }
  .evidence-title {
    color: var(--gold);
    font-weight: 700;
    margin-bottom: 10px;
    font-size: 1.1em;
  }
  .evidence-content {
    font-size: 0.95em;
  }

  /* ================================ */
  /* 真相解明                         */
  /* ================================ */

  .revelation {
    background: linear-gradient(135deg, var(--accent) 0%, #c0392b 100%);
    border-radius: 15px;
    padding: 25px;
    text-align: center;
    margin: 20px 0;
    box-shadow: 0 0 30px rgba(233, 69, 96, 0.5);
  }
  .revelation h2 {
    color: white;
    margin: 0 0 15px;
    font-size: 1.5em;
  }
  .revelation p {
    color: white;
    font-size: 1.1em;
    margin: 0;
  }

  /* ================================ */
  /* 学びボックス                     */
  /* ================================ */

  .learning-box {
    background: linear-gradient(135deg, var(--accent2) 0%, #1a3a5c 100%);
    border-radius: 15px;
    padding: 20px;
    border-left: 5px solid var(--gold);
    margin: 15px 0;
  }
  .learning-title {
    color: var(--gold);
    font-weight: 700;
    font-size: 1.1em;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .learning-content {
    font-size: 0.95em;
    line-height: 1.6;
  }

  /* ================================ */
  /* タイムライン                     */
  /* ================================ */

  .case-timeline {
    position: relative;
    padding-left: 30px;
    margin: 20px 0;
  }
  .case-timeline::before {
    content: "";
    position: absolute;
    left: 8px;
    top: 0;
    bottom: 0;
    width: 3px;
    background: var(--accent);
  }
  .timeline-event {
    position: relative;
    margin-bottom: 15px;
    padding-left: 20px;
  }
  .timeline-event::before {
    content: "";
    position: absolute;
    left: -26px;
    top: 5px;
    width: 12px;
    height: 12px;
    background: var(--accent);
    border-radius: 50%;
    border: 3px solid var(--bg-dark);
  }
  .timeline-date {
    color: var(--gold);
    font-size: 0.85em;
    font-weight: 600;
  }
  .timeline-title {
    font-weight: 600;
    margin: 3px 0;
  }
  .timeline-desc {
    font-size: 0.85em;
    color: var(--text-dim);
  }

  /* ================================ */
  /* 容疑者プロファイル               */
  /* ================================ */

  .suspect-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
  }
  .suspect-card {
    background: var(--bg-card);
    border-radius: 12px;
    padding: 15px;
    text-align: center;
    border: 2px solid transparent;
    transition: all 0.3s;
  }
  .suspect-card.guilty {
    border-color: var(--accent);
    box-shadow: 0 0 15px rgba(233, 69, 96, 0.5);
  }
  .suspect-icon { font-size: 2.5em; margin-bottom: 8px; }
  .suspect-name { font-weight: 700; color: var(--gold); }
  .suspect-title { font-size: 0.8em; color: var(--text-dim); }
  .suspect-status {
    margin-top: 8px;
    font-size: 0.75em;
    padding: 3px 10px;
    border-radius: 10px;
    display: inline-block;
  }
  .status-innocent { background: var(--success); color: white; }
  .status-guilty { background: var(--accent); color: white; }

  /* ================================ */
  /* 数字ハイライト                   */
  /* ================================ */

  .stats-mystery {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
    margin: 20px 0;
  }
  .stat-item {
    background: var(--bg-card);
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    border: 1px solid var(--accent2);
  }
  .stat-value {
    font-size: 2.5em;
    font-weight: 700;
    color: var(--accent);
  }
  .stat-label {
    font-size: 0.9em;
    color: var(--text-dim);
    margin-top: 5px;
  }

  /* ================================ */
  /* 伏線・ヒント                     */
  /* ================================ */

  .hint-box {
    background: var(--bg-card);
    border: 2px dashed var(--warning);
    border-radius: 12px;
    padding: 15px;
    margin: 10px 0;
    display: flex;
    align-items: center;
    gap: 15px;
  }
  .hint-icon {
    font-size: 2em;
    flex-shrink: 0;
  }
  .hint-text {
    font-size: 0.95em;
    line-height: 1.5;
  }

  /* ================================ */
  /* セクション区切り                 */
  /* ================================ */

  .section-break {
    text-align: center;
    padding: 80px 0;
  }
  .section-break h1 {
    font-size: 2.5em;
    color: var(--accent);
    text-shadow: 0 0 30px var(--accent);
  }
  .section-break .chapter {
    font-size: 1em;
    color: var(--gold);
    margin-bottom: 10px;
  }

  /* ================================ */
  /* まとめスライド                   */
  /* ================================ */

  .summary-mystery {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
  }
  .summary-item {
    background: var(--bg-card);
    border-radius: 12px;
    padding: 15px;
    border-left: 4px solid var(--gold);
  }
  .summary-num {
    font-size: 1.5em;
    font-weight: 700;
    color: var(--accent);
    margin-right: 10px;
  }
  .summary-title {
    font-weight: 600;
    color: var(--gold);
    margin-bottom: 5px;
  }
  .summary-desc {
    font-size: 0.85em;
    color: var(--text-dim);
  }

---

<!-- スライド1: タイトル -->
<div class="title-mystery">

# 🔍 消えた10億円の謎

<div class="subtitle">〜 優秀なチームはなぜ失敗したのか 〜</div>

<div class="tagline">認知バイアスが引き起こした連続殺人...ならぬ、連続判断ミス事件</div>

</div>

---

<!-- スライド2: プロローグ -->

## 📁 Case File #2024-CB

<div class="stats-mystery">
<div class="stat-item">
<div class="stat-value">10億円</div>
<div class="stat-label">消失した投資額</div>
</div>
<div class="stat-item">
<div class="stat-value">18ヶ月</div>
<div class="stat-label">プロジェクト期間</div>
</div>
<div class="stat-item">
<div class="stat-value">12人</div>
<div class="stat-label">精鋭チーム</div>
</div>
</div>

<div class="hint-box">
<span class="hint-icon">🤔</span>
<div class="hint-text">
エリート揃いのチームが、なぜ大失敗したのか？<br>
その答えは...誰も「悪意」を持っていなかったことにある。
</div>
</div>

---

<!-- スライド3: 登場人物 -->

## 🎭 登場人物

<div class="character-intro">
<div class="character-card detective">
<div class="character-icon">🕵️</div>
<div class="character-name">佐藤アナリスト</div>
<div class="character-role">失敗分析の専門家<br>「数字は嘘をつかない」が口癖</div>
</div>
<div class="character-card">
<div class="character-icon">👩‍💼</div>
<div class="character-name">田中さん</div>
<div class="character-role">新人コンサルタント<br>素直な疑問を投げかける</div>
</div>
<div class="character-card victim">
<div class="character-icon">😰</div>
<div class="character-name">山田PM</div>
<div class="character-role">プロジェクトマネージャー<br>依頼者（被害者？）</div>
</div>
</div>

---

<!-- スライド4: 依頼 -->

## 🚨 依頼

<div class="dialogue">
<span class="speaker-icon">😰</span>
<div class="speech-bubble">
<div class="speaker-name">山田PM</div>
助けてください...私のプロジェクトが<strong>大失敗</strong>しました。<br>
10億円の投資が、すべて水の泡に...
</div>
</div>

<div class="dialogue right">
<span class="speaker-icon">🕵️</span>
<div class="speech-bubble">
<div class="speaker-name">佐藤アナリスト</div>
状況を教えてください。チームに問題があったのですか？
</div>
</div>

<div class="dialogue">
<span class="speaker-icon">😰</span>
<div class="speech-bubble">
<div class="speaker-name">山田PM</div>
それが...<em>全員が優秀</em>だったんです。<br>
東大卒のエンジニア、元外資コンサルのマーケター、MBAホルダーの事業開発...<br>
<strong>なぜこんなことに？</strong>
</div>
</div>

---

<!-- スライド5: 事件の概要 -->

## 📋 事件の概要

<div class="case-timeline">
<div class="timeline-event">
<div class="timeline-date">2023年1月</div>
<div class="timeline-title">新規事業プロジェクト始動</div>
<div class="timeline-desc">「AIを活用した革新的なサービス」を開発</div>
</div>
<div class="timeline-event">
<div class="timeline-date">2023年6月</div>
<div class="timeline-title">順調に開発進行...のはずだった</div>
<div class="timeline-desc">経営陣への報告は常に「順調です」</div>
</div>
<div class="timeline-event">
<div class="timeline-date">2023年12月</div>
<div class="timeline-title">ローンチ延期（1回目）</div>
<div class="timeline-desc">「もう少しで完成」という報告</div>
</div>
<div class="timeline-event">
<div class="timeline-date">2024年6月</div>
<div class="timeline-title">プロジェクト中止</div>
<div class="timeline-desc">10億円の投資が回収不能に</div>
</div>
</div>

---

<!-- スライド6: セクション1 -->
<div class="section-break">
<div class="chapter">第1章</div>

# 最初の違和感

</div>

---

<!-- スライド7: 証拠1 -->

## 🔍 証拠品 #1

<div class="dialogue right">
<span class="speaker-icon">👩‍💼</span>
<div class="speech-bubble">
<div class="speaker-name">田中さん</div>
佐藤さん、議事録を見つけました！<br>
初期の市場調査レポートです。
</div>
</div>

<div class="evidence-card">
<div class="evidence-title">📄 市場調査レポート（2023年2月）</div>
<div class="evidence-content">

- 調査対象: 100名（全員が既存顧客）
- 結果: 「このサービス使いたい」**92%**
- 結論: 市場ニーズは明確に存在する ✓

</div>
</div>

<div class="dialogue">
<span class="speaker-icon">🕵️</span>
<div class="speech-bubble">
<div class="speaker-name">佐藤アナリスト</div>
...田中さん、この調査の<strong>対象者</strong>に気づきましたか？
</div>
</div>

---

<!-- スライド8: 真相1 -->

<div class="revelation">
<h2>🚨 真相 #1</h2>
<p>確証バイアス（Confirmation Bias）</p>
</div>

<div class="dialogue">
<span class="speaker-icon">🕵️</span>
<div class="speech-bubble">
<div class="speaker-name">佐藤アナリスト</div>
調査対象は<strong>全員が既存顧客</strong>です。<br>
つまり、最初から「良い回答」が返ってくる人にしか聞いていない。<br>
<em>「自分に都合の良い情報」だけを集めてしまった</em>のです。
</div>
</div>

<div class="learning-box">
<div class="learning-title">📚 学び：確証バイアス</div>
<div class="learning-content">
自分の信じたいことを裏付ける情報ばかりを集め、反証する情報を無視してしまう心理傾向。<br>
<strong>対策</strong>: 意図的に「反対意見」や「否定的なデータ」を探す習慣をつける。
</div>
</div>

---

<!-- スライド9: セクション2 -->
<div class="section-break">
<div class="chapter">第2章</div>

# 引き返せない沼

</div>

---

<!-- スライド10: 証拠2 -->

## 🔍 証拠品 #2

<div class="dialogue">
<span class="speaker-icon">😰</span>
<div class="speech-bubble">
<div class="speaker-name">山田PM</div>
実は...6ヶ月目で「方向性が違うかも」と思ったんです。<br>
でも、その時点で<strong>3億円</strong>使っていて...
</div>
</div>

<div class="evidence-card">
<div class="evidence-title">📊 予算消化状況</div>
<div class="evidence-content">

| 時期 | 投資額 | 山田PMの心理 |
|------|--------|-------------|
| 3ヶ月目 | 1億円 | 「まだ始まったばかり」 |
| 6ヶ月目 | 3億円 | 「ここで止めたら3億円が無駄に...」 |
| 12ヶ月目 | 7億円 | 「もう引き返せない...」 |
| 18ヶ月目 | 10億円 | 「なぜ止められなかった...」 |

</div>
</div>

---

<!-- スライド11: 真相2 -->

<div class="revelation">
<h2>🚨 真相 #2</h2>
<p>サンクコストの呪縛（Sunk Cost Fallacy）</p>
</div>

<div class="dialogue right">
<span class="speaker-icon">👩‍💼</span>
<div class="speech-bubble">
<div class="speaker-name">田中さん</div>
「もったいない」と思って続けてしまったんですね...<br>
でもそれ、<strong>合理的な判断</strong>なんでしょうか？
</div>
</div>

<div class="learning-box">
<div class="learning-title">📚 学び：サンクコスト効果</div>
<div class="learning-content">
すでに投じた回収不能なコスト（時間・お金・労力）を惜しんで、損な選択を続けてしまう心理。<br>
<strong>対策</strong>: 「今からゼロスタートだとしても、この選択をするか？」と問いかける。<br>
過去の投資は「判断材料」ではなく「学習材料」と考える。
</div>
</div>

---

<!-- スライド12: セクション3 -->
<div class="section-break">
<div class="chapter">第3章</div>

# 沈黙の共犯者たち

</div>

---

<!-- スライド13: 証拠3 -->

## 🔍 証拠品 #3

<div class="dialogue">
<span class="speaker-icon">🕵️</span>
<div class="speech-bubble">
<div class="speaker-name">佐藤アナリスト</div>
チームメンバーに個別インタビューしました。<br>
興味深い証言が得られましたよ。
</div>
</div>

<div class="evidence-card">
<div class="evidence-title">🎤 メンバーの証言</div>
<div class="evidence-content">

👨‍💻 エンジニアA: 「正直、技術的に厳しいと思ってた。でも皆やる気だったし...」

👩‍💼 マーケターB: 「市場調査に疑問はあった。でも空気を読んで黙ってた」

👔 事業開発C: 「反対意見を言ったら"ネガティブな奴"と思われそうで...」

</div>
</div>

---

<!-- スライド14: 真相3 -->

<div class="revelation">
<h2>🚨 真相 #3</h2>
<p>集団思考（Groupthink）</p>
</div>

<div class="dialogue">
<span class="speaker-icon">🕵️</span>
<div class="speech-bubble">
<div class="speaker-name">佐藤アナリスト</div>
<strong>全員が違和感を持っていた</strong>のに、<br>
<strong>誰も声を上げなかった</strong>。<br>
<em>「和を乱したくない」という心理が、チームを破滅に導いた</em>のです。
</div>
</div>

<div class="learning-box">
<div class="learning-title">📚 学び：集団思考</div>
<div class="learning-content">
集団の調和を保とうとするあまり、批判的思考が抑制され、非合理的な意思決定をしてしまう現象。<br>
<strong>対策</strong>:
・意図的に「悪魔の代弁者」役を設ける
・匿名で意見を集める仕組みを作る
・リーダーが最後に意見を言う
</div>
</div>

---

<!-- スライド15: セクション4 -->
<div class="section-break">
<div class="chapter">第4章</div>

# 見えない敵

</div>

---

<!-- スライド16: 証拠4 -->

## 🔍 証拠品 #4

<div class="dialogue right">
<span class="speaker-icon">👩‍💼</span>
<div class="speech-bubble">
<div class="speaker-name">田中さん</div>
佐藤さん、不思議なんです。<br>
なぜ優秀な人たちが、自分たちの間違いに気づけなかったんでしょう？
</div>
</div>

<div class="evidence-card">
<div class="evidence-title">📋 チームメンバーのプロフィール</div>
<div class="evidence-content">

- 東大工学部卒エンジニア（AI分野は初めて）
- 元外資コンサル（toBは得意、toCは未経験）
- MBAホルダー（起業経験なし）

→ 全員が「自分の専門外」の領域で判断していた

</div>
</div>

---

<!-- スライド17: 真相4 -->

<div class="revelation">
<h2>🚨 真相 #4</h2>
<p>ダニング＝クルーガー効果</p>
</div>

<div class="dialogue">
<span class="speaker-icon">🕵️</span>
<div class="speech-bubble">
<div class="speaker-name">佐藤アナリスト</div>
<em>「優秀な人ほど、専門外の分野で過信する」</em><br>
「私は東大出身だから」「外資で鍛えられたから」という<strong>過去の成功体験</strong>が、<br>
未知の領域での<strong>謙虚さ</strong>を奪ってしまったのです。
</div>
</div>

<div class="learning-box">
<div class="learning-title">📚 学び：ダニング＝クルーガー効果</div>
<div class="learning-content">
能力の低い人は自分を過大評価し、能力の高い人は過小評価する傾向。<br>
ただし「別分野で優秀な人」が「新しい分野でも優秀」と錯覚するケースも多い。<br>
<strong>対策</strong>: 新しい分野では「初心者マインド」を持つ。専門家の意見を謙虚に聞く。
</div>
</div>

---

<!-- スライド18: セクション5 -->
<div class="section-break">
<div class="chapter">最終章</div>

# 事件の全貌

</div>

---

<!-- スライド19: 犯人たち -->

## 🎯 真犯人の正体

<div class="dialogue">
<span class="speaker-icon">🕵️</span>
<div class="speech-bubble">
<div class="speaker-name">佐藤アナリスト</div>
この事件の犯人は...<strong>誰でもない。そして、全員だ。</strong>
</div>
</div>

<div class="suspect-grid">
<div class="suspect-card guilty">
<div class="suspect-icon">🔍</div>
<div class="suspect-name">確証バイアス</div>
<div class="suspect-title">都合の良い情報だけ収集</div>
<div class="suspect-status status-guilty">有罪</div>
</div>
<div class="suspect-card guilty">
<div class="suspect-icon">💸</div>
<div class="suspect-name">サンクコスト</div>
<div class="suspect-title">引き返す勇気を奪う</div>
<div class="suspect-status status-guilty">有罪</div>
</div>
<div class="suspect-card guilty">
<div class="suspect-icon">🤝</div>
<div class="suspect-name">集団思考</div>
<div class="suspect-title">批判を封じ込める</div>
<div class="suspect-status status-guilty">有罪</div>
</div>
<div class="suspect-card guilty">
<div class="suspect-icon">🎓</div>
<div class="suspect-name">過信バイアス</div>
<div class="suspect-title">謙虚さを奪う</div>
<div class="suspect-status status-guilty">有罪</div>
</div>
</div>

---

<!-- スライド20: エピローグ -->

## 📖 エピローグ

<div class="dialogue">
<span class="speaker-icon">😰</span>
<div class="speech-bubble">
<div class="speaker-name">山田PM</div>
...全部、私たちの<strong>脳</strong>が敵だったんですね。<br>
悪意がなくても、こんなことが起きてしまう...
</div>
</div>

<div class="dialogue right">
<span class="speaker-icon">🕵️</span>
<div class="speech-bubble">
<div class="speaker-name">佐藤アナリスト</div>
認知バイアスは<em>「人間の仕様」</em>です。<br>
バグではなく、フィーチャー。だから誰にでも起こる。<br>
<strong>大切なのは「知っておくこと」と「仕組みで防ぐこと」</strong>です。
</div>
</div>

<div class="dialogue">
<span class="speaker-icon">👩‍💼</span>
<div class="speech-bubble">
<div class="speaker-name">田中さん</div>
私も気をつけます...！
</div>
</div>

---

<!-- スライド21: まとめ -->

## 📚 本日の学び

<div class="summary-mystery">
<div class="summary-item">
<span class="summary-num">1</span>
<div class="summary-title">確証バイアス</div>
<div class="summary-desc">意図的に反対意見を探せ</div>
</div>
<div class="summary-item">
<span class="summary-num">2</span>
<div class="summary-title">サンクコスト効果</div>
<div class="summary-desc">「今からゼロなら？」と問え</div>
</div>
<div class="summary-item">
<span class="summary-num">3</span>
<div class="summary-title">集団思考</div>
<div class="summary-desc">悪魔の代弁者を置け</div>
</div>
<div class="summary-item">
<span class="summary-num">4</span>
<div class="summary-title">ダニング＝クルーガー</div>
<div class="summary-desc">専門外では謙虚であれ</div>
</div>
</div>

<div class="hint-box">
<span class="hint-icon">💡</span>
<div class="hint-text">
認知バイアスは「知っている」だけで半分防げる。<br>
残り半分は「仕組み」と「習慣」で防ぐ。
</div>
</div>

---

<!-- スライド22: エンディング -->
<div class="title-mystery">

# 🔍 Case Closed

<div class="subtitle">認知バイアスは、あなたのすぐそばにいる</div>

<div class="tagline">
次の事件を防ぐのは...あなた自身です。<br><br>
🔖 #確証バイアス #サンクコスト #集団思考 #ダニングクルーガー
</div>

</div>
