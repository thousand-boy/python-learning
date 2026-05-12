# python-learning

作業療法士からAIアプリケーションエンジニア転職を目指して独学中。
Python基礎の学習記録リポジトリです。

---

## 学習環境

| ツール | 用途 |
|---|---|
| Google Colab | 1行ずつ実行して結果を確認しながら学習 |
| VS Code | 完成コードの保存・管理 |
| GitHub | 学習証跡の蓄積・公開 |

---

## 進捗

| 日付 | 内容 | ファイル |
|---|---|---|
| 2026-05-12 | Google ColabからVS Codeへの移行・GitHub使用方法習得 | - |
| 2026-05-12 | Python基礎（変数・データ型・文字列・型変換） | chapter01_03.py |
| 2026-05-12 | リスト・辞書・関数（def・return） | chapter04.py |

---

## 学習内容サマリー

### chapter01_03.py（第1〜3章）
- `print()` による出力
- 変数（文字列・数値・真偽値）
- 四則演算・BMI計算
- データ型（int・float・str・bool）と `type()` 関数
- 文字列操作（結合・スライス・`len()`）
- f文字列（f"Hello,{name}"）
- 型変換（`str()` / `int()` / `float()`）

### chapter04.py（第4章）
- リスト（作成・取得・更新・追加・削除・件数）
- 辞書（作成・取得・追加・更新・削除・結合）
- 関数（`def`・`print` と `return` の違い）

---

## 学習した主な構文

```python
# リスト
sweets = ["プリン","ケーキ","チョコ"]
sweets.append("アイス")   # 追加
del sweets[1]              # 削除
print(len(sweets))         # 件数

# 辞書
onsen = {"下呂温泉":"岐阜県"}
onsen["有馬温泉"] = "兵庫県"  # 追加

# 関数
def add_numbers(a, b):
    return a + b

output = add_numbers(5, 7)
print(output)  # → 12
```

---

## GitHub学習記録（2026-05-12）

初めてGitHubを使用し、以下を習得：

- SSHキーの生成・GitHubへの登録
- リポジトリの作成・クローン
- 毎日のコミット手順（add → commit → push）
- .gitignoreの設定（.DS_Storeの除外）
- コミットメッセージの書き方

---

## フォルダ構成

```
python-learning/
├── README.md
├── .gitignore
├── 01_basics/
│   ├── chapter01_03.py   # 第1〜3章
│   └── chapter04.py      # 第4章
└── notes/
    └── 2026-05-12.md
```

---

## 使用教材

- 作りたいものがない人のためのPython入門（KS情報科学専門書）
