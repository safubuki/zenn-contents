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

これを可能にしたのが「**TripoSR**」です。TripoSRは、1枚の画像から素早く高品質な3Dモデルデータを作成するAIです。Stable Diffusionなどの画像生成AIで有名な、Stability AIが、Tripo AIという企業と提携して作成したものです。

詳細は以下のページをご覧ください。
https://ja.stability.ai/blog/triposr-3d-generation

これまで、AIと3Dプリンタは別々に楽しんでいましたが、TripoSRを活用することで、AIと3Dプリンタの距離がグッと縮まり、モノづくりへの活用の範囲が一気に広がりました！

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

- **ソフト**
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
  - **Windows版 Python**
  TripoSRは、Python上で動作しますので、ご準備ください。

- **ハード**
  - **3Dプリンタ**
  所有されている3Dプリンタをご使用ください。私は次の機種を愛用しています。
    - ***Neptune 3 pro***（ELEGOO社）
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

環境構築では、肝となる「**TripoSR**」のみを詳細に解説させていただき、その他については、簡易的な説明か、最低限必要なURLを提示させていただきます。なお、既に導入済みのものについては、スキップしてください。

### ●Python

TripoSR利用にあたって、Pythonがインストールされていることが前提となりますので、まだの方はまずインストールしてください。

1. **インストーラをダウンロード**
以下の公式サイトにアクセスして、インストーラをダウンロードします。

https://www.python.org/downloads/

![](/images/turtle-20240721-tripo-3dp/python_1.png =500x)
*インストーラのダウンロード*

2. **Pythonインストール**
インストーラを実行すると、次のような画面が表示されますので、画面下部のチェックボックス両方にチェックを入れて「Install Now」をクリックしてください。インストールが完了したら「Close」ボタンで終了します。
※「***Add python.exe to PATH***」は、デフォルトでチェックが入っていないので、チェックを入れ忘れないよう注意してください。

![](/images/turtle-20240721-tripo-3dp/python_2.png =500x)
*Pythonインストーラ画面*

### ●Git for Windows

TripoSR環境構築の際に、Gitというソースコードを管理する仕組みを利用して、必要なソフトを取得する必要があります。「Git for Windows」というツールを利用します。以下の記事を参考にして、インストールしてください。

https://qiita.com/T-H9703EnAc/items/4fbe6593d42f9a844b1c

### ●Build Tools for Visual Studio

TripoSRそのものはpythonですが、torchmcubesのような一部のライブラリのコンパイルにC++コンパイラとして「Build Tools for Visual Studio」を使用します。

1. **インストーラをダウンロード**
以下の公式サイトにアクセスして、インストーラをダウンロードします。
※リンクをクリックすると目的の箇所にフォーカスします。

https://visualstudio.microsoft.com/ja/downloads/#build-tools-for-visual-studio-2022

![](/images/turtle-20240721-tripo-3dp/down_build_tool.png =600x)
*インストーラのダウンロード*

2. **Build Toolsのインストール**
インストーラを実行すると、次のような画面が表示されますので「**C++によるデスクトップ開発**」**チェックボックスにチェック**を入れてインストールをクリックしてください。
※インストールの詳細は、デフォルトチェックのままでOKです。

![](/images/turtle-20240721-tripo-3dp/build_tool.png =600x)
*Build Toolsインストーラ画面*

### ●CUDA Toolkit

TripoSR環境構築の際に、Gitというソースコードを管理する仕組みを利用して、必要なソフトを取得する必要があります。「Git for Windows」というツールを利用します。以下の記事を参考にして、インストールしてください。

1. **Toolkitが既にあるか確認**
次のコマンドを実行して、例のようにバージョン表示などがされる場合は、既に存在していますので、以降の手順は不要です。

https://visualstudio.microsoft.com/ja/downloads/#build-tools-for-visual-studio-2022

![](/images/turtle-20240721-tripo-3dp/down_build_tool.png =600x)
*インストーラのダウンロード*

1. **インストーラをダウンロード**
以下の公式サイトにアクセスして、インストーラをダウンロードします。
※リンクをクリックすると目的の箇所にフォーカスします。

https://visualstudio.microsoft.com/ja/downloads/#build-tools-for-visual-studio-2022

![](/images/turtle-20240721-tripo-3dp/down_build_tool.png =600x)
*インストーラのダウンロード*

2. **Build Toolsのインストール**
インストーラを実行すると、次のような画面が表示されますので「**C++によるデスクトップ開発**」**チェックボックスにチェック**を入れてインストールをクリックしてください。
※インストールの詳細は、デフォルトチェックのままでOKです。

![](/images/turtle-20240721-tripo-3dp/build_tool.png =600x)
*Build Toolsインストーラ画面*

### ●TripoSR

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

2. **Windows PowerShell起動**
検索窓に「windowspowershell」と入力し、PowerShellを起動します。

![](/images/turtle-20240721-tripo-3dp/power_shell.png =250x)

3. **TripoSRのフォルダ内に移動**
PowerShellで、TripoSRのフォルダに移動します。
CドライブにTripoSRのフォルダを保存、展開した場合は、次のコマンドを入力します。
※ご自身の環境に応じて、適宜以下のコマンドは変更ください。

```
cd c:\TripoSR
```

![](/images/turtle-20240721-tripo-3dp/cmd_tripo_cd.png =350x)
*TripoSRフォルダ内へ移動*

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

![](/images/turtle-20240721-tripo-3dp/cmd_tripo_active.png =350x)
*仮想環境アクティベート（有効化）*

5. **ツールアップデート**
コマンド入力し、仮想環境内のpip, wheel, setuptoolsのアップデートを行います。
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

:::details 以前のバージョンのPytorchをインストールしたい場合（クリックで開く）
今後、Pytorchのバージョンがどんどん上がっていき、場合によっては最新のバージョンだと正常に動作しないケースが出てくる可能性があります。そのような場合、以下の公式サイトを参考にすることで、以前のバージョンをインストールことができます。

https://pytorch.org/get-started/previous-versions/

例えば、v2.3.1（CUDA12.1）をインストールするときは、次の内容を参照して、

![](/images/turtle-20240721-tripo-3dp/prev_torch.png =600x)
*v2.3.1のインストールコマンド*

赤枠で囲った、次のコマンドを入力します。

```
pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cu121
```
※ご自身の環境に応じて、適切なコマンドを選択してください。
なお、本記事執筆時点（2024年7月）においては、v2.3.1、v2.4.0で動作を確認しております。
:::
::::

7. **pytorchインストール（コマンド実行）**
前の手順でコピーしたコマンドをコマンドプロンプトに貼り付けて実行します。
エラーなど無く無事終わると、次のような画面になります。

![](/images/turtle-20240721-tripo-3dp/pytorch_success.png =550x)
*Pytorch コマンド実行画面*

8. **環境変数設定**
次のコマンドを実行して、環境変数を設定します。

```
set DISTUTILS_USE_SDK=1
```

8. **TripoSRのrequirements.txt書き換え**
TripoSRの環境構築に必要な依存モジュールを記した**requirements.txt**を書き換えます。
具体的には、この中の「torchmcubes」というモジュールが、最新バージョンだとcmakeコンパイルに失敗するため、以前のバージョンを指定します。
変更するファイルの場所は`C:\TripoSR\requirements.txt`です。
※ ご自身でTripoSRを保存した場所によって、ファイルの場所も異なります。


![](/images/turtle-20240721-tripo-3dp/req_before.png =550x)
*requirements.txt 変更前*

![](/images/turtle-20240721-tripo-3dp/req_after.png =550x)
*requirements.txt 変更後*

```
git+https://github.com/tatsy/torchmcubes.git@cbb3c3795b1e168bf81e8dee28623eaf5c33cd1c
```

9. **TripoSRが必要なライブラリをインストール**
次のコマンドを実行して、requirements.txt（要求ファイル）に基づき、TripoSRが必要なライブラリをインストールします。

```
pip install -r requirements.txt
```

★環境構築に失敗するので、環境作り直して再度実験
★可能性→コマンドプロンプト、Cフォルダ直下→再確認



### ●Copilot

画像生成にCopilotを使用する場合、Microsoft Edgeブラウザを開いて、検索欄の次のアイコンをクリックするだけで使用できます。

![](/images/turtle-20240721-tripo-3dp/cop_icon.png =250x)
*Copilotアイコン*

### ●AUTODESK Fusion

OBJファイル→STLファイル変換にFusionを利用する場合、以下の公式サイトのページを開きます。「無償体験版をダウンロード」選択し、非商用を選択した後、手順に従って進めます。アカウント作成まだの方は必要になります。

https://www.autodesk.com/jp/products/fusion-360/overview?term=1-YEAR&tab=subscription


## 実行手順

### ○○する

### ○○する

### ○○する