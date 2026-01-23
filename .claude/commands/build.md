# /build - スライドをビルド・出力

`2_slides/` のMarpスライドをHTML/PDF等に変換する。

## 使い方

```
/build [ファイルパス] [--format 形式] [--output 出力先]
```

## 引数

| 引数 | 必須 | 説明 |
|------|------|------|
| ファイルパス | - | 対象ファイル（省略時は最新 or 選択） |
| `--format` | - | 出力形式（省略時は選択肢表示、複数指定可） |
| `--output` | - | 出力先ディレクトリ（デフォルト: `3_output/`） |

## 出力形式

| 形式 | 説明 |
|------|------|
| `html` | ブラウザでプレゼン可能なHTML |
| `pdf` | 印刷・配布用PDF |
| `png` | スライドごとの画像（連番） |
| `jpg` | スライドごとの画像（連番） |

## 例

```
/build 2_slides/proposal.md --format html
/build 2_slides/proposal.md --format html,pdf
/build --format html --output 3_output/2024-01/
```

## 出力先構造

```
3_output/
├── html/
│   └── proposal.html
├── pdf/
│   └── proposal.pdf
└── images/
    ├── proposal-001.png
    ├── proposal-002.png
    └── ...
```

## 処理フロー

```
1. 対象ファイル特定（引数 or 選択）
2. 出力形式選択（引数 or 選択、複数可）
3. Marp CLIでビルド実行
4. 指定ディレクトリに出力
5. 完了報告（ファイルパス表示）
```

## 依存

- Marp CLI (`@marp-team/marp-cli`)
- Chromium（PDF/画像出力時）
