# /export-gslides - Google Slidesへエクスポート

Marpスライドまたはビルド済みファイルをGoogle Slidesにエクスポートする。

## 使い方

```
/export-gslides [ファイルパス] [--mode new|update] [--template テンプレートID] [--title タイトル]
```

## 引数

| 引数 | 必須 | 説明 |
|------|------|------|
| ファイルパス | - | 対象ファイル（省略時は選択） |
| `--mode` | - | `new`（新規作成）or `update`（既存更新） |
| `--template` | - | Google Slidesテンプレートの ID or URL |
| `--title` | - | スライドのタイトル |
| `--id` | - | 更新対象のスライドID（`--mode update`時） |

## モード

### new（新規作成）
- Google Driveに新しいスライドを作成
- `--template` 指定時はそのテンプレートを適用
- 指定なしの場合はこちらのデザインを反映

### update（既存更新）
- `--id` で指定したスライドを更新
- 内容のみ更新 or 全体置換を選択可能

## 例

```
/export-gslides 2_slides/proposal.md --mode new --title "提案書2024"
/export-gslides 2_slides/proposal.md --mode new --template 1ABC...xyz
/export-gslides 2_slides/proposal.md --mode update --id 1DEF...uvw
```

## デザイン反映について

- **テンプレート指定なし**: Marpのスタイルを可能な限り再現
  - 色、フォント、レイアウトを変換
  - 手書き風（Rough.js）要素は画像として埋め込み

- **テンプレート指定あり**: Google Slides側のテンプレートに内容を流し込み
  - テキスト、画像のみ転送
  - デザインはテンプレート依存

## 出力

- 作成/更新されたGoogle SlidesのURL
- 編集可能な状態で出力

## 処理フロー

```
1. 対象ファイル特定
2. モード選択（new/update）
3. Google API認証確認
4. テンプレート適用 or デザイン変換
5. スライド作成/更新
6. URL返却
```

## 認証

- `credentials.json` が必要（Google Cloud Console から取得）
- 初回実行時にOAuth認証フロー
- トークンは `.credentials/` に保存
