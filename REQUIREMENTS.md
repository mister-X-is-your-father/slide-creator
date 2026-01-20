# スライド自動生成システム 要件定義

## 概要

Claude Codeを使用して、自然言語の指示からプレゼンテーションスライドを自動生成するシステム。
複数のアプローチを並行して管理・テストできる構成。

---

## ディレクトリ構成

```
slide-creator/
├── 1_marp_basic/              # 基本Marp（VSCode拡張）
├── 2_marp_design_system/      # デザインシステム付きMarp
├── 3_marp_subagents/          # Subagents活用
├── 4_marp_ai_image/           # AI画像生成連携
├── 5_html_direct/             # HTML直接生成
├── 6_pptx_direct/             # .pptx直接生成
└── REQUIREMENTS.md            # 本ドキュメント
```

---

## アプローチ一覧

### 1_marp_basic（基本Marp）

**出典**: SIOS Tech Lab

**概要**: VSCode + Marp拡張機能で基本的なスライド生成

**特徴**:
- 学習コスト最小
- VSCodeでリアルタイムプレビュー
- シンプルなワークフロー

**ワークフロー**:
```
1_input/draft.md → Claudeで変換 → 2_slides/slides.md → Marp拡張でプレビュー → 3_output/
```

**依存**:
- VSCode
- Marp for VS Code拡張機能

---

### 2_marp_design_system（デザインシステム付き）

**出典**: Zenn (loglass)

**概要**: 30種類以上の再利用可能CSSコンポーネント + カスタムコマンド

**特徴**:
- デザイン一貫性
- 豊富なコンポーネント
- 3層構成（theme.css + slide_rules.mdc + template）

**構成**:
```
2_marp_design_system/
├── 1_input/
├── 2_slides/
├── 3_output/
├── theme/
│   ├── theme.css
│   └── components.css
├── .claude/
│   ├── commands/
│   └── slide_rules.mdc
└── CLAUDE.md
```

**CSSコンポーネント**:
- `.title-slide` - タイトルスライド
- `.section-header` - セクション区切り
- `.two-column` / `.three-column` - カラムレイアウト
- `.metric-card` - KPI/数値表示
- `.code-block` - コードブロック強調
- `.quote-box` - 引用ボックス
- `.comparison-table` - 比較表
- `.timeline` - タイムライン
- `.highlight-box` - 強調ボックス

---

### 3_marp_subagents（Subagents活用）

**出典**: Qiita (toku345)

**概要**: 3つの専門エージェント（作成・レビュー・ビルド）で自動化

**特徴**:
- Agent Skills活用（`.claude/skills/marp/skill.md`）
- 自然言語トリガーで実行
- 役割分担による品質向上

**構成**:
```
3_marp_subagents/
├── 1_input/
├── 2_slides/
├── 3_output/
├── .claude/
│   ├── skills/
│   │   └── marp/
│   │       └── skill.md
│   └── commands/
│       ├── create-slide.md
│       ├── review-slide.md
│       └── build-slide.md
└── CLAUDE.md
```

**Subagents**:
1. **create-agent**: スライド作成
2. **review-agent**: 構文・内容レビュー
3. **build-agent**: HTML/PDF出力

---

### 4_marp_ai_image（AI画像生成連携）

**出典**: Classmethod

**概要**: Marp + Gemini（Nano Banana Pro）で画像自動生成

**特徴**:
- テンプレートに可変/固定セクション分離
- Mermaid記法で図解生成
- 画像自動生成・置換

**構成**:
```
4_marp_ai_image/
├── 1_input/
├── 2_slides/
├── 3_output/
├── scripts/
│   └── gemini_image.py
├── .claude/
│   └── commands/
└── CLAUDE.md
```

**依存**:
- Vertex AI / Gemini API
- Python

---

### 5_html_direct（HTML直接生成）

**出典**: Zenn (oikon)

**概要**: Marpを使わず、HTML/CSSでスライドを直接生成

**特徴**:
- 専門ツール学習不要
- 自由度が高い
- CSS調整で全ページ一括変更

**構成**:
```
5_html_direct/
├── 1_input/
│   └── slides.md
├── 2_artifacts/
│   ├── slides.yaml
│   └── slides.html
├── 3_output/
│   └── slides.pdf
├── scripts/
│   └── html-to-pdf.js
├── fig/
├── .claude/
│   └── commands/
│       └── update-slide.md
└── CLAUDE.md
```

**ワークフロー**:
```
slides.md → YAML変換 → HTML生成 → PDF出力
```

**依存**:
- Puppeteer（PDF変換）

---

### 6_pptx_direct（.pptx直接生成）

**出典**: Qiita (AoraNow)

**概要**: Claude Max/Team/Enterpriseで直接PowerPoint生成

**特徴**:
- 追加ツール不要
- 即座にPowerPoint形式
- 叩き台として十分なクオリティ

**制限**:
- 有料プラン必須（Max/Team/Enterprise）
- 部分修正が困難
- 5時間セッション制限

**推奨プロンプト構成**:
1. 事前に骨子を作成
2. タイトル・リード文・ボディの3層構造
3. ビジュアルは適切に（無闘なグラフ化を避ける）

---

## 共通ルール

### スライド構成ルール

| 要素 | 制限 |
|------|------|
| タイトル | 最大30文字 |
| リード文 | 最大2行（結論を記述） |
| 箇条書き | 1項目25文字以内、最大5項目 |

### 3層構造

```
タイトル（何について）
    ↓
リード文（結論・最も伝えたいこと）
    ↓
ボディ（根拠・詳細）
```

### カラーパレット（共通）

```css
:root {
  --primary: #2563eb;      /* メインカラー */
  --secondary: #64748b;    /* サブカラー */
  --accent: #f59e0b;       /* アクセント */
  --background: #ffffff;   /* 背景 */
  --text: #1e293b;         /* テキスト */
  --code-bg: #f1f5f9;      /* コード背景 */
}
```

---

## 依存ツール一覧

| ツール | 用途 | アプローチ |
|--------|------|-----------|
| Marp CLI | MD→HTML/PDF変換 | 1, 2, 3, 4 |
| Marp for VS Code | プレビュー | 1, 2, 3, 4 |
| Puppeteer | HTML→PDF変換 | 5 |
| Gemini API | 画像生成 | 4 |
| Claude Max/Team | .pptx生成 | 6 |

---

## 参考記事

| # | 出典 | URL |
|---|------|-----|
| 1 | SIOS Tech Lab | https://tech-lab.sios.jp/archives/48479 |
| 2 | Zenn (loglass) | https://zenn.dev/loglass/articles/a8b4b069c09002 |
| 3 | Qiita (toku345) | https://qiita.com/toku345/items/11158328ca098957ff27 |
| 4 | Classmethod | https://dev.classmethod.jp/articles/claude-code-nano-banana-pro-proposal-slide-generation/ |
| 5 | Zenn (oikon) | https://zenn.dev/oikon/articles/953921403e9cf2 |
| 6 | Qiita (AoraNow) | https://qiita.com/AoraNow_Yoshiyuki_Ito/items/e7e85ef32ba87c2c5d8c |
| 7 | Note (七夕研究所) | https://note.com/tanabata_lab/n/nd1384e4f0a22 |
| 8 | 侍エンジニア | https://generative-ai.sejuku.net/blog/9233/ |
