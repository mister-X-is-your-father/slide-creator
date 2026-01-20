# 3_marp_subagents - Subagents活用

## 概要

3つの専門エージェント（作成・レビュー・ビルド）による自動化ワークフロー。
Agent Skills（`.claude/skills/`）を活用し、自然言語トリガーで実行。

## ディレクトリ構成

```
3_marp_subagents/
├── 1_input/           # 下書き・アイデア
├── 2_slides/          # Marp形式スライド
├── 3_output/          # HTML/PDF出力
├── .claude/
│   ├── skills/
│   │   └── marp/
│   │       └── skill.md   # Marp構文・ベストプラクティス
│   └── commands/
│       ├── create-slide.md   # 作成エージェント
│       ├── review-slide.md   # レビューエージェント
│       └── build-slide.md    # ビルドエージェント
└── CLAUDE.md          # 本ファイル
```

## Subagents

### 1. create-agent（作成）

**トリガー**: `/create-slide` または「スライドを作成して」

**役割**:
- 1_input/draft.md を読み込み
- Marp形式に変換
- 2_slides/slides.md に出力

### 2. review-agent（レビュー）

**トリガー**: `/review-slide` または「スライドをレビューして」

**役割**:
- 2_slides/slides.md を検証
- 構文チェック
- 文字数・情報量の検証
- デザインルール準拠確認
- 改善提案

### 3. build-agent（ビルド）

**トリガー**: `/build-slide` または「スライドをビルドして」

**役割**:
- Marp CLIでビルド
- HTML/PDF出力
- 3_output/ に保存

## ワークフロー

```
「スライドを作成して」
    ↓
create-agent: 1_input → 2_slides
    ↓
「スライドをレビューして」
    ↓
review-agent: 検証・改善提案
    ↓
（修正）
    ↓
「スライドをビルドして」
    ↓
build-agent: 2_slides → 3_output
```

## 依存ツール

- Marp CLI (`npm install -g @marp-team/marp-cli`)
