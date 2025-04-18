---
title: "【TripoSR】驚きの技術！画像一枚から3Dプリンタでリアルな造形物を簡単作成"
emoji: "🐢"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [AI,LLM,3d,3dプリンタ]
published: true
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

必要なソフトウェアとハードウェアをリストにしました。使用するソフトウェアが多く感じるかもしれませんが、環境構築や実行手順についても詳しく説明しますので、ご安心ください。

![](/images/turtle-20240721-tripo-3dp/needs_list.png)
*必要なものリスト*

**PCスペックの補足：**
TripoSRを使用する際、下図のようにGPUメモリを消費します。8GBのGPUメモリではエラーが発生することがあるため、12GB以上のGPUメモリを搭載したGPUを選ぶと安心です。

![](/images/turtle-20240721-tripo-3dp/gpu_memory.png =550x)
*使用時のGPUメモリ消費量*

## 環境構築

環境構築では「**TripoSR**」を中心に説明します。その他、TripoSRの環境を構築する上で必要なPythonやCUDA Toolkit等についても簡単に説明しますので、未導入の場合は必要な項目を参照し、環境を構築してください。なお、環境構築は上から順に実施してください。

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
次のコマンドで、CUDA Toolkitインストールができていることを確認します。バージョンなどが表示されたら成功です(手順1と同等の表示)。

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
※ご自身の環境に合わせて、適宜以下のコマンドを変更してください。

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

```
.\.venv\Scripts\activate
```
&emsp;&emsp;下図のように(.venv)が表示されたら、アクティベート成功です。

![](/images/turtle-20240721-tripo-3dp/cmd_tripo_active.png =350x)
*仮想環境アクティベート*

::::message alert
仮想環境をアクティベートする際に実行権限エラーが発生したら
:::details システムではスクリプトの実行が無効メッセージ（クリックで開く）
`.\.venv\Scripts\activate`を実行した際に「**このシステムではスクリプトの実行が無効になっているため**」のようなメッセージが出力された場合、スクリプトの実行ポリシーを変更する必要があります。次の手順を行ってください。

&emsp;　

1. **スクリプトの実行ポリシーを変更するコマンドを実行**

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

&emsp;　

2. **再度、仮想環境のアクティベートを実行**

```
.\.venv\Scripts\activate
```

&emsp;　
**※手順１ 設定の意味（参考）：**

- **実行ポリシーの種類**
  - **RemoteSigned**:ローカルで作成されたスクリプト（例えば、今回のvenvアクティベートスクリプトなど）は実行を許可するが、インターネットからダウンロードされたスクリプトは信頼された発行元によって署名されている必要がある。
- **実行ポリシーのスコープ**
  - **CurrentUser**：現在のユーザーにのみ適用される実行ポリシー。システム全体の設定には影響を与えません。

:::
::::

6. **ツールアップデート (仮想環境)**
コマンド入力し、仮想環境内のpip, wheel, setuptoolsのアップデートを行います。

```
py.exe -m pip install --upgrade pip wheel setuptools
```

&emsp;&emsp;エラー表示なく、次の画面のようにsuccessfullyが表示されたら成功です。

![](/images/turtle-20240721-tripo-3dp/cmd_update_success.png =600x)
*ツールアップデート成功*

7. **pytorchインストールコマンド取得**
pytorchと呼ばれる機械学習ライブラリをインストールします。
以下のPytorch.orgサイトにアクセスし、少し下にスクロールすると、環境の選択画面があります。この選択画面で、自身の環境に合わせてポチポチ選択します。すると「Run this Command」欄（赤線で囲った箇所）にコマンドが表示されますので、これをコピーしてください。
  
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
次のような表示がされますので、CUDA Version（赤線部分）を参照してください。
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
なお、本記事執筆時点（2024年7月）においては、v2.3.1、v2.4.0で動作を確認しています。
:::
::::

8. **pytorchインストールコマンド実行 (仮想環境)**
手順7でコピーしたコマンドをPowerShellに貼り付けて実行します。
エラー表示なく、次の画面のようにsuccessfullyが表示されたら成功です。

![](/images/turtle-20240721-tripo-3dp/pytorch_success.png =550x)
*Pytorch コマンド実行画面*

9. **TripoSRのrequirements.txt書き換え**
TripoSRの環境構築に必要な依存モジュールを記した**requirements.txt**を書き換えます。
「torchmcubes」というモジュールが、最新バージョンだとcmakeコンパイルに失敗するため、以前のバージョンを指定します。
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

10.   **TripoSRが必要なライブラリをインストール (仮想環境)**
次のコマンドを実行して、手順9で一部書き換えたrequirements.txt（要求ファイル）に基づき、TripoSRが必要なライブラリをインストールします。

```
pip install -r requirements.txt
```

&emsp;&emsp;エラー表示なく、次の画面のようにsuccessfullyが表示されたら成功です。

![](/images/turtle-20240721-tripo-3dp/req_success.png =600x)
*requirements.txt installコマンド実行画面*

::::message
エラー時の対処法
:::details ライブラリをインストール中にエラーが出た場合（クリックで開く）
もしライブラリのインストール中にエラーが発生し、中断してしまった場合は、**x64 Native Tools Command Promptを利用して**、再度以下のコマンドを実行してください。

![](/images/turtle-20240721-tripo-3dp/native_cmd.png =550x)
*x64 Native Tools Command Prompt*

**再度実行するコマンド**
```
.\.venv\Scripts\activate
```
```
set DISTUTILS_USE_SDK=1
```
```
pip install -r requirements.txt
```
※venv環境の構築、pip,wheel,setuptoolsのアップグレード、Pytorchのインストールは済んでいるため、再度実行は不要です。
:::
::::

11. **TripoSRの起動確認 (仮想環境)**
コマンドを実行して、TripoSRアプリケーションを起動します。

```
python gradio_app.py
```

&emsp;&emsp;次の画面のように、Running on local URLが表示されたら成功です。

![](/images/turtle-20240721-tripo-3dp/app_success.png =550x)
*アプリケーション 起動成功*

12. **TripoSRのWeb UI画面を起動**
Webブラウザを開き、手順11の画面に表示された「Running on local URL」のアドレス「*http://127.0.0.1:7860*」をブラウザに入力します。次の画面がブラウザ上に表示されたら成功です。

![](/images/turtle-20240721-tripo-3dp/webui.png =550x)
*WebUI画面*

13. **起動用バッチファイルの作成**
次回からの起動を楽にするために、起動用のバッチファイルを作成します。以下の内容を参考にファイルを作成し、TripoSRのフォルダ直下（`gradio_app.py`や`requirements.txt`と同じ階層）に保存してください。このファイルのショートカットを作成してデスクトップに置けば、ワンクリックで起動が可能になります👍
**注意**： バッチファイル実行後、すぐにブラウザが起動しますが、TripoSRアプリがまだ起動していないため「ページに到達できません」と表示されることがあります。その場合は、TripoSRアプリが起動するのを待ってから、ブラウザを再度読み込んでください。


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

お疲れさまでした！
これで、全ての環境構築の説明が終わりました。
引き続き、実行手順を参照して、実際の動作方法を理解してください。

## 実行手順

作成の流れをつかみやすくするために、ブログの最初で示した図を再掲します。この図の順序に従って、画像生成AIで画像を作成する際のポイントや、TripoSRの具体的な使い方などを説明します。

![](/images/turtle-20240721-tripo-3dp/ai_3d_flow.png)
*生成AIによる3Dプリントの流れ（再掲）*

### ●画像生成AI

まず、TripoSRにインプットするための画像を、画像生成AIで作成します。ここでは、手軽に画像を生成する方法と、その際のコツを紹介します。

#### 手軽に画像を生成する方法

画像生成AIは、普段使い慣れたものを使用するのが一番ですが、無料で画像を生成したい場合は「**Copilot**」がオススメです。無料とはいえ、侮るなかれ。Copilotは、DALL-E3というChatGPTと同じ画像生成AIを使用しているため、とてもきれいな画像を生成できます！

使い方はとても簡単です。Microsoft Edgeブラウザを開き、検索欄の「Copilotを開く」アイコンをクリックします。

![](/images/turtle-20240721-tripo-3dp/cop_icon.png =600x)
*Copilotアイコン*

あとは、画像生成のためのプロンプト（指示文）を入力するだけで画像が生成されます。

#### TripoSR向けの画像生成のコツ

通常、画像生成AIを利用するときは、非常に凝ったプロンプトを考えます。しかし、TripoSR向けの画像を生成する場合は、それほど凝る必要はありません。ポイントは次の2点です。

- **シンプルな背景にする**
- **3D形状を把握しやすい画像を生成する**

TripoSRは、ノイズとなるものが多い複雑な背景では失敗しやすいため、シンプルな背景にします。また、平面的な画像から3Dデータを作成することも苦手ですから、できる限り3D形状を把握しやすい画像を生成することがポイントです。具体的に示します。

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

画像生成AIで作成した画像を元に、TripoSRで3Dデータを作成します。ここでは、TripoSRの使い方と、いくつかのパターンを試した際の成功事例と失敗事例を紹介します。

#### TripoSRの使い方

環境構築時に作成した起動用バッチファイル「tripo_run.bat」を実行して、TripoSRを起動します。起動後のアプリケーションの使い方は、以下のgif動画で動きを交えながら説明します。キャプションも画面下部に表示していますので、あわせてご確認ください。シンプルな操作なので、使い方に戸惑うことはないと思います。

![](/images/turtle-20240721-tripo-3dp/tripo_use_gif.gif)
*TripoSR 使い方 gif動画*

#### 3Dデータ成功・失敗事例

いくつか試した中から、成功事例と失敗事例をピックアップして紹介します。それぞれの結果について寸評を述べます。

![](/images/turtle-20240721-tripo-3dp/tripo_result.jpg)
*TripoSR 成功・失敗事例*

##### 成功事例

- **男性キャラ**
  人型のキャラは成功しにくいと思っていましたが、意外と成功します。AIが人間をイメージしやすいのかもしれません。
- **カーゴタイプゴミ箱**
  画像では見えていないタイヤの部分も3Dデータとして出力されており、結果にとても驚きました！
- **ゴミ箱**
  単純な形状は比較的成功率が高く、質感も含めて高品質に出力されました。

##### 失敗事例

- **カメ**
  奥行き方向の距離感が掴めていないようで、前後にギュッと縮んだ感じになりました。個人的に成功してほしかったです…。
- **植物**
  成功しそうな形状ですが、結果は失敗です。植物の位置関係など、少しバランスが悪いことが影響しているかもしれません。
- **イチゴキューブ**
  透明なものや複数のものが存在すると失敗するようです。

### ●3D CADソフト（Fusion）

FusionによるOBJファイルからSTLファイルへの変換方法をgif動画で示します。Fusionは非常に魅力的なソフトですが、今回は変換のみに使用します。なお、Fusionは商用利用ではない個人利用の場合、一部機能が制限されますが、無料で利用できます（個人利用では全く問題ないレベルです）。

![](/images/turtle-20240721-tripo-3dp/fusion_use_gif.gif)
*Fusion 使い方 gif動画*

### ●スライサー＆プリンタ

あとは、いつも通り使い慣れたスライサーとプリンタを使って印刷を行うだけです👍

![](/images/turtle-20240721-tripo-3dp/slice_print.jpg)
*スライサー＆3Dプリント*

このように、画像一枚から素敵な造形物たちが誕生しました！

![](/images/turtle-20240721-tripo-3dp/result.jpg)
*1枚の画像から作られた造形物たち*

以上で全ての説明は完了となります！
本当にお疲れさまでした🎉

## まとめ

画像1枚から3Dプリンタで造形物を作ることができました。AIはこれまで文章や画像、プログラミングなどパソコンの中で扱うことが多かったですが、今回の内容で実際のモノづくりにも生かせることが分かりました。今はまだ途上の技術ですが、これからが本当に楽しみです。

この記事を読んだ方のAIライフ、3Dプリンタライフがさらに充実したものになればと思います。もし、分からないことや、ちょっとした疑問などありましたら、遠慮なくコメント欄に書き込んでください。🐢

今回も長い記事になりましたが、最後まで読んでくださりありがとうございました！

## リンク

私が書いたAI関連ツールの記事のリンクを紹介します。興味があればぜひご覧ください。

私が書いた、GitHub CopilotというAIを利用したコーディングツールの記事もあります。プログラミングに興味がある方は、ぜひこちらの記事も読んでみてください。AIをうまく活用すると、モノづくりの速度が劇的に改善します。

https://zenn.dev/safubuki/articles/turtle-20240223-gitcopilot

Tripo 2.0というAIで3Dモデルを生成する技術に関する記事です。TripoSR後継モデルで、精度が劇的に向上しています。モノづくり、動画、VRなど幅広い分野に応用できる可能性があります。現在は未実装ですが、3Dワールドの生成やヒューマノイドモデルを自在に動かして動画を作成する機能もリリース予定とのことで、今後の展開が非常に楽しみです。

https://zenn.dev/safubuki/articles/turtle-20240929-tripo2-evo

Googleの動画生成AI「Veo2」は、Geminiなど、私たちが普段利用しているGoogleのプラットフォームから手軽に試せます。基本的な操作はシンプルですが、いくつかのコツを押さえることで、より魅力的な動画を作成できます。この記事では、Geminiの強力なカスタマイズ機能「Gem」を活用した動画生成テクニックなど、実践的な内容を解説しています。
https://zenn.dev/safubuki/articles/turtle-20250417-veo2

画像1枚から動画を生成するAIツール『Kling AI』の使い方やコツを紹介します。さらに、CM風の動画を作成することで、実際のシーンでの活用例も示しました。うまく融合させれば、モノづくりとプロモーションが画像1枚から可能になります♪

https://zenn.dev/safubuki/articles/turtle-20240916-klingai

## 更新履歴

更新履歴は折りたたみ表示にしています。
確認したい場合は、以下のバーをクリック（タップ）してください。

:::details 更新履歴（最終更新日：2025/04/17）
**更新履歴**

- **2025/4/17**
  Veo2のブログへのリンクを追加しました。

- **2024/08/04**
  AI関連のStable Fast 3Dの記事を追加し、説明文を追加しました。

- **2024/08/05**
  手順11にエラー時の対処法を追加しました。
  不要な手順を削除しました。

- **2024/08/06**
  リンクのブログ紹介文を微修正しました。

- **2024/08/07**
  Python仮想環境アクティベート時のエラー対処方法を追加しました。

- **2024/09/17**
  AI関連の動作生成AIツール『Kling AI』の記事をリンクに追加しました。

- **2024/09/30**
  Tripo 2.0リンク及び、説明文を追加しました。
:::
