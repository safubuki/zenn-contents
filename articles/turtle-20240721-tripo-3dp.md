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

## 必要なもの

次に、必要なものをソフトウェアとハードウェアに分類してリストにしました。使用するソフトウェアが多く感じるかもしれませんが、環境構築や実行手順で触れますので、ご安心ください。

![](/images/turtle-20240721-tripo-3dp/needs_list.png)
*必要なものリスト*

**PCスペックの補足：**
TripoSR使用時、下図のようにGPUメモリを消費します。8GBのGPUメモリですと、エラーになるという報告もありますので、GPUメモリを12GB以上搭載しているGPUを選定すると安心です。

![](/images/turtle-20240721-tripo-3dp/gpu_memory.png =550x)
*使用時のGPUメモリ消費量*

## 環境構築

環境構築では「**TripoSR**」を中心に説明します。その他、TripoSRの環境を構築する上で必要なPythonやCUDA Toolkit等については、簡易的な説明を用意しておりますので、未導入の場合に限り、必要な項目を参照し、環境を構築してください。なお、環境構築は上から順に実施してください。

### ●Python

::::message
Python環境構築方法
:::details Windows版Pythonのインストール手順（クリックで開く）
1. **インストーラをダウンロード**
以下の公式サイトにアクセスして、インストーラをダウンロードします。

[![](/images/turtle-20240721-tripo-3dp/link_python.png)](https://www.python.org/downloads/)

![](/images/turtle-20240721-tripo-3dp/python_1.png =550x)
*インストーラのダウンロード*

2. **Pythonインストール**
インストーラを実行すると、次のような画面が表示されますので、画面下部のチェックボックス両方にチェック（※）を入れて「Install Now」をクリックしてください。インストールが完了したら「Close」ボタンで終了します。
※「***Add python.exe to PATH***」は、デフォルトでチェックが入っていないので、チェックを入れ忘れないよう注意してください。

![](/images/turtle-20240721-tripo-3dp/python_2.png =550x)
*Pythonインストーラ画面*
:::
::::

### ●Git

::::message
Git環境構築方法
:::details Git for Windowsインストール手順（クリックで開く）
以下の記事を参考に、インストールしてください。

[![](/images/turtle-20240721-tripo-3dp/link_git.png)](https://qiita.com/T-H9703EnAc/items/4fbe6593d42f9a844b1c)
:::
::::

### ●Build Tools

::::message
Build Tools（C++コンパイラ）環境構築方法
:::details Build Tools for Visual Studioインストール手順（クリックで開く）
1. **インストーラをダウンロード**
以下の公式サイトにアクセスして、インストーラをダウンロードします。
※リンクをクリックすると目的の箇所にフォーカスします。

[![](/images/turtle-20240721-tripo-3dp/link_msbuild.png)](https://visualstudio.microsoft.com/ja/downloads/#build-tools-for-visual-studio-2022)

![](/images/turtle-20240721-tripo-3dp/down_build_tool.png =600x)
*インストーラのダウンロード*

2. **Build Toolsのインストール**
インストーラを起動すると、次のような画面が表示されるので「**C++によるデスクトップ開発**」**にチェック**を入れてインストールボタンをクリックしてください。
※インストールの詳細は、デフォルトチェックのままでOKです。

![](/images/turtle-20240721-tripo-3dp/build_tool.png =600x)
*Build Toolsインストーラ画面*
:::
::::

### ●CUDA Toolkit

::::message
CUDA 環境構築方法
:::details CUDA Toolkitインストール手順（クリックで開く）
1. **Toolkitが既にインストール済みか確認**
次のコマンドを実行して、バージョンなどが表示されたら、Toolkitインストール済みのため、スキップしてください。

```
nvcc --version
```

![](/images/turtle-20240721-tripo-3dp/nvcc_check.png =400x)
*nvcc --versionコマンド実行（インストール済み）*

2. **CUDA Toolkitのダウンロード①**
次の公式サイトにアクセスして、GPUドライババージョンに応じたToolkitをArchived Releasesの中から選択します。
※私の場合、GPUドライババージョン「546.01」にマッチする「CUDA Toolkit 12.3.0 (October 2023)」を選択しました。

[![](/images/turtle-20240721-tripo-3dp/link_cuda.png)](https://developer.nvidia.com/cuda-toolkit-archive)

※GPUの型番やGPUドライバのバージョンに応じて、適切なCUDAバージョンの選択方法について、次のページで解説されています。必要に応じて参照ください。なお、同ページ内の「Dockerイメージを用いたCUDA環境構築」については対象外とします。
[![](/images/turtle-20240721-tripo-3dp/link_cuda_ver.png)](https://zenn.dev/yumizz/articles/73d6c7d1085d2f)

3. **CUDA Toolkitのダウンロード②**
選択すると、次のような画面が表示されるので、自身の環境に応じて選択し、ダウンロードします。

![](/images/turtle-20240721-tripo-3dp/toolkit_down.png =550x)
*インストーラのダウンロード*

4. **CUDA Toolkitのインストール**
インストーラを実行すると、次のような画面が表示されるので、使用許諾了承して、高速（推奨）選択し、CUDA Visual Studio Integrationの確認項目にチェックを入れて、次々進みます。

![](/images/turtle-20240721-tripo-3dp/nvidia_2.png =500x)
*CUDA Toolkitインストーラ画面 オプション選択（一部抜粋）*

5. **CUDA Toolkitのインストール確認**
次のコマンドで、CUDA Toolkitインストールができていることを確認します。バージョンなどが表示されたら成功です

```
nvcc --version
```

:::
::::

### ●TripoSR

TripoSRについて、導入方法を詳細に解説します。

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
※ご自身の環境に合わせて、適宜以下のコマンドを変更ください。

```
cd c:\TripoSR
```

![](/images/turtle-20240721-tripo-3dp/cmd_tripo_cd.png =350x)
*TripoSRフォルダ内へ移動*

4. **venv（Python仮想環境）を作成**
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

仮想環境を使うことで、Pythonのプロジェクト管理がより効率的かつ安全になります。venvが初めてという方は、今後、生成AIに限らず、開発や実行環境の構築などで利用してみてください。
:::
::::

5. **仮想環境アクティベート**
コマンドを入力し、仮想環境をアクティベート（有効化）します。
下図のように(.venv)が表示されたら、アクティベート成功です。

```
.\.venv\Scripts\activate
```

![](/images/turtle-20240721-tripo-3dp/cmd_tripo_active.png =350x)
*仮想環境アクティベート*

6. **ツールアップデート (仮想環境)**
コマンド入力し、仮想環境内のpip, wheel, setuptoolsのアップデートを行います。
エラー表示なく、次の画面のようにsuccessfullyが表示されたら成功です。

```
py.exe -m pip install --upgrade pip wheel setuptools
```

![](/images/turtle-20240721-tripo-3dp/cmd_update_success.png =600x)
*ツールアップデート成功*

7. **pytorchインストールコマンド取得**
pytorchと呼ばれる機械学習ライブラリをインストールします。
以下のPytorch.orgサイトにアクセスし、少し下にスクロールすると、環境の選択画面があります。
この選択画面で、自身の環境に合わせてポチポチ選択します。
すると「Run this Command」欄（赤線で囲った箇所）にコマンドが表示されますので、これをコピーしてください。
  
https://pytorch.org/get-started/locally/

![](/images/turtle-20240721-tripo-3dp/pytorch_select.png =600x)
*Pytorch 環境選択画面*

::::message
Tips
:::details Compute Platform（CUDAバージョン）が分からない場合（クリックで開く）
Compute Platformの項目で何を選択したらよいかわからない場合、次のコマンドを実行してください。
```
nvidia-smi
```
すると次のような表示がされますので、CUDA Version（赤線部分）を参照してください。
![](/images/turtle-20240721-tripo-3dp/nvidiasmi_cmd.png =550x)
*nvidia-smi コマンド実行画面*

なお、Pytorchの選択画面にバージョン「12.3」はありませんが、12.3が表示された場合は「12.1」を選択します。
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
※ご自身の環境に合わせて、適切なコマンドを選択してください。
なお、本記事執筆時点（2024年7月）においては、v2.3.1、v2.4.0で動作を確認しております。
:::
::::

8. **pytorchインストールコマンド実行 (仮想環境)**
手順7でコピーしたコマンドをコマンドプロンプトに貼り付けて実行します。
エラー表示なく、次の画面のようにsuccessfullyが表示されたら成功です。

![](/images/turtle-20240721-tripo-3dp/pytorch_success.png =550x)
*Pytorch コマンド実行画面*

9. **環境変数設定 (仮想環境)**
次のコマンドを実行して、環境変数を設定します。

```
set DISTUTILS_USE_SDK=1
```

10. **TripoSRのrequirements.txt書き換え**
TripoSRの環境構築に必要な依存モジュールを記した**requirements.txt**を書き換えます。
具体的には、この中の「torchmcubes」というモジュールが、最新バージョンだとcmakeコンパイルに失敗するため、以前のバージョンを指定します。
変更するファイルの場所は`<path>\TripoSR\requirements.txt`です。
※ requirements.txtは、TripoSRフォルダの直下にあります。


![](/images/turtle-20240721-tripo-3dp/req_before.png =550x)
*requirements.txt 変更前*

&emsp;&emsp;4行目を次の通り、書き換えます。

![](/images/turtle-20240721-tripo-3dp/req_after.png =550x)
*requirements.txt 変更後*

&emsp;&emsp;同じ内容のテキスト用意していますので、適宜ご使用ください。

```
git+https://github.com/tatsy/torchmcubes.git@cbb3c3795b1e168bf81e8dee28623eaf5c33cd1c
```

11.  **TripoSRが必要なライブラリをインストール (仮想環境)**
次のコマンドを実行して、手順10で一部書き換えたrequirements.txt（要求ファイル）に基づき、TripoSRが必要なライブラリをインストールします。

```
pip install -r requirements.txt
```

&emsp;&emsp;エラー表示なく、次の画面のようにsuccessfullyが表示されたら成功です。

![](/images/turtle-20240721-tripo-3dp/req_success.png =600x)
*requirements.txt installコマンド実行画面*

12. **TripoSRの起動確認 (仮想環境)**
コマンドを実行して、TripoSRアプリケーションを起動します。
次の画面のように、Running on local URLが表示されたら成功です。

```
python gradio_app.py
```

![](/images/turtle-20240721-tripo-3dp/app_success.png =550x)
*アプリケーション 起動成功*

13. **TripoSRのWeb UI画面を起動**
Webブラウザを開き、手順12の画面に表示された「Running on local URL」のアドレス「http://127.0.0.1:7860」をブラウザに入力します。次の画面がブラウザ上に表示されたら成功です。

![](/images/turtle-20240721-tripo-3dp/webui.png =550x)
*WebUI画面*

14. **起動用バッチファイルの作成**
次回からの起動を楽にするために、起動用のバッチファイルを作成します。次の内容を参考にファイルを作成したら、TripoSRのフォルダ直下（gradio_app.pyやrequirements.txtと同一階層）に保存します。このファイルのショートカットを作成して、デスクトップにでも置いておけば、以降ワンクリックで起動が可能になります👍
※ バッチファイル実行後、すぐにブラウザが起動しますが、TripoSRアプリが起動していないため「ページに到達できません」が表示されると思います。その場合は、TripoSRアプリが起動するの待ってから、ブラウザを再度読み込んでください。


```batch:tripo_run.bat（起動用バッチファイル）
@echo off
REM Move to TripoSR directory
cd /d %~dp0

REM Open URL in browser
start http://127.0.0.1:7860

REM Activate the virtual environment
call .venv\Scripts\activate

REM Run gradio_app.py
python gradio_app.py

REM Deactivate the virtual environment (if necessary)
deactivate

REM Prevent the command prompt from closing
pause
```

以上で、TripoSRの導入方法の解説は終了です。

### ●3D CADソフト

::::message
3D CADソフト環境構築
:::details AUTODESK Fusionインストール手順（クリックで開く）
OBJファイル→STLファイル変換にAUTODESK Fusionを利用する場合、次の手順でインストールしてください。

1. 次の公式サイトのページにアクセスします。

[![](/images/turtle-20240721-tripo-3dp/link_cad.png)](https://www.autodesk.com/jp/products/fusion-360/overview?term=1-YEAR&tab=subscription)

2. 「無償体験版をダウンロード」ボタンをクリックします。
3. 次のページが表示されたら「非商用（趣味利用版 機能限定 ）」を選択し「個人用Fusion360を入手」ボタンをクリックします。
4. 以降は手順に従ってインストールを進めます。途中、アカウント作成の作成が必要になりますので作成してください。
:::
::::

## 実行手順

作成の流れで示した図を再掲します。この図で示す順序に従って、画像生成AIで画像を作成する際のポイントや、TripoSRの具体的な使い方等を示したいと思います。

![](/images/turtle-20240721-tripo-3dp/ai_3d_flow.png)
*生成AIによる3Dプリントの流れ（再掲）*

### ●画像生成AI

まず、TripoSRにインプットするための画像を、画像生成AIで作成します。
ここでは手っ取り早く、画像を生成する方法と、生成する際のコツを示します。

#### 画像を生成する方法

画像生成AIは、普段使い慣れたものをご使用いただくのが一番ですが、無料でとりあえず画像を生成したい場合は「**Copilot**」がオススメです。無料といっても侮るなかれ。Copilotは、DALL-E3というChatGPTと同じ画像生成AIを用いているため、とてもきれいな画像を生成することができます！

使い方はとても簡単。Microsoft Edgeブラウザを開いて、検索欄の「Copilotを開く」アイコンをクリックします。

![](/images/turtle-20240721-tripo-3dp/cop_icon.png =600x)
*Copilotアイコン*

あとは、画像生成のためのプロンプト（指示文）を入力するだけで画像が生成されます。

#### TripoSRに特化した画像生成のコツ

通常、画像生成AIを利用するときは、とても凝ったプロンプトを考えます。しかし、TripoSR向けの画像を生成する場合は、それほど凝る必要はありません。ポイントは次の2点です。

- **シンプルな背景にする**
- **3D形状を把握しやすい画像を生成する**

TripoSRは、ノイズとなるものが多い複雑な背景は失敗しやすいため、シンプルな背景にします。また、平面的な画像から3Dデータを作成することも苦手ですから、できる限り3D形状を把握しやすい画像を生成することもポイントです。具体的に示します。

![](/images/turtle-20240721-tripo-3dp/boy_3d.jpg =300x)
*カートゥーン風男性 AI生成画像*

```text: プロンプト
1人のカートゥーン風男性のデフォルメされた3DCGイラストです。
背景はシンプルな白色背景です。
1人のカートゥーン風男性は、かっこいいポーズをしています。
1人のカートゥーン風男性の全身のCG画像です。
1人のカートゥーン風男性は、陰影がはっきりしており、3D形状がよくわかるCG画像です。
```

![](/images/turtle-20240721-tripo-3dp/cargo_3d.jpg =300x)
*タイヤ付きゴミ箱 AI生成画像*

```text: プロンプト
古びたゴミ箱の3DCGイラストです。
背景はシンプルな白色背景です。
ゴミ箱は、古びた感じがあり、錆びている部分もあります。
蓋とタイヤがあるシンプルなデザインのゴミ箱です。
陰影がはっきりしており、3D形状がよくわかるCG画像です。
```
どちらのプロンプトも、シンプルな背景と3D形状を把握しやすい画像を生成することを重視しています。これにより、生成された画像を使用することで、TripoSRは3Dデータをより正確に生成しやすくなり、成功率も高まります。シンプルな背景はノイズを減らし、3D形状の明確な表現はデータの精度を向上させるため、これらのポイントを押さえたプロンプトが効果的です。

### ●3Dモデル生成AI（TripoSR）

続いて、画像生成AIで作成した画像を元に、TripoSRで3Dデータを作成します。TripoSRの使い方と、実際にいくつかのパターンを試した際の成功事例と失敗事例を示したいと思います。

#### TripoSRの使い方

環境構築時に作成した起動用バッチファイル「tripo_run.bat」を実行して、TripoSRを起動します。起動後のアプリケーションの使い方は、gif動画で動きを交えながら示します。説明用のキャプションを画面下部に示していますので、あわせてご確認ください。シンプルですので、それほど使い方に戸惑うことはないと思います。

![](/images/turtle-20240721-tripo-3dp/tripo_use_gif.gif)
*TripoSR 使い方 gif動画*

#### 3Dデータ成功・失敗事例

色々試した中からいくつかピックアップして成功事例と失敗事例を示します。それぞれの結果については、寸評を述べたいと思います。

![](/images/turtle-20240721-tripo-3dp/tripo_result.jpg)
*TripoSR 成功・失敗事例*

- **男性キャラ**
  人型のキャラは、成功すると思っていませんでしたが、意外と成功します。AIが人間をイメージしやすいのかもしれません。
- **カーゴタイプゴミ箱**
  画像では見えてないタイヤの部分も3Dデータとして出力されており、出力結果にとても驚かされました！
- **ゴミ箱**
  単純な形状は、比較的成功率が高かったです。質感含めて品質高く出力されました。
- **カメ**
  奥行き方向の距離感が掴めていないようで、前後にギュッと縮めた感じになりました。個人的に成功してほしかったです・・。
- **植物**
  成功しそうな形状ですが、結果は失敗です。植物の位置関係など少しバランスが悪いことが影響しているかもしれません。
- **イチゴキューブ**
  透明のものや、複数のものが存在すると失敗するようです。

### ●3D CADソフト（Fusion）

FusionによるOBJファイル→STLファイルへの変換方法をgif動画で示します。Fusionは魅力的なソフトですから、本当はもっといろいろ解説したいところですが、今回は変換のみに使います。なお、Fusionは商用利用ではない個人利用の場合、一部機能は制限されますが、無料で利用することができます（機能制限されるといっても個人利用では全く問題ないレベルです）。

![](/images/turtle-20240721-tripo-3dp/fusion_use_gif.gif)
*Fusion 使い方 gif動画*

### ●スライサー＆プリンタ

あとは、いつも通り使い慣れたスライサーとプリンタを使って印刷を行うだけです👍

![](/images/turtle-20240721-tripo-3dp/slice_print.jpg)
*スライサー＆3Dプリント*

このように画像一枚から素敵な造形物たちが誕生しました！

![](/images/turtle-20240721-tripo-3dp/result.jpg)
*1枚の画像から作られた造形物たち*

以上で全ての説明は完了となります！
本当にお疲れさまでした🎉

## まとめ

画像1枚から3Dプリンタで造形物を作ることができました。
AIは、これまで文章や画像、プログラミングなどパソコンの中に閉じて扱うことが多かったですが、今回の内容で実際のモノづくりにも生かせそうだということが分かりました。今はまだ途上の技術ですが、これからが本当に楽しみです。この記事を読んだ方のAIライフ、3Dプリンタライフがさらに充実したものになればと思います。もし、分からないことや、分かりにくい部分がありましたら遠慮なくコメント欄に書き込んでください。🐢

今回も長い記事になりましたが、最後まで読んでくださりありがとうございました！

## リンク

私が書いた、GitHub CopilotというAIを利用したコーディングツールの記事です。
プログラミングに興味がある方は、ぜひこちらの記事も読んでみてください。
AIをうまく活用するとモノづくりの速度が劇的に改善します。

https://zenn.dev/safubuki/articles/turtle-20240223-gitcopilot