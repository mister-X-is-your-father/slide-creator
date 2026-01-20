---
marp: true
theme: default
paginate: true
style: |
  :root {
    --primary: #2563eb;
    --secondary: #64748b;
    --accent: #f59e0b;
    --background: #ffffff;
    --text: #1e293b;
    --code-bg: #f1f5f9;
    --success: #10b981;
    --error: #ef4444;
  }
  section {
    background-color: var(--background);
    color: var(--text);
    font-family: 'Noto Sans JP', sans-serif;
  }
  h1 {
    color: var(--primary);
    border-bottom: 3px solid var(--primary);
    padding-bottom: 0.3em;
  }
  .title-slide {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  .title-slide h1 {
    border-bottom: none;
    font-size: 2.5em;
  }
  .two-column {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2em;
  }
  .metric-card {
    background: linear-gradient(135deg, var(--code-bg) 0%, white 100%);
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.5em;
    text-align: center;
  }
  .metric-card .number {
    font-size: 2.5em;
    font-weight: bold;
    color: var(--primary);
  }
  .metric-card .label {
    color: var(--secondary);
  }
  .highlight-box {
    background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
    border: 2px solid var(--primary);
    border-radius: 8px;
    padding: 1em;
  }
  .timeline-item {
    border-left: 3px solid var(--primary);
    padding-left: 1em;
    margin-bottom: 1em;
  }
  .timeline-item .date {
    color: var(--secondary);
    font-weight: bold;
  }
  .check { color: var(--success); }
  .cross { color: var(--error); }
---

<div class="title-slide">

# AIスライド生成の比較

6つのアプローチと使い分け

</div>

---

# アジェンダ

1. 6つのアプローチ概要
2. 比較表
3. 導入効果
4. タイムライン
5. まとめ

---

# 6つのアプローチ

用途に応じた最適な選択肢

<div class="two-column">
<div>

### Marp系
1. **基本** - シンプル
2. **デザインシステム** - 統一感
3. **Subagents** - 自動化
4. **AI画像** - リッチ

</div>
<div>

### 非Marp系
5. **HTML直接** - 自由度
6. **PPTX直接** - 即座

</div>
</div>

---

# 比較表

| アプローチ | 学習コスト | カスタマイズ | 自動化 |
|-----------|:--------:|:----------:|:-----:|
| Marp基本 | 低 | 低 | - |
| デザインシステム | 中 | 高 | 中 |
| Subagents | 中 | 高 | 高 |
| AI画像 | 高 | 高 | 高 |
| HTML直接 | 中 | 最高 | 低 |
| PPTX直接 | 低 | 低 | - |

---

# 導入効果

作業時間を大幅削減

<div class="two-column">
<div class="metric-card">
<div class="number">86%</div>
<div class="label">作業時間削減</div>
</div>
<div class="metric-card">
<div class="number">80→11h</div>
<div class="label">従来 → 導入後</div>
</div>
</div>

---

# タイムライン

導入までの流れ

<div class="timeline-item">
<div class="date">2024/01</div>
調査開始 - 各手法のリサーチ
</div>

<div class="timeline-item">
<div class="date">2024/02</div>
プロトタイプ - 検証環境構築
</div>

<div class="timeline-item">
<div class="date">2024/03</div>
本番導入 - チーム展開
</div>

---

# まとめ

<div class="highlight-box">

- **6つのアプローチ**から選択可能
- **用途に応じて**使い分ける
- **デザインシステム**がバランス良い

</div>

---

<div class="title-slide">

# ご清聴ありがとうございました

</div>
