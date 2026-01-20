---
marp: true
theme: default
paginate: false
style: |
  /* ================================ */
  /* りもにゃん風デザインシステム     */
  /* ================================ */

  /* --- カラーパレット --- */
  :root {
    --bg-cream: #FFF8F0;
    --bg-light: #FFFBF5;
    --orange: #FF9B50;
    --orange-light: #FFCF9D;
    --coral: #FF6B6B;
    --coral-light: #FFB4B4;
    --mint: #7ED4AD;
    --mint-light: #C5F0DD;
    --blue: #64B5F6;
    --blue-light: #BBDEFB;
    --purple: #B39DDB;
    --purple-light: #E1D5F0;
    --yellow: #FFE066;
    --yellow-light: #FFF4CC;
    --text-dark: #5D4E37;
    --text-gray: #8B7E6A;
    --border: #E8DFD5;
    --white: #FFFFFF;
  }

  section {
    background: var(--bg-cream);
    font-family: "Hiragino Maru Gothic Pro", "BIZ UDPGothic", "Noto Sans JP", sans-serif;
    color: var(--text-dark);
    padding: 30px;
  }

  h1, h2, h3 {
    color: var(--text-dark);
    font-weight: 700;
  }

  /* ================================ */
  /* タイトルスライド                 */
  /* ================================ */

  .title-rimonyan {
    text-align: center;
    padding-top: 80px;
  }
  .title-rimonyan h1 {
    font-size: 2.2em;
    color: var(--orange);
    margin-bottom: 0.3em;
    text-shadow: 2px 2px 0 var(--orange-light);
  }
  .title-rimonyan .subtitle {
    font-size: 1.1em;
    color: var(--text-gray);
    margin-bottom: 2em;
  }
  .title-rimonyan .cat-icon {
    font-size: 4em;
    margin-bottom: 0.5em;
  }

  /* ================================ */
  /* 猫キャラ吹き出し                 */
  /* ================================ */

  .cat-says {
    display: flex;
    align-items: flex-start;
    gap: 15px;
    margin: 1em 0;
  }
  .cat-face {
    font-size: 2.5em;
    flex-shrink: 0;
  }
  .cat-bubble {
    background: var(--white);
    border: 3px solid var(--orange);
    border-radius: 20px;
    padding: 15px 20px;
    position: relative;
    font-size: 0.95em;
    line-height: 1.6;
    flex: 1;
  }
  .cat-bubble::before {
    content: "";
    position: absolute;
    left: -12px;
    top: 20px;
    border: 6px solid transparent;
    border-right-color: var(--orange);
  }
  .cat-bubble.right {
    order: -1;
  }
  .cat-bubble.right::before {
    left: auto;
    right: -12px;
    border-right-color: transparent;
    border-left-color: var(--orange);
  }

  /* ================================ */
  /* ポイントボックス                 */
  /* ================================ */

  .point-box {
    background: var(--white);
    border: 2px solid var(--border);
    border-radius: 15px;
    padding: 15px 20px;
    margin: 0.8em 0;
    border-left: 5px solid var(--orange);
  }
  .point-box.mint { border-left-color: var(--mint); }
  .point-box.coral { border-left-color: var(--coral); }
  .point-box.blue { border-left-color: var(--blue); }
  .point-box.purple { border-left-color: var(--purple); }

  .point-title {
    font-weight: 700;
    color: var(--orange);
    font-size: 1.05em;
    margin-bottom: 0.3em;
  }
  .point-box.mint .point-title { color: var(--mint); }
  .point-box.coral .point-title { color: var(--coral); }
  .point-box.blue .point-title { color: var(--blue); }
  .point-box.purple .point-title { color: var(--purple); }

  /* ================================ */
  /* 番号付きステップ                 */
  /* ================================ */

  .steps-rimonyan {
    counter-reset: step;
  }
  .step-item {
    display: flex;
    align-items: flex-start;
    gap: 15px;
    margin: 0.8em 0;
    background: var(--white);
    border-radius: 12px;
    padding: 12px 15px;
  }
  .step-num {
    background: var(--orange);
    color: var(--white);
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 1.1em;
    flex-shrink: 0;
  }
  .step-item:nth-child(2) .step-num { background: var(--coral); }
  .step-item:nth-child(3) .step-num { background: var(--mint); }
  .step-item:nth-child(4) .step-num { background: var(--blue); }
  .step-item:nth-child(5) .step-num { background: var(--purple); }
  .step-content {
    flex: 1;
    padding-top: 4px;
  }
  .step-content strong {
    color: var(--text-dark);
  }

  /* ================================ */
  /* チェックリスト                   */
  /* ================================ */

  .checklist {
    background: var(--white);
    border-radius: 15px;
    padding: 15px 20px;
  }
  .check-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 0;
    border-bottom: 1px dashed var(--border);
  }
  .check-item:last-child {
    border-bottom: none;
  }
  .check-ok {
    color: var(--mint);
    font-size: 1.3em;
  }
  .check-ng {
    color: var(--coral);
    font-size: 1.3em;
  }

  /* ================================ */
  /* 比較表（◯×）                    */
  /* ================================ */

  .compare-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    background: var(--white);
    border-radius: 15px;
    overflow: hidden;
    font-size: 0.9em;
  }
  .compare-table th {
    background: var(--orange);
    color: var(--white);
    padding: 12px;
    text-align: center;
    font-weight: 700;
  }
  .compare-table th:first-child {
    background: var(--text-gray);
  }
  .compare-table th.good {
    background: var(--mint);
  }
  .compare-table th.bad {
    background: var(--coral);
  }
  .compare-table td {
    padding: 10px 12px;
    border-bottom: 1px solid var(--border);
    text-align: center;
  }
  .compare-table td:first-child {
    text-align: left;
    font-weight: 500;
  }
  .compare-table tr:last-child td {
    border-bottom: none;
  }
  .mark-ok { color: var(--mint); font-size: 1.4em; }
  .mark-ng { color: var(--coral); font-size: 1.4em; }
  .mark-triangle { color: var(--yellow); font-size: 1.4em; }

  /* ================================ */
  /* 情報カード（ぎゅうぎゅう詰め）   */
  /* ================================ */

  .info-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }
  .info-card {
    background: var(--white);
    border-radius: 12px;
    padding: 12px 15px;
    border: 2px solid var(--border);
  }
  .info-card-title {
    background: var(--orange);
    color: var(--white);
    font-weight: 700;
    font-size: 0.85em;
    padding: 4px 10px;
    border-radius: 8px;
    display: inline-block;
    margin-bottom: 8px;
  }
  .info-card.mint .info-card-title { background: var(--mint); }
  .info-card.coral .info-card-title { background: var(--coral); }
  .info-card.blue .info-card-title { background: var(--blue); }
  .info-card.purple .info-card-title { background: var(--purple); }
  .info-card ul {
    margin: 0;
    padding-left: 1.2em;
    font-size: 0.85em;
  }
  .info-card li {
    margin: 4px 0;
  }

  /* ================================ */
  /* NGとOK比較                       */
  /* ================================ */

  .ng-ok-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
  }
  .ng-box, .ok-box {
    border-radius: 15px;
    padding: 15px;
  }
  .ng-box {
    background: var(--coral-light);
    border: 2px solid var(--coral);
  }
  .ok-box {
    background: var(--mint-light);
    border: 2px solid var(--mint);
  }
  .ng-label, .ok-label {
    font-weight: 700;
    font-size: 1.1em;
    margin-bottom: 10px;
    text-align: center;
  }
  .ng-label { color: var(--coral); }
  .ok-label { color: #2E7D32; }

  /* ================================ */
  /* タグ・ラベル                     */
  /* ================================ */

  .tag-row {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin: 0.5em 0;
  }
  .tag {
    background: var(--orange-light);
    color: var(--text-dark);
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.85em;
    font-weight: 500;
  }
  .tag.mint { background: var(--mint-light); }
  .tag.coral { background: var(--coral-light); }
  .tag.blue { background: var(--blue-light); }
  .tag.purple { background: var(--purple-light); }
  .tag.yellow { background: var(--yellow-light); }

  /* ================================ */
  /* まとめボックス                   */
  /* ================================ */

  .summary-box {
    background: linear-gradient(135deg, var(--orange-light) 0%, var(--yellow-light) 100%);
    border-radius: 20px;
    padding: 20px;
    text-align: center;
    border: 3px solid var(--orange);
  }
  .summary-box h2 {
    color: var(--orange);
    margin: 0 0 0.5em;
    font-size: 1.3em;
  }
  .summary-box p {
    margin: 0;
    font-size: 1.05em;
    line-height: 1.6;
  }

  /* ================================ */
  /* セクションヘッダー               */
  /* ================================ */

  .section-rimonyan {
    background: linear-gradient(135deg, var(--orange) 0%, var(--coral) 100%);
    color: var(--white);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  .section-rimonyan h1 {
    color: var(--white);
    font-size: 2.5em;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
  }
  .section-rimonyan .section-num {
    font-size: 3em;
    opacity: 0.3;
    margin-bottom: 0.2em;
  }

  /* ================================ */
  /* 吹き出し解説                     */
  /* ================================ */

  .bubble-explain {
    background: var(--white);
    border: 3px solid var(--orange);
    border-radius: 20px;
    padding: 15px 20px;
    margin: 0.5em 0;
    position: relative;
  }
  .bubble-explain::after {
    content: "💡";
    position: absolute;
    top: -15px;
    left: 15px;
    font-size: 1.5em;
  }

  /* ================================ */
  /* フロー・手順                     */
  /* ================================ */

  .flow-rimonyan {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    margin: 1em 0;
  }
  .flow-item {
    background: var(--white);
    border: 2px solid var(--orange);
    border-radius: 12px;
    padding: 12px;
    text-align: center;
    flex: 1;
    font-size: 0.9em;
  }
  .flow-item:nth-child(1) { border-color: var(--orange); }
  .flow-item:nth-child(2) { border-color: var(--coral); }
  .flow-item:nth-child(3) { border-color: var(--mint); }
  .flow-item:nth-child(4) { border-color: var(--blue); }
  .flow-arrow {
    color: var(--text-gray);
    font-size: 1.5em;
    flex-shrink: 0;
  }

  /* ================================ */
  /* 数字ハイライト                   */
  /* ================================ */

  .num-highlight {
    display: flex;
    justify-content: space-around;
    gap: 15px;
    margin: 1em 0;
  }
  .num-item {
    text-align: center;
    background: var(--white);
    border-radius: 15px;
    padding: 15px 20px;
    flex: 1;
    border: 2px solid var(--border);
  }
  .num-big {
    font-size: 2.5em;
    font-weight: 700;
    color: var(--orange);
  }
  .num-unit {
    font-size: 0.9em;
    color: var(--text-gray);
  }
  .num-label {
    font-size: 0.85em;
    margin-top: 5px;
  }

  /* ================================ */
  /* ヒントボックス                   */
  /* ================================ */

  .hint-box {
    background: var(--yellow-light);
    border: 2px dashed var(--yellow);
    border-radius: 15px;
    padding: 15px;
    display: flex;
    align-items: flex-start;
    gap: 10px;
  }
  .hint-icon {
    font-size: 1.5em;
    flex-shrink: 0;
  }
  .hint-text {
    flex: 1;
    font-size: 0.95em;
    line-height: 1.5;
  }

  /* ================================ */
  /* 引用・名言                       */
  /* ================================ */

  .quote-rimonyan {
    background: var(--white);
    border-left: 5px solid var(--purple);
    border-radius: 0 15px 15px 0;
    padding: 15px 20px;
    font-style: italic;
    color: var(--text-gray);
  }
  .quote-author {
    text-align: right;
    font-size: 0.85em;
    margin-top: 10px;
    font-style: normal;
    color: var(--text-dark);
  }

---

<!-- スライド1: タイトル -->
<div class="title-rimonyan">
<div class="cat-icon">🐱</div>

# にゃるほど！仕事術図解

<div class="subtitle">りもにゃん風デザインコンポーネント集</div>
</div>

---

<!-- スライド2: 猫キャラ吹き出し -->

## 🐱 猫キャラ吹き出しコンポーネント

<div class="cat-says">
<div class="cat-face">😺</div>
<div class="cat-bubble">
<strong>にゃるほど！</strong><br>
吹き出しを使うと、キャラクターがアドバイスしてるみたいで親しみやすいにゃ！
</div>
</div>

<div class="cat-says">
<div class="cat-face">😸</div>
<div class="cat-bubble">
難しい内容も、友達から教わるような感覚で伝えられるにゃ〜
</div>
</div>

<div class="cat-says">
<div class="cat-face">🙀</div>
<div class="cat-bubble">
表情を変えると、感情も伝わりやすくなるにゃ！
</div>
</div>

---

<!-- スライド3: ポイントボックス -->

## 📦 ポイントボックス

<div class="point-box">
<div class="point-title">💡 ポイント1</div>
情報を整理して見やすくまとめることで、一目で内容が伝わるよ！
</div>

<div class="point-box mint">
<div class="point-title">✅ ポイント2</div>
色を変えることで、情報の種類を視覚的に区別できるよ！
</div>

<div class="point-box coral">
<div class="point-title">⚠️ 注意点</div>
色を使いすぎると見にくくなるから、3〜4色に絞ろう！
</div>

---

<!-- スライド4: 番号付きステップ -->

## 📝 番号付きステップ

<div class="steps-rimonyan">
<div class="step-item">
<div class="step-num">1</div>
<div class="step-content"><strong>情報を整理する</strong><br>伝えたいことを箇条書きにしよう</div>
</div>
<div class="step-item">
<div class="step-num">2</div>
<div class="step-content"><strong>優先順位をつける</strong><br>大事なことから順番に並べよう</div>
</div>
<div class="step-item">
<div class="step-num">3</div>
<div class="step-content"><strong>図解にする</strong><br>テキストを視覚的に表現しよう</div>
</div>
<div class="step-item">
<div class="step-num">4</div>
<div class="step-content"><strong>見直す</strong><br>パッと見てわかるかチェック！</div>
</div>
</div>

---

<!-- スライド5: チェックリスト -->

## ✅ チェックリスト

<div class="checklist">
<div class="check-item"><span class="check-ok">✅</span> タイトルは30文字以内におさまってる？</div>
<div class="check-item"><span class="check-ok">✅</span> 情報が詰め込みすぎてない？</div>
<div class="check-item"><span class="check-ok">✅</span> 色は3〜4色に絞ってる？</div>
<div class="check-item"><span class="check-ng">❌</span> 文字が小さすぎない？</div>
<div class="check-item"><span class="check-ok">✅</span> パッと見てわかる？</div>
</div>

<div class="cat-says" style="margin-top: 1em;">
<div class="cat-face">😺</div>
<div class="cat-bubble">
チェックリストで確認すると、抜け漏れを防げるにゃ！
</div>
</div>

---

<!-- スライド6: 比較表 -->

## 📊 比較表（◯×）

<table class="compare-table">
<tr>
<th>項目</th>
<th class="good">良い例 ◯</th>
<th class="bad">悪い例 ×</th>
</tr>
<tr>
<td>文字量</td>
<td>簡潔に要点のみ</td>
<td>長文でダラダラ</td>
</tr>
<tr>
<td>色の使い方</td>
<td>3〜4色で統一感</td>
<td>カラフルすぎ</td>
</tr>
<tr>
<td>レイアウト</td>
<td>整列・余白あり</td>
<td>バラバラ・詰め込み</td>
</tr>
<tr>
<td>フォント</td>
<td>読みやすい大きさ</td>
<td>小さくて見えない</td>
</tr>
</table>

---

<!-- スライド7: NG/OK比較 -->

## ⚡ NG例 vs OK例

<div class="ng-ok-compare">
<div class="ng-box">
<div class="ng-label">❌ NG例</div>

- 文字が多すぎる
- 色がバラバラ
- 何が言いたいかわからない
- 読むのに時間がかかる

</div>
<div class="ok-box">
<div class="ok-label">✅ OK例</div>

- 要点が絞られてる
- 色に統一感がある
- 一目で伝わる
- サクッと読める

</div>
</div>

---

<!-- スライド8: 情報カード -->

## 🃏 情報カード（ぎゅうぎゅう詰め）

<div class="info-grid">
<div class="info-card">
<span class="info-card-title">📧 メール術</span>

- 件名は具体的に
- 結論を最初に書く
- 箇条書きを活用

</div>
<div class="info-card mint">
<span class="info-card-title">💬 チャット術</span>

- 即レスを心がける
- スタンプも活用OK
- 長文は分割する

</div>
<div class="info-card coral">
<span class="info-card-title">📅 スケジュール</span>

- バッファを設ける
- 優先順位をつける
- 定期的に見直す

</div>
<div class="info-card blue">
<span class="info-card-title">🎯 タスク管理</span>

- 細かく分解する
- 期限を決める
- 完了したら消す

</div>
</div>

---

<!-- スライド9: タグ・ラベル -->

## 🏷️ タグ・ラベル

<div class="tag-row">
<span class="tag">#仕事術</span>
<span class="tag mint">#時短</span>
<span class="tag coral">#効率化</span>
<span class="tag blue">#リモートワーク</span>
<span class="tag purple">#コミュニケーション</span>
</div>

<div class="tag-row">
<span class="tag yellow">#初心者向け</span>
<span class="tag">#すぐ使える</span>
<span class="tag mint">#便利ツール</span>
</div>

<div class="cat-says" style="margin-top: 1.5em;">
<div class="cat-face">😻</div>
<div class="cat-bubble">
タグを使うとカテゴリが一目でわかるにゃ！<br>
SNS投稿でもよく使われるテクニックだよ〜
</div>
</div>

---

<!-- スライド10: フロー図 -->

## ➡️ フロー・手順

<div class="flow-rimonyan">
<div class="flow-item">📝<br><strong>下書き</strong></div>
<span class="flow-arrow">→</span>
<div class="flow-item">🎨<br><strong>デザイン</strong></div>
<span class="flow-arrow">→</span>
<div class="flow-item">👀<br><strong>確認</strong></div>
<span class="flow-arrow">→</span>
<div class="flow-item">🚀<br><strong>投稿</strong></div>
</div>

<div class="bubble-explain">
フロー図は左から右へ、または上から下へ流れるように配置すると、順番がわかりやすいよ！矢印を使って視線を誘導しよう。
</div>

---

<!-- スライド11: 数字ハイライト -->

## 🔢 数字ハイライト

<div class="num-highlight">
<div class="num-item">
<div class="num-big">3<span class="num-unit">色</span></div>
<div class="num-label">最適な配色数</div>
</div>
<div class="num-item">
<div class="num-big">30<span class="num-unit">文字</span></div>
<div class="num-label">タイトル上限</div>
</div>
<div class="num-item">
<div class="num-big">5<span class="num-unit">秒</span></div>
<div class="num-label">理解までの目安</div>
</div>
</div>

<div class="hint-box">
<span class="hint-icon">💡</span>
<div class="hint-text">
数字を大きく見せると、インパクトが増して記憶に残りやすくなるよ！
</div>
</div>

---

<!-- スライド12: まとめボックス -->

## 🎁 まとめボックス

<div class="summary-box">

## 今日のまとめ

- 情報は整理して、要点を絞ろう
- 色は3〜4色に統一しよう
- パッと見てわかるデザインを心がけよう
- キャラクターで親しみやすさUP！

</div>

<div class="cat-says">
<div class="cat-face">😸</div>
<div class="cat-bubble">
最後にまとめを入れると、学んだことが定着するにゃ〜！
</div>
</div>

---

<!-- スライド13: セクションヘッダー -->
<section class="section-rimonyan">
<div class="section-num">01</div>

# メール・チャット術

コミュニケーションの基本を学ぼう！

</section>

---

<!-- スライド14: 引用・名言 -->

## 💬 引用・名言

<div class="quote-rimonyan">
「シンプルであることは、複雑であることよりも難しい。物事をシンプルにするためには、懸命に努力して思考を明瞭にしなければならないからだ。」
<div class="quote-author">— スティーブ・ジョブズ</div>
</div>

<div class="cat-says" style="margin-top: 1em;">
<div class="cat-face">🐱</div>
<div class="cat-bubble">
シンプルに伝えることが一番大事にゃ！<br>
難しいことを簡単に伝えるのが図解の力だよ〜
</div>
</div>

---

<!-- スライド15: ヒントボックス -->

## 💡 ヒントボックス

<div class="hint-box">
<span class="hint-icon">💡</span>
<div class="hint-text">
<strong>デザインのコツ：</strong>余白を恐れないこと！詰め込みすぎると逆に見にくくなるよ。
</div>
</div>

<div class="hint-box" style="border-color: var(--mint); background: var(--mint-light);">
<span class="hint-icon">✨</span>
<div class="hint-text">
<strong>上級テク：</strong>同じレイアウトを繰り返すと、統一感が出てプロっぽく見えるよ！
</div>
</div>

<div class="hint-box" style="border-color: var(--coral); background: var(--coral-light);">
<span class="hint-icon">⚠️</span>
<div class="hint-text">
<strong>注意：</strong>フォントは2種類までに絞ろう。多すぎると雑多な印象になっちゃう！
</div>
</div>

---

<!-- スライド16: 組み合わせ例 -->

## 🎨 組み合わせ例

<div class="cat-says">
<div class="cat-face">😺</div>
<div class="cat-bubble">
<strong>リモートワークで大切な3つのこと</strong>を教えるにゃ！
</div>
</div>

<div class="steps-rimonyan">
<div class="step-item">
<div class="step-num">1</div>
<div class="step-content"><strong>こまめな報連相</strong><br>進捗を共有して安心感を与えよう</div>
</div>
<div class="step-item">
<div class="step-num">2</div>
<div class="step-content"><strong>オンオフの切り替え</strong><br>仕事とプライベートを分けよう</div>
</div>
<div class="step-item">
<div class="step-num">3</div>
<div class="step-content"><strong>自己管理能力</strong><br>誰も見てなくても頑張れる！</div>
</div>
</div>

---

<!-- スライド17: 比較表の活用 -->

## 📋 ツール比較

<table class="compare-table">
<tr>
<th>ツール</th>
<th>速度</th>
<th>記録</th>
<th>雰囲気</th>
</tr>
<tr>
<td>📧 メール</td>
<td><span class="mark-triangle">△</span></td>
<td><span class="mark-ok">◎</span></td>
<td>フォーマル</td>
</tr>
<tr>
<td>💬 チャット</td>
<td><span class="mark-ok">◎</span></td>
<td><span class="mark-ok">○</span></td>
<td>カジュアル</td>
</tr>
<tr>
<td>📞 電話</td>
<td><span class="mark-ok">◎</span></td>
<td><span class="mark-ng">×</span></td>
<td>臨機応変</td>
</tr>
<tr>
<td>🎥 ビデオ</td>
<td><span class="mark-ok">○</span></td>
<td><span class="mark-triangle">△</span></td>
<td>対面に近い</td>
</tr>
</table>

---

<!-- スライド18: 最終まとめ -->

## 🐱 りもにゃん風デザインまとめ

<div class="info-grid">
<div class="info-card">
<span class="info-card-title">🎨 配色</span>

- クリーム系背景
- オレンジ系アクセント
- パステルカラー

</div>
<div class="info-card mint">
<span class="info-card-title">📐 レイアウト</span>

- 情報をぎゅっと詰める
- 枠で区切って整理
- 余白も大切に

</div>
<div class="info-card coral">
<span class="info-card-title">🐱 キャラクター</span>

- 吹き出しで解説
- 表情で感情表現
- 親しみやすさUP

</div>
<div class="info-card blue">
<span class="info-card-title">✍️ 文章</span>

- 友達みたいな口調
- 簡潔でわかりやすく
- 「〜にゃ」で可愛く

</div>
</div>
