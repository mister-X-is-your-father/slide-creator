# 2_marp_design_system - デザインシステム付きMarp

## 概要

30種類以上の再利用可能CSSコンポーネント + カスタムコマンドによる自動化。

## ディレクトリ構成

```
2_marp_design_system/
├── 1_input/           # 下書き・アイデア・テンプレート
├── 2_slides/          # Marp形式スライド
├── 3_output/          # HTML/PDF出力
├── theme/
│   ├── theme.css      # メインテーマ（ビジネス用）
│   ├── components.css # 再利用可能コンポーネント
│   └── handdrawn.css  # 手書き風テーマ（物語用）
├── assets/
│   ├── icons/         # アイコン素材（Lucide, Phosphor）
│   ├── characters/    # キャラクター素材
│   └── illustrations/ # イラスト素材
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

## 手書き風テーマ（handdrawn.css）

物語・絵本スライド用の専用テーマ。

### スタイルバリエーション

| クラス | スタイル | 用途 |
|--------|----------|------|
| `.style-picturebook` | 絵本風 | 子供向け、温かい物語 |
| `.style-notebook` | ノート風 | ホラー、日常系 |
| `.style-sketch` | スケッチ風 | アート系 |
| `.style-comic` | コミック風 | アクション、コメディ |
| `.style-diary` | 日記風 | 回想、エモーショナル |

### 手書き風コンポーネント

| クラス | 用途 |
|--------|------|
| `.character` | キャラクターアイコン（丸枠） |
| `.bubble` | 吹き出し |
| `.bubble-think` | 思考吹き出し |
| `.bubble-shout` | 叫び吹き出し |
| `.story-text` | 物語本文 |
| `.moral-box` | 教訓ボックス |
| `.bg-day/sunset/night/forest/sea` | シーン背景 |

### 物語テンプレート

`1_input/template_story_handdrawn.md` を参照。

## アセット

### アイコン（assets/icons/）

- **Lucide**: 1,600+ アイコン（MIT）
- **Phosphor**: 1,200+ アイコン（MIT）

### 使い方

```html
<!-- SVGを直接埋め込み -->
<img src="assets/icons/lucide/icons/heart.svg" width="24">

<!-- または CSS background -->
.icon-heart {
  background: url('assets/icons/lucide/icons/heart.svg');
}
```

## 依存ツール

- Marp CLI (`npm install -g @marp-team/marp-cli`)
- VSCode + Marp for VS Code拡張機能
