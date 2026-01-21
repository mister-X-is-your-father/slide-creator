---
marp: true
theme: default
paginate: false
size: 16:9
style: |
  /* ================================ */
  /* 手書きノート風デザイン           */
  /* 物語：消えた30分                 */
  /* ================================ */

  @import url('https://fonts.googleapis.com/css2?family=Zen+Kurenaido&family=Yuji+Boku&display=swap');

  :root {
    --paper: #FDF6E3;
    --ink: #2C1810;
    --ink-light: #5D4E37;
    --red-ink: #C41E3A;
    --blue-ink: #1E4D8C;
    --pencil: #4A4A4A;
    --highlight: #FFEB3B;
  }

  section {
    background: var(--paper);
    background-image:
      linear-gradient(var(--ink-light) 1px, transparent 1px);
    background-size: 100% 32px;
    background-position: 0 60px;
    font-family: "Zen Kurenaido", "Yuji Boku", cursive, sans-serif;
    color: var(--ink);
    padding: 30px 50px;
    font-size: 20px;
    line-height: 1.8;
  }

  h1 {
    font-family: "Yuji Boku", serif;
    font-size: 2em;
    color: var(--ink);
    border-bottom: 3px solid var(--ink);
    padding-bottom: 10px;
    margin-bottom: 20px;
  }

  h2 {
    font-size: 1.4em;
    color: var(--blue-ink);
    margin-bottom: 15px;
  }

  /* 手書き風テキスト */
  .handwrite {
    font-family: "Zen Kurenaido", cursive;
    line-height: 2;
  }

  /* 日記エントリー */
  .diary-entry {
    background: rgba(255,255,255,0.5);
    border-left: 4px solid var(--blue-ink);
    padding: 15px 20px;
    margin: 15px 0;
    transform: rotate(-0.5deg);
  }

  .diary-date {
    font-size: 0.85em;
    color: var(--ink-light);
    margin-bottom: 10px;
  }

  /* マーカー */
  .marker-yellow {
    background: linear-gradient(transparent 60%, #FFEB3B 60%);
    padding: 0 4px;
  }

  .marker-pink {
    background: linear-gradient(transparent 60%, #FFB6C1 60%);
    padding: 0 4px;
  }

  /* 取り消し線 */
  .crossed {
    text-decoration: line-through;
    color: var(--ink-light);
  }

  /* 赤ペン */
  .red {
    color: var(--red-ink);
    font-weight: bold;
  }

  /* メモ書き */
  .memo {
    background: #FFFACD;
    padding: 12px 15px;
    margin: 10px 0;
    transform: rotate(1deg);
    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    font-size: 0.9em;
  }

  /* 矢印メモ */
  .arrow-note {
    color: var(--red-ink);
    font-size: 0.9em;
    margin-left: 20px;
  }

  /* タイトルページ */
  .title-page {
    text-align: center;
    padding-top: 80px;
  }

  .title-page h1 {
    font-size: 2.8em;
    border: none;
    margin-bottom: 30px;
  }

  .title-page .subtitle {
    font-size: 1.2em;
    color: var(--ink-light);
  }

  /* 証拠写真風 */
  .evidence {
    background: white;
    padding: 10px;
    box-shadow: 3px 3px 10px rgba(0,0,0,0.2);
    transform: rotate(-2deg);
    display: inline-block;
    margin: 10px;
  }

  .evidence-label {
    font-size: 0.8em;
    color: var(--red-ink);
    margin-top: 8px;
    text-align: center;
  }

  /* 時系列 */
  .timeline {
    border-left: 3px dashed var(--pencil);
    padding-left: 20px;
    margin: 15px 0;
  }

  .timeline-item {
    position: relative;
    margin: 12px 0;
    padding-left: 15px;
  }

  .timeline-item::before {
    content: "●";
    position: absolute;
    left: -28px;
    color: var(--blue-ink);
  }

  .timeline-time {
    font-weight: bold;
    color: var(--blue-ink);
  }

  /* 考察ボックス */
  .thinking {
    border: 2px dashed var(--pencil);
    padding: 15px;
    margin: 15px 0;
    background: rgba(255,255,255,0.3);
  }

  .thinking-title {
    font-weight: bold;
    color: var(--blue-ink);
    margin-bottom: 10px;
  }

  /* 吹き出し */
  .speech {
    background: white;
    border: 2px solid var(--ink);
    border-radius: 20px;
    padding: 12px 18px;
    margin: 10px 0;
    position: relative;
    display: inline-block;
  }

  .speech-name {
    font-size: 0.75em;
    color: var(--ink-light);
    margin-bottom: 5px;
  }

  /* 衝撃 */
  .shock {
    font-size: 1.5em;
    color: var(--red-ink);
    text-align: center;
    padding: 20px;
    transform: rotate(-3deg);
  }

  /* 結末 */
  .ending {
    text-align: center;
    padding-top: 50px;
  }

  .ending h1 {
    border: none;
    font-size: 2.5em;
  }

---

<!-- タイトル -->
<div class="title-page">

# 消えた30分

<div class="subtitle">〜 私のノートに残された、奇妙な記録 〜</div>

<div class="memo" style="margin-top: 50px; display: inline-block;">
このノートを見つけた人へ：<br>
最後まで読んでください。<br>
そして、<span class="red">同じ過ちを繰り返さないで</span>。
</div>

</div>

---

# 4月7日（月）

<div class="diary-entry">
<div class="diary-date">AM 8:45 - 通勤電車内</div>

今日から新しいプロジェクトが始まる。

チームリーダーの<span class="marker-yellow">佐藤さん</span>は「これは会社の命運を賭けた案件だ」と言っていた。

プレッシャーはあるけど、<span class="marker-pink">やりがいがある</span>。

頑張ろう。
</div>

<div class="memo">
メンバー：佐藤（リーダー）、田中、私、<span class="crossed">山本</span>
<div class="arrow-note">← 山本さんは急遽外れたらしい。理由は不明。</div>
</div>

---

# 4月14日（月）

<div class="diary-entry">
<div class="diary-date">PM 11:30 - 自宅</div>

おかしい。

今日、<span class="marker-yellow">30分間の記憶がない</span>。

15:00に会議室に入って、気づいたら15:30だった。

みんな普通に話してた。私だけが「あれ？」って顔をしてたらしい。
</div>

<div class="thinking">
<div class="thinking-title">【自分メモ】</div>
・疲れてた？ → でも寝てない<br>
・ぼーっとしてた？ → 30分は長すぎる<br>
・<span class="red">誰も何も言わなかったのが不自然</span>
</div>

---

# 4月15日（火）

<div class="diary-entry">
<div class="diary-date">AM 7:00 - 自宅</div>

昨夜、夢を見た。

会議室で、<span class="marker-pink">誰かが私の名前を呼んでいた</span>。

でも振り向いても誰もいない。

ただ、テーブルの上に<span class="red">「見るな」</span>と書かれた紙があった。
</div>

<div class="memo">
今日、こっそり会議室を調べてみよう。
</div>

---

# 4月15日（火）続き

<div class="diary-entry">
<div class="diary-date">PM 12:30 - 会社・会議室</div>

昼休み、一人で会議室に入った。

テーブルの下、椅子の裏、ホワイトボードの後ろ...

<span class="marker-yellow">何もなかった。</span>

...と思った。

でも、帰り際に気づいた。
</div>

<div class="shock">
天井のタイルが、<br>
<span style="font-size: 1.3em;">1枚だけ色が違う</span>
</div>

---

# 4月16日（水）

<div class="timeline">
<div class="timeline-item">
<span class="timeline-time">AM 9:00</span> - 田中さんに天井のこと聞いてみた
</div>
<div class="timeline-item">
<span class="timeline-time">AM 9:01</span> - 田中さん「え？何の話？」
</div>
<div class="timeline-item">
<span class="timeline-time">AM 9:05</span> - 一緒に会議室へ
</div>
<div class="timeline-item">
<span class="timeline-time">AM 9:06</span> - <span class="red">天井は全部同じ色だった</span>
</div>
</div>

<div class="thinking">
<div class="thinking-title">【どういうこと？】</div>
昨日は確かに違った。見間違い？<br>
いや、写真を... <span class="crossed">撮ってない</span><br>
<span class="red">なぜ撮らなかった？</span>
</div>

---

# 4月18日（金）

<div class="diary-entry">
<div class="diary-date">PM 3:00 - 会議中</div>

また起きた。

今度は<span class="marker-yellow">15分</span>。

でも今回は違った。

<span class="red">「戻ってきた」瞬間を覚えてる。</span>
</div>

<div class="speech">
<div class="speech-name">私の声（？）</div>
「大丈夫、もう少しで終わる」
</div>

<div class="memo">
誰の声？ 私の声なのに、私じゃない。<br>
<span class="red">頭の中で響いた。</span>
</div>

---

# 4月20日（日）

<div class="diary-entry">
<div class="diary-date">PM 2:00 - 自宅</div>

今日、<span class="marker-pink">山本さんに連絡を取った</span>。

プロジェクトを急に外れた理由。
</div>

<div class="speech">
<div class="speech-name">山本さん（電話）</div>
「...あの会議室には近づかない方がいい」<br>
「俺も最初は記憶が飛ぶところから始まった」<br>
「今は...もう大丈夫。でも代わりに<span class="red">███████</span>」
</div>

<div class="memo">
電話が途中で切れた。<br>
かけ直しても繋がらない。<br>
<span class="red">最後、何て言おうとしてた？</span>
</div>

---

# 4月21日（月）

<div class="diary-entry">
<div class="diary-date">AM 8:00 - 通勤電車内</div>

今朝、鏡を見て気づいた。

<span class="marker-yellow">目の下に、小さな傷</span>。

いつついた？ 覚えてない。
</div>

<div class="diary-entry">
<div class="diary-date">PM 6:00 - 会社</div>

佐藤さんに呼び出された。

「最近、大丈夫？疲れてない？」

<span class="red">佐藤さんの目の下にも、同じ場所に傷があった。</span>
</div>

---

# 4月23日（水）

<div class="shock">
今日、私は重大なことに気づいた。
</div>

<div class="diary-entry">
<div class="diary-date">PM 11:00 - 自宅</div>

このノートを最初から読み返した。

4月7日の記述。

<span class="marker-yellow">「山本さんは急遽外れたらしい」</span>

でも私、<span class="red">山本さんと働いたことがない</span>。

入社以来、一度も。

<span class="red">なぜ私は山本さんを知っている？</span>
</div>

---

# 4月24日（木）

<div class="diary-entry">
<div class="diary-date">AM 3:00 - 自宅</div>

眠れない。

さっき、<span class="marker-pink">自分の手が勝手に動いた</span>。

このノートに何かを書こうとしてた。

慌てて止めた。

でも一文字だけ、書かれてた。
</div>

<div style="text-align: center; margin-top: 30px;">
<span style="font-size: 3em; color: var(--red-ink);">忘</span>
</div>

---

# 4月25日（金）

<div class="diary-entry">
<div class="diary-date">PM 3:00 - 会議室</div>

今日の会議で、<span class="marker-yellow">45分消えた</span>。

戻ってきたとき、全員が私を見ていた。

佐藤さんが言った。
</div>

<div class="speech">
<div class="speech-name">佐藤さん</div>
「おかえり。<span class="red">君も仲間だね</span>」
</div>

<div class="speech">
<div class="speech-name">田中さん</div>
「<span class="red">楽になるよ。全部忘れられるから</span>」
</div>

---

# 4月26日（土）

<div class="diary-entry">
<div class="diary-date">AM 6:00 - 自宅</div>

やっと分かった。

<span class="marker-yellow">消えた30分は、「消された」んじゃない。</span>

<span class="red">「上書き」されてたんだ。</span>

私の中に、もう一人いる。
</div>

<div class="thinking">
<div class="thinking-title">【真実】</div>
あの会議室で、何かが「入ってくる」。<br>
最初は短い時間だけ。でもだんだん長くなる。<br>
山本さんは、きっと<span class="red">完全に入れ替わった</span>。<br>
佐藤さんも、田中さんも、もう...
</div>

---

# 4月27日（日）

<div class="diary-entry">
<div class="diary-date">PM 8:00 - 自宅</div>

明日、会社に行かなければならない。

でも会議室には絶対に入らない。

このノートを<span class="marker-yellow">誰かに見つけてもらえるように</span>隠しておく。

もし私が「普通」に見えたら、それは私じゃない。
</div>

<div class="memo">
本当の私を見分ける方法：<br>
<span class="red">左手の薬指を見て。</span><br>
私は昔の怪我で、第一関節が曲がらない。
</div>

---

# 4月28日（月）

<div class="diary-entry">
<div class="diary-date">??? - ???</div>

<span class="crossed">大丈夫、もう怖くない。</span>

<span class="crossed">やっと楽になれた。</span>

<span class="crossed">全部忘れられた。</span>
</div>

<br>

<div style="text-align: center;">
<span style="font-family: sans-serif; color: var(--red-ink); font-size: 1.3em;">
この日の記述は、別人の筆跡で書かれていた。
</span>
</div>

---

# 最後のページ

<div style="text-align: center; padding-top: 50px;">

<div class="memo" style="display: inline-block; transform: rotate(-2deg);">
このノートを見つけた あなたへ

もし職場に「入ったら記憶が飛ぶ場所」があったら

<span class="red">絶対に近づかないで。</span>

そして、周りの人の「目の下」を見て。

同じ場所に傷があったら...

<span class="red">もう手遅れ。</span>
</div>

</div>

<div style="text-align: right; margin-top: 50px; font-size: 0.9em; color: var(--ink-light);">
追記：このノートの持ち主は、現在も同じ会社で働いています。<br>
毎日笑顔で出社しています。<br>
左手の薬指は、問題なく曲がるようになりました。
</div>

---

<div class="ending">

# FIN

<div style="margin-top: 40px; color: var(--ink-light);">
〜 消えた30分 〜
</div>

<div class="memo" style="margin-top: 40px; display: inline-block;">
<span class="red">あなたの職場は、大丈夫ですか？</span>
</div>

</div>

