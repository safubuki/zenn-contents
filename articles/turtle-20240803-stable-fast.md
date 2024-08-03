---
title: "【Stable Fast 3D】驚きの進化！画像一枚から素早くキレイに3Dデータ生成"
emoji: "🐢"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [AI,LLM,3d,3dプリンタ]
published: false
---
技術の進化すごいです！ほんの数日前、私は次のような記事を書きました。

https://zenn.dev/safubuki/articles/turtle-20240721-tripo-3dp

一生懸命書き上げて「やり切ったなぁ～」と思っていたら、次の記事がリリースされました💦

https://ja.stability.ai/blog/introducing-stable-fast-3d

「Stable Fast 3D」は、私の記事の中で紹介した「TripoSR」と同じ、一枚の画像から3Dデータを生成するAIです。そして、Stable Fast 3Dは、TripoSRの後継バージョンになります。それでは、早速比較してみましょう。

![](/images/turtle-20240803-stable-fast/sr3d_vs_tripo.jpg)

進化すごくないですか？服やズボンの細かい表現、髪の毛の質感、豊かな表情。TripoSRでも十分驚いたのに、Stable Fast 3Dには、腰を抜かすくらい驚かされました。
この感動はぜひとも、記事にして皆さまにお伝えしなければと思い、作成しました。

この記事を読んで、Stable Fast 3Dの凄さを体感してください👍

#### ブログ対象者

本ブログ記事は、画像生成AIや画像一枚から3Dデータ生成に興味ある方を対象にしています。「Stable Fast 3D」は、Web上にデモ用の環境がありますから、特に環境構築せずともすぐに試すことができます（[Webデモアプリ リンク](https://huggingface.co/spaces/stabilityai/stable-fast-3d)）。また、この記事ではローカルな自身の環境へ「Stable Fast 3D」環境を構築する方法も解説します。こちらは少々PCのスキルが必要かと思いますが、できる限り分かりやすく説明します。

## 作成の流れ

まず、画像一枚から3Dデータを作成するまでの流れを示します。

![](/images/turtle-20240803-stable-fast/flow.png)
*3Dデータ作成の流れ*

3Dデータ作成以降は、生成したデータを利用して3Dプリントをしてもよいですし、Stable Fast 3Dはデータの見た目が大変綺麗ですからゲームやVR等で利用するのもよいと思います。

## 必要なもの

自身の環境を構築するために必要なソフトウェアとハードウェアをリストにしました。3Dプリントまで行いたい方は、スライサーソフトと3Dプリンタ準備ください。また、TripoSRを利用したことがある方、概ね必要な環境は同じなのですが、一部環境構築にあたって注意が必要な個所を赤字で示しております。詳細は環境構築の手順で説明します。

![](/images/turtle-20240803-stable-fast/needs.png)
*必要なものリスト*

**PCスペックの補足：**
元々2.5GB~3.0GB消費している状況で、データを生成すると下図のようにGPUメモリを消費しました。6~7GB程度を消費するようですから、うまくやりくりすれば、8GBのGPUメモリのGPUでも動作しそうです。12GBあると安心して動作させることができます。

![](/images/turtle-20240803-stable-fast/cpu.png =500x)
*使用時のGPUメモリ消費量*

## 環境構築

環境構築では「**Stable Fast 3D**」を中心に説明します。その他、環境を構築する上で必要なPythonやCUDA Toolkit等についても簡単に説明しますので、未導入の場合は必要な項目を参照し、環境を構築してください。なお、環境構築は上から順に実施してください。

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

### ●Visual Studio

::::message
Visual Studio 環境構築方法
:::details Visual Studio 2022 community インストール手順（クリックで開く）
1. **インストーラをダウンロード**
以下の公式サイトにアクセスして、インストーラをダウンロードします。

[![](/images/turtle-20240803-stable-fast/link_vs2022.png)](https://visualstudio.microsoft.com/ja/vs/community/)

![](/images/turtle-20240803-stable-fast/vs2022_down.png =550x)
*インストーラのダウンロード*

2. **Visual Studioのインストール**
インストーラを起動すると、次のような画面が表示されるので「**C++によるデスクトップ開発**」**にチェック**を入れてインストールボタンをクリックしてください。
※インストールの詳細は、デフォルトチェックのままでOKです。

![](/images/turtle-20240803-stable-fast/vs2022_inst.png =550x)
*Visual Studioインストーラ画面*
:::
::::

### ●CUDA Toolkit (v12.4)

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
※私の場合、GPUドライババージョン「560.70」にマッチする「CUDA Toolkit 12.4.1 (April 2024)」を選択しました。

[![](/images/turtle-20240721-tripo-3dp/link_cuda.png)](https://developer.nvidia.com/cuda-toolkit-archive)

※GPUの型番やGPUドライバのバージョンに応じて、適切なCUDAバージョンの選択方法について、次のページで解説されています。必要に応じて参照ください。なお、同ページ内の「Dockerイメージを用いたCUDA環境構築」については対象外とします。
[![](/images/turtle-20240721-tripo-3dp/link_cuda_ver.png)](https://zenn.dev/yumizz/articles/73d6c7d1085d2f)

3. **CUDA Toolkitのダウンロード②**
選択すると、次のような画面が表示されるので、自身の環境に応じて選択し、ダウンロードします。

![](/images/turtle-20240803-stable-fast/cuda_down.png =550x)
*インストーラのダウンロード*

4. **CUDA Toolkitのインストール**
インストーラを実行すると、次のような画面が表示されるので、使用許諾了承して、高速（推奨）選択し、CUDA Visual Studio Integrationの確認項目にチェックを入れて、次々進みます。

![](/images/turtle-20240803-stable-fast/cuda_inst.png =500x)
*CUDA Toolkitインストーラ画面 オプション選択（一部抜粋）*

5. **CUDA Toolkitのインストール確認**
次のコマンドで、CUDA Toolkitインストールができていることを確認します。バージョンなどが表示されたら成功です(手順1と同等の表示)。

```
nvcc --version
```

:::
::::

### ●Stable Fast 3D

Stable Fast 3Dについて、導入方法を詳細に解説します。

1. **Hugging Faceでアクセストークンを作成**
次のサイトで、アクセストークンを作成します。

https://huggingface.co/settings/tokens
　　Create new tokenボタンを選択し、トークン作成します。

![](/images/turtle-20240803-stable-fast/token_create.png =300x)
*トークン作成ボタン*

2. **トークンのパーミッションを設定**
次の画像のようにトークン名入力し、パーミッションを選択して、ページ下部にあるCreate tokenボタンを押します。

![](/images/turtle-20240803-stable-fast/token_select.png =600x)
*トークン作成画面*

3. **作成されたトークンを保存**
トークンを作成すると次のような画面が表示されるので、トークン文字列をコピーして、テキストなどに保存します（他人には見せない）。このトークン文字列は後ほど使います。

![](/images/turtle-20240803-stable-fast/token_result.png =400x)
*トークン保存画面*

4. **モデルへのアクセスを承認する**
次のサイトで、モデルへのアクセス承認を行います。名前、メールアドレスなど必要事項を入力して、Agree and access repositoryボタンを押します。

https://huggingface.co/stabilityai/stable-fast-3d

![](/images/turtle-20240803-stable-fast/grante_model.png =550x)
*モデルへのアクセス承認*

5. **Stable Fast 3DのソースをGitHubから取得**
まず、次のサイトにアクセスします。

https://github.com/Stability-AI/stable-fast-3d
　　Codeボタンを選択し、Download ZIPで任意の場所に保存後、展開します。

![](/images/turtle-20240803-stable-fast/git_sf3d.png =600x)
*Stable Fast 3D GitHub*

:::details Gitを扱える方の場合（クリックで開く）
Gitを扱える方は、zipでダウンロードせずに、cloneコマンドでクローンしても良いです。
```
git clone https://github.com/Stability-AI/stable-fast-3d.git
```
:::

6. **Windows PowerShell起動**
検索窓に「windowspowershell」と入力し、PowerShellを起動します。

![](/images/turtle-20240721-tripo-3dp/power_shell.png =250x)

7. **Stable Fast 3Dのフォルダ内に移動**
PowerShellで、Stable Fast 3Dのフォルダに移動します。
CドライブにStable Fast 3Dのフォルダを保存、展開した場合は、次のコマンドを入力します。
※ご自身の環境に合わせて、適宜以下のコマンドを変更してください。

```
cd c:\stable-fast-3d
```

![](/images/turtle-20240803-stable-fast/ps_dir.png =350x)
*Stable Fast 3Dフォルダ内へ移動*

8. **venv（Python仮想環境）を作成**
コマンドを入力し、Stable Fast 3Dフォルダ内にvenv（Python仮想環境）を作成します。

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

9. **仮想環境アクティベート**
コマンドを入力し、仮想環境をアクティベート（有効化）します。

```
.\.venv\Scripts\activate
```
&emsp;&emsp;下図のように(.venv)が表示されたら、アクティベート成功です。

![](/images/turtle-20240803-stable-fast/ps_venv.png =350x)
*仮想環境アクティベート*

10. **ツールアップデート (仮想環境)**
コマンド入力し、仮想環境内のpip, wheel, setuptoolsのアップデートを行います。

```
py.exe -m pip install --upgrade pip wheel setuptools
```

&emsp;&emsp;エラー表示なく、successfullyが表示されたら成功です。

11. **pytorchインストールコマンド取得**
pytorchと呼ばれる機械学習ライブラリをインストールします。
以下のPytorch.orgサイトにアクセスし、少し下にスクロールすると、環境の選択画面があります。この選択画面で、自身の環境に合わせてポチポチ選択します。すると「Run this Command」欄（赤線で囲った箇所）にコマンドが表示されますので、これをコピーしてください。
  
https://pytorch.org/get-started/locally/

![](/images/turtle-20240803-stable-fast/torch.png =600x)
*Pytorch 環境選択画面*

:::message
Stable Fast 3Dでは、CUDA12.4の環境を準備して、上記選択画面でも12.4を選択してください。
:::

12. **pytorchインストールコマンド実行 (仮想環境)**
手順11でコピーしたコマンドをPowerShellに貼り付けて実行します。
エラー表示なく、successfullyが表示されたら成功です。

13. **環境変数設定 (仮想環境)**
次のコマンドを実行して、環境変数を設定します。

```
set DISTUTILS_USE_SDK=1
```

14. **Stable Fast 3Dが必要なライブラリをインストール (仮想環境)**
次のコマンドを実行して、Stable Fast 3Dが必要なライブラリをインストールします。エラー表示なく、successfullyが表示されたら成功です。

```
pip install -r requirements.txt
```

15. **Gradio demo(WebUI画面)が必要なライブラリをインストール (仮想環境)**
次のコマンドを実行して、Gradio demo(WebUI画面)が必要なライブラリをインストールします。エラー表示なく、successfullyが表示されたら成功です。

```
pip install -r requirements-demo.txt
```

16. **Hugging Face CLIをインストール**
次のコマンドを実行して、Hugging Face CLIをインストールします。

```
pip install -U "huggingface_hub[cli]"
```

17.  **アクセストークンを使ってHugging Faceにログイン① (仮想環境)**
次のコマンドを実行して、Pythonの対話モードにします。

```
python
```
&emsp;&emsp;対話モードで次の内容を入力します。
```
from huggingface_hub import login
login()
```

18. **アクセストークンを使ってHugging Faceにログイン② (仮想環境)**
次のような画面が表示されるので、Enter your token（入力非表示）に手順3でテキストに保存したトークンを貼り付け、Add token as git credential?で「Y」を入力する。内容に問題が無ければ、Login successfulが表示される。
そして、Ctrl + zでpythonの対話モードから抜けます。

![](/images/turtle-20240803-stable-fast/hug_login.png)
*Hugging Faceログイン*


19.  **Stable Fast 3Dの起動確認 (仮想環境)**
コマンドを実行して、Stable Fast 3Dアプリケーションを起動します。Running on local URLが表示されたら成功です。
※ PythonをUTF-8モードで動作するように環境変数を設定してから実行しないとエラーが出るため次の次のコマンドを実行します。

```
$env:PYTHONUTF8 = "1"; python gradio_app.py
```

20.  **Stable Fast 3DのWeb UI画面を起動**
Webブラウザを開き、手順12の画面に表示された「Running on local URL」のアドレス「*http://127.0.0.1:7860*」をブラウザに入力します。次の画面がブラウザ上に表示されたら成功です。

![](/images/turtle-20240803-stable-fast/webui.png =650x)
*WebUI画面*

21.  **起動用バッチファイルの作成**
次回からの起動を楽にするために、起動用のバッチファイルを作成します。以下の内容を参考にファイルを作成し、Stable Fast 3Dのフォルダ直下（`gradio_app.py`や`requirements.txt`と同じ階層）に保存してください。このファイルのショートカットを作成してデスクトップに置けば、ワンクリックで起動が可能になります👍
**注意**： バッチファイル実行後、すぐにブラウザが起動しますが、Stable Fast 3Dアプリがまだ起動していないため「ページに到達できません」と表示されることがあります。その場合は、Stable Fast 3Dアプリが起動するのを待ってから、ブラウザを再度読み込んでください。


```batch:sf3d_run.bat（起動用バッチファイル）
@echo off
REM Move to Stable Fast 3D directory
cd /d %~dp0

REM Open URL in browser
start http://127.0.0.1:7860

REM Activate the virtual environment
call .venv\Scripts\activate

REM Set the PYTHONUTF8 environment variable and run gradio_app.py
set PYTHONUTF8=1
python gradio_app.py

REM Deactivate the virtual environment (if necessary)
deactivate

REM Prevent the command prompt from closing
pause
```

お疲れさまでした！
これで、全ての環境構築の説明が終わりました。
引き続き、環境構築時に発生したトラブルの対処方法を示したいと思います。

## トラブル対処法

この章ではトラブルの対処方法を示します。
次に示すエラーは、いずれも`gradio_app.py`というUIを起動するプログラムを実行すると、依存するモジュールで発生します。もし、同様のエラーが発生したら以下の内容を参考にしてみてください。
::::message alert
トークン未設定・モデル利用未承認時に発生するエラー
:::details raise GatedRepoError（クリックで開く）
**[現象]**

- GatedRepoError例外が発生。
- config.yamlのあるレポジトリにアクセスできないというメッセージ。

```
File "C:\stable-fast-3d\.venv\lib\site-packages\huggingface_hub\utils\_errors.py", line 321, in hf_raise_for_status   
    raise GatedRepoError(message, response) from e
huggingface_hub.utils._errors.GatedRepoError: 401 Client Error. (Request ID: Root=1-66ada95b-5ac3648d7296503c4c9a0661;4caa2940-663f-468d-9e13-37cca9407329)

Cannot access gated repo for url https://huggingface.co/stabilityai/stable-fast-3d/resolve/main/config.yaml.
Access to model stabilityai/stable-fast-3d is restricted. You must be authenticated to access it.
```

**[原因]**

- Hugging Faceのトークンを作成していない・作成に失敗した。
- モデル利用の承認を行っていない。
- Hugging Faceにトークンを利用してログインしていない。

**[対処方法]**

- 環境構築の手順1～手順4を見直し、トークン作成・設定及び、モデル利用承認を行う。
- 環境構築の手順16～手順18を見直し、Hugging Faceにログインする。
:::
::::
::::message alert
Build Tools for Visual Studio 2022を利用時に発生するエラー
:::details raise ValueError cl.exe not found
**[現象]**

- ValueError例外が発生。
- cl.exeのインストールパスが見つからないというメッセージ。

```
File "C:\git_home\stable-fast-3d\.venv\lib\site-packages\slangtorch\slangtorch.py", line 74, in find_cl
    raise ValueError(f"cl.exe not found in default Visual Studio installation path.\n"
ValueError: cl.exe not found in default Visual Studio installation path.
```

**[原因]**

- Build Tools for Visual Studio 2022だと、cl.exeあり、環境変数など設定してもcl.exeのインストールパスを見つけられないため。エラー発生の`slangtorch.py`に追加で、エラーログ仕込み、確かにpath取得できていないことを確認。
※ コードの記述がやや環境に依存した書き方のように見受けられたが、詳細は未確認。

```
vswhere_path: C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe
vs_install_path:
cl_path: []
```

**[対処方法]**

- Build Tools for Visual Studio 2022 をアンインストールする。
- Visual Studio 2022 communityをインストールする。

:::
::::
::::message alert
CUDA Toolkitのバージョンが最新のVisual Studio非対応により発生するエラー
:::details RuntimeError unsupported Microsoft Visual Studio version!
**[現象]**

- RuntimeError例外が発生。
- CUDA ToolkitがMicrosoft Visual Studio のバージョン未サポートのメッセージ。

```
File "C:\git_home\stable-fast-3d\.venv\lib\site-packages\torch\utils\cpp_extension.py", line 2121, in _run_ninja_build
    raise RuntimeError(message) from e
RuntimeError: Error building extension '_slangtorch_texture_baker_44136fa355b3678a': [1/2] C:\Program Files\NVIDIA GPU Computing
(省略)
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.3\include\crt/host_config.h(164): fatal error C1189: #error:  -- unsupported Microsoft Visual Studio version! Only the versions between 2017 and 2022 (inclusive) are supported! The nvcc flag '-allow-unsupported-compiler' can be used to override this version check; however, using an unsupported host compiler may cause compilation failure or incorrect run time execution. Use at your own risk.
```

**[原因]**

- CUDA v12.3が最新のVisual Studioに対応していないため。

**[対処方法]**

- CUDA toolkit v12.3をアンインストールする。
- Nvidia ドライバーを更新する。
- CUDA toolkit v12.4 Update 1をインストールする。
:::
::::

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

私が書いた、GitHub CopilotというAIを利用したコーディングツールの記事もあります。プログラミングに興味がある方は、ぜひこちらの記事も読んでみてください。AIをうまく活用すると、モノづくりの速度が劇的に改善します。

https://zenn.dev/safubuki/articles/turtle-20240223-gitcopilot