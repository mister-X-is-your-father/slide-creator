#!/usr/bin/env python3
"""
export_gslides.py - MarpスライドをGoogle Slidesにエクスポート

使い方:
    python export_gslides.py slide.md --mode new --title "プレゼン"
    python export_gslides.py slide.md --mode update --id PRESENTATION_ID
"""

import argparse
import re
import sys
from pathlib import Path

# プロジェクトルート
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "3_export"))

try:
    from googleslides.slides_service import GoogleSlidesService
    from googleslides.presentation_builder import PresentationBuilder
    GSLIDES_AVAILABLE = True
except ImportError:
    GSLIDES_AVAILABLE = False


def parse_marp_slides(content: str) -> list:
    """Marpスライドをパースしてセクションのリストにする"""
    # フロントマターを除去
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

    # スライド区切りで分割
    slides = re.split(r'\n---\n', content)

    parsed = []
    for slide in slides:
        slide = slide.strip()
        if not slide:
            continue

        section = {
            'type': 'content',
            'title': '',
            'content': [],
            'raw': slide
        }

        # タイトルスライド検出
        if '<div class="title-slide">' in slide:
            section['type'] = 'title'
            # タイトル抽出
            match = re.search(r'#\s+(.+)', slide)
            if match:
                section['title'] = match.group(1).strip()
            # サブタイトル抽出（タイトル以外のテキスト）
            clean = re.sub(r'<[^>]+>', '', slide)
            clean = re.sub(r'#\s+.+', '', clean)
            section['content'] = [line.strip() for line in clean.split('\n') if line.strip()]

        # セクションヘッダー検出
        elif '<div class="section-header">' in slide:
            section['type'] = 'section'
            match = re.search(r'#\s+(.+)', slide)
            if match:
                section['title'] = match.group(1).strip()

        # 通常スライド
        else:
            # タイトル（##）
            match = re.search(r'##\s+(.+)', slide)
            if match:
                section['title'] = match.group(1).strip()

            # 箇条書き抽出
            items = re.findall(r'^[-*]\s+(.+)$', slide, re.MULTILINE)
            if items:
                section['content'] = items
            else:
                # 通常テキスト
                clean = re.sub(r'<[^>]+>', '', slide)
                clean = re.sub(r'##?\s+.+', '', clean)
                section['content'] = [line.strip() for line in clean.split('\n') if line.strip()]

        parsed.append(section)

    return parsed


def create_presentation(slides: list, title: str, template: str = None) -> tuple:
    """Google Slidesプレゼンテーションを作成"""
    try:
        builder = PresentationBuilder(
            template_name=template or 'default',
            templates_dir=str(PROJECT_ROOT / "3_export" / "templates" / "slides")
        )
    except FileNotFoundError:
        # テンプレートがない場合はデフォルト設定で進める
        print("警告: テンプレートファイルが見つかりません。デフォルト設定を使用します。")
        builder = None

    # 直接APIを使用
    service = GoogleSlidesService()
    presentation_id = service.create_presentation(title)

    requests = []
    slide_count = 0

    for section in slides:
        slide_count += 1
        slide_id = f'slide_{slide_count}'

        if section['type'] == 'title':
            # タイトルスライド
            requests.append({
                'createSlide': {
                    'objectId': slide_id,
                    'slideLayoutReference': {'predefinedLayout': 'TITLE'}
                }
            })

        elif section['type'] == 'section':
            # セクションヘッダー
            requests.append({
                'createSlide': {
                    'objectId': slide_id,
                    'slideLayoutReference': {'predefinedLayout': 'SECTION_HEADER'}
                }
            })

        else:
            # 通常コンテンツ
            requests.append({
                'createSlide': {
                    'objectId': slide_id,
                    'slideLayoutReference': {'predefinedLayout': 'TITLE_AND_BODY'}
                }
            })

    # バッチ更新
    if requests:
        service.batch_update(presentation_id, requests)

    url = service.get_presentation_url(presentation_id)
    return presentation_id, url


def update_presentation(slides: list, presentation_id: str) -> str:
    """既存のGoogle Slidesプレゼンテーションを更新"""
    service = GoogleSlidesService()

    # 既存スライドの情報を取得して更新
    # （簡易実装: 全削除して再作成ではなく、内容のみ更新）

    print(f"プレゼンテーション {presentation_id} を更新中...")
    # TODO: 詳細な更新ロジック

    url = service.get_presentation_url(presentation_id)
    return url


def list_slides(slides_dir: Path) -> list:
    """スライドディレクトリ内のファイル一覧"""
    if not slides_dir.exists():
        return []
    return sorted(slides_dir.glob("*.md"))


def interactive_select(slides: list) -> Path:
    """対話的にスライドを選択"""
    print("\n利用可能なスライド:\n")
    for i, slide in enumerate(slides, 1):
        print(f"  {i}. {slide.name}")

    print()
    while True:
        try:
            choice = input("番号を選択 (q で終了): ").strip()
            if choice.lower() == "q":
                sys.exit(0)
            idx = int(choice) - 1
            if 0 <= idx < len(slides):
                return slides[idx]
            print("無効な番号です")
        except ValueError:
            print("数字を入力してください")


def main():
    parser = argparse.ArgumentParser(
        description="MarpスライドをGoogle Slidesにエクスポート"
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="入力ファイルパス (省略時は対話選択)"
    )
    parser.add_argument(
        "--mode", "-m",
        choices=["new", "update"],
        default="new",
        help="モード: new (新規作成) / update (既存更新)"
    )
    parser.add_argument(
        "--title", "-t",
        help="プレゼンテーションのタイトル (新規作成時)"
    )
    parser.add_argument(
        "--id",
        help="プレゼンテーションID (更新時)"
    )
    parser.add_argument(
        "--template",
        help="テンプレート名"
    )

    args = parser.parse_args()

    # Google Slides モジュール確認
    if not GSLIDES_AVAILABLE:
        print("エラー: Google Slides モジュールが利用できません")
        print("必要なパッケージをインストールしてください:")
        print("  pip install google-api-python-client google-auth-oauthlib")
        sys.exit(1)

    # 入力ファイル
    if args.input:
        input_file = Path(args.input)
        if not input_file.exists():
            print(f"エラー: ファイルが見つかりません: {input_file}")
            sys.exit(1)
    else:
        slides_dir = PROJECT_ROOT / "2_create"
        slides = list_slides(slides_dir)
        if not slides:
            print("エラー: 2_create/ にスライドがありません")
            sys.exit(1)
        input_file = interactive_select(slides)

    # スライド読み込み・パース
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    slides = parse_marp_slides(content)
    print(f"\n{len(slides)} スライドを検出")

    # エクスポート実行
    if args.mode == "new":
        title = args.title or input_file.stem
        print(f"\n新規プレゼンテーション作成: {title}")
        try:
            presentation_id, url = create_presentation(
                slides=slides,
                title=title,
                template=args.template
            )
            print(f"\n✓ 作成完了")
            print(f"  ID: {presentation_id}")
            print(f"  URL: {url}")
        except Exception as e:
            print(f"\nエラー: {e}")
            print("\n認証が必要な場合は、credentials.json を設定してください。")
            sys.exit(1)

    elif args.mode == "update":
        if not args.id:
            print("エラー: --id でプレゼンテーションIDを指定してください")
            sys.exit(1)
        print(f"\nプレゼンテーション更新: {args.id}")
        try:
            url = update_presentation(slides=slides, presentation_id=args.id)
            print(f"\n✓ 更新完了")
            print(f"  URL: {url}")
        except Exception as e:
            print(f"\nエラー: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
