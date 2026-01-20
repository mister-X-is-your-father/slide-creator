#!/usr/bin/env python3
"""
Markdown to Google Slides 変換スクリプト

使用方法:
    python md_to_gslides.py input.md "プレゼンテーションタイトル"

初回実行時:
    ブラウザでGoogle認証が必要です

必要な依存:
    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
"""

import os
import sys
import re
from pathlib import Path

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
except ImportError:
    print("Error: 必要なライブラリがインストールされていません")
    print("pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client")
    sys.exit(1)

# スコープ設定
SCOPES = [
    'https://www.googleapis.com/auth/presentations',
    'https://www.googleapis.com/auth/drive.file'
]

# 認証情報のパス
SCRIPT_DIR = Path(__file__).parent.parent
CREDENTIALS_DIR = SCRIPT_DIR / 'credentials'
CLIENT_SECRET_FILE = CREDENTIALS_DIR / 'client_secret.json'
TOKEN_FILE = CREDENTIALS_DIR / 'token.json'


def get_credentials():
    """Google API認証情報を取得"""
    creds = None

    # 既存のトークンを確認
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    # トークンがない or 無効な場合は再認証
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CLIENT_SECRET_FILE.exists():
                print(f"Error: {CLIENT_SECRET_FILE} が見つかりません")
                print("Google Cloud ConsoleからOAuth認証情報をダウンロードしてください")
                sys.exit(1)

            flow = InstalledAppFlow.from_client_secrets_file(
                str(CLIENT_SECRET_FILE), SCOPES
            )
            creds = flow.run_local_server(port=0)

        # トークンを保存
        CREDENTIALS_DIR.mkdir(exist_ok=True)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    return creds


def parse_markdown(md_content: str) -> list:
    """Markdownをスライドごとにパース"""
    slides = []

    # --- で分割
    raw_slides = re.split(r'\n---\n', md_content)

    for raw_slide in raw_slides:
        slide = {'title': '', 'body': []}
        lines = raw_slide.strip().split('\n')

        for line in lines:
            # タイトル行 (# で始まる)
            if line.startswith('# '):
                slide['title'] = line[2:].strip()
            # 箇条書き
            elif line.startswith('- '):
                slide['body'].append(line[2:].strip())
            # 通常テキスト
            elif line.strip() and not line.startswith('#'):
                slide['body'].append(line.strip())

        if slide['title'] or slide['body']:
            slides.append(slide)

    return slides


def create_presentation(service, title: str) -> str:
    """新しいプレゼンテーションを作成"""
    presentation = {
        'title': title
    }
    presentation = service.presentations().create(body=presentation).execute()
    return presentation.get('presentationId')


def add_slide(service, presentation_id: str, slide_data: dict, index: int):
    """スライドを追加"""
    requests = []

    # スライドを追加
    slide_id = f'slide_{index}'
    requests.append({
        'createSlide': {
            'objectId': slide_id,
            'insertionIndex': index,
            'slideLayoutReference': {
                'predefinedLayout': 'TITLE_AND_BODY' if slide_data['body'] else 'TITLE'
            }
        }
    })

    # まずスライドを作成
    service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()

    # スライド情報を取得してプレースホルダーIDを確認
    presentation = service.presentations().get(
        presentationId=presentation_id
    ).execute()

    # 追加したスライドを検索
    slide = None
    for s in presentation.get('slides', []):
        if s.get('objectId') == slide_id:
            slide = s
            break

    if not slide:
        return

    # テキスト挿入リクエスト
    text_requests = []

    for element in slide.get('pageElements', []):
        shape = element.get('shape', {})
        placeholder = shape.get('placeholder', {})
        placeholder_type = placeholder.get('type', '')
        element_id = element.get('objectId')

        # タイトル
        if placeholder_type in ['TITLE', 'CENTERED_TITLE'] and slide_data['title']:
            text_requests.append({
                'insertText': {
                    'objectId': element_id,
                    'text': slide_data['title'],
                    'insertionIndex': 0
                }
            })

        # 本文
        elif placeholder_type == 'BODY' and slide_data['body']:
            body_text = '\n'.join(f'• {item}' for item in slide_data['body'])
            text_requests.append({
                'insertText': {
                    'objectId': element_id,
                    'text': body_text,
                    'insertionIndex': 0
                }
            })

    if text_requests:
        service.presentations().batchUpdate(
            presentationId=presentation_id,
            body={'requests': text_requests}
        ).execute()


def main():
    if len(sys.argv) < 3:
        print("使用方法: python md_to_gslides.py <input.md> <タイトル>")
        sys.exit(1)

    input_file = sys.argv[1]
    title = sys.argv[2]

    # Markdown読み込み
    if not os.path.exists(input_file):
        print(f"Error: {input_file} が見つかりません")
        sys.exit(1)

    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # パース
    slides = parse_markdown(md_content)
    print(f"パース完了: {len(slides)} スライド")

    # 認証
    creds = get_credentials()
    service = build('slides', 'v1', credentials=creds)

    # プレゼンテーション作成
    presentation_id = create_presentation(service, title)
    print(f"プレゼンテーション作成: {presentation_id}")

    # 最初の空白スライドを削除
    presentation = service.presentations().get(
        presentationId=presentation_id
    ).execute()

    if presentation.get('slides'):
        first_slide_id = presentation['slides'][0]['objectId']
        service.presentations().batchUpdate(
            presentationId=presentation_id,
            body={'requests': [{'deleteObject': {'objectId': first_slide_id}}]}
        ).execute()

    # スライド追加
    for i, slide_data in enumerate(slides):
        add_slide(service, presentation_id, slide_data, i)
        print(f"スライド {i+1}/{len(slides)} 追加完了")

    # 結果URL
    url = f"https://docs.google.com/presentation/d/{presentation_id}/edit"
    print(f"\n完了: {url}")

    # URL保存
    output_file = SCRIPT_DIR / '3_output' / 'slides_url.txt'
    output_file.parent.mkdir(exist_ok=True)
    with open(output_file, 'w') as f:
        f.write(url)
    print(f"URL保存: {output_file}")


if __name__ == '__main__':
    main()
