---
marp: true
theme: default
paginate: true
footer: 'システムアーキテクチャ解説'
style: |
  section {
    font-family: 'Noto Sans CJK JP', 'Noto Sans JP', sans-serif;
  }
---

# システムアーキテクチャ解説

図解で理解するシステム構成

---

# アジェンダ

1. 全体構成
2. データフロー
3. まとめ

---

# 全体構成

システムの主要コンポーネント

```mermaid
flowchart LR
    A[ユーザー] --> B[フロントエンド]
    B --> C[API Gateway]
    C --> D[バックエンド]
    D --> E[データベース]
```

---

# データフロー

リクエストからレスポンスまで

```mermaid
sequenceDiagram
    User->>Frontend: リクエスト
    Frontend->>API: APIコール
    API->>DB: クエリ
    DB-->>API: 結果
    API-->>Frontend: レスポンス
    Frontend-->>User: 表示
```

---

# 各コンポーネントの役割

| コンポーネント | 役割 |
|--------------|------|
| フロントエンド | UI表示、ユーザー入力処理 |
| API Gateway | 認証、ルーティング |
| バックエンド | ビジネスロジック |
| データベース | データ永続化 |

---

# まとめ

- シンプルな3層アーキテクチャ
- API Gatewayで認証を一元化
- 各層の責務が明確

---

# ご清聴ありがとうございました
