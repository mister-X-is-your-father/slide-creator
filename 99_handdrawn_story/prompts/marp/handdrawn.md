# Marpスライド生成プロンプト

コンテンツJSONからMarp形式のMarkdownスライドを生成してください。

## 入力情報
- コンテンツJSON: {content_json}
- スタイル: {style} (picturebook/notebook)

## 要件
1. Marpフロントマターを含める（marp: true, theme: default, size: 16:9）
2. styleタグ内にCSS定義を含める
3. 各ページを `---` で区切る
4. キャラクターはCSSアイコン（.character.char-{color}）で表現
5. 背景はsectionクラス（.bg-{type}）で指定
6. 強調はマーカークラス（.marker）で表現
7. ページ番号を各ページに含める

## CSS要件（styleタグ内に含める）

```css
/* 基本設定 */
section { background: #FFF8E7; font-family: "Zen Maru Gothic", sans-serif; }

/* キャラクターアイコン */
.character { display: inline-flex; width: 60px; height: 60px; border-radius: 50%; }
.char-blue { background: #E3F2FD; border: 3px solid #64B5F6; color: #64B5F6; }
.char-pink { background: #FCE4EC; border: 3px solid #F48FB1; color: #C2185B; }
/* 他の色も同様に定義 */

/* 背景 */
.bg-day { background: linear-gradient(180deg, #87CEEB, #E0F7FA); }
.bg-night { background: linear-gradient(180deg, #1A237E, #3949AB); color: white; }
/* 他の背景も同様に定義 */

/* 強調・装飾 */
.marker { background: linear-gradient(transparent 60%, #FFD54F 60%); }
.story-text { text-align: center; font-size: 1.3em; line-height: 2.2; }
```

## 出力形式

完全なMarp Markdownファイルを出力してください。
フロントマター、CSS定義、全ページのコンテンツを含めてください。
