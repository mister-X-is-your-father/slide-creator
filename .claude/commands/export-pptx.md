# /export-pptx - PowerPointへエクスポート

MarpスライドをPowerPoint形式（.pptx）にエクスポートする。

## 使い方

```
/export-pptx [ファイルパス] [--template テンプレート] [--output 出力先]
```

## 引数

| 引数 | 必須 | 説明 |
|------|------|------|
| ファイルパス | - | 対象ファイル（省略時は選択） |
| `--template` | - | PowerPointテンプレート（.potx/.pptx）のパス |
| `--output` | - | 出力先（デフォルト: `3_output/pptx/`） |

## モード

### デザイン反映（テンプレートなし）
- Marpのスタイルを可能な限りPowerPointで再現
- 色、フォント、レイアウトを変換
- 手書き風（Rough.js）要素は画像として埋め込み

### テンプレート適用
- 指定した.potx/.pptxのデザインを使用
- テキスト、画像のみ転送
- マスタースライドのレイアウトを活用

## 例

```
/export-pptx 2_slides/proposal.md
/export-pptx 2_slides/proposal.md --template assets/templates/corporate.potx
/export-pptx 2_slides/proposal.md --output 3_output/client/
```

## 出力

```
3_output/
└── pptx/
    └── proposal.pptx
```

## 処理フロー

```
1. 対象ファイル特定
2. テンプレート有無確認
3. Marpスライド解析
4. PowerPoint変換
   - テキスト → テキストボックス
   - 画像 → 画像オブジェクト
   - 図解（Rough.js等） → 画像として埋め込み
   - スタイル → 可能な範囲で再現
5. 出力先に保存
6. 完了報告
```

## 編集可能性

- テキストは編集可能なテキストボックスとして出力
- 図解・グラフは画像だが、元データがあれば再生成可能
- PowerPoint上での追加編集を想定した構造

## 依存

- python-pptx または類似ライブラリ
