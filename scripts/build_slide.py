#!/usr/bin/env python3
"""
build_slide.py - MarpスライドをHTML/PDF/画像に変換

使い方:
    python build_slide.py slide.md --format html,pdf --output 3_export/
"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import List

# プロジェクトルート
PROJECT_ROOT = Path(__file__).parent.parent

# デフォルト出力ディレクトリ
DEFAULT_OUTPUT = PROJECT_ROOT / "3_export"

# サポートする出力形式
SUPPORTED_FORMATS = ["html", "pdf", "png", "jpg", "jpeg"]


def check_marp_cli() -> bool:
    """Marp CLIがインストールされているか確認"""
    try:
        result = subprocess.run(
            ["marp", "--version"],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def build_slide(
    input_file: Path,
    output_dir: Path,
    formats: List[str],
    theme_dir: Path = None
) -> List[Path]:
    """Marpスライドをビルド"""

    if not check_marp_cli():
        print("エラー: Marp CLIがインストールされていません")
        print("インストール: npm install -g @marp-team/marp-cli")
        sys.exit(1)

    output_files = []
    theme_dir = theme_dir or PROJECT_ROOT / "theme"

    for fmt in formats:
        fmt = fmt.lower().strip()
        if fmt not in SUPPORTED_FORMATS:
            print(f"警告: サポートされていない形式をスキップ: {fmt}")
            continue

        # 出力サブディレクトリ
        fmt_dir = output_dir / fmt
        fmt_dir.mkdir(parents=True, exist_ok=True)

        # 出力ファイル名
        if fmt in ["png", "jpg", "jpeg"]:
            # 画像の場合は連番で出力される
            output_file = fmt_dir / f"{input_file.stem}.{fmt}"
        else:
            output_file = fmt_dir / f"{input_file.stem}.{fmt}"

        # Marpコマンド構築
        cmd = [
            "marp",
            str(input_file),
            "--output", str(output_file),
            "--theme-set", str(theme_dir),
            "--allow-local-files"
        ]

        # 画像形式の場合
        if fmt in ["png", "jpg", "jpeg"]:
            cmd.extend(["--images", fmt])

        # PDF の場合
        if fmt == "pdf":
            cmd.append("--pdf")

        print(f"ビルド中: {fmt}...")
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=PROJECT_ROOT
            )

            if result.returncode == 0:
                output_files.append(output_file)
                print(f"  → {output_file}")
            else:
                print(f"エラー: {fmt}のビルドに失敗")
                if result.stderr:
                    print(f"  {result.stderr}")

        except Exception as e:
            print(f"エラー: {e}")

    return output_files


def list_slides(slides_dir: Path) -> List[Path]:
    """スライドディレクトリ内のファイル一覧"""
    if not slides_dir.exists():
        return []
    return sorted(slides_dir.glob("*.md"))


def interactive_select(slides: List[Path]) -> Path:
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


def interactive_format() -> List[str]:
    """対話的に出力形式を選択"""
    print("\n出力形式を選択 (複数可、カンマ区切り):\n")
    print("  1. html - ブラウザでプレゼン")
    print("  2. pdf - 印刷・配布用")
    print("  3. png - 画像 (連番)")
    print("  4. all - すべて")

    print()
    choice = input("選択 (デフォルト: html): ").strip() or "1"

    if choice == "4" or choice.lower() == "all":
        return ["html", "pdf", "png"]

    formats = []
    for c in choice.split(","):
        c = c.strip()
        if c == "1" or c.lower() == "html":
            formats.append("html")
        elif c == "2" or c.lower() == "pdf":
            formats.append("pdf")
        elif c == "3" or c.lower() == "png":
            formats.append("png")

    return formats or ["html"]


def main():
    parser = argparse.ArgumentParser(
        description="MarpスライドをHTML/PDF/画像に変換"
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="入力ファイルパス (省略時は対話選択)"
    )
    parser.add_argument(
        "--format", "-f",
        help="出力形式 (カンマ区切り: html,pdf,png)"
    )
    parser.add_argument(
        "--output", "-o",
        default="3_export",
        help="出力ディレクトリ (デフォルト: 3_export)"
    )
    parser.add_argument(
        "--theme-dir", "-t",
        help="テーマディレクトリ (デフォルト: theme/)"
    )

    args = parser.parse_args()

    # 入力ファイル
    if args.input:
        input_file = Path(args.input)
        if not input_file.exists():
            print(f"エラー: ファイルが見つかりません: {input_file}")
            sys.exit(1)
    else:
        # 対話的に選択
        slides_dir = PROJECT_ROOT / "2_create"
        slides = list_slides(slides_dir)
        if not slides:
            print("エラー: 2_create/ にスライドがありません")
            sys.exit(1)
        input_file = interactive_select(slides)

    # 出力形式
    if args.format:
        formats = [f.strip() for f in args.format.split(",")]
    else:
        formats = interactive_format()

    # 出力ディレクトリ
    output_dir = PROJECT_ROOT / args.output
    output_dir.mkdir(parents=True, exist_ok=True)

    # テーマディレクトリ
    theme_dir = Path(args.theme_dir) if args.theme_dir else PROJECT_ROOT / "theme"

    # ビルド実行
    print(f"\n入力: {input_file}")
    print(f"出力: {output_dir}")
    print(f"形式: {', '.join(formats)}")
    print()

    output_files = build_slide(
        input_file=input_file,
        output_dir=output_dir,
        formats=formats,
        theme_dir=theme_dir
    )

    print(f"\n完了: {len(output_files)} ファイル生成")


if __name__ == "__main__":
    main()
