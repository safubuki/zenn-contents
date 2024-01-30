---
title: "【Stable Diffusion】WebUI拡張機能開発！作り方から公式Indexリスト登録まで"
emoji: "🐢"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [StableDiffusion,AI]
published: false
---
画像生成AIは、掛け算の組み合わせ（例えば、猫×犬や花×鳥など）から、想像もできないようなものを生み出し、とても驚かされます。そして、画像生成AIには、DALL-E3、Midjourney、StableDiffusionなど様々なツールがあります。その中でも今回は扱うStableDiffusion(WebUI)は、オンラインではなく、自身のPCの中に環境を作ることができます。さらに、有志が作成した拡張機能を自由に組み合わせて、自分好みにカスタマイズすることができます。

私は拡張機能を便利に利用していますが、**自分でも拡張機能を作ってみたい**と思うようになり、2024年正月、実際に作ってみることにチャレンジしました！

また、WebUIには、Indexリストという一覧から目的の拡張機能を探して、簡単にインストールできる便利な機能があります。私は、作成したものを個人の中にとどめるのではなく、他の人とも共有できたらいいなと思いました。そこで、**WebUIのIndexリストに拡張機能を登録する**こともやってみました。

これら私が行ってきたことを、この記事で紹介したいと思います。「私もこんな機能を作ってみたいな」「これくらいなら自分にもできそう」と思ってもらえたら嬉しいです😊

#### ブログ対象者

- **自分好みの拡張機能を作ってみたい人**
  
ただし、作成にあたって次のスキルが必要になります。
- **Stable Diffusion WebUIの拡張機能を扱える**
- **Pythonでプログラムを作成できる**
- **GitHubを扱える**

自分には少し難しそうかも・・・と思われる方がいるかもしれませんが、便利な学習サイトがいろいろあります。末尾にリンクを載せますので、拡張機能をテーマに学習するのもイイと思います👍

#### 得られる効果

- **Stable Diffusion WebUI拡張機能を作れるようになります。**
次のようなものになります。入力に基づいて簡単な計算をして、出力欄に出力するだけのシンプルな機能になります。機能の詳細については以下のリンクにアクセスしてみてください（日本語READMEもあります）。

https://github.com/safubuki/sd-webui-latent-regional-helper

![lr_helper](/images/turtle-20240128-stable-ext/lr_helper.png =500x)
*図1：Latent Regional Helper（著者作成の拡張機能）*


- **WebUI拡張機能Indexリストに登録して、自分の拡張機能を広く公開できるようになります。**
GitHubのURLを直接張り付ける方法の他に、このようなリストを参照してインストールする方法もあります。少なからず、WebUIを使っている人の目に触れると思います。

![index_list](/images/turtle-20240128-stable-ext/index_list.png =500x)
*図2：拡張機能 Indexリスト*

## 開発環境の準備

まず開発を行うための準備を行います。
拡張機能の環境は、次のようなフォルダ構成で作成していきます。

![ext_env](/images/turtle-20240128-stable-ext/ext_env.png =600x)
*図3：拡張機能 環境構成*

もし、すでにいくつか拡張機能をインストールされている方は、extensionsフォルダにアクセスすると、これまでに入れたもの見ることができます。

それでは手順を解説します。

### 手順

1. 自身のGitHubページでレポジトリを作成します。
   - レポジトリ名は、**自身の拡張機能の名前**を設定してください。
   ※後から変更可能ですので、とりあえずの名前でもOKです。
   - 公開を前提としていますから、公開設定は**Public**を選択します。
   - Add a README fileには、**チェックを入れて**ください。

   ![git_repos](/images/turtle-20240128-stable-ext/git_repos.png =500x)

2. 作成したGitHubレポジトリのアドレスをコピーします。
3. StableDiffusion WebUIを開き、Extensionsタブ→Install from URLタブに移動します。
4. 先ほどコピーしたアドレスを赤枠の欄に張り付けて、Installします。
   
   ![stable](/images/turtle-20240128-stable-ext/stable.png =400x)

5. 図3で示したextensionsフォルダの下に、自分の拡張機能のフォルダ(＝GitHubレポジトリ名)ができていることを確認します。
※フォルダにはまだREADME.mdしかありません。
6. 自分の拡張機能のフォルダの中に移動し、**scriptsフォルダを作成**します。
7. scriptsフォルダの中に移動し、**開発用のpyファイルを作成**します。
※ ファイル名は、main.pyやext_func.pyなど何でも構いません。
8. 以下のGitHubに拡張機能のテンプレート（雛形）があります。
アクセスして、READMEを確認してください。なお、ファイルはそれぞれ次の内容になっています。
   - **template.py**：txt2imgやimg2imgタブの中に機能を作ります。
   - **template_on_settings.py**：Settingsタブに設定を作ります。
   - **template_on_tab.py**：txt2img等と同じようにタブに機能を作ります。

https://github.com/udon-universe/stable-diffusion-webui-extension-templates

9. 今回は説明は「タブ上に拡張機能を作る」内容で進めますので**template_on_tab.py**の内容をコピーして、手順7で作成した開発用のpyファイルにペーストします。

https://github.com/udon-universe/stable-diffusion-webui-extension-templates/blob/main/scripts/template_on_tab.py

以上で、環境は整いました。

## 拡張機能の実装方法

機能の実装を進める前に、拡張機能のUIについて説明します。
今までの説明の中で、拡張機能の画面のいくつかお見せしてきましたが、こう思いませんでしたか？「もっと華やかにしてみたいな」「ボタンの形、表現を変えみようかな」と。私はちょっと思いました。しかし、これは残念ながらできません。

理由は、**Gradio**というフレームワークを使っているからです。
このGradioは、Webアプリケーションを簡単に作ることができるPythonのライブラリです。関数と入出力の形式を指定するだけで、インタラクティブ（双方向）なUIを作成できる大変優れものです。ただ、それゆえに表現できるUIはある程度固定されます。

Gradioでどのようなことができるかは、公式サイトのインタフェースを確認すると分かります。

https://www.gradio.app/docs/interface

その他、Gradioでどのようなことをができるのかを把握するには、皆さんが使い慣れている拡張機能を参考にするのも一つの手です。既にいくつかをインストールしているなら、extensionsフォルダにありますので、参考にしてみてください。
ただし、高機能な拡張機能は中身の実装を紐解くのが大変ですから、シンプルな機能のものを参照すると良いと思います。

**それでは、実装の仕方を解説します。**
解説は、私が作成した拡張機能の画面およびコードを参考に解説していきます。

![lr_helper_all](/images/turtle-20240128-stable-ext/lr_helper_all.png)
*図1：Latent Regional Helper 全体（著者作成の拡張機能）*

[ソースコードへのリンク（latent_regional_helper.py)](https://github.com/safubuki/sd-webui-latent-regional-helper/blob/main/scripts/latent_regional_helper.py)

### インポート
まず、必要なモジュールをインポートします。

```Python:latent_regional_helper.py
from typing import List, Tuple
import gradio as gr
from modules import script_callbacks
```
それぞれのモジュールについて説明します。
- **typing**
Pythonの型ヒントのために使用します。拡張機能に直接関係はありません。
- **gradio**
Gradioを利用するために必要です。
- **modules.script_callbacks**
StableDiffusion WebUI(AUTOMATIC1111)が提供するインタフェースです。
ここでは、uiを新しいタブに追加するために利用しています。
extensionsフォルダと同階層のmodulesフォルダにコードあります。
解説ページなどは無い(と思います)ので、コードから紐解く必要あります。

### UI画面
以下の関数が、UI表示を行っている箇所になります。
```Python:latent_regional_helper.py
def on_ui_tabs() -> List[Tuple[gr.Blocks, str, str]]:
```
#### レイアウト
on_ui_tabsの中を見ていくと`Blocks` `Row` `Column`が目に付くと思います。
それぞれについて説明します。
- **Blocks**
  gradio のインターフェイスを利用するために必要な要素です。まずこれで全体を囲います。
- **Row**
  子要素を水平方向に並べます。
- **Column**
  子要素を垂直方向に並べます。

コードから`Blocks` `Row` `Column`の部分だけを抜き出すと次のようになります。
```Python
with gr.Blocks():
    with gr.Row():
        with gr.Column():
            # ラジオボタン
            # ドロップダウンリスト × 5
            with gr.Row():
                # テキストボックス
                # テキストボックス
                # チェックボックス
            # コマンドボタン
            # テキストボックス
            with gr.Row():
                # テキストボックス
                # テキストボックス
        with gr.Column():
            pass
```
- `Blocks`で全体を囲み、その後`Row`を使用して、2つの`Column`を水平方向に並べます。
- 左側の`Column`では、垂直方向に要素を並べますが、途中で`Row`が出現します。
  このとき、`Column`の中で、`Row`によりテキストボックスやチェックボックスを水平方向に並べます。
- 以降、垂直方向に並べつつ、`Row`が出現すると水平方向に並べます。
- 右側の`Column`には、何も記述が無いため表示をしません。

これを図で示すと次のようになります。

![layout](/images/turtle-20240128-stable-ext/layout.png =650x)
*図1：Latent Regional Helper 全体（著者作成の拡張機能）*

慣れるまでは少し大変かもしれませんが、慣れてくるとテキストボックスやボタンなどを目的の場所に配置できるようになります。

#### コンポーネント

コンポーネントは、`Textbox`や`Button`などのUI画面を構成する要素です。
それぞれのコンポーネントの詳細な使い方は、割愛させていただければと思います。
私のコードやGradioのページ、各種拡張機能の中身を見ることによって理解が進むと思います。
なお、利用する上で押さえておくべきポイントを以下に記します。
- コンポーネントを生成したときのインスタンスはキーイベント等で利用しますので、変数に保存してください。例えば、次の`textbox_back_weight`に保存しています。
  ```Python:latent_regional_helper.py
   textbox_back_weight: gr.Textbox = gr.Textbox(
      label='Background Weight (Latent Only)',
      interactive=True,
      value=str(default_back_weight))
  ```
- 各種コンポーネント生成時の引数で使われる代表的なものは次の通りです。
  - **label**：
  　テキストボックスやボタンなどの名前表示に使います。
  - **value**：
  　デフォルトであらかじめ表示、利用する値を設定します。
  - **interactive**：
  　`TextBox`などTrueの時編集可能です。Falseは編集できません。
- タイトルや項目名などちょっとした文字表示は`HTML`を使用します。

### ロジック処理

個々のロジック処理について詳細な説明はしませんが、計算などを行う個所は別の関数やファイルなどを設けて、処理をするのが良いかと思います。
私のコードでは、以下の関数が、キーイベントからの受け口となってロジック処理部が実行されています。
```Python:latent_regional_helper.py
def division_output(radio_sel: str, col_num_1: str, col_num_2: str, col_num_3: str, col_num_4: str,
                    col_num_5: str, div_weight: str, back_weight: str,
                    chkbox_back: bool) -> Tuple[str, str, str]:
```

### キーイベント

キーイベントは、以下の`Button`コンポーネント生成時`button_execute`に保存したインスタンスを利用します。
```Python:latent_regional_helper.py
# Run button
button_execute: gr.Button = gr.Button(value='execute', variant='primary')
```
キーが押された時のイベント処理は次の箇所になります。
```Python:latent_regional_helper.py
button_execute.click(
    # Function to be executed when button_execute is clicked
    fn=division_output,
    # Arguments for the division_output function
    # NOTE: column_num_row_list cannot be passed as a list.
    #       It needs to be passed as a gradio block object.
    inputs=[
        radio_sel, dropdown_col_num_list[0], dropdown_col_num_list[1],
        dropdown_col_num_list[2], dropdown_col_num_list[3], dropdown_col_num_list[4],
        textbox_div_weight, textbox_back_weight, chkbox_back
    ],
    # Return values of the division_output function
    outputs=[textbox_division, textbox_position, textbox_weight])
```
キーイベント(click)実行時に指定するパラメータについて説明します。
- **fn**
　クリック時に実行される関数名を設定します。
　ここでは、ロジック処理部の`division_output`を指定しています。
- **inputs**
  fnで設定した関数に渡す引数を指定します。
  各コンポーネント生成時に保存した変数を必要に応じて設定します。
- **output**
  fnで設定した関数からの戻り値を格納する先を設定します。
  各コンポーネント生成時に保存した変数を必要に応じて設定します。

### つまずいたポイント・TIPS

:::message
ここから書き始める！
:::

:::message
インスタンスなどの言葉が分かりにくくないか！確認。別にインスタンスのままでもいいけど。
:::

#### gradioのブロック型をリストに詰めてエラー発生

#### SD拡張UIのテキストボックスにValue値設定しても反映されない

#### install.pyは、インストールするライブラリが無ければ、全く用意しなくてよい


## Indexリスト登録方法

ブログの内容（大きく項目を分ける）

## 参考サイト

udon

公式

公式のextention手順

## まとめ

内容を振り返る
今後に向けての紹介する

:::message
拡張機能について簡単に紹介する？
:::

## リンク

Pythonの学習に最適です。入門から段階的に学べます。
今回の私のプログラムであれば、基礎編＋応用の関数とかwith文で理解できるかと思います。
https://www.python-izm.com/

私もGitの基本はこのサイトで学びました。
https://backlog.com/ja/git-tutorial/
