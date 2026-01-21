# 99_handdrawn_story - 手書き風ストーリースライド生成

## 概要

AIプロンプト + テンプレートシステムで手書き風の物語スライドを生成。

## ディレクトリ構成

```
99_handdrawn_story/
├── prompts/
│   ├── outline/       # アウトライン生成プロンプト
│   │   ├── picturebook.md   # 絵本風
│   │   ├── horror.md        # ホラー・ノート風
│   │   └── learning.md      # 学習・教訓系
│   ├── content/       # コンテンツ展開プロンプト
│   │   └── detailed.md      # 詳細化
│   └── style/         # スタイル指定プロンプト
│       ├── handdrawn.md     # 手書き風共通
│       └── characters.md    # キャラクター生成
├── templates/
│   ├── story/         # ストーリー構造テンプレート
│   │   ├── basic.json       # 基本構造
│   │   ├── three_act.json   # 3幕構成
│   │   └── journey.json     # 旅・冒険構造
│   └── slide/         # Marpスライドテンプレート
│       ├── picturebook.md   # 絵本風
│       ├── notebook.md      # ノート風
│       └── sketch.md        # スケッチ風
├── output/            # 生成物出力
├── assets/            # 素材リンク（2から参照）
└── CLAUDE.md          # 本ファイル
```

## ワークフロー

```
1. トピック入力
   ↓
2. アウトライン生成（prompts/outline/*.md）
   ↓
3. コンテンツ展開（prompts/content/detailed.md）
   ↓
4. スタイル適用（prompts/style/*.md + templates/slide/*.md）
   ↓
5. Marpスライド出力（output/）
```

## 使い方

### 1. アウトラインプロンプトを選択

```bash
# 絵本風ストーリー
cat prompts/outline/picturebook.md

# ホラー風ストーリー
cat prompts/outline/horror.md
```

### 2. AIにトピックと共にプロンプトを渡す

```
[トピック]: 友情の大切さ
[対象]: 子供向け
[ページ数]: 20

上記のプロンプトで物語のアウトラインを生成してください。
```

### 3. テンプレートでスライド化

```bash
# テンプレート確認
cat templates/slide/picturebook.md
```

## プロンプト変数

| 変数 | 説明 | 例 |
|------|------|-----|
| `{topic}` | テーマ・トピック | 友情、勇気、夢 |
| `{audience}` | 対象者 | 子供向け、大人向け |
| `{page_count}` | ページ数 | 15-30 |
| `{style}` | スタイル | 絵本風、ホラー風 |
| `{lesson}` | 教訓（任意） | コミュニケーションのコツ |

## 出力形式

### アウトライン（JSON）

```json
{
  "title": "物語タイトル",
  "style": "picturebook",
  "pages": [
    {
      "number": 1,
      "type": "cover",
      "title": "表紙タイトル",
      "illustration": "イラスト説明"
    },
    {
      "number": 2,
      "type": "story",
      "text": "本文",
      "illustration": "イラスト説明",
      "characters": ["キャラA", "キャラB"]
    }
  ],
  "characters": [
    {
      "name": "主人公名",
      "role": "主人公",
      "color": "blue",
      "symbol": "A"
    }
  ],
  "lesson": "教訓"
}
```

## 2番との連携

```
assets/ → 2_marp_design_system/assets/ へのシンボリックリンク
templates/slide/*.md は 2_marp_design_system/theme/handdrawn.css を使用
```

## コマンド例（Claude Code）

```
「友情」をテーマに絵本風のストーリースライドを作成して。
20ページくらいで、子供向け。教訓は「助け合いの大切さ」。
```

## 依存

- 2_marp_design_system/theme/handdrawn.css
- 2_marp_design_system/assets/icons/
- Marp CLI
