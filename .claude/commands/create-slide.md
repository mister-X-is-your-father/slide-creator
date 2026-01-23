# /create-slide - テキストからスライド生成

入力テキスト/Markdownファイルを指定されたテイストでMarpスライドに変換する。

## 使い方

```
/create-slide [ファイルパス] [--style テイスト] [--characters ディレクトリ]
```

## 引数

| 引数 | 必須 | 説明 |
|------|------|------|
| ファイルパス | ○ | 入力ファイル（`1_input/` 内推奨） |
| `--style` | - | テイスト指定（省略時は選択肢表示） |
| `--characters` | - | キャラクター画像ディレクトリ |

## テイスト一覧

### business（ビジネス向け）
- `business/default` - 標準ビジネス
- `business/modern` - モダン
- `business/corporate` - コーポレート
- `business/minimal` - ミニマル

### handdrawn（手書き風）
- `handdrawn/light` - 軽い手書き（ビジネスでも使える）
- `handdrawn/normal` - 標準的な手書き
- `handdrawn/sketchy` - しっかり手書き
- `handdrawn/rough` - 荒い落書き風
- `handdrawn/crayon` - クレヨン風
- `handdrawn/pen` - ペン風
- `handdrawn/marker` - マーカー風

### picturebook（絵本風）
- `picturebook/warm` - 暖色系
- `picturebook/pastel` - パステル
- `picturebook/colorful` - カラフル

## 処理ルール

1. **テキストはリライトしない** - 原文をそのまま使用
2. **配置は最適化する** - スライド分割、レイアウト調整
3. **図解は自動生成** - 内容に応じてcomponents.css/infographics.cssから適切なものを選択
4. **Rough.js使用** - handdrawn系テイストの場合、`assets/js/handdrawn.js`を活用

## 出力

`2_slides/` ディレクトリにMarp形式のMarkdownファイルを生成。

## 例

```
/create-slide 1_input/proposal.md --style business/modern
/create-slide 1_input/story.md --style picturebook/warm --characters assets/characters/animals/
```

## 処理フロー

```
1. 入力ファイル読み込み
2. テイスト未指定なら選択肢表示
3. テキスト構造解析（見出し、段落、箇条書き）
4. スライド分割（1スライド = 1トピック目安）
5. 各スライドに適切なコンポーネント割り当て
6. キャラクター画像があれば配置提案
7. Marp Markdown生成
8. 2_slides/ に出力
```
