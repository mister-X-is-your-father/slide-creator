---
marp: true
theme: default
paginate: true
style: |
  @import url('./theme/components.css');
  :root {
    --primary: #2563eb;
    --secondary: #64748b;
    --accent: #f59e0b;
    --background: #ffffff;
    --text: #1e293b;
    --code-bg: #f1f5f9;
    --success: #10b981;
    --error: #ef4444;
    --warning: #f59e0b;
    --border: #e2e8f0;
  }
  section {
    background-color: var(--background);
    color: var(--text);
    font-family: 'Noto Sans CJK JP', 'Noto Sans JP', sans-serif;
    padding: 40px;
  }
  h1 {
    color: var(--primary);
    border-bottom: 3px solid var(--primary);
    padding-bottom: 0.3em;
  }
  h2 { color: var(--primary); }
  /* タイトルスライド */
  .title-slide {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    text-align: center;
  }
  .title-slide h1 {
    font-size: 2.8em;
    border-bottom: none;
    margin-bottom: 0.3em;
  }
  .title-slide p {
    font-size: 1.4em;
    color: var(--secondary);
  }
  /* セクションヘッダー */
  .section-header {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    background: linear-gradient(135deg, var(--primary) 0%, #1d4ed8 100%);
    color: white;
    text-align: center;
    margin: -40px;
    padding: 40px;
  }
  .section-header h1 {
    color: white;
    border-bottom: none;
    font-size: 3em;
  }
  .section-header p { color: rgba(255,255,255,0.8); font-size: 1.3em; }
  /* 2カラムレイアウト */
  .two-column {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2em;
  }
  /* 3カラムレイアウト */
  .three-column {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 1.5em;
  }
  /* 4カラムレイアウト */
  .four-column {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1em;
  }
  /* メトリックカード */
  .metric-card {
    background: linear-gradient(135deg, var(--code-bg) 0%, white 100%);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5em;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  }
  .metric-card .number {
    font-size: 3em;
    font-weight: bold;
    color: var(--primary);
    line-height: 1.2;
  }
  .metric-card .label {
    font-size: 1em;
    color: var(--secondary);
    margin-top: 0.5em;
  }
  .metric-card .change { font-size: 0.9em; margin-top: 0.3em; }
  .metric-card .change.positive { color: var(--success); }
  .metric-card .change.negative { color: var(--error); }
  /* 大きな数値 */
  .big-number {
    text-align: center;
    padding: 1em;
  }
  .big-number .value {
    font-size: 5em;
    font-weight: bold;
    color: var(--primary);
    line-height: 1;
  }
  .big-number .unit {
    font-size: 2em;
    color: var(--secondary);
  }
  .big-number .description {
    font-size: 1.2em;
    color: var(--text);
    margin-top: 0.5em;
  }
  /* 進捗バー */
  .progress-bar {
    background: var(--code-bg);
    border-radius: 10px;
    height: 24px;
    overflow: hidden;
    margin: 0.5em 0;
  }
  .progress-bar .fill {
    height: 100%;
    background: linear-gradient(90deg, var(--primary) 0%, #3b82f6 100%);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding-right: 10px;
    color: white;
    font-weight: bold;
    font-size: 0.8em;
  }
  /* 横フロー */
  .flow-horizontal {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0;
  }
  .flow-horizontal .flow-item {
    background: var(--primary);
    color: white;
    padding: 1em 1.5em;
    border-radius: 8px;
    text-align: center;
    min-width: 120px;
  }
  .flow-horizontal .flow-arrow {
    font-size: 2em;
    color: var(--primary);
    padding: 0 0.3em;
  }
  /* 縦フロー */
  .flow-vertical {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0;
  }
  .flow-vertical .flow-item {
    background: var(--primary);
    color: white;
    padding: 1em 2em;
    border-radius: 8px;
    text-align: center;
    min-width: 200px;
  }
  .flow-vertical .flow-arrow {
    font-size: 2em;
    color: var(--primary);
    padding: 0.2em 0;
  }
  /* 分岐フロー */
  .flow-branch {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .flow-branch .branch-point {
    background: var(--accent);
    color: white;
    padding: 1em 2em;
    border-radius: 50%;
    font-weight: bold;
  }
  .flow-branch .branches {
    display: flex;
    gap: 3em;
    margin-top: 1em;
  }
  .flow-branch .branch { text-align: center; }
  .flow-branch .branch-label {
    color: var(--secondary);
    font-size: 0.9em;
    margin-bottom: 0.5em;
  }
  .flow-branch .branch-item {
    background: var(--primary);
    color: white;
    padding: 1em 1.5em;
    border-radius: 8px;
  }
  /* 組織図 */
  .org-chart {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .org-chart .level {
    display: flex;
    justify-content: center;
    gap: 2em;
    margin-bottom: 1em;
  }
  .org-chart .node {
    background: white;
    border: 2px solid var(--primary);
    border-radius: 8px;
    padding: 0.8em 1.5em;
    text-align: center;
    min-width: 120px;
  }
  .org-chart .node.highlight {
    background: var(--primary);
    color: white;
  }
  .org-chart .connector {
    width: 2px;
    height: 20px;
    background: var(--primary);
    margin: 0 auto;
  }
  /* ピラミッド */
  .pyramid {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .pyramid .layer {
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    font-weight: bold;
    padding: 0.8em;
    margin-bottom: 2px;
  }
  .pyramid .layer-1 { width: 40%; background: #1e40af; }
  .pyramid .layer-2 { width: 55%; background: #2563eb; }
  .pyramid .layer-3 { width: 70%; background: #3b82f6; }
  .pyramid .layer-4 { width: 85%; background: #60a5fa; }
  .pyramid .layer-5 { width: 100%; background: #93c5fd; color: var(--text); }
  /* ファネル */
  .funnel {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .funnel .layer {
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    font-weight: bold;
    padding: 0.8em;
    margin-bottom: 2px;
  }
  .funnel .layer-1 { width: 100%; background: #1e40af; }
  .funnel .layer-2 { width: 85%; background: #2563eb; }
  .funnel .layer-3 { width: 70%; background: #3b82f6; }
  .funnel .layer-4 { width: 55%; background: #60a5fa; }
  .funnel .layer-5 { width: 40%; background: #93c5fd; color: var(--text); }
  /* サイクル4象限 */
  .cycle-4 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 1em;
    max-width: 500px;
    margin: 0 auto;
  }
  .cycle-4 .quadrant {
    background: white;
    border: 2px solid var(--primary);
    border-radius: 8px;
    padding: 1.5em;
    text-align: center;
  }
  .cycle-4 .quadrant .number {
    font-size: 2em;
    font-weight: bold;
    color: var(--primary);
  }
  /* SWOT */
  .swot {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 1em;
  }
  .swot .quadrant {
    padding: 1em;
    border-radius: 8px;
  }
  .swot .quadrant h3 { margin-bottom: 0.5em; font-size: 1.1em; }
  .swot .strengths { background: #dcfce7; border: 2px solid #10b981; }
  .swot .weaknesses { background: #fee2e2; border: 2px solid #ef4444; }
  .swot .opportunities { background: #dbeafe; border: 2px solid #2563eb; }
  .swot .threats { background: #fef3c7; border: 2px solid #f59e0b; }
  /* 2x2マトリクス */
  .matrix-2x2 {
    display: grid;
    grid-template-columns: auto 1fr 1fr;
    grid-template-rows: auto 1fr 1fr;
    gap: 2px;
    background: var(--border);
    border-radius: 8px;
    overflow: hidden;
  }
  .matrix-2x2 .axis-label {
    background: var(--secondary);
    color: white;
    padding: 0.8em;
    font-weight: bold;
    text-align: center;
  }
  .matrix-2x2 .corner { background: var(--code-bg); }
  .matrix-2x2 .cell {
    background: white;
    padding: 1.5em;
    text-align: center;
  }
  .matrix-2x2 .cell.q1 { background: #dcfce7; }
  .matrix-2x2 .cell.q2 { background: #fef3c7; }
  .matrix-2x2 .cell.q3 { background: #fee2e2; }
  .matrix-2x2 .cell.q4 { background: #dbeafe; }
  /* タイムライン */
  .timeline {
    position: relative;
    padding-left: 2em;
  }
  .timeline::before {
    content: '';
    position: absolute;
    left: 0.5em;
    top: 0;
    bottom: 0;
    width: 3px;
    background-color: var(--primary);
  }
  .timeline-item {
    position: relative;
    margin-bottom: 1.5em;
    padding-left: 1em;
  }
  .timeline-item::before {
    content: '';
    position: absolute;
    left: -1.5em;
    top: 0.5em;
    width: 12px;
    height: 12px;
    background-color: var(--primary);
    border-radius: 50%;
    border: 3px solid white;
    box-shadow: 0 0 0 2px var(--primary);
  }
  .timeline-item .date {
    font-size: 0.9em;
    color: var(--secondary);
    font-weight: bold;
  }
  /* 横タイムライン */
  .timeline-horizontal {
    display: flex;
    justify-content: space-between;
    position: relative;
    padding-top: 2em;
  }
  .timeline-horizontal::before {
    content: '';
    position: absolute;
    top: 0.5em;
    left: 0;
    right: 0;
    height: 3px;
    background: var(--primary);
  }
  .timeline-horizontal .item {
    text-align: center;
    position: relative;
    flex: 1;
  }
  .timeline-horizontal .item::before {
    content: '';
    position: absolute;
    top: -1.5em;
    left: 50%;
    transform: translateX(-50%);
    width: 16px;
    height: 16px;
    background: var(--primary);
    border-radius: 50%;
    border: 3px solid white;
    box-shadow: 0 0 0 2px var(--primary);
  }
  .timeline-horizontal .item .date { font-weight: bold; color: var(--primary); }
  /* ロードマップ */
  .roadmap {
    display: flex;
    gap: 1em;
  }
  .roadmap .phase {
    flex: 1;
    background: white;
    border: 2px solid var(--border);
    border-radius: 8px;
    padding: 1em;
  }
  .roadmap .phase.current {
    border-color: var(--primary);
    background: #eff6ff;
  }
  .roadmap .phase-header {
    background: var(--primary);
    color: white;
    margin: -1em -1em 1em -1em;
    padding: 0.5em 1em;
    border-radius: 6px 6px 0 0;
    font-weight: bold;
  }
  /* ガントチャート風 */
  .gantt {
    display: flex;
    flex-direction: column;
    gap: 0.5em;
  }
  .gantt .row {
    display: flex;
    align-items: center;
    gap: 1em;
  }
  .gantt .label {
    width: 120px;
    font-weight: bold;
  }
  .gantt .bar-container {
    flex: 1;
    background: var(--code-bg);
    height: 30px;
    border-radius: 4px;
    position: relative;
  }
  .gantt .bar {
    position: absolute;
    height: 100%;
    background: var(--primary);
    border-radius: 4px;
  }
  /* Before/After */
  .before-after {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: 1em;
    align-items: center;
  }
  .before-after .before {
    background: #fee2e2;
    border: 2px solid var(--error);
    border-radius: 8px;
    padding: 1.5em;
  }
  .before-after .after {
    background: #dcfce7;
    border: 2px solid var(--success);
    border-radius: 8px;
    padding: 1.5em;
  }
  .before-after .arrow {
    font-size: 3em;
    color: var(--primary);
  }
  /* プロ・コン */
  .pros-cons {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2em;
  }
  .pros {
    background: #dcfce7;
    border-radius: 8px;
    padding: 1em;
  }
  .cons {
    background: #fee2e2;
    border-radius: 8px;
    padding: 1em;
  }
  /* VS比較 */
  .vs-comparison {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: 1em;
    align-items: center;
  }
  .vs-comparison .option {
    background: white;
    border: 2px solid var(--border);
    border-radius: 8px;
    padding: 1.5em;
    text-align: center;
  }
  .vs-comparison .vs {
    font-size: 2em;
    font-weight: bold;
    color: var(--accent);
  }
  /* カードグリッド */
  .card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1em;
  }
  .card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5em;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  }
  .card .icon { font-size: 2em; margin-bottom: 0.5em; }
  .card .title { font-weight: bold; margin-bottom: 0.5em; }
  .card .description { font-size: 0.9em; color: var(--secondary); }
  /* フィーチャーカード */
  .feature-card {
    background: linear-gradient(135deg, #eff6ff 0%, white 100%);
    border-left: 4px solid var(--primary);
    border-radius: 0 8px 8px 0;
    padding: 1em 1.5em;
    margin-bottom: 1em;
  }
  .feature-card .title { font-weight: bold; color: var(--primary); }
  /* チェックリスト */
  .checklist {
    list-style: none;
    padding: 0;
  }
  .checklist li {
    display: flex;
    align-items: center;
    gap: 0.8em;
    margin-bottom: 0.8em;
    padding: 0.5em;
    background: var(--code-bg);
    border-radius: 6px;
  }
  .checklist li::before {
    content: '☐';
    font-size: 1.2em;
    color: var(--secondary);
  }
  .checklist li.checked::before {
    content: '☑';
    color: var(--success);
  }
  /* 番号付きリスト */
  .numbered-list {
    list-style: none;
    padding: 0;
    counter-reset: step;
  }
  .numbered-list li {
    display: flex;
    align-items: flex-start;
    gap: 1em;
    margin-bottom: 1em;
    counter-increment: step;
  }
  .numbered-list li::before {
    content: counter(step);
    background: var(--primary);
    color: white;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    flex-shrink: 0;
  }
  /* ステップ */
  .steps {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 0.5em;
  }
  .step {
    flex: 1;
    text-align: center;
    padding: 1em;
    position: relative;
  }
  .step:not(:last-child)::after {
    content: '→';
    position: absolute;
    right: -0.8em;
    top: 50%;
    transform: translateY(-50%);
    font-size: 1.5em;
    color: var(--primary);
  }
  .step .number {
    width: 50px;
    height: 50px;
    background-color: var(--primary);
    color: white;
    border-radius: 50%;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    font-size: 1.4em;
    margin-bottom: 0.5em;
  }
  .step .title { font-weight: bold; margin-bottom: 0.3em; }
  .step .description { font-size: 0.85em; color: var(--secondary); }
  /* 引用ボックス */
  .quote-box {
    background-color: var(--code-bg);
    border-left: 5px solid var(--accent);
    padding: 1.5em 2em;
    margin: 1em 0;
    border-radius: 0 8px 8px 0;
  }
  .quote-box p {
    font-size: 1.2em;
    font-style: italic;
    margin: 0;
    line-height: 1.6;
  }
  .quote-box .author {
    text-align: right;
    color: var(--secondary);
    font-style: normal;
    margin-top: 1em;
  }
  /* 強調ボックス */
  .highlight-box {
    background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
    border: 2px solid var(--accent);
    border-radius: 8px;
    padding: 1em 1.5em;
    margin: 1em 0;
  }
  .highlight-box.info {
    background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
    border-color: var(--primary);
  }
  .highlight-box.success {
    background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
    border-color: var(--success);
  }
  .highlight-box.error {
    background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
    border-color: var(--error);
  }
  /* コールアウト */
  .callout {
    display: flex;
    gap: 1em;
    background: var(--code-bg);
    border-radius: 8px;
    padding: 1em;
  }
  .callout .icon { font-size: 1.5em; }
  .callout.tip { border-left: 4px solid var(--success); }
  .callout.warning { border-left: 4px solid var(--accent); }
  .callout.danger { border-left: 4px solid var(--error); }
  .callout.info { border-left: 4px solid var(--primary); }
  /* バッジ */
  .badge {
    display: inline-block;
    padding: 0.25em 0.75em;
    border-radius: 9999px;
    font-size: 0.85em;
    font-weight: bold;
  }
  .badge.primary { background: var(--primary); color: white; }
  .badge.success { background: var(--success); color: white; }
  .badge.warning { background: var(--accent); color: white; }
  .badge.error { background: var(--error); color: white; }
  /* タグリスト */
  .tag-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5em;
  }
  .tag {
    display: inline-block;
    padding: 0.3em 0.8em;
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 4px;
    font-size: 0.9em;
  }
  /* ステータス */
  .status {
    display: inline-flex;
    align-items: center;
    gap: 0.5em;
  }
  .status::before {
    content: '';
    width: 8px;
    height: 8px;
    border-radius: 50%;
  }
  .status.active::before { background: var(--success); }
  .status.pending::before { background: var(--accent); }
  .status.inactive::before { background: var(--secondary); }
  /* 価格表 */
  .pricing {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1em;
  }
  .pricing .plan {
    background: white;
    border: 2px solid var(--border);
    border-radius: 12px;
    padding: 1.5em;
    text-align: center;
  }
  .pricing .plan.featured {
    border-color: var(--primary);
    transform: scale(1.05);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
  .pricing .plan-name { font-size: 1.2em; font-weight: bold; }
  .pricing .plan-price {
    font-size: 2.5em;
    font-weight: bold;
    color: var(--primary);
    margin: 0.3em 0;
  }
  .pricing .plan-features {
    list-style: none;
    padding: 0;
    text-align: left;
  }
  .pricing .plan-features li {
    padding: 0.5em 0;
    border-bottom: 1px solid var(--border);
  }
  /* レイヤー図 */
  .layers {
    display: flex;
    flex-direction: column;
    gap: 0.5em;
  }
  .layers .layer {
    padding: 1em;
    text-align: center;
    color: white;
    font-weight: bold;
    border-radius: 8px;
  }
  .layers .layer-1 { background: #1e40af; }
  .layers .layer-2 { background: #2563eb; }
  .layers .layer-3 { background: #3b82f6; }
  .layers .layer-4 { background: #60a5fa; }
  /* ブロック図 */
  .block-diagram {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1em;
  }
  .block-diagram .block {
    background: white;
    border: 2px solid var(--primary);
    border-radius: 8px;
    padding: 1em 1.5em;
    text-align: center;
  }
  .block-diagram .block.highlight {
    background: var(--primary);
    color: white;
  }
  .block-diagram .connector { font-size: 1.5em; color: var(--primary); }
  /* 3層アーキテクチャ */
  .architecture-3tier {
    display: flex;
    justify-content: space-around;
    align-items: stretch;
    gap: 2em;
  }
  .architecture-3tier .tier {
    flex: 1;
    background: white;
    border: 2px solid var(--primary);
    border-radius: 8px;
    padding: 1em;
    text-align: center;
  }
  .architecture-3tier .tier-header {
    background: var(--primary);
    color: white;
    margin: -1em -1em 1em -1em;
    padding: 0.5em;
    border-radius: 6px 6px 0 0;
    font-weight: bold;
  }
  /* コードブロック */
  .code-block {
    background-color: #1e293b;
    color: #e2e8f0;
    padding: 1.5em;
    border-radius: 8px;
    font-family: 'Fira Code', 'Consolas', monospace;
    font-size: 0.9em;
    overflow-x: auto;
  }
  .code-block .comment { color: #64748b; }
  .code-block .keyword { color: #c084fc; }
  .code-block .string { color: #4ade80; }
  .code-block .function { color: #60a5fa; }
  /* ターミナル */
  .terminal {
    background: #0f172a;
    border-radius: 8px;
    overflow: hidden;
  }
  .terminal .header {
    background: #1e293b;
    padding: 0.5em 1em;
    display: flex;
    gap: 0.5em;
  }
  .terminal .header .dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
  }
  .terminal .header .dot.red { background: #ef4444; }
  .terminal .header .dot.yellow { background: #f59e0b; }
  .terminal .header .dot.green { background: #10b981; }
  .terminal .content {
    padding: 1em;
    color: #10b981;
    font-family: monospace;
  }
  /* FAQ */
  .faq .question {
    font-weight: bold;
    color: var(--primary);
    margin-bottom: 0.3em;
  }
  .faq .question::before { content: 'Q. '; }
  .faq .answer {
    padding-left: 1.5em;
    margin-bottom: 1em;
    color: var(--text);
  }
  .faq .answer::before {
    content: 'A. ';
    font-weight: bold;
    color: var(--secondary);
  }
  /* 統計 */
  .stats {
    display: flex;
    justify-content: space-around;
    text-align: center;
  }
  .stats .stat { padding: 1em; }
  .stats .stat .value {
    font-size: 3em;
    font-weight: bold;
    color: var(--primary);
  }
  .stats .stat .label { color: var(--secondary); }
  /* 大きな引用 */
  .big-quote {
    font-size: 1.8em;
    font-style: italic;
    text-align: center;
    color: var(--secondary);
    padding: 1em;
    position: relative;
  }
  .big-quote::before {
    content: '"';
    font-size: 3em;
    color: var(--primary);
    opacity: 0.3;
    position: absolute;
    top: 0;
    left: 0;
  }
  /* グラデーション背景 */
  .gradient-bg {
    background: linear-gradient(135deg, var(--primary) 0%, #7c3aed 100%);
    color: white;
    padding: 2em;
    border-radius: 12px;
    margin: -20px;
  }
  .gradient-bg h1, .gradient-bg h2, .gradient-bg h3 {
    color: white;
    border: none;
  }
  /* 比較表 */
  table {
    width: 100%;
    border-collapse: collapse;
  }
  th, td {
    border: 1px solid var(--border);
    padding: 0.8em;
    text-align: left;
  }
  th {
    background: var(--primary);
    color: white;
  }
  .check { color: var(--success); font-weight: bold; }
  .cross { color: var(--error); font-weight: bold; }
  /* 実要素タイムライン（縦）- テーブル形式 */
  .timeline-v { border-collapse: collapse; }
  .timeline-v td { padding: 0.2em 0.5em; vertical-align: top; }
  .timeline-v .col-line { text-align: center; color: var(--primary); line-height: 1.2; width: 30px; }
  .timeline-v .col-date { font-weight: bold; color: var(--secondary); white-space: nowrap; }
  .timeline-v .col-content { }
  /* 実要素タイムライン（横）- 線を背景で描画 */
  .timeline-h {
    display: flex; justify-content: space-between; text-align: center;
    position: relative; padding-top: 1.5em;
  }
  .timeline-h-line {
    position: absolute; top: 0.6em; left: 10%; right: 10%;
    height: 3px; background: var(--primary);
  }
  .timeline-h .tl-h-item { flex: 1; position: relative; }
  .timeline-h .tl-h-dot {
    display: inline-block; width: 16px; height: 16px;
    background: var(--primary); border-radius: 50%;
    position: absolute; top: -1.2em; left: 50%; transform: translateX(-50%);
  }
  .timeline-h .tl-h-date { font-weight: bold; color: var(--primary); margin-top: 0.5em; }
  /* 実要素ステップ */
  .steps-real { display: flex; justify-content: center; align-items: center; gap: 0.3em; }
  .steps-real .st-item {
    background: var(--primary); color: white; padding: 0.8em 1.2em;
    border-radius: 8px; text-align: center; min-width: 100px;
  }
  .steps-real .st-arrow { color: var(--primary); font-size: 1.5em; }
  /* 実要素チェックリスト */
  .check-list { list-style: none; padding: 0; }
  .check-list li { display: flex; align-items: center; gap: 0.5em; margin-bottom: 0.5em; padding: 0.4em; background: var(--code-bg); border-radius: 6px; }
  .check-list .icon { font-size: 1.1em; }
  .check-list .done { color: var(--success); }
  .check-list .pending { color: var(--secondary); }
  /* 実要素番号リスト */
  .num-list { list-style: none; padding: 0; }
  .num-list li { display: flex; align-items: flex-start; gap: 0.8em; margin-bottom: 0.6em; }
  .num-list .num {
    background: var(--primary); color: white; width: 28px; height: 28px;
    border-radius: 50%; display: flex; justify-content: center; align-items: center;
    font-weight: bold; flex-shrink: 0; font-size: 0.9em;
  }
  /* 実要素ステータス */
  .st-dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 0.4em; }
  .st-dot.active { background: var(--success); }
  .st-dot.pending { background: var(--accent); }
  .st-dot.inactive { background: var(--secondary); }
  /* コンパクト化 */
  .compact { font-size: 0.85em; }
  .compact h1 { font-size: 1.5em; margin-bottom: 0.3em; }
  .compact h3 { font-size: 1em; margin: 0.3em 0; }
  .compact ul, .compact ol { margin: 0.3em 0; }
  .compact li { margin-bottom: 0.2em; }
  /* ベン図 */
  .venn { display: flex; justify-content: center; align-items: center; position: relative; min-height: 280px; }
  .venn .circle {
    width: 180px; height: 180px; border-radius: 50%; position: absolute;
    display: flex; justify-content: center; align-items: center;
    font-weight: bold; opacity: 0.7;
  }
  .venn .circle-a { background: #3b82f6; left: 20%; }
  .venn .circle-b { background: #10b981; right: 20%; }
  .venn .center-text { position: absolute; z-index: 10; font-weight: bold; }
  /* ツリー図 */
  .tree { text-align: center; }
  .tree .root {
    display: inline-block; background: var(--primary); color: white;
    padding: 0.8em 2em; border-radius: 8px; font-weight: bold;
  }
  .tree .branches { display: flex; justify-content: center; gap: 2em; margin-top: 0.5em; }
  .tree .branch-line { color: var(--primary); font-size: 1.5em; }
  .tree .branch-item {
    background: white; border: 2px solid var(--primary);
    padding: 0.6em 1.2em; border-radius: 8px; text-align: center;
  }
  /* 因果関係 */
  .cause-effect { display: flex; justify-content: center; align-items: center; gap: 1em; }
  .cause-effect .cause, .cause-effect .effect {
    background: white; border: 2px solid var(--primary);
    padding: 1em 1.5em; border-radius: 8px; text-align: center;
  }
  .cause-effect .cause { border-color: var(--accent); }
  .cause-effect .effect { border-color: var(--success); }
  .cause-effect .arrow { font-size: 2em; color: var(--primary); }
  /* 数式（足し算・掛け算） */
  .formula { display: flex; justify-content: center; align-items: center; gap: 0.8em; font-size: 1.1em; }
  .formula .element {
    background: var(--primary); color: white;
    padding: 1em 1.5em; border-radius: 8px; text-align: center; min-width: 100px;
  }
  .formula .operator { font-size: 2em; font-weight: bold; color: var(--primary); }
  .formula .result {
    background: var(--success); color: white;
    padding: 1em 1.5em; border-radius: 8px; text-align: center; min-width: 120px;
  }
  /* ランキング */
  .ranking { display: flex; flex-direction: column; gap: 0.5em; }
  .ranking .rank-item { display: flex; align-items: center; gap: 1em; padding: 0.5em; }
  .ranking .rank-num {
    width: 40px; height: 40px; border-radius: 50%; display: flex;
    justify-content: center; align-items: center; font-weight: bold; color: white;
  }
  .ranking .rank-1 { background: #fbbf24; }
  .ranking .rank-2 { background: #9ca3af; }
  .ranking .rank-3 { background: #b45309; }
  .ranking .rank-other { background: var(--secondary); }
  .ranking .rank-bar {
    flex: 1; background: var(--code-bg); height: 30px; border-radius: 4px;
    display: flex; align-items: center;
  }
  .ranking .rank-fill { height: 100%; background: var(--primary); border-radius: 4px; }
  .ranking .rank-label { margin-left: 0.5em; font-weight: bold; }
  /* 階段図 */
  .stairs { display: flex; align-items: flex-end; justify-content: center; gap: 0.5em; }
  .stairs .stair {
    background: var(--primary); color: white; text-align: center;
    padding: 0.5em 1em; border-radius: 4px 4px 0 0; min-width: 80px;
  }
  .stairs .stair-1 { height: 60px; opacity: 0.5; }
  .stairs .stair-2 { height: 100px; opacity: 0.65; }
  .stairs .stair-3 { height: 140px; opacity: 0.8; }
  .stairs .stair-4 { height: 180px; opacity: 1; }
  /* 包括図 */
  .nested {
    border: 3px solid var(--primary); border-radius: 12px; padding: 1em;
    background: #eff6ff; text-align: center;
  }
  .nested .outer-label { font-weight: bold; color: var(--primary); margin-bottom: 0.5em; }
  .nested .inner {
    border: 2px solid var(--secondary); border-radius: 8px; padding: 0.8em;
    background: white; display: inline-block;
  }
  /* 相互関係 */
  .mutual { display: flex; justify-content: center; align-items: center; gap: 0.5em; }
  .mutual .element {
    background: white; border: 2px solid var(--primary);
    padding: 1em 1.5em; border-radius: 8px; text-align: center;
  }
  .mutual .arrows { display: flex; flex-direction: column; color: var(--primary); font-size: 1.2em; }
---

<div class="title-slide">

# Marpデザインシステム
# 全図解コンポーネント集

50種類以上のCSSコンポーネントを完全網羅

</div>

---

<div class="section-header">

# 基本レイアウト

2〜4カラムレイアウトとタイトルスライド

</div>

---

# 2カラムレイアウト

左右に均等配置

<div class="two-column">
<div>

### 左カラム
- 項目A-1
- 項目A-2
- 項目A-3

</div>
<div>

### 右カラム
- 項目B-1
- 項目B-2
- 項目B-3

</div>
</div>

---

# 3カラムレイアウト

3つの要素を並列表示

<div class="three-column">
<div>

### 第1列
短い説明文をここに記述

</div>
<div>

### 第2列
中央のコンテンツ領域

</div>
<div>

### 第3列
右側の情報エリア

</div>
</div>

---

# 4カラムレイアウト

4つの要素を横並びに

<div class="four-column">
<div class="card">

### 項目1
説明

</div>
<div class="card">

### 項目2
説明

</div>
<div class="card">

### 項目3
説明

</div>
<div class="card">

### 項目4
説明

</div>
</div>

---

<div class="section-header">

# メトリクス・KPI

数値を効果的に見せる表現

</div>

---

# メトリックカード

重要な数値を強調表示

<div class="three-column">
<div class="metric-card">
<div class="number">98%</div>
<div class="label">顧客満足度</div>
<div class="change positive">↑ 12%</div>
</div>
<div class="metric-card">
<div class="number">1.2M</div>
<div class="label">月間ユーザー</div>
<div class="change positive">↑ 28%</div>
</div>
<div class="metric-card">
<div class="number">45ms</div>
<div class="label">応答時間</div>
<div class="change negative">↓ 35%</div>
</div>
</div>

---

# 大きな数値表示

インパクトのある単一KPI

<div class="big-number">
<span class="value">86</span><span class="unit">%</span>
<div class="description">作業時間を削減</div>
</div>

---

# 進捗バー

タスクの進捗状況を可視化

**プロジェクトA**
<div class="progress-bar">
<div class="fill" style="width: 85%;">85%</div>
</div>

**プロジェクトB**
<div class="progress-bar">
<div class="fill" style="width: 60%;">60%</div>
</div>

**プロジェクトC**
<div class="progress-bar">
<div class="fill" style="width: 30%;">30%</div>
</div>

---

<div class="section-header">

# フローチャート

処理の流れを可視化

</div>

---

# 横フロー

プロセスの水平表示

<div class="flow-horizontal">
<div class="flow-item">入力</div>
<span class="flow-arrow">→</span>
<div class="flow-item">処理</div>
<span class="flow-arrow">→</span>
<div class="flow-item">検証</div>
<span class="flow-arrow">→</span>
<div class="flow-item">出力</div>
</div>

---

# 縦フロー

プロセスの垂直表示

<div class="flow-vertical">
<div class="flow-item">ユーザー要求</div>
<span class="flow-arrow">↓</span>
<div class="flow-item">要件分析</div>
<span class="flow-arrow">↓</span>
<div class="flow-item">設計・実装</div>
<span class="flow-arrow">↓</span>
<div class="flow-item">デリバリー</div>
</div>

---

# 分岐フロー

条件分岐の可視化

<div class="flow-branch">
<div class="branch-point">判定</div>
<div class="branches">
<div class="branch">
<div class="branch-label">Yes</div>
<div class="branch-item">処理A</div>
</div>
<div class="branch">
<div class="branch-label">No</div>
<div class="branch-item">処理B</div>
</div>
</div>
</div>

---

<div class="section-header">

# 組織図・階層構造

組織や概念の階層を表現

</div>

---

# 組織図

組織構造の可視化

<div class="org-chart">
<div class="level">
<div class="node highlight">CEO</div>
</div>
<div class="connector"></div>
<div class="level">
<div class="node">CTO</div>
<div class="node">CFO</div>
<div class="node">COO</div>
</div>
<div class="connector"></div>
<div class="level">
<div class="node">開発部</div>
<div class="node">経理部</div>
<div class="node">営業部</div>
</div>
</div>

---

<div class="section-header">

# ピラミッド・ファネル

階層構造を視覚的に表現

</div>

---

# ピラミッド図

上位概念から下位概念へ

<div class="pyramid">
<div class="layer layer-1">ビジョン</div>
<div class="layer layer-2">戦略</div>
<div class="layer layer-3">戦術</div>
<div class="layer layer-4">施策</div>
<div class="layer layer-5">日常業務</div>
</div>

---

# ファネル図

段階的な絞り込みを表現

<div class="funnel">
<div class="layer layer-1">認知 (10,000人)</div>
<div class="layer layer-2">興味 (5,000人)</div>
<div class="layer layer-3">検討 (2,000人)</div>
<div class="layer layer-4">購入 (800人)</div>
<div class="layer layer-5">リピート (300人)</div>
</div>

---

<div class="section-header">

# サイクル・循環図

繰り返しプロセスの表現

</div>

---

# PDCAサイクル

4象限での循環表現

<div class="cycle-4">
<div class="quadrant">
<div class="number">1</div>
<strong>Plan</strong><br>計画
</div>
<div class="quadrant">
<div class="number">2</div>
<strong>Do</strong><br>実行
</div>
<div class="quadrant">
<div class="number">4</div>
<strong>Act</strong><br>改善
</div>
<div class="quadrant">
<div class="number">3</div>
<strong>Check</strong><br>評価
</div>
</div>

---

<div class="section-header">

# マトリクス・2x2

4象限分析の表現

</div>

---

# 2x2マトリクス

優先度マトリクス

<div class="matrix-2x2">
<div class="corner"></div>
<div class="axis-label">緊急</div>
<div class="axis-label">非緊急</div>
<div class="axis-label">重要</div>
<div class="cell q1"><strong>第1象限</strong><br>即座に対応</div>
<div class="cell q2"><strong>第2象限</strong><br>計画的に実施</div>
<div class="axis-label">非重要</div>
<div class="cell q3"><strong>第3象限</strong><br>委任検討</div>
<div class="cell q4"><strong>第4象限</strong><br>削減・廃止</div>
</div>

---

# SWOT分析

戦略分析フレームワーク

<div class="swot">
<div class="quadrant strengths">
<h3>強み (Strengths)</h3>

- 技術力が高い
- ブランド認知度

</div>
<div class="quadrant weaknesses">
<h3>弱み (Weaknesses)</h3>

- リソース不足
- 海外展開遅れ

</div>
<div class="quadrant opportunities">
<h3>機会 (Opportunities)</h3>

- 市場拡大
- DX推進需要

</div>
<div class="quadrant threats">
<h3>脅威 (Threats)</h3>

- 競合激化
- 規制強化

</div>
</div>

---

<div class="section-header">

# タイムライン・ロードマップ

時系列の表現

</div>

---

# 縦タイムライン

時系列での出来事表示

<table class="timeline-v">
<tr><td class="col-line">●<br>│</td><td class="col-date">2024/01</td><td class="col-content">プロジェクト開始・要件定義</td></tr>
<tr><td class="col-line">●<br>│</td><td class="col-date">2024/03</td><td class="col-content">設計完了・開発着手</td></tr>
<tr><td class="col-line">●<br>│</td><td class="col-date">2024/06</td><td class="col-content">テスト・品質保証</td></tr>
<tr><td class="col-line">●</td><td class="col-date">2024/09</td><td class="col-content">本番リリース</td></tr>
</table>

---

# 横タイムライン

マイルストーン表示

<div class="timeline-h">
<div class="timeline-h-line"></div>
<div class="tl-h-item"><div class="tl-h-dot"></div><div class="tl-h-date">Q1</div><div>企画</div></div>
<div class="tl-h-item"><div class="tl-h-dot"></div><div class="tl-h-date">Q2</div><div>開発</div></div>
<div class="tl-h-item"><div class="tl-h-dot"></div><div class="tl-h-date">Q3</div><div>テスト</div></div>
<div class="tl-h-item"><div class="tl-h-dot"></div><div class="tl-h-date">Q4</div><div>リリース</div></div>
</div>

---

# ロードマップ

フェーズ別計画表示

<div class="roadmap">
<div class="phase">
<div class="phase-header">Phase 1</div>

- 要件定義
- 基本設計

</div>
<div class="phase current">
<div class="phase-header">Phase 2</div>

- 詳細設計
- 実装

</div>
<div class="phase">
<div class="phase-header">Phase 3</div>

- テスト
- リリース

</div>
</div>

---

# ガントチャート風

タスクスケジュール表示

<div class="gantt">
<div class="row">
<div class="label">企画</div>
<div class="bar-container">
<div class="bar" style="left: 0%; width: 25%; background: #1e40af;"></div>
</div>
</div>
<div class="row">
<div class="label">設計</div>
<div class="bar-container">
<div class="bar" style="left: 20%; width: 30%; background: #2563eb;"></div>
</div>
</div>
<div class="row">
<div class="label">開発</div>
<div class="bar-container">
<div class="bar" style="left: 40%; width: 40%; background: #3b82f6;"></div>
</div>
</div>
<div class="row">
<div class="label">テスト</div>
<div class="bar-container">
<div class="bar" style="left: 70%; width: 30%; background: #60a5fa;"></div>
</div>
</div>
</div>

---

<div class="section-header">

# 比較・対比

Before/After、プロコンなど

</div>

---

# Before/After

変化の可視化

<div class="before-after">
<div class="before">
<h3>Before</h3>

- 手作業で80時間
- ミス率10%
- 属人化

</div>
<div class="arrow">→</div>
<div class="after">
<h3>After</h3>

- 自動化で11時間
- ミス率0.5%
- 標準化

</div>
</div>

---

# プロ・コンリスト

メリット・デメリット比較

<div class="pros-cons">
<div class="pros">
<h3>メリット</h3>

- コスト削減
- 時間短縮
- 品質向上
- スケーラビリティ

</div>
<div class="cons">
<h3>デメリット</h3>

- 初期投資
- 学習コスト
- 移行リスク
- 依存性

</div>
</div>

---

# VS比較

二者比較

<div class="vs-comparison">
<div class="option">
<h3>オプションA</h3>

- 安価
- 導入簡単
- 機能限定

</div>
<div class="vs">VS</div>
<div class="option">
<h3>オプションB</h3>

- 高機能
- スケーラブル
- 要専門知識

</div>
</div>

---

# 比較表

機能比較マトリクス

| 機能 | 製品A | 製品B | 製品C |
|------|:-----:|:-----:|:-----:|
| 自動化 | <span class="check">✓</span> | <span class="check">✓</span> | <span class="cross">✗</span> |
| API連携 | <span class="check">✓</span> | <span class="cross">✗</span> | <span class="check">✓</span> |
| 日本語対応 | <span class="check">✓</span> | <span class="check">✓</span> | <span class="check">✓</span> |
| 価格 | ¥10,000 | ¥5,000 | ¥15,000 |

---

<div class="section-header">

# カード・リスト

情報の整理と表示

</div>

---

# カードグリッド

情報カードの配列

<div class="card-grid">
<div class="card">
<div class="icon">🚀</div>
<div class="title">高速</div>
<div class="description">処理速度が従来の10倍</div>
</div>
<div class="card">
<div class="icon">🔒</div>
<div class="title">安全</div>
<div class="description">エンタープライズレベルのセキュリティ</div>
</div>
<div class="card">
<div class="icon">📊</div>
<div class="title">分析</div>
<div class="description">リアルタイムダッシュボード</div>
</div>
</div>

---

# フィーチャーカード

特徴を強調表示

<div class="feature-card">
<div class="title">自動スケーリング</div>
<div>需要に応じて自動的にリソースを調整</div>
</div>

<div class="feature-card">
<div class="title">ゼロダウンタイム</div>
<div>メンテナンス中もサービス継続</div>
</div>

<div class="feature-card">
<div class="title">グローバル展開</div>
<div>世界20拠点でのエッジ配信</div>
</div>

---

# チェックリスト

タスク管理用リスト

<ul class="check-list">
<li><span class="icon done">☑</span>要件定義完了</li>
<li><span class="icon done">☑</span>基本設計完了</li>
<li><span class="icon done">☑</span>詳細設計完了</li>
<li><span class="icon pending">☐</span>実装中</li>
<li><span class="icon pending">☐</span>テスト</li>
<li><span class="icon pending">☐</span>リリース</li>
</ul>

---

# 番号付きリスト

手順の明示

<ul class="num-list">
<li><span class="num">1</span>アカウントを作成する</li>
<li><span class="num">2</span>プロジェクトを新規作成</li>
<li><span class="num">3</span>設定ファイルを配置</li>
<li><span class="num">4</span>デプロイコマンドを実行</li>
</ul>

---

<div class="section-header">

# ステップ・プロセス

手順の可視化

</div>

---

# ステップ表示

プロセスの段階表示

<div class="steps">
<div class="step">
<div class="number">1</div>
<div class="title">計画</div>
<div class="description">要件整理</div>
</div>
<div class="step">
<div class="number">2</div>
<div class="title">設計</div>
<div class="description">アーキテクチャ</div>
</div>
<div class="step">
<div class="number">3</div>
<div class="title">実装</div>
<div class="description">コーディング</div>
</div>
<div class="step">
<div class="number">4</div>
<div class="title">テスト</div>
<div class="description">品質保証</div>
</div>
</div>

---

<div class="section-header">

# ボックス・ハイライト

重要情報の強調

</div>

---

# 引用ボックス

名言・重要発言の引用

<div class="quote-box">
<p>シンプルであることは、複雑であることよりも難しい。</p>
<div class="author">— スティーブ・ジョブズ</div>
</div>

---

# 強調ボックス

重要情報のハイライト

<div class="highlight-box">

**注意**: この機能は本番環境でのみ利用可能です。

</div>

<div class="highlight-box info">

**情報**: 詳細はドキュメントを参照してください。

</div>

<div class="highlight-box success">

**成功**: 処理が正常に完了しました。

</div>

<div class="highlight-box error">

**エラー**: 入力値を確認してください。

</div>

---

# コールアウト

補足情報の表示

<div class="callout tip">
<span class="icon">💡</span>
<div><strong>ヒント:</strong> ショートカットキー Ctrl+S で保存できます。</div>
</div>

<div class="callout warning">
<span class="icon">⚠️</span>
<div><strong>警告:</strong> この操作は取り消せません。</div>
</div>

<div class="callout danger">
<span class="icon">🚨</span>
<div><strong>危険:</strong> 本番データが削除されます。</div>
</div>

---

<div class="section-header">

# バッジ・タグ

ラベル表示

</div>

---

# バッジとステータス

状態表示

<span class="badge primary">新機能</span>
<span class="badge success">完了</span>
<span class="badge warning">進行中</span>
<span class="badge error">緊急</span>

<br><br>

**プロジェクト状態:**

<span class="st-dot active"></span>稼働中 &nbsp;&nbsp;
<span class="st-dot pending"></span>保留中 &nbsp;&nbsp;
<span class="st-dot inactive"></span>停止中

---

# タグリスト

カテゴリ・キーワード表示

<div class="tag-list">
<span class="tag">JavaScript</span>
<span class="tag">TypeScript</span>
<span class="tag">React</span>
<span class="tag">Node.js</span>
<span class="tag">GraphQL</span>
<span class="tag">Docker</span>
<span class="tag">Kubernetes</span>
<span class="tag">AWS</span>
</div>

---

<div class="section-header">

# 価格表

プラン比較

</div>

---

# 価格プラン

サービスプラン比較

<div class="pricing">
<div class="plan">
<div class="plan-name">スターター</div>
<div class="plan-price">¥0</div>
<ul class="plan-features">
<li>5プロジェクト</li>
<li>1GBストレージ</li>
<li>メールサポート</li>
</ul>
</div>
<div class="plan featured">
<div class="plan-name">プロ</div>
<div class="plan-price">¥2,980</div>
<ul class="plan-features">
<li>無制限プロジェクト</li>
<li>100GBストレージ</li>
<li>優先サポート</li>
</ul>
</div>
<div class="plan">
<div class="plan-name">エンタープライズ</div>
<div class="plan-price">要相談</div>
<ul class="plan-features">
<li>カスタム機能</li>
<li>専用インフラ</li>
<li>24/7サポート</li>
</ul>
</div>
</div>

---

<div class="section-header">

# アーキテクチャ図

システム構成の表現

</div>

---

# レイヤー図

システム層構造

<div class="layers">
<div class="layer layer-1">プレゼンテーション層 (UI)</div>
<div class="layer layer-2">アプリケーション層 (API)</div>
<div class="layer layer-3">ドメイン層 (ビジネスロジック)</div>
<div class="layer layer-4">インフラ層 (DB, 外部サービス)</div>
</div>

---

# ブロック図

コンポーネント接続

<div class="block-diagram">
<div class="block">クライアント</div>
<span class="connector">→</span>
<div class="block highlight">API Gateway</div>
<span class="connector">→</span>
<div class="block">マイクロサービス</div>
<span class="connector">→</span>
<div class="block">データベース</div>
</div>

---

# 3層アーキテクチャ

Web三層構成

<div class="architecture-3tier">
<div class="tier">
<div class="tier-header">フロントエンド</div>

- React
- Next.js
- Tailwind CSS

</div>
<div class="tier">
<div class="tier-header">バックエンド</div>

- Node.js
- Express
- GraphQL

</div>
<div class="tier">
<div class="tier-header">データベース</div>

- PostgreSQL
- Redis
- S3

</div>
</div>

---

<div class="section-header">

# コード・技術系

コード表示とターミナル

</div>

---

# コードブロック

シンタックスハイライト

<div class="code-block">
<span class="comment">// APIリクエストの例</span><br>
<span class="keyword">const</span> response = <span class="keyword">await</span> <span class="function">fetch</span>(<span class="string">'/api/users'</span>);<br>
<span class="keyword">const</span> data = <span class="keyword">await</span> response.<span class="function">json</span>();<br>
<span class="function">console</span>.<span class="function">log</span>(data);
</div>

---

# ターミナル表示

コマンドライン風

<div class="terminal">
<div class="header">
<span class="dot red"></span>
<span class="dot yellow"></span>
<span class="dot green"></span>
</div>
<div class="content">
$ npm install<br>
$ npm run build<br>
$ npm start<br>
<br>
Server running on http://localhost:3000
</div>
</div>

---

<div class="section-header">

# その他

FAQ、統計、引用など

</div>

---

# FAQ

よくある質問

<div class="faq">
<div class="question">利用料金はいくらですか？</div>
<div class="answer">基本プランは無料です。プロプランは月額2,980円からご利用いただけます。</div>

<div class="question">サポートはありますか？</div>
<div class="answer">はい、メールとチャットでのサポートを提供しています。</div>

<div class="question">解約はいつでもできますか？</div>
<div class="answer">はい、いつでも解約可能です。日割り返金にも対応しています。</div>
</div>

---

# 統計表示

主要メトリクスを並列表示

<div class="stats">
<div class="stat">
<div class="value">500+</div>
<div class="label">導入企業</div>
</div>
<div class="stat">
<div class="value">99.9%</div>
<div class="label">稼働率</div>
</div>
<div class="stat">
<div class="value">24/7</div>
<div class="label">サポート</div>
</div>
<div class="stat">
<div class="value">4.8★</div>
<div class="label">評価</div>
</div>
</div>

---

# 大きな引用

インパクトのある引用表示

<div class="big-quote">
完璧を目指すより、まず終わらせろ。
</div>

<p style="text-align: center; color: var(--secondary);">— マーク・ザッカーバーグ</p>

---

# グラデーション背景

強調スライド

<div class="gradient-bg">

## 今すぐ始めましょう

**30日間の無料トライアル**で、すべての機能をお試しいただけます。

クレジットカード不要 • いつでも解約可能

</div>

---

<div class="section-header">

# 追加図解パターン

ベン図、ツリー図、因果関係など

</div>

---

# ベン図

集合関係の表現

<div class="venn">
<div class="circle circle-a">デザイン</div>
<div class="circle circle-b">技術</div>
<div class="center-text">UX</div>
</div>

---

# ツリー図

階層構造の枝分かれ

<div class="tree">
<div class="root">戦略</div>
<div class="branch-line">├────┼────┤</div>
<div class="branches">
<div class="branch-item">施策A</div>
<div class="branch-item">施策B</div>
<div class="branch-item">施策C</div>
</div>
</div>

---

# 因果関係図

原因と結果の関係

<div class="cause-effect">
<div class="cause"><strong>原因</strong><br>コスト増加</div>
<div class="arrow">→</div>
<div class="cause"><strong>要因</strong><br>人件費高騰</div>
<div class="arrow">→</div>
<div class="effect"><strong>結果</strong><br>価格改定</div>
</div>

---

# 数式図（足し算）

要素の組み合わせ

<div class="formula">
<div class="element">技術力</div>
<span class="operator">+</span>
<div class="element">デザイン</div>
<span class="operator">=</span>
<div class="result">優れたUX</div>
</div>

---

# 数式図（掛け算）

相乗効果の表現

<div class="formula">
<div class="element">品質</div>
<span class="operator">×</span>
<div class="element">スピード</div>
<span class="operator">=</span>
<div class="result">競争優位性</div>
</div>

---

# ランキング

順位と比較

<div class="ranking">
<div class="rank-item">
<div class="rank-num rank-1">1</div>
<div class="rank-bar"><div class="rank-fill" style="width:100%;"></div></div>
<span class="rank-label">製品A (45%)</span>
</div>
<div class="rank-item">
<div class="rank-num rank-2">2</div>
<div class="rank-bar"><div class="rank-fill" style="width:70%;"></div></div>
<span class="rank-label">製品B (32%)</span>
</div>
<div class="rank-item">
<div class="rank-num rank-3">3</div>
<div class="rank-bar"><div class="rank-fill" style="width:40%;"></div></div>
<span class="rank-label">製品C (18%)</span>
</div>
</div>

---

# 階段図

段階的な成長・進化

<div class="stairs">
<div class="stair stair-1">基礎</div>
<div class="stair stair-2">応用</div>
<div class="stair stair-3">実践</div>
<div class="stair stair-4">熟達</div>
</div>

---

# 包括図

入れ子関係の表現

<div class="nested">
<div class="outer-label">経営戦略</div>
<div class="nested" style="margin: 0.5em;">
<div class="outer-label">事業戦略</div>
<div class="inner">機能戦略</div>
</div>
</div>

---

# 相互関係図

双方向の影響

<div class="mutual">
<div class="element"><strong>顧客</strong><br>ニーズ提供</div>
<div class="arrows">→<br>←</div>
<div class="element"><strong>企業</strong><br>価値提供</div>
</div>

---

<div class="title-slide">

# 全60種類の図解コンポーネント

このデザインシステムで表現力豊かなスライドを作成できます

</div>
