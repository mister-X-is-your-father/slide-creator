---
marp: true
theme: default
paginate: false
size: 16:9
style: |
  /* ================================ */
  /* ノート・手記風テンプレート       */
  /* ================================ */

  @import url('https://fonts.googleapis.com/css2?family=Yomogi&family=Klee+One&display=swap');

  :root {
    --paper: #FAFAFA;
    --line: #E5E7EB;
    --ink: #2D2D2D;
    --ink-light: #6B7280;
    --red: #DC2626;
    --blue: #3B82F6;
  }

  section {
    background:
      repeating-linear-gradient(
        transparent,
        transparent 31px,
        var(--line) 31px,
        var(--line) 32px
      ),
      var(--paper);
    font-family: "Yomogi", "Klee One", cursive;
    color: var(--ink);
    padding: 40px 60px;
    font-size: 24px;
    line-height: 1.8;
  }

  /* 日付・時刻 */
  .entry-date {
    font-size: 0.9em;
    color: var(--ink-light);
    margin-bottom: 15px;
    padding-bottom: 5px;
    border-bottom: 1px solid var(--line);
  }

  /* 本文 */
  .entry-text {
    font-size: 1.1em;
    line-height: 2;
    max-width: 900px;
  }

  /* 手書き風強調 */
  .underline { text-decoration: underline wavy var(--red); }
  .circled { border: 2px solid var(--red); border-radius: 50%; padding: 2px 8px; }
  .crossed { text-decoration: line-through; color: var(--ink-light); }
  .scribble { background: repeating-linear-gradient(45deg, transparent, transparent 2px, var(--ink-light) 2px, var(--ink-light) 3px); }

  /* 筆跡状態 */
  .handwriting-shaky { font-style: italic; letter-spacing: 0.05em; }
  .handwriting-rushed { font-size: 0.95em; letter-spacing: -0.02em; }
  .handwriting-large { font-size: 1.3em; font-weight: bold; }

  /* マージンメモ */
  .margin-note {
    position: absolute;
    right: 30px;
    font-size: 0.8em;
    color: var(--blue);
    max-width: 150px;
    text-align: right;
  }

  /* 図・スケッチ */
  .sketch-area {
    border: 1px dashed var(--ink-light);
    border-radius: 5px;
    padding: 20px;
    margin: 20px 0;
    text-align: center;
    background: rgba(255,255,255,0.5);
  }

  /* 貼り付け物風 */
  .attachment {
    background: #FFFDE7;
    border: 1px solid #FBC02D;
    padding: 10px 15px;
    margin: 15px 0;
    transform: rotate(-1deg);
    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
  }

  /* ページ状態 */
  .page-stained {
    background:
      radial-gradient(ellipse at 80% 20%, rgba(139,69,19,0.1) 0%, transparent 50%),
      repeating-linear-gradient(
        transparent,
        transparent 31px,
        var(--line) 31px,
        var(--line) 32px
      ),
      var(--paper);
  }

  .page-torn {
    clip-path: polygon(0 0, 100% 0, 100% 95%, 95% 100%, 90% 96%, 85% 100%, 80% 97%, 75% 100%, 70% 96%, 0 100%);
  }

  /* 区切り */
  .divider { text-align: center; margin: 30px 0; color: var(--ink-light); }

  /* 警告・重要 */
  .warning {
    background: #FEF2F2;
    border-left: 4px solid var(--red);
    padding: 10px 15px;
    margin: 15px 0;
  }

  /* ページ番号 */
  .page-num {
    position: absolute;
    bottom: 20px;
    right: 40px;
    font-size: 0.8em;
    color: var(--ink-light);
  }

  /* 最終ページ */
  .final-entry {
    font-size: 1.2em;
  }

  .final-entry .unanswered {
    color: var(--red);
    font-style: italic;
  }

---

<!-- 表紙 -->
<div style="text-align: center; padding-top: 100px;">

<div style="font-size: 0.9em; color: var(--ink-light);">
[ 発見されたノート ]
</div>

# タイトル

<div style="margin-top: 50px; font-size: 0.85em; color: var(--ink-light);">
○年○月○日 〜 ○月○日の記録
</div>

</div>

---

<!-- 通常エントリー例 -->
<div class="entry-date">
○月○日（曜日）
</div>

<div class="entry-text">
今日は普通の一日だった。

特に変わったことはない。<span class="underline">はずだった。</span>

夜、奇妙な音を聞いた気がする。
気のせいだと思いたい。
</div>

<div class="page-num">- 1 -</div>

---

<!-- 動揺エントリー例 -->
<section class="page-stained">

<div class="entry-date">
○月○日（曜日）深夜
</div>

<div class="entry-text handwriting-shaky">
また聞こえた。

今度は<span class="circled">確実に</span>聞こえた。

<span class="crossed">誰かがいる</span>

いや、そんなはずは...
</div>

<div class="margin-note">
後で確認すること：
- 窓の鍵
- 隣室の住人
</div>

<div class="page-num">- 5 -</div>

</section>

---

<!-- スケッチ付きエントリー例 -->
<div class="entry-date">
○月○日（曜日）
</div>

<div class="sketch-area">
[ 見たものの簡単なスケッチ ]
</div>

<div class="entry-text">
忘れないうちに描いておく。

これが何なのか、分からない。
</div>

<div class="page-num">- 8 -</div>

---

<!-- 最終エントリー例 -->
<section class="page-torn">

<div class="entry-date">
○月○日（曜日）
</div>

<div class="entry-text final-entry handwriting-rushed">
分かった。全部分かった。

でももう<span class="underline">時間がない</span>。

これを読んでいる人へ。

絶対に

</div>

<div class="warning">
[ ここで記録は途切れている ]
</div>

</section>
