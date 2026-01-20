# Marp Skill

Marp（Markdown Presentation Ecosystem）を使用したスライド生成のベストプラクティス。

## Marp基本構文

### フロントマター

```yaml
---
marp: true
theme: default        # default, gaia, uncover
paginate: true        # ページ番号表示
header: 'ヘッダー'
footer: 'フッター'
backgroundColor: #fff
color: #333
---
```

### スライド区切り

```markdown
# スライド1

内容

---

# スライド2

内容
```

### 画像

```markdown
![width:500px](image.png)
![height:300px](image.png)
![bg](background.png)        # 背景画像
![bg left:40%](image.png)    # 左に40%で配置
![bg right](image.png)       # 右に配置
```

### 分割レイアウト

```markdown
![bg left:50%](image.png)

# タイトル

右側にテキスト
```

### カラム（CSS使用）

```markdown
<style>
.columns { display: grid; grid-template-columns: 1fr 1fr; gap: 1em; }
</style>

<div class="columns">
<div>

## 左カラム
- 内容

</div>
<div>

## 右カラム
- 内容

</div>
</div>
```

## ベストプラクティス

### 構成

1. **タイトルスライド**: 発表タイトル、発表者、日付
2. **アジェンダ**: 発表の流れ
3. **コンテンツ**: 本編（1スライド1メッセージ）
4. **まとめ**: 要点の振り返り
5. **クロージング**: 質疑応答、連絡先

### 文字数制限

- タイトル: 30文字以内
- リード文: 2行以内
- 箇条書き: 1項目25文字以内、最大5項目

### 3層構造

```
タイトル: 何について
    ↓
リード文: 結論（最も伝えたいこと）
    ↓
ボディ: 根拠・詳細
```

## よくあるミス

- 文字が多すぎる → 箇条書きで簡潔に
- 画像が小さい → `width:` / `height:` で調整
- 背景画像が見にくい → 半透明オーバーレイを追加
- フォントサイズ不統一 → CSSで統一

## コマンドリファレンス

```bash
# HTML出力
marp slides.md -o slides.html

# PDF出力
marp slides.md --pdf -o slides.pdf

# PPTX出力
marp slides.md --pptx -o slides.pptx

# プレビューサーバー
marp -s slides.md

# テーマ指定
marp slides.md --theme theme.css -o slides.html
```
