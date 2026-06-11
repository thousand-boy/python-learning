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
| 2026-05-15・16 | PDF操作自動化（PyMuPDF）、画像処理自動化（Pillow） | chapter07.py |
| 2026-05-18 | Webスクレイピング（requests・BeautifulSoup） | chapter08.py |
| 2026-05-19 | 機械学習（scikit-learn・NumPy・手書き数字認識） | chapter09.py |
| 2026-05-20 | WebアプリUI作成（Gradio）・画像生成AI（Stable Diffusion）・画像生成AIアプリ作成 | chapter10.py |
| 2026-05-22 | 音声文字起こし（Whisper）・生成AI連携（Gemini API）・会議自動要約アプリ作成 | chapter11.py |

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

### chapter07.py（第7章）
- `PyMuPDF` によるPDF操作自動化
  - テキスト抽出（`get_text()`）
  - ページ抽出・保存（`select()`）
  - ページ回転（`set_rotation()`）
  - PDFの結合（`insert_file()`）
  - ページ削除（`delete_page()`）
- `Pillow` による画像処理自動化
  - 画像サイズ取得（`img.size`）
  - リサイズ（`resize()`）
  - 回転（`rotate()`）
  - グレースケール変換（`convert("L")`）

### chapter08.py（第8章）
- `requests` によるWebページの取得（`requests.get()`）
- レスポンスのエンコーディング指定（`response.encoding`）
- `BeautifulSoup` によるHTMLパース（`html.parser`）
- タグ単位でのデータ抽出（`soup.find()`・`.text`）
  - `h1` / `h2` / `p` タグのテキスト取得

  ### chapter09.py（第9章）
- `scikit-learn` による教師あり学習の体験
  - `datasets.load_digits()`：手書き数字データセットの読み込み
  - データの形状確認（`digits.data.shape` / `digits.target` / `digits.images`）
  - `matplotlib.pyplot` による画像表示（`plt.imshow()`）
  - 白黒反転処理（`16 - digits.images`）
  - `sklearn.svm.SVC` による分類モデルの作成
  - `model.fit()` で学習、`model.predict()` で予測
- `NumPy` を用いた画像データの前処理
  - `np.asarray()` で画像を数値配列に変換
  - 0〜16の範囲への正規化（`* 17 // 256`）
  - `flatten()` による2次元→1次元変換
- `Pillow` との連携：自作画像の読み込み・グレースケール化・8×8リサイズ

### chapter10.py（第10章）
- `Gradio` によるWebアプリUI作成
  - `gr.Interface()` でWebアプリを構築（`fn` / `inputs` / `outputs` / `flagging_mode`）
  - `app.launch()` でWebブラウザ上にアプリを起動
  - 入力フォーム（`gr.Textbox`）・出力表示（`gr.Image`）のカスタマイズ
- `Stable Diffusion` による画像生成AI
  - `diffusers` ライブラリから `StableDiffusionPipeline` をインポート
  - `from_pretrained()` でモデルをロード（`CompVis/stable-diffusion-v1-4`）
  - `.to("cuda")` でGPU上で動作させる設定
  - テキストプロンプトから画像を生成（`pipeline(prompt).images[0]`）
  - 生成画像をファイルに保存（`image.save()`）
- GradioとStable Diffusionを組み合わせた**画像生成AIアプリ**の作成
  - テキスト入力 → AI画像生成 → 結果表示までを1つのWebアプリに統合
  - 関数のdocstring（処理内容・引数・戻り値の説明文）の書き方

### chapter11.py（第11章）
- `openai-whisper` による音声・動画の文字起こし
  - `whisper.load_model()` でモデルを選択（`"medium"` など）
  - `model.transcribe()` で動画ファイルを文字起こし
  - `result["text"]` で文字起こし結果を取得
- `Gemini API` による生成AI連携
  - API・APIキーの概念理解（Application Programming Interfaceの略）
  - `getpass()` でAPIキーを安全に入力（入力内容が画面に表示されない）
  - `google-genai` ライブラリで Gemini に接続
  - `genai.Client()` でクライアントを作成
  - `client.models.generate_content()` でモデルを選択しプロンプトを送信
  - `response.text` で回答テキストを取得
- WhisperとGeminiを組み合わせた**会議自動要約アプリ**の作成
  - 動画ファイルをアップロード → 文字起こし → Geminiで要約 の一連の流れを実装
  - f文字列でプロンプトに文字起こし結果を埋め込む
---

## 学習した主な構文

### 第1〜3章：Python基礎

```python
# 出力・変数
print("Hello Python")
a = 100
b = "Hello Python"

# 四則演算
print(1 + 2)   # 足し算
print(2 - 1)   # 引き算
print(1 * 2)   # 掛け算
print(1 / 2)   # 割り算
print(3 // 2)  # 切り捨て除算
print(5 % 2)   # 余り

# BMI計算
height = 1.75
weight = 70
bmi = weight / (height * height)
print(bmi)

# データ型と type()
i = 123
f = 1.23
s = "ぱいせん"
b = True
print(type(i), type(f), type(s), type(b))

# 文字列操作
my_name = "私はPython仙人"
print(len(my_name))     # 文字数
print(my_name[2])       # インデックス指定
print(my_name[-2])      # 後ろからインデックス
print(my_name[2:8])     # スライス
print(my_name[1:8:2])   # ステップ付きスライス

# f文字列
name = "ぱいせん"
message = f"Hello,{name}"
print(message)

# 型変換
str_num = str(12.3)          # 数値 → 文字列
int_num = int("123")         # 文字列 → 整数
float_num = float("123.45")  # 文字列 → 小数
print("富士山の高さは" + str(3776) + "メートルです")
```

### 第4章：リスト・辞書・関数

```python
# リスト
sweets = ["プリン", "ケーキ", "チョコ"]
print(sweets[0])          # 取得
sweets[1] = "アイス"      # 更新
sweets.append("アイス")   # 追加（1件）
sweets.extend(["アイス", "クッキー"])  # 追加（複数）
del sweets[1]             # 削除
print(len(sweets))        # 件数

# 辞書
onsen = {"下呂温泉": "岐阜県", "草津温泉": "群馬県"}
print(onsen.get("下呂温泉"))        # 取得
onsen["有馬温泉"] = "兵庫県"        # 追加
onsen["下呂温泉"] = "岐阜県下呂市"  # 更新
rivers1.update(rivers2)            # 結合
del rivers1["天塩川"]              # 削除

# 関数
def add_numbers(a, b):
    return a + b

output = add_numbers(5, 7)
print(output)  # → 12

def triangle_area(base, height):
    area = base * height / 2
    return area
```

### 第5章：外部ライブラリ

```python
# 乱数
import random
num = random.randint(1, 10)  # 1〜10のランダムな整数
print(num)

# QRコード生成
import qrcode
img = qrcode.make("Python楽しい!")
img.save("qrcode.png")
```

### 第6章：条件分岐・繰り返し

```python
# if / elif / else
weather = "雨"
if weather == "晴れ":
    print("お買い物へ行きます")
elif weather == "雨":
    print("お家でゴロゴロします")
else:
    print("近所をお散歩します")

# おみくじ（randint + if）
omikuji = random.randint(0, 3)
if omikuji == 0:
    print("大吉")
elif omikuji == 1:
    print("中吉")
else:
    print("小吉")

# for ループ
names = ["oda", "toyotomi", "tokugawa"]
for name in names:
    print(name)

for i in range(5):        # 0〜4
    print(i)

for i in range(1, 10, 2): # 1,3,5,7,9（ステップ2）
    print(i)

# ネストされたforループ（九九）
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}×{j}={i*j}")
```

### 第7章：PDF操作・画像処理

```python
# PDF操作（PyMuPDF）
import pymupdf

doc = pymupdf.open("error.pdf")
text = doc[0].get_text()   # テキスト抽出
doc.close()

doc.select([0])            # 1ページ目のみ抽出
doc.save("error_1page.pdf")

doc[0].set_rotation(90)    # ページ回転
doc.save("rotated.pdf")

doc_a.insert_file(doc_b)   # PDF結合
doc_a.save("inserted.pdf")

doc.delete_page(2)         # ページ削除
doc.save("deleted.pdf")

# 画像処理（Pillow）
from PIL import Image

img = Image.open("sample.jpg")
print(f"画像の幅は{img.size[0]}")  # サイズ取得
print(f"画像の高さは{img.size[1]}")

resized_img = img.resize((int(img.size[0]*2), int(img.size[1]*0.5)))
resized_img.save("resized.jpg")     # リサイズ

rotated_img = img.rotate(90)
rotated_img.save("rotated.jpg")     # 回転

grayscale_img = img.convert("L")
grayscale_img.save("grayscale.jpg") # グレースケール変換
```

### 第8章：Webスクレイピング

```python
# Webページ取得（requests）
import requests

url = "https://miyashinblog.com/books/sample.html"
response = requests.get(url)
response.encoding = "utf-8"  # 文字化け防止
print(response.text)         # HTMLソース表示

# HTMLパース（BeautifulSoup）
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")
print(soup.find("h1").text)  # h1タグのテキスト取得
print(soup.find("h2").text)  # h2タグのテキスト取得
print(soup.find("p").text)   # pタグのテキスト取得
```

### 第9章：機械学習（手書き数字認識）
 
```python
# データセットの読み込み
from sklearn import datasets
digits = datasets.load_digits()
 
print(digits.data.shape)   # (1797, 64)：1797枚×64画素
print(digits.target[:5])   # 先頭5枚の正解ラベル
print(digits.images[0])    # 1枚目の8×8画像データ
 
# 画像表示
import matplotlib.pyplot as plt
plt.imshow(digits.images[0], cmap="gray")
plt.show()
 
# 白黒反転（学習データに合わせる）
inverted_imgs = 16 - digits.images
plt.imshow(inverted_imgs[0], cmap="gray")
plt.show()
 
# モデルの学習
import sklearn.svm
model = sklearn.svm.SVC()
model.fit(16 - digits.data, digits.target)  # 反転データで学習
 
# 新しい画像で予測（前処理）
from PIL import Image
import numpy as np
 
image = Image.open("0.jpg")
grayscale_img = image.convert("L")          # グレースケール化
resize_img = grayscale_img.resize((8, 8))   # 8×8にリサイズ
 
num_img = np.asarray(resize_img, dtype=int) # 数値配列に変換
normalized_img = num_img * 17 // 256        # 0〜16に正規化
flattened_img = normalized_img.flatten()    # 1×64に変換
 
# 予測
pred = model.predict([flattened_img])
print(pred)  # → [0]（予測結果）
```

### 第10章：WebアプリUI・画像生成AI

```python
# Gradioであいさつアプリ
import gradio as gr

def greet(name):
    return "こんにちは、" + name + "さん!"

app = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
    flagging_mode="never"
)
app.launch()

# Stable Diffusionで画像生成
from diffusers import StableDiffusionPipeline
import torch

pipeline = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4"
).to("cuda")                          # GPUで動作

prompt = "cat by picasso"
image = pipeline(prompt).images[0]    # プロンプトから画像生成
image.save(f"{prompt}.png")           # ファイルに保存

# GradioとStable Diffusionを組み合わせた画像生成AIアプリ
from diffusers import StableDiffusionPipeline
import gradio as gr
import torch

def generative_image(text):
    """
    引数で受け取ったテキストから画像を生成する関数

    引数：
        text(str型)：生成したい画像を指示するテキスト
    戻り値：
        image(画像データ)：生成した画像データ
    """
    pipeline = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4"
    ).to("cuda")
    image = pipeline(text).images[0]
    return image

app = gr.Interface(
    fn=generative_image,
    inputs=gr.Textbox(label="生成したい画像の特徴を入力"),
    outputs=gr.Image(label="画像生成結果"),
    title="画像生成アプリ",
    description="テキストを入力して画像を生成します",
    flagging_mode="never",
)
app.launch()
```

### 第11章：音声文字起こし・生成AI連携

```python
# Whisperで文字起こし
import whisper

model = whisper.load_model("medium")       # モデルを読み込む
result = model.transcribe("meeting.mp4")   # 動画を文字起こし
print(result["text"])                      # テキストを表示

# APIキーを安全に入力
from getpass import getpass
google_api_key = getpass("APIキーを入力して下さい:")

# Gemini APIで質問
from google import genai

client = genai.Client(api_key=google_api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Pythonでエラーが出たらGeminiに聞いても良い？簡潔に教えて",
)
print(response.text)  # 回答テキストを表示

# WhisperとGeminiを組み合わせた会議自動要約アプリ
import whisper
from google import genai
from getpass import getpass

# 文字起こし
model = whisper.load_model("medium")
result = model.transcribe("meeting.mp4")
transcribed_text = result["text"]
print(transcribed_text)

# Geminiで要約
google_api_key = getpass("APIキーを入力して下さい:")
client = genai.Client(api_key=google_api_key)

prompt = f"次の会議内容を簡潔に要約して下さい:{transcribed_text}"

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)
print("要約結果:")
print(response.text)
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
│   ├── chapter06.py      # 第6章
│   ├── chapter07.py      # 第7章
│   ├── chapter08.py      # 第8章
│   ├── chapter09.py      # 第9章
│   └── chapter10.py      # 第10章
└── notes/
    ├── 2026-05-12.md     # 環境構築・Python基礎
    ├── 2026-05-13.md     # リスト・辞書・関数
    ├── 2026-05-14.md     # 外部ライブラリ・条件分岐・繰り返し
    ├── 2026-05-15_16.md  # PDF操作・画像処理
    ├── 2026-05-18.md     # Webスクレイピング
    ├── 2026-05-19.md     # 機械学習
    ├── chapter10.py      # 第10章
    └── chapter11.py      # 第11章
```

---

## 📚 使用教材、読書ログ

| 著者 | タイトル | 出版社 | 出版年 | ステータス |
| :--- | :--- | :--- | :--- | :--- |
| みやさかしんや | [作りたいものがない人のためのPython入門](https://kodansha.co.jp) | 講談社 | 2026年 | 読了 (Completed) |
