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
8. 以下のGitHubに便利な拡張機能のテンプレート（雛形）が公開されています。
こちらにアクセスして`scripts`フォルダを参照ください。ファイルはそれぞれ次の内容になっています。
   - **template.py**：txt2imgやimg2imgタブの中に拡張機能を作ります。
   - **template_on_settings.py**：Settingsタブに設定を作ります。
   - **template_on_tab.py**：txt2img等と同じようにタブ上に拡張機能を作ります。

https://github.com/udon-universe/stable-diffusion-webui-extension-templates

9. 今回は説明は「タブ上に拡張機能を作る」内容で進めますので**template_on_tab.py**の内容をコピーして、手順7で作成した開発用のpyファイルにペーストします。

https://github.com/udon-universe/stable-diffusion-webui-extension-templates/blob/main/scripts/template_on_tab.py

10. 拡張機能のテンプレート（雛形）から以下のファイルを自身の環境にコピー

以上で、実装をするための環境は整いました🎉

## 拡張機能の実装方法

機能の実装を進める前に、拡張機能のUIについて説明します。
今までの説明の中で、拡張機能の画面のいくつかお見せしてきましたが、こう思いませんでしたか？「もっと華やかにしてみたいな」「ボタンの形、表現を変えみようかな」と。私はちょっと思いました。しかし、これはできないようです。

理由は、**Gradio**というフレームワークを使っているからです。
このGradioは、Webアプリケーションを簡単に作ることができるPythonのライブラリです。関数と入出力の形式を指定するだけで、インタラクティブ（双方向）なUIを作成できる大変優れものです。ただ、それゆえに表現できるUIはある程度固定されます。

Gradioでどのようなことができるかは、公式サイトのインタフェースを確認すると分かります。

https://www.gradio.app/docs/interface

その他、Gradioでどのようなことをができるのかを把握するには、皆さんが使い慣れている拡張機能を参考にするのも一つの手です。既にいくつかをインストールしているなら、extensionsフォルダにありますので、参考にしてみてください。
ただし、高機能な拡張機能は中身の実装を紐解くのが大変ですから、シンプルな機能のものを参照すると良いと思います。

**それでは、実装の仕方を解説します。**
解説は、私が作成した拡張機能の画面およびコードで解説していきます。

- **画面**
![lr_helper_all](/images/turtle-20240128-stable-ext/lr_helper_all.png)
*図1：Latent Regional Helper 全体（著者作成の拡張機能）*

- **ソースコード**
:::message
以下のリンク先のコードを元に説明しますので、ご確認お願いします。
:::
**[safubuki/sd-webui-latent-regional-helper/blob/main/scripts/latent_regional_helper.py](https://github.com/safubuki/sd-webui-latent-regional-helper/blob/main/scripts/latent_regional_helper.py)**


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
解説ページなどは無い(と思います)ので、コードから紐解く必要があります。

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

コンポーネントとは、`Textbox`や`Button`などのUI画面を構成する要素です。
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

::::message alert
つまづきポイント！
:::details テキストボックスにValue値を設定してもUI上で値が反映されない（クリックで表示）
- 現象
コード上でvalueを都度変更しても、UI表示に値が反映されない。
- 原因
デフォルト値を設定すると、stable-diffusion-webui/ui-config.jsonに値が反映される。以降、WebUIはui-config.jsonの値を参照して、デフォルト値をテキストボックスなどに反映するため、コード側のvalueを変更してもWebUIには反映されない。

![uiconfig](/images/turtle-20240128-stable-ext/uiconfig.png =500x)
*ui-config.json*

- 解決
  1. コードのデフォルト値を自身が希望する値に変更する。
  2. ui-config.jsonから自身が開発している開発の設定を削除する。
  3. WebUIを再起動する。
:::
::::

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

::::message alert
つまづきポイント！
:::details リスト形式でinputsに引数として渡すとエラーが発生した（クリックで表示）
- 現象
ドロップダウンリストの値をリストに設定してinputsに設定すると、AttributeErrorが発生した。

![listerror](/images/turtle-20240128-stable-ext/listerror.png =500x)
*エラー発生時の実装*

- 原因
inputsにはgradioのブロック型の値を渡す必要があるが、リスト型で渡したためエラーが発生した。

- 解決
  1. リスト形式ではなく、一つ一つgradioのブロック型の値を引数として渡す
:::
::::

このようにしてキーが押された時の振る舞い決めています。

以上で拡張機能の実装方法の説明は終了です。
いかがでしたか？拡張機能の作成イメージはつかめましたでしょうか？
準備で作成した開発用のpyファイルに自身でコードを書いて、動きを確かめてみてください。

## 周辺ファイル

ここでは、拡張機能のメイン処理以外に必要な以下の3つのファイルを解説します。
自身の拡張機能フォルダの直下に次のファイルを用意してください。
書き方は

### LICENSE
開発した拡張機能のOSSライセンス形態、内容を記載します。
自身の拡張機能をOSSとして公開する予定が無ければ不要ですが、公開するのであればあった方が良いです。

https://github.com/safubuki/sd-webui-latent-regional-helper/blob/main/LICENSE

特にこだわりが無ければMITライセンスで良いと思いますが、OSSのライセンス形態各種ありますので、以下のページなどを参考にしてみてください。

https://manumaruscript.com/oss-licences-comparison/

### README.md
拡張機能の使い方を記載します。
こちらを記載してGitHubにプッシュすると、自身のGitHubレポジトリのトップページにREADME.mdの内容が自動的に表示されます。こちらはMarkdown記法を用いて作成します。Markdown記法については、以下のページを参照してみてください。

https://qiita.com/tbpgr/items/989c6badefff69377da7

また、Markdownの記述はVSCodeを使って編集すると、作成イメージを確認しながら作成できて便利です。

![readme](/images/turtle-20240128-stable-ext/readme.png =600x)
*readmeの作成*

この作成イメージは、VSCode右上の虫眼鏡のマークがついたプレビューボタンを押すことで表示できます。

![preview](/images/turtle-20240128-stable-ext/preview.png =300x)
*プレビューボタン*

### install.py
拡張機能を動作させる際に必要なモジュールを記載します。
もし、Python標準のモジュールだけで動作する拡張機能であれば、install.pyは不要です。しかし`pip`を使用して何らかモジュールをインストールしなければ動作しない拡張機能を作成する場合、install.pyのL5-L6にあるコメントを外して、必要な記述を行う必要があります。こうすることで拡張機能を起動するとき、自動で必要なモジュールがインストールされます。

https://github.com/udon-universe/stable-diffusion-webui-extension-templates/blob/main/install.py

- L5:既にモジュールがインストールされていないか確認します。
- L6:動作に必要なモジュールがインストールされます。

::::message
ワンポイント！
:::details install.pyが不要な場合、中身のコメントアウトではなく、ファイルを削除しよう！（クリックで表示）
Python標準のモジュールだけで動作する拡張機能の場合、install.pyは不要です。
ここで「コメントアウトしているから、ファイルは残しておいてもいいか」と思われるかもしれません。しかし、このファイルはコメントアウトして処理が無かったとしても、残しておくだけで拡張機能の起動時間に影響を与えます。

![start_prof](/images/turtle-20240128-stable-ext/start_prof.png =400x)

起動時間は、WebUI画面下部の`Startup profile`をクリックすると確認できます。
  
- **install.pyあり**（中身はコメントアウトして処理なし）
  ![install_ari](/images/turtle-20240128-stable-ext/install_ari.png =500x)

- **install.pyなし**
  ![install_nashi](/images/turtle-20240128-stable-ext/install_nashi.png =500x)

ありの場合、58ミリ秒かかっていることが分かります。最大で100ミリ秒の時もありました。非常に小さい値に感じるかもしれませんが、これが積み重なると意外と侮れない時間になります。

実は私も最初はコメントアウトして残していましたが、StableDiffusion WebUI 拡張機能のPull Request時にレビューでアドバイスを受けて気づきました。

**install.pyは不要ならファイルごと削除でOKです！**
:::
::::

大変長い道のりでしたが、お疲れさまでした！
以上で実装の解説は終わりになります。
ここまでの内容を読めば、私と同じように小さな拡張機能は作れるのではないでしょうか。

「ここが分かりにくい」などありましたら、補足説明や解説を追加しますので、遠慮なくコメントいただければと思います。

次の章では、WebUIのIndexリストへの登録方法を解説します。
あともう少しですので、最後までお付き合いください。

## Indexリスト登録方法

ブログの内容（大きく項目を分ける）

## 参考サイト

udon

公式

公式のextention手順


:::message
インスタンスなどの言葉が分かりにくくないか！確認。別にインスタンスのままでもいいけど。
:::


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
