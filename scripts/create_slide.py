#!/usr/bin/env python3
"""
create_slide.py - テキストからMarpスライドを生成

使い方:
    python create_slide.py input.md --style business/modern --characters assets/characters/
"""

import argparse
import json
import re
from pathlib import Path
from typing import List, Dict, Optional, Tuple

# プロジェクトルート
PROJECT_ROOT = Path(__file__).parent.parent

# テイスト設定ファイル
STYLES_JSON = PROJECT_ROOT / "theme" / "styles.json"


def load_styles() -> Dict:
    """styles.jsonを読み込む"""
    with open(STYLES_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def parse_style_arg(style_arg: str) -> Tuple[str, str]:
    """スタイル引数をパース (例: 'business/modern' -> ('business', 'modern'))"""
    if "/" in style_arg:
        category, variant = style_arg.split("/", 1)
    else:
        category = style_arg
        variant = "default"
    return category, variant


def get_style_config(category: str, variant: str, styles_data: Dict) -> Dict:
    """スタイル設定を取得"""
    style_info = styles_data["styles"].get(category, {})
    variant_info = style_info.get("variants", {}).get(variant, {})
    return {
        "category": category,
        "variant": variant,
        "name": style_info.get("name", category),
        "css": style_info.get("css", []),
        "js": style_info.get("js", []),
        "variant_config": variant_info
    }


def analyze_text_structure(content: str) -> List[Dict]:
    """テキスト構造を解析してセクションに分割"""
    lines = content.strip().split("\n")
    sections = []
    current_section = None

    for line in lines:
        stripped = line.strip()

        # 見出し検出
        if stripped.startswith("# "):
            if current_section:
                sections.append(current_section)
            current_section = {
                "type": "title",
                "level": 1,
                "title": stripped[2:].strip(),
                "content": []
            }
        elif stripped.startswith("## "):
            if current_section:
                sections.append(current_section)
            current_section = {
                "type": "section",
                "level": 2,
                "title": stripped[3:].strip(),
                "content": []
            }
        elif stripped.startswith("### "):
            if current_section:
                sections.append(current_section)
            current_section = {
                "type": "subsection",
                "level": 3,
                "title": stripped[4:].strip(),
                "content": []
            }
        elif stripped.startswith("- ") or stripped.startswith("* "):
            # 箇条書き
            if current_section is None:
                current_section = {"type": "list", "title": "", "content": []}
            current_section["content"].append({
                "type": "list_item",
                "text": stripped[2:].strip()
            })
        elif stripped.startswith(tuple(f"{i}." for i in range(1, 10))):
            # 番号付きリスト
            if current_section is None:
                current_section = {"type": "numbered_list", "title": "", "content": []}
            text = re.sub(r"^\d+\.\s*", "", stripped)
            current_section["content"].append({
                "type": "numbered_item",
                "text": text
            })
        elif stripped:
            # 通常のテキスト
            if current_section is None:
                current_section = {"type": "text", "title": "", "content": []}
            current_section["content"].append({
                "type": "paragraph",
                "text": stripped
            })
        # 空行は無視

    if current_section:
        sections.append(current_section)

    return sections


def select_component(section: Dict, style_config: Dict) -> str:
    """セクションに適したコンポーネントを選択"""
    section_type = section.get("type", "")
    content = section.get("content", [])
    content_count = len(content)

    # タイトルスライド
    if section_type == "title":
        return "title-slide"

    # セクションヘッダー
    if section_type == "section" and content_count == 0:
        return "section-header"

    # リスト系
    if section_type == "list" or any(c.get("type") == "list_item" for c in content):
        if content_count <= 3:
            return "icon-list"
        elif content_count <= 5:
            return "bullet-points"
        else:
            return "checklist"

    # 番号付きリスト → ステップ
    if section_type == "numbered_list" or any(c.get("type") == "numbered_item" for c in content):
        if content_count <= 4:
            return "steps"
        else:
            return "numbered-list"

    # テキストが多い場合
    if content_count >= 3:
        return "two-column"

    return "default"


def generate_slide_content(section: Dict, component: str, style_config: Dict) -> str:
    """セクションからスライドコンテンツを生成"""
    title = section.get("title", "")
    content = section.get("content", [])

    lines = []

    # コンポーネントに応じたHTML構造
    if component == "title-slide":
        lines.append('<div class="title-slide">')
        lines.append("")
        lines.append(f"# {title}")
        if content:
            lines.append("")
            for item in content:
                lines.append(item.get("text", ""))
        lines.append("")
        lines.append("</div>")

    elif component == "section-header":
        lines.append('<div class="section-header">')
        lines.append("")
        lines.append(f"# {title}")
        lines.append("")
        lines.append("</div>")

    elif component == "steps":
        lines.append(f"## {title}" if title else "")
        lines.append("")
        lines.append('<div class="steps">')
        for i, item in enumerate(content, 1):
            text = item.get("text", "")
            lines.append(f'<div class="step">')
            lines.append(f'<div class="number">{i}</div>')
            lines.append(f'<div class="title">{text}</div>')
            lines.append('</div>')
        lines.append('</div>')

    elif component == "icon-list":
        lines.append(f"## {title}" if title else "")
        lines.append("")
        lines.append('<ul class="icon-list">')
        for item in content:
            text = item.get("text", "")
            lines.append(f'<li><span class="icon">▸</span><div class="content"><span class="title">{text}</span></div></li>')
        lines.append('</ul>')

    elif component == "two-column":
        lines.append(f"## {title}" if title else "")
        lines.append("")
        lines.append('<div class="two-column">')
        lines.append('<div class="column">')
        lines.append("")
        mid = len(content) // 2
        for item in content[:mid]:
            text = item.get("text", "")
            if item.get("type") == "list_item":
                lines.append(f"- {text}")
            else:
                lines.append(text)
        lines.append("")
        lines.append('</div>')
        lines.append('<div class="column">')
        lines.append("")
        for item in content[mid:]:
            text = item.get("text", "")
            if item.get("type") == "list_item":
                lines.append(f"- {text}")
            else:
                lines.append(text)
        lines.append("")
        lines.append('</div>')
        lines.append('</div>')

    else:
        # デフォルト
        if title:
            lines.append(f"## {title}")
            lines.append("")
        for item in content:
            text = item.get("text", "")
            item_type = item.get("type", "")
            if item_type == "list_item":
                lines.append(f"- {text}")
            elif item_type == "numbered_item":
                lines.append(f"1. {text}")
            else:
                lines.append(text)

    return "\n".join(lines)


def generate_marp_header(style_config: Dict) -> str:
    """Marpヘッダーを生成"""
    category = style_config["category"]
    css_files = style_config.get("css", [])

    # CSS読み込み（実際にはthemeディレクトリからの相対パス）
    # Marpではthemeオプションでカスタムテーマを指定

    header_lines = [
        "---",
        "marp: true",
        f"theme: {category}",
        "paginate: true",
        "---",
        ""
    ]

    return "\n".join(header_lines)


def create_slide(
    input_file: Path,
    output_dir: Path,
    style: str,
    characters_dir: Optional[Path] = None
) -> Path:
    """メイン処理: テキストからMarpスライドを生成"""

    # スタイル設定読み込み
    styles_data = load_styles()
    category, variant = parse_style_arg(style)
    style_config = get_style_config(category, variant, styles_data)

    # 入力ファイル読み込み
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # テキスト構造解析
    sections = analyze_text_structure(content)

    # 各セクションをスライドに変換
    slides = []
    for section in sections:
        component = select_component(section, style_config)
        slide_content = generate_slide_content(section, component, style_config)
        slides.append(slide_content)

    # Marpドキュメント生成
    marp_header = generate_marp_header(style_config)
    marp_content = marp_header + "\n---\n\n".join(slides)

    # 出力
    output_file = output_dir / f"{input_file.stem}.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(marp_content)

    return output_file


def list_styles(styles_data: Dict) -> None:
    """利用可能なスタイル一覧を表示"""
    print("\n利用可能なスタイル:\n")
    for category, info in styles_data["styles"].items():
        print(f"  {category}/ ({info.get('name', '')})")
        for variant, vinfo in info.get("variants", {}).items():
            vname = vinfo.get("name", variant) if isinstance(vinfo, dict) else variant
            print(f"    - {category}/{variant}: {vname}")
        print()


def main():
    parser = argparse.ArgumentParser(
        description="テキストからMarpスライドを生成"
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="入力ファイルパス"
    )
    parser.add_argument(
        "--style", "-s",
        default="business/default",
        help="スタイル指定 (例: business/modern, handdrawn/sketchy)"
    )
    parser.add_argument(
        "--output", "-o",
        default="2_create",
        help="出力ディレクトリ (デフォルト: 2_create)"
    )
    parser.add_argument(
        "--characters", "-c",
        help="キャラクター画像ディレクトリ"
    )
    parser.add_argument(
        "--list-styles", "-l",
        action="store_true",
        help="利用可能なスタイル一覧を表示"
    )

    args = parser.parse_args()

    # スタイル一覧表示
    if args.list_styles:
        styles_data = load_styles()
        list_styles(styles_data)
        return

    # 入力ファイル必須チェック
    if not args.input:
        parser.error("入力ファイルを指定してください")

    input_file = Path(args.input)
    if not input_file.exists():
        print(f"エラー: ファイルが見つかりません: {input_file}")
        return

    output_dir = PROJECT_ROOT / args.output
    output_dir.mkdir(parents=True, exist_ok=True)

    characters_dir = Path(args.characters) if args.characters else None

    # スライド生成
    output_file = create_slide(
        input_file=input_file,
        output_dir=output_dir,
        style=args.style,
        characters_dir=characters_dir
    )

    print(f"生成完了: {output_file}")
    print(f"スタイル: {args.style}")


if __name__ == "__main__":
    main()
