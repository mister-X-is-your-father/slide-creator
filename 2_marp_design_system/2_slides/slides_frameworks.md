---
marp: true
theme: default
paginate: true
style: |
  /* ================================ */
  /* ビジネスフレームワーク           */
  /* 図解コンポーネント集             */
  /* ================================ */

  :root {
    --primary: #2563EB;
    --secondary: #7C3AED;
    --success: #10B981;
    --warning: #F59E0B;
    --danger: #EF4444;
    --info: #06B6D4;
    --dark: #1F2937;
    --gray: #6B7280;
    --light: #F3F4F6;
    --white: #FFFFFF;
    --blue-light: #DBEAFE;
    --green-light: #D1FAE5;
    --yellow-light: #FEF3C7;
    --red-light: #FEE2E2;
    --purple-light: #EDE9FE;
  }

  section {
    background: var(--white);
    font-family: "Noto Sans JP", "Hiragino Sans", sans-serif;
    color: var(--dark);
    padding: 40px;
  }

  h1 { color: var(--primary); font-size: 1.8em; margin-bottom: 0.5em; }
  h2 { color: var(--dark); font-size: 1.4em; margin-bottom: 0.5em; }

  /* ================================ */
  /* SWOT分析                         */
  /* ================================ */

  .swot {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    height: 400px;
  }
  .swot-box {
    border-radius: 12px;
    padding: 15px;
    display: flex;
    flex-direction: column;
  }
  .swot-title {
    font-weight: 700;
    font-size: 1.1em;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .swot-s { background: var(--blue-light); }
  .swot-s .swot-title { color: var(--primary); }
  .swot-w { background: var(--red-light); }
  .swot-w .swot-title { color: var(--danger); }
  .swot-o { background: var(--green-light); }
  .swot-o .swot-title { color: var(--success); }
  .swot-t { background: var(--yellow-light); }
  .swot-t .swot-title { color: var(--warning); }
  .swot-box ul { margin: 0; padding-left: 1.2em; font-size: 0.85em; }
  .swot-box li { margin: 4px 0; }
  .swot-label {
    position: absolute;
    font-size: 0.7em;
    color: var(--gray);
  }
  .swot-header {
    display: grid;
    grid-template-columns: 100px 1fr 1fr;
    gap: 10px;
    margin-bottom: 5px;
    font-size: 0.8em;
    color: var(--gray);
    text-align: center;
  }
  .swot-row-label {
    writing-mode: vertical-rl;
    text-orientation: mixed;
    font-size: 0.8em;
    color: var(--gray);
    text-align: center;
    padding: 0 10px;
  }

  /* ================================ */
  /* PEST分析                         */
  /* ================================ */

  .pest {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
  }
  .pest-box {
    border-radius: 12px;
    padding: 15px;
    text-align: center;
  }
  .pest-icon { font-size: 2em; margin-bottom: 8px; }
  .pest-title { font-weight: 700; margin-bottom: 10px; }
  .pest-p { background: var(--blue-light); color: var(--primary); }
  .pest-e { background: var(--green-light); color: var(--success); }
  .pest-s { background: var(--yellow-light); color: var(--warning); }
  .pest-t { background: var(--purple-light); color: var(--secondary); }
  .pest-box ul { text-align: left; margin: 0; padding-left: 1em; font-size: 0.8em; color: var(--dark); }

  /* ================================ */
  /* 3C分析                           */
  /* ================================ */

  .three-c {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
  }
  .three-c-circle {
    width: 180px;
    height: 180px;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 20px;
    box-sizing: border-box;
  }
  .three-c-customer { background: var(--blue-light); border: 3px solid var(--primary); }
  .three-c-competitor { background: var(--red-light); border: 3px solid var(--danger); }
  .three-c-company { background: var(--green-light); border: 3px solid var(--success); }
  .three-c-icon { font-size: 2em; margin-bottom: 5px; }
  .three-c-title { font-weight: 700; font-size: 1em; }
  .three-c-desc { font-size: 0.75em; color: var(--gray); margin-top: 5px; }
  .three-c-arrow {
    font-size: 2em;
    color: var(--gray);
  }

  /* ================================ */
  /* 4P分析                           */
  /* ================================ */

  .four-p {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
  }
  .four-p-box {
    border-radius: 12px;
    padding: 20px 15px;
    text-align: center;
    border: 2px solid;
  }
  .four-p-product { background: var(--blue-light); border-color: var(--primary); }
  .four-p-price { background: var(--green-light); border-color: var(--success); }
  .four-p-place { background: var(--yellow-light); border-color: var(--warning); }
  .four-p-promotion { background: var(--purple-light); border-color: var(--secondary); }
  .four-p-icon { font-size: 2.5em; margin-bottom: 10px; }
  .four-p-title { font-weight: 700; font-size: 1.1em; margin-bottom: 5px; }
  .four-p-sub { font-size: 0.8em; color: var(--gray); }

  /* ================================ */
  /* 2x2マトリックス                  */
  /* ================================ */

  .matrix-2x2 {
    position: relative;
    width: 500px;
    height: 400px;
    margin: 0 auto;
  }
  .matrix-axis-y {
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 2px;
    background: var(--gray);
  }
  .matrix-axis-x {
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    height: 2px;
    background: var(--gray);
  }
  .matrix-label {
    position: absolute;
    font-size: 0.85em;
    color: var(--gray);
    font-weight: 500;
  }
  .matrix-label-top { top: -25px; left: 50%; transform: translateX(-50%); }
  .matrix-label-bottom { bottom: -25px; left: 50%; transform: translateX(-50%); }
  .matrix-label-left { left: -60px; top: 50%; transform: translateY(-50%) rotate(-90deg); }
  .matrix-label-right { right: -60px; top: 50%; transform: translateY(-50%) rotate(90deg); }
  .matrix-quadrant {
    position: absolute;
    width: 48%;
    height: 48%;
    border-radius: 10px;
    padding: 10px;
    font-size: 0.85em;
    display: flex;
    flex-direction: column;
  }
  .matrix-q1 { top: 1%; right: 1%; background: var(--green-light); }
  .matrix-q2 { top: 1%; left: 1%; background: var(--blue-light); }
  .matrix-q3 { bottom: 1%; left: 1%; background: var(--light); }
  .matrix-q4 { bottom: 1%; right: 1%; background: var(--yellow-light); }
  .matrix-q-title { font-weight: 700; margin-bottom: 5px; }

  /* ================================ */
  /* ファネル図                       */
  /* ================================ */

  .funnel {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0;
  }
  .funnel-step {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 50px;
    color: var(--white);
    font-weight: 600;
    position: relative;
  }
  .funnel-step:nth-child(1) { width: 100%; background: var(--primary); border-radius: 8px 8px 0 0; }
  .funnel-step:nth-child(2) { width: 85%; background: var(--info); }
  .funnel-step:nth-child(3) { width: 70%; background: var(--success); }
  .funnel-step:nth-child(4) { width: 55%; background: var(--warning); }
  .funnel-step:nth-child(5) { width: 40%; background: var(--danger); border-radius: 0 0 8px 8px; }
  .funnel-num {
    position: absolute;
    right: -60px;
    font-size: 0.9em;
    color: var(--gray);
  }

  /* ================================ */
  /* ロードマップ/年表                */
  /* ================================ */

  .roadmap {
    position: relative;
    padding: 20px 0;
  }
  .roadmap-line {
    position: absolute;
    top: 50%;
    left: 5%;
    right: 5%;
    height: 4px;
    background: linear-gradient(90deg, var(--primary), var(--secondary));
    border-radius: 2px;
  }
  .roadmap-items {
    display: flex;
    justify-content: space-between;
    position: relative;
  }
  .roadmap-item {
    text-align: center;
    flex: 1;
  }
  .roadmap-dot {
    width: 20px;
    height: 20px;
    background: var(--primary);
    border-radius: 50%;
    margin: 0 auto 10px;
    border: 3px solid var(--white);
    box-shadow: 0 0 0 3px var(--primary);
    position: relative;
    z-index: 1;
  }
  .roadmap-item:nth-child(2) .roadmap-dot { background: var(--info); box-shadow: 0 0 0 3px var(--info); }
  .roadmap-item:nth-child(3) .roadmap-dot { background: var(--success); box-shadow: 0 0 0 3px var(--success); }
  .roadmap-item:nth-child(4) .roadmap-dot { background: var(--secondary); box-shadow: 0 0 0 3px var(--secondary); }
  .roadmap-date { font-weight: 700; font-size: 0.9em; color: var(--primary); }
  .roadmap-title { font-weight: 600; margin: 5px 0; }
  .roadmap-desc { font-size: 0.8em; color: var(--gray); }

  /* ================================ */
  /* KPIダッシュボード                */
  /* ================================ */

  .kpi-dashboard {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
  }
  .kpi-card {
    background: var(--light);
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    border-left: 4px solid var(--primary);
  }
  .kpi-card:nth-child(2) { border-left-color: var(--success); }
  .kpi-card:nth-child(3) { border-left-color: var(--warning); }
  .kpi-card:nth-child(4) { border-left-color: var(--danger); }
  .kpi-value {
    font-size: 2.5em;
    font-weight: 700;
    color: var(--primary);
  }
  .kpi-card:nth-child(2) .kpi-value { color: var(--success); }
  .kpi-card:nth-child(3) .kpi-value { color: var(--warning); }
  .kpi-card:nth-child(4) .kpi-value { color: var(--danger); }
  .kpi-label { font-size: 0.9em; color: var(--gray); margin-top: 5px; }
  .kpi-change { font-size: 0.8em; margin-top: 8px; }
  .kpi-up { color: var(--success); }
  .kpi-down { color: var(--danger); }

  /* ================================ */
  /* 因果関係図                       */
  /* ================================ */

  .cause-effect {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;
  }
  .cause-box, .effect-box {
    padding: 20px 30px;
    border-radius: 12px;
    text-align: center;
    min-width: 150px;
  }
  .cause-box {
    background: var(--blue-light);
    border: 2px solid var(--primary);
  }
  .effect-box {
    background: var(--green-light);
    border: 2px solid var(--success);
  }
  .cause-effect-arrow {
    font-size: 2.5em;
    color: var(--gray);
  }
  .cause-label, .effect-label {
    font-size: 0.75em;
    color: var(--gray);
    margin-bottom: 5px;
  }
  .cause-text, .effect-text {
    font-weight: 600;
    font-size: 1.1em;
  }

  /* ================================ */
  /* 対立関係図                       */
  /* ================================ */

  .versus {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 30px;
  }
  .versus-box {
    padding: 25px 40px;
    border-radius: 12px;
    text-align: center;
    min-width: 180px;
  }
  .versus-a {
    background: var(--blue-light);
    border: 3px solid var(--primary);
  }
  .versus-b {
    background: var(--red-light);
    border: 3px solid var(--danger);
  }
  .versus-icon { font-size: 2em; margin-bottom: 10px; }
  .versus-title { font-weight: 700; font-size: 1.2em; }
  .versus-vs {
    font-size: 2em;
    font-weight: 900;
    color: var(--warning);
    text-shadow: 2px 2px 0 var(--dark);
  }

  /* ================================ */
  /* グループ化                       */
  /* ================================ */

  .grouping {
    display: flex;
    gap: 20px;
    justify-content: center;
  }
  .group-container {
    border: 2px dashed var(--gray);
    border-radius: 15px;
    padding: 15px;
  }
  .group-title {
    background: var(--dark);
    color: var(--white);
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 0.85em;
    font-weight: 600;
    margin-bottom: 10px;
    display: inline-block;
  }
  .group-items {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
  }
  .group-item {
    background: var(--light);
    padding: 10px 15px;
    border-radius: 8px;
    font-size: 0.9em;
  }
  .group-a { border-color: var(--primary); }
  .group-a .group-title { background: var(--primary); }
  .group-b { border-color: var(--success); }
  .group-b .group-title { background: var(--success); }

  /* ================================ */
  /* プロセスステップ（横）           */
  /* ================================ */

  .process-h {
    display: flex;
    align-items: center;
    gap: 0;
  }
  .process-step {
    background: var(--primary);
    color: var(--white);
    padding: 15px 25px 15px 35px;
    clip-path: polygon(0 0, calc(100% - 15px) 0, 100% 50%, calc(100% - 15px) 100%, 0 100%, 15px 50%);
    font-weight: 600;
    font-size: 0.9em;
    margin-left: -15px;
  }
  .process-step:first-child {
    clip-path: polygon(0 0, calc(100% - 15px) 0, 100% 50%, calc(100% - 15px) 100%, 0 100%);
    margin-left: 0;
    padding-left: 20px;
    border-radius: 8px 0 0 8px;
  }
  .process-step:last-child {
    border-radius: 0 8px 8px 0;
  }
  .process-step:nth-child(2) { background: var(--info); }
  .process-step:nth-child(3) { background: var(--success); }
  .process-step:nth-child(4) { background: var(--warning); }
  .process-step:nth-child(5) { background: var(--danger); }

  /* ================================ */
  /* 比較カード                       */
  /* ================================ */

  .compare-cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
  }
  .compare-card {
    border: 2px solid var(--light);
    border-radius: 12px;
    overflow: hidden;
  }
  .compare-card-header {
    background: var(--primary);
    color: var(--white);
    padding: 15px;
    text-align: center;
    font-weight: 700;
  }
  .compare-card:nth-child(2) .compare-card-header { background: var(--success); }
  .compare-card:nth-child(3) .compare-card-header { background: var(--secondary); }
  .compare-card-body {
    padding: 15px;
  }
  .compare-card-price {
    text-align: center;
    font-size: 2em;
    font-weight: 700;
    color: var(--dark);
    margin: 10px 0;
  }
  .compare-card-price span { font-size: 0.5em; color: var(--gray); }
  .compare-card ul {
    margin: 0;
    padding: 0;
    list-style: none;
  }
  .compare-card li {
    padding: 8px 0;
    border-bottom: 1px solid var(--light);
    font-size: 0.85em;
  }
  .compare-card li:last-child { border-bottom: none; }

  /* ================================ */
  /* アラートボックス                 */
  /* ================================ */

  .alert {
    padding: 15px 20px;
    border-radius: 8px;
    margin: 10px 0;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }
  .alert-icon { font-size: 1.3em; flex-shrink: 0; }
  .alert-info { background: var(--blue-light); border-left: 4px solid var(--primary); }
  .alert-success { background: var(--green-light); border-left: 4px solid var(--success); }
  .alert-warning { background: var(--yellow-light); border-left: 4px solid var(--warning); }
  .alert-danger { background: var(--red-light); border-left: 4px solid var(--danger); }

  /* ================================ */
  /* 引用ボックス                     */
  /* ================================ */

  .quote-box {
    background: var(--light);
    border-left: 5px solid var(--secondary);
    padding: 20px 25px;
    border-radius: 0 12px 12px 0;
    font-style: italic;
    position: relative;
  }
  .quote-box::before {
    content: '"';
    font-size: 4em;
    color: var(--secondary);
    opacity: 0.3;
    position: absolute;
    top: -10px;
    left: 10px;
    font-family: Georgia, serif;
  }
  .quote-author {
    text-align: right;
    margin-top: 10px;
    font-style: normal;
    color: var(--gray);
    font-size: 0.9em;
  }

  /* ================================ */
  /* カードグリッド                   */
  /* ================================ */

  .card-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
  }
  .card {
    background: var(--white);
    border: 1px solid var(--light);
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  }
  .card-icon {
    font-size: 2em;
    margin-bottom: 10px;
  }
  .card-title {
    font-weight: 700;
    margin-bottom: 8px;
  }
  .card-desc {
    font-size: 0.85em;
    color: var(--gray);
  }

  /* ================================ */
  /* タイムライン縦                   */
  /* ================================ */

  .timeline-vertical {
    position: relative;
    padding-left: 30px;
  }
  .timeline-vertical::before {
    content: "";
    position: absolute;
    left: 8px;
    top: 0;
    bottom: 0;
    width: 3px;
    background: var(--primary);
  }
  .tl-item {
    position: relative;
    padding-bottom: 20px;
  }
  .tl-dot {
    position: absolute;
    left: -26px;
    width: 14px;
    height: 14px;
    background: var(--primary);
    border-radius: 50%;
    border: 3px solid var(--white);
  }
  .tl-date {
    font-size: 0.8em;
    color: var(--primary);
    font-weight: 600;
  }
  .tl-title {
    font-weight: 600;
    margin: 3px 0;
  }
  .tl-desc {
    font-size: 0.85em;
    color: var(--gray);
  }

  /* ================================ */
  /* バッジ/タグ                      */
  /* ================================ */

  .badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.8em;
    font-weight: 600;
  }
  .badge-primary { background: var(--primary); color: var(--white); }
  .badge-success { background: var(--success); color: var(--white); }
  .badge-warning { background: var(--warning); color: var(--white); }
  .badge-danger { background: var(--danger); color: var(--white); }
  .badge-outline {
    background: transparent;
    border: 2px solid var(--primary);
    color: var(--primary);
  }

  /* ================================ */
  /* プログレスバー                   */
  /* ================================ */

  .progress-container {
    margin: 15px 0;
  }
  .progress-label {
    display: flex;
    justify-content: space-between;
    margin-bottom: 5px;
    font-size: 0.9em;
  }
  .progress-bar {
    height: 12px;
    background: var(--light);
    border-radius: 6px;
    overflow: hidden;
  }
  .progress-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--primary), var(--info));
    border-radius: 6px;
  }

  /* ================================ */
  /* 統計カード                       */
  /* ================================ */

  .stat-cards {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
  }
  .stat-card {
    background: linear-gradient(135deg, var(--primary), var(--info));
    color: var(--white);
    padding: 20px;
    border-radius: 12px;
    text-align: center;
  }
  .stat-card:nth-child(2) { background: linear-gradient(135deg, var(--success), #34D399); }
  .stat-card:nth-child(3) { background: linear-gradient(135deg, var(--warning), #FBBF24); }
  .stat-card:nth-child(4) { background: linear-gradient(135deg, var(--secondary), #A78BFA); }
  .stat-value { font-size: 2.5em; font-weight: 700; }
  .stat-label { font-size: 0.9em; opacity: 0.9; }

  /* ================================ */
  /* チェックリスト                   */
  /* ================================ */

  .checklist-pro {
    background: var(--light);
    border-radius: 12px;
    padding: 20px;
  }
  .check-item-pro {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 0;
    border-bottom: 1px solid var(--white);
  }
  .check-item-pro:last-child { border-bottom: none; }
  .check-icon-pro {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.8em;
    flex-shrink: 0;
  }
  .check-done { background: var(--success); color: var(--white); }
  .check-pending { background: var(--white); border: 2px solid var(--gray); }

  /* ================================ */
  /* 比較表（横）                     */
  /* ================================ */

  .compare-table-h {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9em;
  }
  .compare-table-h th {
    background: var(--dark);
    color: var(--white);
    padding: 12px;
    text-align: left;
  }
  .compare-table-h th:first-child { border-radius: 8px 0 0 0; }
  .compare-table-h th:last-child { border-radius: 0 8px 0 0; }
  .compare-table-h td {
    padding: 12px;
    border-bottom: 1px solid var(--light);
  }
  .compare-table-h tr:nth-child(even) { background: var(--light); }
  .compare-table-h .check { color: var(--success); font-size: 1.2em; }
  .compare-table-h .cross { color: var(--danger); font-size: 1.2em; }

---

<!-- スライド1: タイトル -->

# ビジネスフレームワーク図解集

**SWOT・PEST・3C・4Pから、マトリックス、ファネルまで**

収集サイト: presentation.style / tridge.work / fbicenter / anagrams / nijibox / virtual-planner / liginc ほか

---

<!-- スライド2: SWOT分析 -->

## SWOT分析

<div class="swot">
<div class="swot-box swot-s">
<div class="swot-title">💪 Strengths（強み）</div>

- 高い技術力
- ブランド認知度
- 優秀な人材

</div>
<div class="swot-box swot-w">
<div class="swot-title">😓 Weaknesses（弱み）</div>

- 資金力不足
- 販路の限定
- 認知度低い

</div>
<div class="swot-box swot-o">
<div class="swot-title">🌟 Opportunities（機会）</div>

- 市場拡大
- 規制緩和
- 新技術登場

</div>
<div class="swot-box swot-t">
<div class="swot-title">⚠️ Threats（脅威）</div>

- 競合参入
- 景気後退
- 法規制強化

</div>
</div>

---

<!-- スライド3: PEST分析 -->

## PEST分析

<div class="pest">
<div class="pest-box pest-p">
<div class="pest-icon">🏛️</div>
<div class="pest-title">Politics</div>

- 法規制の変化
- 税制改正
- 政治的安定性

</div>
<div class="pest-box pest-e">
<div class="pest-icon">💹</div>
<div class="pest-title">Economy</div>

- GDP成長率
- 為替レート
- 金利動向

</div>
<div class="pest-box pest-s">
<div class="pest-icon">👥</div>
<div class="pest-title">Society</div>

- 人口動態
- ライフスタイル
- 価値観の変化

</div>
<div class="pest-box pest-t">
<div class="pest-icon">🔬</div>
<div class="pest-title">Technology</div>

- AI・DX推進
- 特許・研究開発
- インフラ整備

</div>
</div>

---

<!-- スライド4: 3C分析 -->

## 3C分析

<div class="three-c">
<div class="three-c-circle three-c-customer">
<div class="three-c-icon">👤</div>
<div class="three-c-title">Customer</div>
<div class="three-c-desc">顧客・市場</div>
</div>
<div class="three-c-arrow">⟷</div>
<div class="three-c-circle three-c-competitor">
<div class="three-c-icon">🏢</div>
<div class="three-c-title">Competitor</div>
<div class="three-c-desc">競合</div>
</div>
<div class="three-c-arrow">⟷</div>
<div class="three-c-circle three-c-company">
<div class="three-c-icon">🏠</div>
<div class="three-c-title">Company</div>
<div class="three-c-desc">自社</div>
</div>
</div>

---

<!-- スライド5: 4P分析 -->

## 4P分析（マーケティングミックス）

<div class="four-p">
<div class="four-p-box four-p-product">
<div class="four-p-icon">📦</div>
<div class="four-p-title">Product</div>
<div class="four-p-sub">製品・サービス</div>
</div>
<div class="four-p-box four-p-price">
<div class="four-p-icon">💰</div>
<div class="four-p-title">Price</div>
<div class="four-p-sub">価格</div>
</div>
<div class="four-p-box four-p-place">
<div class="four-p-icon">🏪</div>
<div class="four-p-title">Place</div>
<div class="four-p-sub">流通・販路</div>
</div>
<div class="four-p-box four-p-promotion">
<div class="four-p-icon">📣</div>
<div class="four-p-title">Promotion</div>
<div class="four-p-sub">販売促進</div>
</div>
</div>

---

<!-- スライド6: 2x2マトリックス -->

## 2x2マトリックス（ポジショニング）

<div class="matrix-2x2">
<div class="matrix-axis-y"></div>
<div class="matrix-axis-x"></div>
<span class="matrix-label matrix-label-top">高い</span>
<span class="matrix-label matrix-label-bottom">低い</span>
<span class="matrix-label matrix-label-left">緊急度</span>
<span class="matrix-label matrix-label-right">重要度</span>
<div class="matrix-quadrant matrix-q1">
<div class="matrix-q-title">🔥 今すぐやる</div>
重要かつ緊急なタスク
</div>
<div class="matrix-quadrant matrix-q2">
<div class="matrix-q-title">📅 計画する</div>
重要だが緊急でない
</div>
<div class="matrix-quadrant matrix-q3">
<div class="matrix-q-title">🗑️ やらない</div>
重要でも緊急でもない
</div>
<div class="matrix-quadrant matrix-q4">
<div class="matrix-q-title">👋 委任する</div>
緊急だが重要でない
</div>
</div>

---

<!-- スライド7: ファネル図 -->

## ファネル図（コンバージョン）

<div class="funnel">
<div class="funnel-step">認知 (Awareness) <span class="funnel-num">10,000</span></div>
<div class="funnel-step">興味 (Interest) <span class="funnel-num">5,000</span></div>
<div class="funnel-step">検討 (Consideration) <span class="funnel-num">2,000</span></div>
<div class="funnel-step">意思決定 (Decision) <span class="funnel-num">500</span></div>
<div class="funnel-step">購入 (Action) <span class="funnel-num">200</span></div>
</div>

---

<!-- スライド8: ロードマップ -->

## ロードマップ / 年表

<div class="roadmap">
<div class="roadmap-line"></div>
<div class="roadmap-items">
<div class="roadmap-item">
<div class="roadmap-dot"></div>
<div class="roadmap-date">2024 Q1</div>
<div class="roadmap-title">企画・調査</div>
<div class="roadmap-desc">市場調査と要件定義</div>
</div>
<div class="roadmap-item">
<div class="roadmap-dot"></div>
<div class="roadmap-date">2024 Q2</div>
<div class="roadmap-title">設計・開発</div>
<div class="roadmap-desc">プロトタイプ作成</div>
</div>
<div class="roadmap-item">
<div class="roadmap-dot"></div>
<div class="roadmap-date">2024 Q3</div>
<div class="roadmap-title">テスト</div>
<div class="roadmap-desc">ベータ版リリース</div>
</div>
<div class="roadmap-item">
<div class="roadmap-dot"></div>
<div class="roadmap-date">2024 Q4</div>
<div class="roadmap-title">ローンチ</div>
<div class="roadmap-desc">正式リリース</div>
</div>
</div>
</div>

---

<!-- スライド9: KPIダッシュボード -->

## KPIダッシュボード

<div class="kpi-dashboard">
<div class="kpi-card">
<div class="kpi-value">1.2M</div>
<div class="kpi-label">月間PV</div>
<div class="kpi-change kpi-up">↑ 15.3%</div>
</div>
<div class="kpi-card">
<div class="kpi-value">45K</div>
<div class="kpi-label">新規ユーザー</div>
<div class="kpi-change kpi-up">↑ 8.7%</div>
</div>
<div class="kpi-card">
<div class="kpi-value">3.2%</div>
<div class="kpi-label">CVR</div>
<div class="kpi-change kpi-down">↓ 0.5%</div>
</div>
<div class="kpi-card">
<div class="kpi-value">¥850</div>
<div class="kpi-label">CPA</div>
<div class="kpi-change kpi-up">↑ 改善</div>
</div>
</div>

---

<!-- スライド10: 因果関係図 -->

## 因果関係図

<div class="cause-effect">
<div class="cause-box">
<div class="cause-label">原因 / INPUT</div>
<div class="cause-text">マーケティング投資</div>
</div>
<div class="cause-effect-arrow">➡️</div>
<div class="effect-box">
<div class="effect-label">結果 / OUTPUT</div>
<div class="effect-text">売上増加</div>
</div>
</div>

<br>

<div class="cause-effect">
<div class="cause-box">
<div class="cause-label">問題</div>
<div class="cause-text">顧客離反率の上昇</div>
</div>
<div class="cause-effect-arrow">➡️</div>
<div class="effect-box">
<div class="effect-label">解決策</div>
<div class="effect-text">カスタマーサポート強化</div>
</div>
</div>

---

<!-- スライド11: 対立関係図 -->

## 対立関係図（VS）

<div class="versus">
<div class="versus-box versus-a">
<div class="versus-icon">🏢</div>
<div class="versus-title">オフライン</div>
</div>
<div class="versus-vs">VS</div>
<div class="versus-box versus-b">
<div class="versus-icon">💻</div>
<div class="versus-title">オンライン</div>
</div>
</div>

---

<!-- スライド12: グループ化 -->

## グループ化

<div class="grouping">
<div class="group-container group-a">
<span class="group-title">フロントエンド</span>
<div class="group-items">
<span class="group-item">HTML</span>
<span class="group-item">CSS</span>
<span class="group-item">JavaScript</span>
<span class="group-item">React</span>
</div>
</div>
<div class="group-container group-b">
<span class="group-title">バックエンド</span>
<div class="group-items">
<span class="group-item">Python</span>
<span class="group-item">Node.js</span>
<span class="group-item">PostgreSQL</span>
<span class="group-item">Redis</span>
</div>
</div>
</div>

---

<!-- スライド13: プロセスステップ（シェブロン） -->

## プロセスステップ（シェブロン）

<div class="process-h">
<div class="process-step">1. 要件定義</div>
<div class="process-step">2. 設計</div>
<div class="process-step">3. 開発</div>
<div class="process-step">4. テスト</div>
<div class="process-step">5. リリース</div>
</div>

---

<!-- スライド14: 比較カード（料金プラン） -->

## 比較カード

<div class="compare-cards">
<div class="compare-card">
<div class="compare-card-header">Basic</div>
<div class="compare-card-body">
<div class="compare-card-price">¥980<span>/月</span></div>

- 基本機能
- 5GBストレージ
- メールサポート

</div>
</div>
<div class="compare-card">
<div class="compare-card-header">Pro</div>
<div class="compare-card-body">
<div class="compare-card-price">¥2,980<span>/月</span></div>

- 全機能
- 50GBストレージ
- 優先サポート

</div>
</div>
<div class="compare-card">
<div class="compare-card-header">Enterprise</div>
<div class="compare-card-body">
<div class="compare-card-price">要問合せ</div>

- カスタマイズ
- 無制限ストレージ
- 専任担当者

</div>
</div>
</div>

---

<!-- スライド15: アラートボックス -->

## アラートボックス

<div class="alert alert-info">
<span class="alert-icon">ℹ️</span>
<div><strong>お知らせ:</strong> 新機能がリリースされました。詳しくはドキュメントをご覧ください。</div>
</div>

<div class="alert alert-success">
<span class="alert-icon">✅</span>
<div><strong>成功:</strong> データが正常に保存されました。</div>
</div>

<div class="alert alert-warning">
<span class="alert-icon">⚠️</span>
<div><strong>警告:</strong> ストレージ容量が80%を超えています。</div>
</div>

<div class="alert alert-danger">
<span class="alert-icon">🚨</span>
<div><strong>エラー:</strong> 接続に失敗しました。再度お試しください。</div>
</div>

---

<!-- スライド16: 引用ボックス -->

## 引用ボックス

<div class="quote-box">
シンプルであることは、複雑であることよりもむずかしいときがある。物事をシンプルにするためには、懸命に努力して思考を明瞭にしなければならないからだ。
<div class="quote-author">— スティーブ・ジョブズ</div>
</div>

---

<!-- スライド17: カードグリッド -->

## カードグリッド

<div class="card-grid">
<div class="card">
<div class="card-icon">📊</div>
<div class="card-title">データ分析</div>
<div class="card-desc">ビッグデータを活用した高度な分析</div>
</div>
<div class="card">
<div class="card-icon">🔒</div>
<div class="card-title">セキュリティ</div>
<div class="card-desc">最新の暗号化技術で安全を確保</div>
</div>
<div class="card">
<div class="card-icon">🚀</div>
<div class="card-title">高速処理</div>
<div class="card-desc">レスポンスタイムを大幅に改善</div>
</div>
<div class="card">
<div class="card-icon">🌐</div>
<div class="card-title">グローバル対応</div>
<div class="card-desc">多言語・多通貨に対応</div>
</div>
<div class="card">
<div class="card-icon">📱</div>
<div class="card-title">モバイル最適化</div>
<div class="card-desc">あらゆるデバイスで快適に</div>
</div>
<div class="card">
<div class="card-icon">🤝</div>
<div class="card-title">サポート</div>
<div class="card-desc">24時間365日対応</div>
</div>
</div>

---

<!-- スライド18: タイムライン縦 -->

## タイムライン（縦）

<div class="timeline-vertical">
<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-date">2020年</div>
<div class="tl-title">会社設立</div>
<div class="tl-desc">東京でスタートアップとして創業</div>
</div>
<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-date">2021年</div>
<div class="tl-title">シリーズA調達</div>
<div class="tl-desc">5億円の資金調達に成功</div>
</div>
<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-date">2022年</div>
<div class="tl-title">海外展開</div>
<div class="tl-desc">アジア5カ国でサービス開始</div>
</div>
<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-date">2023年</div>
<div class="tl-title">100万ユーザー突破</div>
<div class="tl-desc">累計ユーザー数が100万人を達成</div>
</div>
</div>

---

<!-- スライド19: バッジ・タグ -->

## バッジ・タグ

<span class="badge badge-primary">新機能</span>
<span class="badge badge-success">完了</span>
<span class="badge badge-warning">進行中</span>
<span class="badge badge-danger">重要</span>
<span class="badge badge-outline">カスタム</span>

---

<!-- スライド20: プログレスバー -->

## プログレスバー

<div class="progress-container">
<div class="progress-label"><span>プロジェクトA</span><span>75%</span></div>
<div class="progress-bar"><div class="progress-fill" style="width: 75%;"></div></div>
</div>

<div class="progress-container">
<div class="progress-label"><span>プロジェクトB</span><span>45%</span></div>
<div class="progress-bar"><div class="progress-fill" style="width: 45%;"></div></div>
</div>

<div class="progress-container">
<div class="progress-label"><span>プロジェクトC</span><span>90%</span></div>
<div class="progress-bar"><div class="progress-fill" style="width: 90%;"></div></div>
</div>

---

<!-- スライド21: 統計カード -->

## 統計カード（グラデーション）

<div class="stat-cards">
<div class="stat-card">
<div class="stat-value">256</div>
<div class="stat-label">プロジェクト</div>
</div>
<div class="stat-card">
<div class="stat-value">1,024</div>
<div class="stat-label">クライアント</div>
</div>
<div class="stat-card">
<div class="stat-value">98%</div>
<div class="stat-label">満足度</div>
</div>
<div class="stat-card">
<div class="stat-value">50+</div>
<div class="stat-label">受賞歴</div>
</div>
</div>

---

<!-- スライド22: チェックリスト -->

## チェックリスト

<div class="checklist-pro">
<div class="check-item-pro">
<span class="check-icon-pro check-done">✓</span>
<span>要件定義書の作成</span>
</div>
<div class="check-item-pro">
<span class="check-icon-pro check-done">✓</span>
<span>デザインカンプの承認</span>
</div>
<div class="check-item-pro">
<span class="check-icon-pro check-done">✓</span>
<span>データベース設計</span>
</div>
<div class="check-item-pro">
<span class="check-icon-pro check-pending"></span>
<span>API開発</span>
</div>
<div class="check-item-pro">
<span class="check-icon-pro check-pending"></span>
<span>フロントエンド実装</span>
</div>
</div>

---

<!-- スライド23: 比較表 -->

## 比較表

<table class="compare-table-h">
<tr>
<th>機能</th>
<th>Basic</th>
<th>Pro</th>
<th>Enterprise</th>
</tr>
<tr>
<td>ユーザー数</td>
<td>5人まで</td>
<td>50人まで</td>
<td>無制限</td>
</tr>
<tr>
<td>ストレージ</td>
<td>10GB</td>
<td>100GB</td>
<td>無制限</td>
</tr>
<tr>
<td>API連携</td>
<td><span class="cross">✕</span></td>
<td><span class="check">✓</span></td>
<td><span class="check">✓</span></td>
</tr>
<tr>
<td>優先サポート</td>
<td><span class="cross">✕</span></td>
<td><span class="check">✓</span></td>
<td><span class="check">✓</span></td>
</tr>
<tr>
<td>SLA保証</td>
<td><span class="cross">✕</span></td>
<td><span class="cross">✕</span></td>
<td><span class="check">✓</span></td>
</tr>
</table>

---

<!-- スライド24: まとめ -->

## 図解パターンまとめ

| カテゴリ | パターン |
|---------|---------|
| フレームワーク | SWOT, PEST, 3C, 4P |
| マトリックス | 2x2, ポジショニング |
| 流れ | ファネル, ロードマップ, タイムライン |
| 関係性 | 因果関係, 対立, グループ化 |
| データ | KPI, 統計カード, プログレス |
| UI部品 | アラート, カード, バッジ, 比較表 |

**参考サイト**: presentation.style / tridge.work / fbicenter / anagrams / nijibox / liginc / raku-pre.com
