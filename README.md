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
| 2026-05-13 | リスト・辞書・関数（def・return） | chapter04.py |
| 2026-05-14 | 外部ライブラリ・QRコード生成（qrcode） | chapter05.py |
| 2026-05-14 | 条件分岐・繰り返し（if文、比較演算子、elif、else、for文） | chapter06.py |

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

### chapter05.py（第5章）
- `random` モジュール（`random.randint()` で乱数生成）
- 外部ライブラリのインストール（`pip install`）
- `qrcode` ライブラリを使ったQRコード生成・保存

### chapter06.py（第6章）
- 条件分岐（`if` / `elif` / `else`）
- `random.randint()` を使ったおみくじアプリ
- `for` ループによるリストの反復処理
- `range()` 関数（開始・終了・ステップ指定）
- ネストされた `for` ループ（九九の計算表）

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

# 乱数・外部ライブラリ（第5章）
import random
num = random.randint(1, 10)  # 1〜10のランダムな整数

import qrcode
img = qrcode.make("Python楽しい!")
img.save("qrcode.png")       # QRコードを画像ファイルとして保存

# 条件分岐（第6章）
weather = "雨"
if weather == "晴れ":
    print("お買い物へ行きます")
elif weather == "雨":
    print("お家でゴロゴロします")
else:
    print("近所をお散歩します")

# for ループ
names = ["oda", "toyotomi", "tokugawa"]
for name in names:
    print(name)

for i in range(1, 10, 2):   # 1,3,5,7,9（ステップ2）
    print(i)

# ネストされたforループ（九九）
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}×{j}={i*j}")
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
│   ├── chapter04.py      # 第4章
│   ├── chapter05.py      # 第5章
│   └── chapter06.py      # 第6章
└── notes/
    └── 2026-05-12.md
```

---

## 使用教材
- 作りたいものがない人のためのPython入門（KS情報科学専門書）