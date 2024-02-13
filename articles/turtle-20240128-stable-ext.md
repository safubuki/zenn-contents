---
title: "【Stable Diffusion】WebUI拡張機能開発！作り方からIndexリスト登録まで"
emoji: "🐢"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [StableDiffusion,Gradio,AI,Python,GitHub]
published: true
---
画像生成AIは、掛け算の組み合わせ（例えば、亀×犬や花×亀など）から、想像もできないようなものを生み出し驚かされます。画像生成AIには様々なツールがありますが、今回は扱うStable Diffusion WebUI（以下、WebUI）は、自分のPCに環境を作ることができます。そして、他の人が作成した拡張機能を自由に組み合わせて、自分の好きなようにカスタマイズすることができます。

私は拡張機能を便利に利用していましたが、**自分でも作ってみたい**と思い、2024年正月に挑戦してみました！

さらに、WebUIには、Indexリストから欲しい拡張機能を探して、簡単にインストールできる仕組みがあります。私は、自分が作ったものを他の人とも共有できたらいいなと思いました。そこで、**WebUI Indexリストへの登録**もしてみました。

この記事では、私がやったことを丁寧に紹介します。「私も作ってみたい」「これなら自分にもできそう」と思ってもらえたら嬉しいです😊

#### ブログ対象者

- **自分で拡張機能を作ってみたい人**
  
ただし、作成にあたって次のスキルが必要になります。

- **WebUIの拡張機能を扱える**
- **Pythonでプログラムを作成できる**
- **GitHubを扱える**

自分には少し難しそうかも・・・と思われる方がいるかもしれませんが、便利な学習サイトがいろいろあります。末尾にリンクを載せていますので、拡張機能をテーマに学習するのもイイと思います👍

#### 得られる効果

- **WebUIの拡張機能を作成できます。**
入力に基づいて簡単な計算をし、出力欄に出力するシンプルな拡張機能を作ることができるようになります。機能の詳細については以下のリンクにアクセスしてみてください（日本語READMEもあります）。

https://github.com/safubuki/sd-webui-latent-regional-helper

![lr_helper](/images/turtle-20240128-stable-ext/lr_helper.png =500x)
*Latent Regional Helper（著者作成の拡張機能）*


- **WebUI Indexリストに登録し、自分の拡張機能を広く公開できるようになります。**
GitHubのURLを直接張り付ける方法の他に、リストを参照してインストールする方法もあります。WebUIを使っている人に、自分の拡張機能を見てもらえるチャンスが増えます。

![index_list](/images/turtle-20240128-stable-ext/index_list.png =500x)
*WebUI Indexリスト*

## 開発環境の準備

まず開発を行うための準備を行います。
拡張機能の環境は、次のようなフォルダ構成になります。

![ext_env](/images/turtle-20240128-stable-ext/ext_env.png =600x)
*拡張機能 フォルダ構成*

もし、すでにいくつか拡張機能をインストールされている方は、extensionsフォルダにアクセスすると、それらを見ることができます。

それでは手順を解説します。

### 手順

1. 自身のGitHubページでレポジトリを作成します。
   - レポジトリ名は、**自身の拡張機能の名前**を設定してください。
   ※後から変更可能ですので、とりあえずの名前でもOKです。
   - 公開を前提としていますから、公開設定は**Public**を選択します。
   - Add a README fileに、**チェックを入れて**ください。
   README.mdファイルが追加されます。

   ![git_repos](/images/turtle-20240128-stable-ext/git_repos.png =500x)

2. 作成したGitHubレポジトリのアドレスをコピーします。
3. StableDiffusion WebUIを開き、`Extensions`タブ→`Install from URL`タブに移動します。
4. 先ほどコピーしたアドレスを赤枠の欄に張り付けて、Installします。

   ![stable](/images/turtle-20240128-stable-ext/stable.png =400x)

5. `extensions`フォルダの下に、自分の拡張機能のフォルダ(＝GitHubレポジトリ名)ができていることを確認します。
※フォルダにはまだ`README.md`しかありません。
6. 自分の拡張機能のフォルダの中に移動し、**`scripts`フォルダを作成**します。
7. scriptsフォルダの中に移動し、**`開発用のpy`ファイルを作成**します。
※ ファイル名は、`main.py`や`ext_func.py`など何でも構いません。
8. 以下のGitHubに便利な拡張機能のテンプレート（雛形）が公開されています。
アクセスして`scripts`フォルダを参照してください。ファイルの内容は次の通りです。
   - **template.py**：txt2imgやimg2imgタブの中に拡張機能を作ります。
   - **template_on_settings.py**：Settingsタブに設定を作ります。
   - **template_on_tab.py**：txt2img等と同じようにタブ上に拡張機能を作ります。

https://github.com/udon-universe/stable-diffusion-webui-extension-templates

9. 今回は「タブ上に拡張機能を作る」で進めますので次の**template_on_tab.py**の内容をコピーし、手順7で作成した開発用のpyファイルにペーストします。

https://github.com/udon-universe/stable-diffusion-webui-extension-templates/blob/main/scripts/template_on_tab.py

以上で、実装をするための環境は整いました🎉

## 拡張機能の実装方法

実装を進める前に、拡張機能のUIについて説明します。
これまでの説明の中で、WebUIや拡張機能の画面をいくつかお見せしましたが、こう思いませんでしたか？「もっと華やかにしてみたいな」「ボタンの形、表現を変えてみたいな」と。私はちょっと思いました。しかし、これはできないようです。

理由は、**Gradio**というフレームワークを使っているからです。
Gradioを使うとWebアプリケーションの作成が簡単にできます。Pythonのモジュールで、関数と入出力の形式を指定するだけで、インタラクティブ（双方向）なUIができる優れものです。ただ、それゆえに表現できる内容は限られます。

Gradioでどのようなことができるかは、公式サイトのドキュメントを見てみてください。

https://www.gradio.app/docs/interface

その他、皆さんが使い慣れている拡張機能を参考にするのも一つの手です。既にいくつかインストールしているなら、`extensions`フォルダで見ることができます。
まずは、シンプルな拡張機能から見てみると理解しやすいです。

**それでは、実装の仕方を解説します。**
解説は、私が作成した拡張機能の画面およびコードで行います。

- **画面**
![lr_helper_all](/images/turtle-20240128-stable-ext/lr_helper_all.png)
*Latent Regional Helper 全体（著者作成の拡張機能）*

- **ソースコード**

:::message
以下のリンク先のコードを元に説明しますので、リンク先にアクセスしてください。  
:::
:::message
2024/02/13 追記
拡張機能の最新のコードはアップデートしております。
この章の説明は、本記事公開時点（2024/02/02）のコードを元に行いますので、
以下のリンク先へのアクセスをお願いします。
:::
**[safubuki/sd-webui-latent-regional-helper/blob/a6d2b18d19a70ebe8f958305e4fc11c71e6f3e7d/scripts/latent_regional_helper.py](https://github.com/safubuki/sd-webui-latent-regional-helper/blob/a6d2b18d19a70ebe8f958305e4fc11c71e6f3e7d/scripts/latent_regional_helper.py)**

### インポート

まず、必要なモジュールをインポートします。

```Python:latent_regional_helper.py
from typing import List, Tuple
import gradio as gr
from modules import script_callbacks
```

- **typing**
Pythonの型ヒントのために使用します。拡張機能に直接関係はありません。
- **gradio**
Gradioを利用するために必要です。
- **modules.script_callbacks**
StableDiffusion WebUI(AUTOMATIC1111)が提供するインタフェースです。
ここでは、uiを新しいタブに追加するために利用しています。
extensionsフォルダと同階層の`modules`フォルダにコードあります。
ドキュメントなどは無い(と思います)ので、コードから紐解く必要があります。

### UI画面

次の関数が、UI画面を作っている箇所になります。

```Python:latent_regional_helper.py
def on_ui_tabs() -> List[Tuple[gr.Blocks, str, str]]:
```

#### レイアウト

on_ui_tabsの中を見ていくと`Blocks` `Row` `Column`が目に付くと思います。
それぞれ説明します。

- **Blocks**
  gradio のインターフェイスを利用するために必要な要素です。まずこれで全体を囲います。
- **Row**
  子要素を水平方向に並べます。
- **Column**
  子要素を垂直方向に並べます。

コードから`Blocks` `Row` `Column`の部分だけを抜き出し、分かりやすくして見ていきます。

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
*UI画面構成図*

慣れるまでは少し苦労しますが、慣れるとテキストボックスやボタンなどを目的の場所に配置できるようになります。

#### コンポーネント

UI画面を作るときに、`Textbox`や`Button`などの部品をコンポーネントと呼びます。 コンポーネントの使い方は、ここでは詳しく説明しませんが、私のコードやGradioのページ、各種拡張機能の中身を見ていただければ、理解できると思います。 なお、コンポーネントを利用する上で押さえておくべきポイントを以下に記します。

- コンポーネントを生成したときの戻り値はキーイベント等で利用しますので、変数に保存しておいてください。以下のケースでは`textbox_back_weight`に保存しています。

  ```Python:latent_regional_helper.py
   textbox_back_weight: gr.Textbox = gr.Textbox(
      label='Background Weight (Latent Only)',
      interactive=True,
      value=str(default_back_weight))
  ```

- 各種コンポーネント生成時の引数で使われる代表的なものは次の通りです。
  - **label**：
  　テキストボックスやボタンなどで表示する名前を設定します。
  - **value**：
  　デフォルトで表示、仕様する値を設定します。
  - **interactive**：
  　`TextBox`などでTrueの時は編集可能です。Falseの時は編集できません。
- タイトルや項目名などの文字表示は`HTML`を使用します。

::::message alert
つまづきポイント！
:::details テキストボックスにValue値を設定してもUI表示で値が反映されない（クリックで表示）

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
私のコードでは、以下の関数が、キーイベントからの受け口となり、ロジック処理部が実行されています。

```Python:latent_regional_helper.py
def division_output(radio_sel: str, col_num_1: str, col_num_2: str, col_num_3: str, col_num_4: str,
                    col_num_5: str, div_weight: str, back_weight: str,
                    chkbox_back: bool) -> Tuple[str, str, str]:
```

### キーイベント

キーイベントは、以下の`Button`コンポーネント生成時`button_execute`に保存した戻り値を利用します。

```Python:latent_regional_helper.py
# Run button
button_execute: gr.Button = gr.Button(value='execute', variant='primary')
```

`execute`キーが押された時のイベント処理は次の箇所になります。

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

キーイベント(=click)実行時に指定するパラメータについて説明します。

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
:::details gradioブロック型のリスト形式でinputsに引数を渡すとAttributeErrorが発生した（クリックで表示）

- 現象
ドロップダウンリストの値をリストに設定してinputsに設定すると、AttributeErrorが発生した。

![listerror](/images/turtle-20240128-stable-ext/listerror.png =500x)
*エラー発生時の実装*

- 原因
inputsにはgradioのブロック型の値を渡す必要があるが、リスト型で渡したためエラーが発生した。

- 解決
  1. リスト形式ではなく、一つ一つgradioのブロック型の値を引数として渡す。
:::
::::

このようにしてキーが押された時の振る舞い決めています。

以上で拡張機能の実装方法の説明は終了です。
拡張機能の作成イメージはつかめましたか？
開発用のpyファイルに自身でコードを書いて、実際の動きを確かめてみてください👍
メインの処理が完成したら、GitHubにコミット、プッシュしてみてください。

## 周辺ファイル作成

ここでは、拡張機能のメイン処理以外に必要な以下の3つのファイルを解説します。
自身の拡張機能フォルダの直下に次のファイルを用意してください。

### LICENSE

開発した拡張機能のOSSライセンス形態、内容を記載します。
自身の拡張機能をOSSとして公開する予定が無ければ不要ですが、公開するのであればあった方が良いです。

https://github.com/safubuki/sd-webui-latent-regional-helper/blob/main/LICENSE

特にこだわりが無ければMITライセンスで良いと思いますが、OSSのライセンス形態各種ありますので、以下のページを参考にしてみてください。

https://manumaruscript.com/oss-licences-comparison/

### README.md

拡張機能の使い方を記載します。
こちらを記載してGitHubにプッシュすると、自身のGitHubレポジトリのトップページにREADME.mdの内容が自動的に表示されます。こちらはMarkdown記法を用いて作成します。Markdown記法については、以下のページを参照してみてください。

https://qiita.com/tbpgr/items/989c6badefff69377da7

また、Markdownの記述はVSCodeを使って編集(左画面)すると、作成イメージ(右画面)を確認しながら作成でき便利です。

![readme](/images/turtle-20240128-stable-ext/readme.png =600x)
*VSCodeによるREADMEの作成*

作成イメージは、VSCode右上の虫眼鏡のマークがついたプレビューボタンを押すことで表示できます。

![preview](/images/turtle-20240128-stable-ext/preview.png =300x)
*プレビューボタン*

### install.py

拡張機能を動作させる際に必要なモジュールを記載します。
もし、Python標準のモジュールだけで使える拡張機能であれば、install.pyは不要です。しかし`pip`でモジュールをインストールしなければ使えない拡張機能の場合、install.pyのL5-L6にあるコメントを外して、インストールするモジュールの名前を記載する必要があります。そうすれば、拡張機能を開くときに、自動で必要なモジュールがインストールされます。

https://github.com/udon-universe/stable-diffusion-webui-extension-templates/blob/main/install.py

- L5:既にモジュールがインストールされていないか確認します。
- L6:動作に必要なモジュールがインストールされます。

::::message
ワンポイント！
:::details install.pyが不要な場合、中身のコメントアウトではなく、ファイルを削除しよう！（クリックで表示）
Python標準のモジュールだけで動作する拡張機能の場合、install.pyは不要です。
ここで「コメントアウトしているから、ファイルは残しておいてもいいか」と思われるかもしれません。しかし、install.pyはコメントアウトして処理が無かったとしても、残しておくだけで拡張機能の起動時間を遅くします。

![start_prof](/images/turtle-20240128-stable-ext/start_prof.png =400x)

起動時間は、WebUI画面下部の`Startup profile`をクリックすると確認できます。
  
- **install.pyあり**（中身はコメントアウトして処理なし）
  ![install_ari](/images/turtle-20240128-stable-ext/install_ari.png =500x)

- **install.pyなし**
  ![install_nashi](/images/turtle-20240128-stable-ext/install_nashi.png =500x)

install.pyありの場合、58ミリ秒かかっていることが分かります。最大で100ミリ秒の時もありました。小さい値に感じるかもしれませんが、これが積み重なると意外と侮れない時間になります。

実は私もコメントアウトしてファイルを残していましたが、後述のIndexリストのPull Request時にレビューでアドバイスを受けて気づきました💦

**install.pyは不要ならファイルごと削除でOKです！**
:::
::::

大変長い道のりでしたが、お疲れさまでした！
以上で実装の解説は終わりになります。
ここまでの内容を読めば、私と同じように小さな拡張機能は作れるのではと思います。
なお、これらのファイルも必要なものを作成したら、GitHubにコミット、プッシュしてみてください。

それでは、あともう少し、最後までお付き合いください。

## Indexリスト登録方法

この章では、WebUIのIndexリストへの登録方法を解説します。
冒頭でもお伝えしましたが、このリストに追加されることで、WebUIを使っている人の目に触れる機会が増えます。

![index_list](/images/turtle-20240128-stable-ext/index_list.png =500x)
*WebUI Indexリスト*

それでは、手順を解説します。

1. 以下のページにアクセスします。
   https://github.com/AUTOMATIC1111/stable-diffusion-webui-extensions
2. リポジトリのFork操作をして、stable-diffusion-webui-extensionsを自身のレポジトリに取り込んでください。画面右上にボタンがあります。
   ![fork](/images/turtle-20240128-stable-ext/fork.png =400x)
   *フォークボタン*
3. 自身のGitHubページに移動し、Forkしたレポジトリをクローンしてください。

   ```text
   git clone https://github.com/{自身のGitHubアカウント名}/stable-diffusion-webui-extensions.git
   ```

4. 上記のレポジトリに作業ブランチを作成してください。
5. 作業ブランチ上で拡張用のjsonを編集します。
   - extension_template.jsonのコピーします。
   - extensionsフォルダにペーストします。
   - ファイル名を変更します。
     - 自身の拡張の名前すると良いです。
     私の場合は`sd-webui-latent-regional-helper.json`にしました。
   - ファイルを編集します。
     - このような形で作成します。

       ```json
       {
          "name": "Latent Regional Helper",
          "url": "https://github.com/safubuki/sd-webui-latent-regional-helper.git",
          "description": "Simplify the region division settings for Latent Couple and Regional Prompter. Simply select from the drop-down list to output the setting values.",
          "tags": [
              "script",
              "tab"
          ]
       }
       ```

       :::message
       added: "YYYY-MM-DD" という項目は自動で設定されるので、設定不要です。
       :::
       :::message
       tagsに何を設定して良いか迷ったら、トップ階層のtags.jsonを参照ください。
       :::
6. 作業ブランチでコミットして、リモートブランチにプッシュします。
7. プルリクエストを行います。
descriptionに自身のGitHubのURLなど簡単な情報を記載して、Checlistにチェックを入れます。チェックはカッコにxを書くことで入れることができます。
![pr](/images/turtle-20240128-stable-ext/pr.png =600x)
*プルリクエスト画面*
8. プルリクエストができていることを確認します。
タイミングにもよりますが、遅くとも1週間くらい待てば、レビューが実施され、特に問題が無ければマージされます。

## 参考サイト

拡張機能を作成するにあたり、以下のサイトには本当にお世話になりました。
こちらのサイトも参考にしてみてください。

ページでの分かりやすい解説はもちろん、GitHubに便利なテンプレートまで公開くださっており、このブログが無ければ、拡張機能の作成はできなかったかもしれません。

https://note.com/udon_universe/n/n5b90689104ce

Stable Diffusion WebUI公式の拡張機能開発のページです。こちらも参考になる内容が多かったです。

https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Developing-extensions

## まとめ

以上で、全ての説明は終了となります！
長い説明に、根気強くお付き合いくださりありがとうございました。
これでStable Diffusion WebUI 拡張機能開発者の仲間入りです。

私もまだまだ、拡張機能についてはできることが限られていますので、少しずつ今の拡張機能をアップデートしながら理解を深めていきたいと思います。

「ここが分かりにくい」などありましたら、補足説明や解説を追加しますので、遠慮なくコメントいただければと思います。

このページを読んでくださった方が、拡張機能を開発するきっかけや少しでも役立っていただけたならとても嬉しいです。改めまして、ありがとうございました。

## おまけ

WebUIの拡張機能ってこうやって作るんだ！自分も作ってみたい。でも、PythonやGitはちょっと・・という方のためにオススメのサイトを紹介します。どちらも有名なサイトなので、私が紹介するまでもないかもしれませんが、参考にしていただければと思います。

Pythonの学習に最適です。入門から段階的に学べます。
今回の私のプログラムであれば、基礎編＋応用の関数とかwith文で理解できるかと思います。
https://www.python-izm.com/

私もGitの基本はこのサイトで学びました。
https://backlog.com/ja/git-tutorial/

## 更新履歴

- **2024/02/14**
  - 「拡張機能の実装方法」で参照するコードを、本記事公開時点（2024/02/02）のものに差し替えました。また、その旨をお伝えする記述を追加しました。
  ※拡張機能がアップデートしても、説明に影響を与えないようにするためです。
