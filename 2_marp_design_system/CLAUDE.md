# 2_marp_design_system - デザインシステム付きMarp

## 概要

30種類以上の再利用可能CSSコンポーネント + カスタムコマンドによる自動化。

## ディレクトリ構成

```
2_marp_design_system/
├── 1_input/           # 下書き・アイデア
├── 2_slides/          # Marp形式スライド
├── 3_output/          # HTML/PDF出力
├── theme/
│   ├── theme.css      # メインテーマ
│   └── components.css # 再利用可能コンポーネント
├── .claude/
│   ├── commands/      # カスタムコマンド
│   └── slide_rules.mdc # スライドルール
└── CLAUDE.md          # 本ファイル
```

## カスタムコマンド

- `/create-slide` - 1_input → 2_slides 変換
- `/build-slide` - 2_slides → 3_output ビルド

## スライドルール

### 文字数制限
- タイトル: 最大30文字
- リード文: 最大2行
- 箇条書き: 1項目25文字以内、最大5項目

### 3層構造
```
タイトル（何について）
    ↓
リード文（結論・最も伝えたいこと）
    ↓
ボディ（根拠・詳細）
```

## CSSコンポーネント使用例

```markdown
---
marp: true
theme: custom
---

<div class="title-slide">

# プレゼンタイトル
発表者名

</div>

---

<div class="two-column">
<div class="column">

## 左カラム
- 項目1
- 項目2

</div>
<div class="column">

## 右カラム
- 項目A
- 項目B

</div>
</div>
```

## 利用可能なコンポーネント

| クラス名 | 用途 |
|----------|------|
| `.title-slide` | タイトルスライド |
| `.section-header` | セクション区切り |
| `.two-column` | 2カラムレイアウト |
| `.three-column` | 3カラムレイアウト |
| `.metric-card` | KPI/数値表示 |
| `.code-block` | コードブロック強調 |
| `.quote-box` | 引用ボックス |
| `.comparison-table` | 比較表 |
| `.timeline` | タイムライン |
| `.highlight-box` | 強調ボックス |
| `.image-caption` | 画像+キャプション |

## 依存ツール

- Marp CLI (`npm install -g @marp-team/marp-cli`)
- VSCode + Marp for VS Code拡張機能
