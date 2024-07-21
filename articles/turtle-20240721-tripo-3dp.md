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

#### 作成の流れ

はじめに、画像一枚から3Dプリンタでリアルな造形物を作成するまでの流れを示します。

![](/images/turtle-20240721-tripo-3dp/ai_3d_flow.png)
*生成AIによる3Dプリントの流れ*

図で示すように、OSS(オープンソースソフトウェア)のAIや非商用利用無償のツールを複数組み合わせることで、費用をかけずに作成することを目指します。

#### ブログ対象者

本ブログ記事は、画像生成AIや3Dプリンタに関して、ある程度の前提知識があることを想定しています。その上で「TripoSR」については、環境設定から利用方法まで、具体的な例を交えながら丁寧に解説いたします。これにより、一連の流れを把握して、AIを活用したモノづくりを目指します。

## 事前準備

### 必要なもの

以下に、必要なものを一覧で示します。

- **画像生成AI**
普段使っている画像生成AIをご使用ください。インターネット上には、TripoSRが精度高く3Dモデルデータを生成するための画像データが少ないため、画像生成AIで目的の画像を生成します。代表的なものは次の通りです。
  - ChatGPT Plus（有料・オンライン）
  - Copilot（無料・オンライン）
  ChatGPTとCopilotは、DALL-E3という同じ画像生成AIを使用しています。ChatGPTでは細かな設定も可能ですが、まずはCopilotで試してみると良いでしょう。
  - Stable Diffusion（無料・ローカル）
  クラウド上に環境構築もできますが、ローカルに環境構築したほうが扱いやすいです。
- **3Dモデル生成AI**
「TripoSR」を使用します。
- **3D CADソフト**
「AUTODESK Fusion」を使用します。手動で3Dモデルを利用する際にも便利なCADソフトです。今回はTripoSRが生成するOBJファイルを、STLファイルに変換するために使用します。
※上記の変換ができるのであれば、他の使い慣れたツールをご使用ください。
- **スライサソフト**
普段使っているスライサソフトをご使用ください。私は、3Dプリンタに付属していた「cura」というツールを利用しています。
- **3Dプリンタ**
私はELEGOOの「Neptune 3 pro」という機種を使用しています。
- **Windows版 Python**
Python上で動作しますので、ご準備ください。
- **Windows PC**
TripoSRを使用するために、後述の動作環境程度のPCを準備してください。

### PC必要スペック

以下に、私が問題なくTripoSRを使用できている、作業用PCの動作環境を示します。
このPCと同等かそれ以上のPCをご準備ください。

- OS：Windows 11
- CPU：AMD Ryzen 5 5500
- メモリ：16GB
- GPU：GeForce RTX3060
- GPUメモリ：12GB

補足：
TripoSR使用時、下図のようにGPUメモリを消費します。8GBのGPUメモリですと、エラーになるという報告もありますので、GPUメモリを12GB以上搭載しているGPUを選定すると安心です。
※この手のGPUメモリ不足は、何らかの回避策がある可能性ありますが、本ブログでは扱いません。ご了承ください。

![](/images/turtle-20240721-tripo-3dp/gpu_memory.png =550x)
*使用時のGPUメモリ消費量*

### 環境構築

ここでは肝となる「**TripoSR**」のみを詳細に解説させていただき、その他については、簡易的な説明か、最低限必要なURLを提示させていただきます。環境構築方法は、リンク先の手順に従っていただくか、インターネットを検索いただくと、分かりやすいブログ記事がヒットすると思います。

#### ● Windows版 Python（必須）

TripoSR利用にあたって、Pythonがインストールされていることが大前提となりますので、まだの方はまずインストールしてください。以下のサイトの「Pythonを導入する」の章が参考になります。

https://www.useful-python.com/env-python-vscode-windows/

#### ★ TripoSR（必須）

1. **TripoSRのソースを次のGitHubから取得**

https://github.com/VAST-AI-Research/TripoSR

2. **Codeボタンを選択、Download ZIPで任意の場所に保存後、展開**

![](/images/turtle-20240721-tripo-3dp/tripo_git.png =600x)

:::details Gitを扱える方の場合（任意）
Gitを扱える方は、zipでダウンロードせずに、cloneコマンドでクローンしていただいてもかまいません。
```
git clone https://github.com/VAST-AI-Research/TripoSR.git
```
:::

3. **コマンドプロンプトでTripoSRのフォルダ内に移動**

![](/images/turtle-20240721-tripo-3dp/cmd_tripo_cd.png =500x)

4. **次のコマンドを入力して、venv（Python仮想環境）を作成。**

```
py.exe -m venv .venv
```

5. **Python仮想環境作成完了後、次のコマンドで仮想環境アクティベート（有効化）**

```
.\.venv\Scripts\activate
```

![](/images/turtle-20240721-tripo-3dp/cmd_tripo_active.png =500x)
*(.venv)が表示されていたらOK*

★★★ ここから ★★★
手順5の説明文から考える。


6.

#### ● Copilot（任意）

画像生成にCopilotを使用する場合、Microsoft Edgeブラウザを開いて、検索欄の次のアイコンをクリックするだけで使用できます。

![](/images/turtle-20240721-tripo-3dp/cop_icon.png =250x)
*Copilotアイコン*

#### ● AUTODESK Fusion（任意）

OBJファイル→STLファイル変換にFusionを利用する場合、以下の公式サイトのページを開きます。「無償体験版をダウンロード」選択し、非商用を選択した後、手順に従って進めます。アカウント作成まだの方は必要になります。

https://www.autodesk.com/jp/products/fusion-360/overview?term=1-YEAR&tab=subscription








