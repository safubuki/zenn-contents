---
title: "【TripoSR】驚きの技術！画像一枚から3Dプリンタでリアルな造形物を簡単作成"
emoji: "🐢"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [AI,LLM,3d,3dプリンタ,stablediffusion]
published: false
---
生成AIを活用すると、一枚の画像から3Dプリンタでリアルな造形物を作成することができます！

![](/images/turtle-20240721-tripo-3dp/top_image.jpg)
*AIモノづくりサンプル画像*

驚きませんか？私はこの技術に初めて出会ったとき、感動すら覚えました！
なぜなら、一般的に3Dプリントする際は、3D形状を表現した3Dモデルデータが必要だからです。サンプル画像で示したようなjpgやpngなど、たった1枚の画像データから3Dプリントすることはできません。
それが、AIを利用することでできるわけですから、趣味の3Dプリンタと組み合わせたらどんな作品が作れるのかとワクワクしました。

これを可能にしたのが「TripoSR」です。TripoSRは、1枚の画像から素早く高品質な3Dモデルデータを作成するAIです。Stable Diffusionなどの画像生成AIで有名な、Stability AIが、Tripo AIという企業と提携して作成したものです。

詳細は以下のページをご覧ください。
https://ja.stability.ai/blog/triposr-3d-generation

これまでAIや3Dプリンタをそれぞれ楽しんでいましたが、TripoSRを活用することで、AIと3Dプリンタのモノづくりの距離が縮まり、活用の範囲が広がります。

この記事を読んで、ぜひAIモノづくりにチャレンジしてみてください👍

#### ブログ対象者

本ブログ記事は、画像生成AIや3Dプリンタに関して、ある程度の前提知識があることを想定しています。その上で「TripoSR」については、環境設定から利用方法まで、具体的な例を交えながら丁寧に解説いたします。これにより、一連の流れを把握して、AIを活用したモノづくりを目指します。

## 作成の流れ

はじめに、画像一枚から3Dプリンタでリアルな造形物を作成するまでの流れを示します。

![](/images/turtle-20240721-tripo-3dp/ai_3d_flow.png)
*生成AIによる3Dプリントの流れ*

図で示すように、OSS(オープンソースソフトウェア)のAIや非商用利用無償のツールを複数組み合わせることで、費用をかけずに作成することを目指します。

## 事前準備

### 必要なもの

以下に、必要なものを一覧で示します。

- **画像生成AI**
インターネット上には、TripoSRにより精度高く3Dモデルデータを生成するための画像データが少ないです。そのため、画像生成AIで目的の画像を生成します。普段使っているものをご使用ください。代表的なものは次の通りです。
  - ***ChatGPT Plus***（有料・オンライン）
  - ***Copilot***（無料・オンライン）
  ChatGPTとCopilotは、DALL-E3という同じ画像生成AIを使用しています。ChatGPTでは細かな設定も可能ですが、まずはCopilotで試してみると良いでしょう。
  - ***Stable Diffusion***（無料・ローカル）
- **3Dモデル生成AI**
  - ***TripoSR***
  今回の主役です！
- **3D CADソフト**
TripoSRが生成するOBJファイルを、STLファイルに変換するために使用します。変換できるのであれば、どのようなソフトでも構いませんが、以下のソフトがオススメです。
  - ***AUTODESK Fusion***
  変換だけではなく、自ら3Dモデルを作成する際にも大変便利なCADソフトです。
- **スライサソフト**
普段使っているものをご使用ください。なお、次のソフトが広く使われいます。
  - ***cura***
  私も3Dプリンタに付属していた、curaベースのソフトを愛用しています。
- **3Dプリンタ**
所有されている3Dプリンタをご使用ください。私は次の機種を愛用しています。
  - ***Neptune 3 pro***（ELEGOO社）
- **Windows版 Python**
TripoSRは、Python上で動作しますので、ご準備ください。
- **Windows PC**
TripoSRを使用するため、後述の動作環境程度のPCを準備してください。

### PC必要スペック

私が問題なくTripoSRを使用している、PCの動作環境を示します。
このPCと同等かそれ以上のPCをご準備ください。

- OS：**Windows 11**
- CPU：**AMD Ryzen 5 5500**
- メモリ：**16GB**
- GPU：**GeForce RTX3060**
- GPUメモリ：**12GB**

補足：
TripoSR使用時、下図のようにGPUメモリを消費します。8GBのGPUメモリですと、エラーになるという報告もありますので、GPUメモリを12GB以上搭載しているGPUを選定すると安心です。
※この手のGPUメモリ不足は、何らかの回避策がある可能性ありますが、本ブログでは扱いません。ご了承ください。

![](/images/turtle-20240721-tripo-3dp/gpu_memory.png =550x)
*使用時のGPUメモリ消費量*

## 環境構築

環境構築では、肝となる「**TripoSR**」のみを詳細に解説させていただき、その他については、簡易的な説明か、最低限必要なURLを提示させていただきます。環境構築方法は、リンク先の手順に従っていただくか、インターネットを検索いただくと、分かりやすいブログ記事などがヒットすると思います。

### Windows版 Python

TripoSR利用にあたって、Pythonがインストールされていることが前提となりますので、まだの方はまずインストールしてください。以下のサイトの「Pythonを導入する」の章が参考になります。

https://www.useful-python.com/env-python-vscode-windows/

### TripoSR

TripoSRについては、導入方法を詳細に解説します。

1. **TripoSRのソースをGitHubから取得**
まず、次のサイトにアクセスします。

https://github.com/VAST-AI-Research/TripoSR
　　Codeボタンを選択し、Download ZIPで任意の場所に保存後、展開します。


![](/images/turtle-20240721-tripo-3dp/tripo_git.png =600x)
*TripoSR GitHub*

:::details Gitを扱える方の場合（クリックで開く）
Gitを扱える方は、zipでダウンロードせずに、cloneコマンドでクローンしても良いです。
```
git clone https://github.com/VAST-AI-Research/TripoSR.git
```
:::

2. **コマンドプロンプトでTripoSRのフォルダ内に移動**
コマンドプロンプトを開き、TripoSRのフォルダに移動します。
CドライブにTripoSRのフォルダを保存、展開した場合は、次のコマンドを入力します。
※ご自身の環境に応じて、適宜以下のコマンドは変更ください。
```
cd c:\TripoSR
```

![](/images/turtle-20240721-tripo-3dp/cmd_tripo_cd.png =400x)
*ripoSRフォルダ内へ移動*

3. **venv（Python仮想環境）を作成**
コマンドを入力し、TripoSRフォルダ内にvenv（Python仮想環境）を作成します。

```
py.exe -m venv .venv
```
::::message
Tips
:::details なぜ、Python仮想環境を利用するのか？（クリックで開く）
Pythonで生成AIの環境を構築する際に、仮想環境を作成することは非常に重要です。なぜなら、生成AIは環境を構築する際に様々なモジュール、ライブラリをインストールするからです。仮想環境を使うことで、以下のようなメリットがあります。

- **ホスト環境を汚さない**
仮想環境内にライブラリをインストールするため、システム全体に影響を与えません。これにより、他のプロジェクトやシステムの安定性を保つことができます。
- **依存関係の管理が容易**
プロジェクトごとに異なるバージョンのライブラリを使用する場合でも、仮想環境内で完結するため、依存関係の競合を避けることができます。
- **簡単に削除可能**
不要になった仮想環境は、フォルダごと削除するだけで簡単に片付けることができます。これにより、システムをクリーンに保つことができます。

以下に、違いをイメージしやすいようvenvあり/なしの場合の開発環境の比較図を示します。

![](/images/turtle-20240721-tripo-3dp/venv_fig.png)
*venv あり/なし比較図（クリックして拡大）*

仮想環境を使うことで、Pythonのプロジェクト管理がより効率的かつ安全になります。venv初めてという方は、今後、生成AIに限らず、開発や実行環境の構築などで利用してみてください。
:::
::::

4. **仮想環境アクティベート（有効化）**
コマンドを入力し、仮想環境をアクティベート（有効化）します。
下図のように(.venv)が表示されたら、アクティベート成功です。

```
.\.venv\Scripts\activate
```

![](/images/turtle-20240721-tripo-3dp/cmd_tripo_active.png =400x)
*仮想環境アクティベート*

5. **ツールアップデート**
コマンド入力し、pip, wheel, setuptoolsのアップデートを行います。
アップデートに成功したら、successfullyが表示されます。

```
py.exe -m pip install --upgrade pip wheel setuptools
```

![](/images/turtle-20240721-tripo-3dp/cmd_update_success.png =600x)
*ツールアップデート成功*

6. **pytorchインストール**
pytorchと呼ばれる機械学習ライブラリをインストールします。
以下のPytorch.orgサイトにアクセスし、少し下にスクロールすると、環境の選択画面があります。
この選択画面で、自身の環境に合わせてポチポチ選択します。
すると「Run this Command」欄（緑の線で囲った箇所）にコマンドが表示されますので、これをコピーしてください。
  
https://pytorch.org/get-started/locally/

![](/images/turtle-20240721-tripo-3dp/pytorch_select.png =600x)
*Pytorch 環境選択画面*

::::message
Tips
:::details もし、Compute Platform（CUDAバージョン）が分からない場合（クリックで開く）
Compute Platformの項目で何を選択したらよいかわからない場合、次のコマンドを実行してください。
```
nvidia-smi
```
すると次のような表示がされますので、CUDA Version（赤線部分）を参照してください。
![](/images/turtle-20240721-tripo-3dp/nvidiasmi_cmd.png =550x)
*nvidia-smi コマンド実行画面*

なお、Pytorchの選択画面にバージョン「12.3」はありませんが、12.3が表示された場合は「12.1」を選択することでうまくいきます。
:::
::::

7. **pytorchインストール（コマンド実行）**
前の手順でコピーしたコマンドをコマンドプロンプトに貼り付けて実行します。
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```
&emsp;&emsp;※ 上記コマンドは私の環境の場合になります。
&emsp;&emsp;エラーなど無く無事終わると、次のような画面になります。

![](/images/turtle-20240721-tripo-3dp/pytorch_success.png =550x)
*Pytorch コマンド実行画面*

8. **環境変数設定**
次のコマンドを実行して、環境変数を設定します。

```
set DISTUTILS_USE_SDK=1
```

9. **TripoSRが必要なライブラリをインストール**
次のコマンドを実行して、requirements.txt（要求ファイル）に基づき、TripoSRが必要なライブラリをインストールします。

```
pip install -r requirements.txt
```

★環境構築に失敗するので、環境作り直して再度実験
★可能性→コマンドプロンプト、Cフォルダ直下→再確認



### Copilot

画像生成にCopilotを使用する場合、Microsoft Edgeブラウザを開いて、検索欄の次のアイコンをクリックするだけで使用できます。

![](/images/turtle-20240721-tripo-3dp/cop_icon.png =250x)
*Copilotアイコン*

### AUTODESK Fusion

OBJファイル→STLファイル変換にFusionを利用する場合、以下の公式サイトのページを開きます。「無償体験版をダウンロード」選択し、非商用を選択した後、手順に従って進めます。アカウント作成まだの方は必要になります。

https://www.autodesk.com/jp/products/fusion-360/overview?term=1-YEAR&tab=subscription


## 実行手順

### ○○する

### ○○する

### ○○する