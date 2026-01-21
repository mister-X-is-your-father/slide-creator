# Google Slides Integration

Google Slides APIを使用してプレゼンテーションを作成・アップロードするモジュール。

## セットアップ

### 1. Google Cloud Console の設定

1. [Google Cloud Console](https://console.cloud.google.com/) にアクセス
2. 新規プロジェクトを作成（または既存のプロジェクトを選択）
3. 「APIとサービス」→「ライブラリ」から「Google Slides API」を有効化
4. 「APIとサービス」→「認証情報」→「認証情報を作成」→「OAuth 2.0 クライアント ID」
5. アプリケーションの種類: 「デスクトップアプリ」を選択
6. 作成後、JSONをダウンロードして `credentials.json` としてプロジェクトルートに配置

### 2. 依存関係のインストール

```bash
pip install -r googleslides/requirements.txt
```

## 使い方

### 基本的な使い方

```python
from googleslides import PresentationBuilder

# テンプレートを指定してビルダーを作成
builder = PresentationBuilder(
    template_name='business-proposal',
    templates_dir='illustrated-curriculum-creator/templates/slides'
)

# スライドを追加
builder.add_title_slide("プロジェクト提案", "2025年度")
builder.add_section_slide("01", "はじめに", "概要説明")
builder.add_content_slide("背景", ["課題1", "課題2", "課題3"])

# プレゼンテーションを作成
presentation_id, url = builder.build("My Presentation")
print(f"作成完了: {url}")
```

### サンプルスクリプトの実行

```bash
python -m googleslides.example
```

## モジュール構成

```
googleslides/
├── __init__.py              # パッケージエントリポイント
├── auth.py                  # OAuth 2.0 認証
├── slides_service.py        # Google Slides API ラッパー
├── presentation_builder.py  # プレゼンテーションビルダー
├── example.py               # サンプルスクリプト
├── requirements.txt         # 依存関係
└── README.md                # このファイル
```

## 利用可能なテンプレート

`illustrated-curriculum-creator/templates/slides/` に配置されているテンプレート:

- `default.json` - シンプルな白背景
- `business-proposal.json` - ビジネス提案書（赤・ベージュ）
- `modern.json` - モダンデザイン
- `academic.json` - アカデミック

## API リファレンス

### PresentationBuilder

```python
builder = PresentationBuilder(template_name='default', templates_dir='templates/slides')
```

**メソッド:**

- `add_title_slide(title, subtitle=None)` - タイトルスライドを追加
- `add_section_slide(section_number, section_title, description=None)` - セクション区切りを追加
- `add_content_slide(title, content_lines)` - コンテンツスライドを追加
- `build(title)` - プレゼンテーションを作成、(presentation_id, url) を返す

### GoogleSlidesService

低レベルAPI操作用:

```python
from googleslides import GoogleSlidesService

service = GoogleSlidesService()
presentation_id = service.create_presentation("タイトル")
service.batch_update(presentation_id, requests)
url = service.get_presentation_url(presentation_id)
```

## 認証トークン

初回実行時にブラウザでGoogle認証が行われ、トークンは `~/.slide-creator/token.pickle` に保存されます。
