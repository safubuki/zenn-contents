---
title: "【Stable Fast 3D】驚きの進化！画像一枚から素早くキレイに3Dデータ生成"
emoji: "🐢"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [AI,LLM,3d,3dプリンタ]
published: true
---
技術の進化は凄いです！数日前、私は次のような記事を書きました。

https://zenn.dev/safubuki/articles/turtle-20240721-tripo-3dp

一生懸命書き上げて「やり切ったなぁ～」と思っていたのも束の間、次の記事がリリースされました💦

https://ja.stability.ai/blog/introducing-stable-fast-3d

「Stable Fast 3D」は、私の記事で紹介した「TripoSR」と同様に、一枚の画像から3Dデータを生成するAIです。そして、Stable Fast 3DはTripoSRの後継バージョンでもあります。それでは、早速比較してみましょう。

![](/images/turtle-20240803-stable-fast/sr3d_vs_tripo.jpg)

進化がすごいと思いませんか？服やズボンの細かい表現、髪の毛の質感、豊かな表情。TripoSRでも十分驚きましたが、Stable Fast 3Dにはさらに驚かされました。この感動をぜひとも皆さまにお伝えしたく、記事を作成しました。

この記事を読んで、Stable Fast 3Dの凄さを体感してください👍

#### ブログ対象者

本ブログ記事は、画像生成AIや画像一枚から3Dデータ生成に興味のある方を対象にしています。「Stable Fast 3D」は、オンライン上にデモ用の環境があり、特に環境構築をせずともすぐに試すことができます。また、この記事ではローカル環境に「Stable Fast 3D」を構築する方法も詳しく紹介します。こちらは少々PCのスキルが必要ですが、できる限り分かりやすく説明します。

**オンラインデモアプリ（お試し）**
使い方は「実行手順」の章をご確認ください。速度はローカル環境で実行するよりも僅かに遅いですが、体験する分には十分です。

https://huggingface.co/spaces/stabilityai/stable-fast-3d

## 作成の流れ

まず、画像一枚から3Dデータを作成するまでの流れを示します。

![](/images/turtle-20240803-stable-fast/flow.png)
*3Dデータ作成の流れ*

3Dデータ作成後は、生成したデータを利用して3Dプリントをすることもできます。また、Stable Fast 3Dはデータの見た目が非常に美しいため、ゲームやVRなどで利用するのも良いでしょう。

## 必要なもの

自身の環境を構築するために必要なソフトウェアとハードウェアをリストにしました。3Dプリントまで行いたい方は、スライサーソフトと3Dプリンタを準備してください。また、TripoSRを利用したことがある方は、概ね必要な環境は同じですが、一部環境構築にあたって注意が必要な個所を赤字で示しております。詳細は環境構築の手順で説明します。

![](/images/turtle-20240803-stable-fast/needs.png)
*必要なものリスト*

**PCスペックの補足：**
元々2.5GB～3.0GB消費している状況で、データを生成すると下図のようにGPUメモリを消費しました。6～7GB程度を消費するようですから、うまくやりくりすれば、8GBのGPUメモリでも動作しそうです。12GBあると安心して動作させることができます。

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
※ Hugging Faceへのログインが必要です。アカウントをお持ちでない方は、Sign Upしてアカウントを作成してください。

https://huggingface.co/settings/tokens
　　Create new tokenボタンを選択し、トークン作成します。

![](/images/turtle-20240803-stable-fast/token_create.png =300x)
*トークン作成ボタン*

2. **トークンのパーミッションを設定**
次の画像のようにトークン名入力し、パーミッションを選択して、ページ下部にあるCreate tokenボタンを押します。

![](/images/turtle-20240803-stable-fast/token_select.png =600x)
*トークン作成画面*

3. **作成されたトークンを保存**
トークンを作成すると次のような画面が表示されるので、トークン文字列をコピーして、テキストなどに保存します（他人には見せないようにしてください）。このトークン文字列は後ほど使います。

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

13. **Stable Fast 3Dが必要なライブラリをインストール (仮想環境)**
次のコマンドを実行して、Stable Fast 3Dが必要なライブラリをインストールします。エラー表示なく、successfullyが表示されたら成功です。

```
pip install -r requirements.txt
```

14. **Gradio demo(WebUI画面)が必要なライブラリをインストール (仮想環境)**
次のコマンドを実行して、Gradio demo(WebUI画面)が必要なライブラリをインストールします。エラー表示なく、successfullyが表示されたら成功です。

```
pip install -r requirements-demo.txt
```

15. **Hugging Face CLIをインストール**
次のコマンドを実行して、Hugging Face CLIをインストールします。

```
pip install -U "huggingface_hub[cli]"
```

16.  **アクセストークンを使ってHugging Faceにログイン① (仮想環境)**
次のコマンドを実行して、Pythonの対話モードにします。

```
python
```
&emsp;&emsp;対話モードで次の内容を入力します。
```
from huggingface_hub import login
login()
```

17. **アクセストークンを使ってHugging Faceにログイン② (仮想環境)**
次のような画面が表示されるので、Enter your token（入力非表示）に手順3でテキストに保存したトークンを貼り付け、Add token as git credential?で「Y」を入力します。内容に問題が無ければ、Login successfulが表示されます。Ctrl + zでPythonの対話モードから抜けます。

![](/images/turtle-20240803-stable-fast/hug_login.png)
*Hugging Faceログイン*


18.  **Stable Fast 3Dの起動確認 (仮想環境)**
コマンドを実行して、Stable Fast 3Dアプリケーションを起動します。Running on local URLが表示されたら成功です。
※ PythonをUTF-8モードで動作するように環境変数を設定してから実行しないとエラーが出るため、次のコマンドを実行します。

```
$env:PYTHONUTF8 = "1"; python gradio_app.py
```

19.  **Stable Fast 3DのWeb UI画面を起動**
Webブラウザを開き、手順18の画面に表示された「Running on local URL」のアドレス「*http://127.0.0.1:7860*」をブラウザに入力します。次の画面がブラウザ上に表示されたら成功です。

![](/images/turtle-20240803-stable-fast/webui.png =650x)
*WebUI画面*

20.  **起動用バッチファイルの作成**
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

この章では、トラブルの対処方法を示します。 次に示すエラーは、いずれも`gradio_app.py`というUIを起動するプログラムを実行するときに依存するモジュールで発生します。もし同様のエラーが発生した場合は、以下の内容を参考にしてください。

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

- Hugging Faceのトークンを作成していない、または作成に失敗した。
- モデル利用の承認を行っていない。
- Hugging Faceにトークンを利用してログインしていない。

**[対処方法]**

- 環境構築の手順1～手順4を見直し、トークン作成・設定およびモデル利用承認を行う。
- 環境構築の手順15～手順17を見直し、Hugging Faceにログインする。
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

- Build Tools for Visual Studio 2022では、cl.exeが存在し、環境変数の設定を正しく行っていても、インストールパスを見つけることができない。
- エラー発生箇所のslangtorch.pyに追加でエラーログを仕込み、パスが取得できていないことを確認。
※ コードの記述がやや環境に依存している可能性がありますが、詳細は未確認。

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

- CUDA v12.3(古いバージョン)が最新のVisual Studioに対応していないため。

**[対処方法]**

- CUDA toolkitの古いバージョン（この場合はv12.3）をアンインストールする。
- Nvidia ドライバーを更新する。
- CUDA toolkit v12.4 Update 1をインストールする。
:::
::::

## 実行手順

作成の流れをつかみやすくするために、ブログの最初で示した図を再掲します。この図の順序に従って、画像生成AIで画像を作成や、Stable Fast 3Dの具体的な使い方を説明します。

![](/images/turtle-20240803-stable-fast/flow.png)
*3Dデータ作成の流れ（再掲）*

### ●画像生成AI

まず、Stable Fast 3Dにインプットするための画像を、画像生成AIで作成します。ここでは、手軽に画像を生成する方法をご紹介します。

#### 手軽に画像を生成する方法

画像生成AIは、普段使い慣れたものを使用するのが一番ですが、無料で画像を生成したい場合は「**Copilot**」がオススメです。Copilotは、DALL-E3というChatGPTと同じ画像生成AIを使用しているため、とてもきれいな画像を生成できます！

Microsoft Edgeブラウザの検索欄で「Copilotを開く」アイコンをクリックし、画像生成のためのプロンプト（指示文）を入力するだけで画像を生成することができます。

![](/images/turtle-20240721-tripo-3dp/cop_icon.png =600x)
*Copilotアイコン*

### ●3Dモデル生成AI（Stable Fast 3D）

画像生成AIで作成した画像を元に、Stable Fast 3Dでデータを作成します。ここでは、Stable Fast 3Dの使い方を紹介します。

#### Stable Fast 3Dの使い方

Stable Fast 3Dの使い方を説明します。シンプルな操作なので、きっとすぐに慣れると思います。

1. **Stable Fast 3Dを起動**
環境構築時に作成した起動用バッチファイル「sf3d_run.bat」を実行して、Stable Fast 3Dを起動します。なお、起動後の画面のTipsには次のような内容が記載されています。
**Tipsに記載の内容**
・画像にすでにアルファチャンネル（透明度情報）が含まれている場合、背景除去のステップをスキップできます。
・背景除去時の前景比率を調整して前景オブジェクトのサイズを制御できます。これにより形状に影響を与えることができます。
・メッシュトポロジー（3Dモデルの表面構造定義）を制御するためにリメッシュオプションを選択できます。薄い表面ではメッシュにアーティファクト（データの誤りやノイズ）が発生する可能性があるため、その場合はオフにする必要があります。
・独自のHDR環境マップをアップロードして3Dモデルの照明条件を調整できます。

![](/images/turtle-20240803-stable-fast/sf3d_1.png)
*起動後の画面*

2. **2D画像用意・背景除去**
2D画像を開き「Remove Background」ボタンを押して背景を除去します。Foreground Ratioを調整することで、前景オブジェクトのサイズを制御し、結果に影響を与えることができます。

![](/images/turtle-20240803-stable-fast/sf3d_2.png)
*2D画像用意・背景削除操作画面*

3. **3Dデータ作成**
背景除去後「Run」ボタンを押して3Dデータを作成します。

![](/images/turtle-20240803-stable-fast/sf3d_3.png)
*データ作成操作画面*

4. **データ作成完了・ダウンロード**
データ作成が完了したら、画面右の赤枠で示したボタンを押してデータをダウンロードできます。

![](/images/turtle-20240803-stable-fast/sf3d_4.png)
*データ作成完了・ダウンロード操作画面*

5. **仕上がりの確認・照明効果変更**
仕上がりは自由な角度から確認できます。きれいな仕上がりをぜひご確認ください✨また、サンプルや自作のHDR環境マップを適用することで照明条件を変更することもできます。

![](/images/turtle-20240803-stable-fast/sf3d_result.gif)

#### Stable Fast 3DとTripoSRの比較

同じ2D画像をインプットとして、Stable Fast 3DとTripoSRそれぞれから3Dデータを出力して比較しました。興味深い結果が得られましたので、紹介したいと思います。

図中では、Stable Fast 3Dを「SF3D」、TripoSRを「Tripo」と省略して表現しています。また、TripoSRは必ず左右反転した3Dデータが出力されるため、比較画像も左右反転した形で示しています。

![](/images/turtle-20240803-stable-fast/comp_1.png)
*Stable Fast 3D・TripoSR 比較①*

- **男性キャラ**
  どちらの3D形状も申し分ありませんが、新しいStable Fast 3Dの方が細部の表現が豊かで、より綺麗です。
- **カーゴタイプゴミ箱**
  質感はStable Fast 3Dの方が優れていますが、3D形状の正確性に関しては、2D画像で見えない部分も含めてTripoSRの方が上だと感じました。Stable Fast 3Dでは中央に大きな穴が開いています。
- **ゴミ箱**
  単純な形状はどちらも正確に出力できました。
- **えんぴつ立て**
  見た目はStable Fast 3Dが鮮やかで、えんぴつ立ての表情も正確に表現しています。一方、TripoSRは暗めですが、鉛筆一本一本の3D形状を正確に出力しようとしています。

![](/images/turtle-20240803-stable-fast/comp_2.png)
*Stable Fast 3D・TripoSR 比較②*

- **カメ**
  元の2D画像の構図や角度の影響で、どちらも奥行きのサイズ感がイマイチです。また、脚のつき方も斜めになっています。これは元画像を工夫する必要がありそうです。
- **リアルカメ**
  リアルなものに関しては、細かい表現も含めてStable Fast 3Dの方が優れています。足が一本消えているのは、背景除去の際に消えてしまったためです。
- **植物**
  正方形の形状はStable Fast 3Dの方が正確ですが、植物の形状は別の角度から見ると省略されているのか潰れています。一方、TripoSRは植物の葉一つ一つを3Dデータにしようとしています。
- **イチゴキューブ**
  どちらも失敗ですが、Stable Fast 3Dのイチゴは鮮やかで美味しそうです。一方、TripoSRは見えない部分も含めて3D化しようとしているのが伝わってきます。

Stable Fast 3Dが新しいからと言って、全ての面で優れているわけではなく、ケースによってはTripoSRを利用したほうが良い場合もあると感じました。私はメインでStable Fast 3Dを利用しつつ、出力結果に満足できなければ、TripoSRをサブ的に使おうと思います。

### ●スライサー＆プリンタ

出力した3Dデータを3Dプリンタで印刷したい場合、いつも通り使い慣れたスライサーとプリンタを使って印刷を行うだけです👍 よく利用されているcuraというスライサーソフトであれば、GLBファイルを読み込むことが可能です。ソフトを起動したら、GLBファイルをドラッグ＆ドロップしてください。

![](/images/turtle-20240721-tripo-3dp/slice_print.jpg)
*スライサー＆3Dプリント*

:::message
スライサーソフトでGLBファイルを読み込むと、Z軸の位置が非常に高い位置になっていることがあります。その場合は、Z軸の位置を「0」に設定してください。
:::

以上で全ての説明は完了となります！
本当にお疲れさまでした🎉

## まとめ

少しでも早く記事をお届けするため、私のTripoSRの記事を流用しつつ、Stable Fast 3Dに関する部分についてはしっかり書き起こしました。それにしても、TripoSRがリリースされてから約5か月でこの進化は本当にすごいです！私は、3Dプリンタに何か活かせないかと思って始めましたが、また別のことにチャレンジしてみるのも面白そうだと思いました。

この記事を読んだ方も、ぜひ様々な取り組みに活用してみてください。もし分からないことや、ちょっとした疑問などがありましたら、遠慮なくコメント欄に書き込んでください。🐢

最後まで読んでくださり、ありがとうございました！

## リンク

私が書いたAI関連ツールの記事のリンクを紹介します。興味があればぜひご覧ください。

私が書いた、GitHub CopilotというAIを利用したコーディングツールの記事もあります。プログラミングに興味がある方は、ぜひこちらの記事も読んでみてください。AIをうまく活用すると、モノづくりの速度が劇的に改善します。

https://zenn.dev/safubuki/articles/turtle-20240223-gitcopilot

Tripo 2.0というAIで3Dモデルを生成する技術に関する記事です。下のリンクのTripoSR後継モデルで、精度が劇的に向上しています。モノづくり、動画、VRなど幅広い分野に応用できる可能性があります。現在は未実装ですが、3Dワールドの生成やヒューマノイドモデルを自在に動かして動画を作成する機能もリリース予定とのことで、今後の展開が非常に楽しみです。

https://zenn.dev/safubuki/articles/turtle-20240929-tripo2-evo

Tripo2.0やStable Fast 3Dのベース技術であるTripoSRの記事です。TripoSRは少し古い技術になってしまいましたが、画像生成のコツや成功・失敗事例なども記載しています。参考になる部分もまだあると思いますので、読んでみてください。

https://zenn.dev/safubuki/articles/turtle-20240721-tripo-3dp

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

- **2024/08/05**
  オンラインデモアプリへのリンクを分かりやすくしました。
  環境構築の不要な手順を削除しました。
  Stable Fast 3Dの使い方の誤記と分かりにくい表現を修正しました。

- **2024/08/06**
  Stable Fast 3DとTripoSRの比較を追加しました。

- **2024/08/07**
  Python仮想環境アクティベート時のエラー対処方法を追加しました。

- **2024/09/17**
  AI関連の動作生成AIツール『Kling AI』の記事をリンクに追加しました。

- **2024/09/30**
  Tripo 2.0リンク及び、説明文を追加しました。
:::