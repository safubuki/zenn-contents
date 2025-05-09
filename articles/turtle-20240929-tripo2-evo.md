---
title: "『Tripo 2.0』で劇的に変わるAIと3Dデータ生成！豊富な実例で見る革新的ツール"
emoji: "🐢"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [AI,LLM,3d,3dプリンタ,tripo]
published: true
---
以前、私のブログで「**Tripo**」というAIツールをご紹介しました。このツールは、たった1枚の画像から3Dデータを作成することができます。

https://zenn.dev/safubuki/articles/turtle-20240721-tripo-3dp

この`Tripo`が異次元の進化を遂げ、新たに「**Tripo 2.0**」としてリリースされました！まず、以前の`Tripo`と`Tripo 2.0`で1枚の画像から生成した結果を比較してみましょう。

![](/images/turtle-20240929-tripo2-evo/comp_kame.png)
*以前のTripoとTripo2.0の比較*

次に、`Tripo 2.0`で生成した亀を様々な角度から確認できるGIF画像をご覧ください。

![](/images/turtle-20240929-tripo2-evo/kame_gif.gif)
*Tripo2.0生成結果 GIF画像*

以前の`Tripo`も画像から3Dデータを生成できる点には驚かされましたが、奥行き方向や見えない部分の生成が苦手でした。しかし、`Tripo 2.0`ではその苦手な部分が解消され、画像の特徴をしっかりと捉えた高品質な3Dデータを生成できるようになりました。

`Tripo 2.0`は、単に3Dデータを生成するだけでなく、生成したデータに動きをつけることも可能です。

![](/images/turtle-20240929-tripo2-evo/rig_walk_gif.gif)
*Tripo2.0リギング&アニメーション GIF画像*

今回は、この魅力的な`Tripo 2.0`の基本的な使い方や特徴的な機能を紹介し、「こんな場合はどうなるのか？」といった気になる内容の検証も行います。

`Tripo 2.0`は商用サービスとして使いやすいインターフェースを提供しており、無料で試すこともできます。ぜひこの記事を読んで、`Tripo 2.0`を実際に触ってみてください。

https://www.tripo3d.ai/

## ブログの構成

このブログは「基本機能」「特徴的な機能」「気になる内容の検証」の3つの大きな章からなります。各章の概要については、次の図をご覧ください。

![](/images/turtle-20240929-tripo2-evo/blog_struct.png)
*ブログの構成（クリックで拡大）*

## 基本機能

`Tripo 2.0`の基本機能として、以下の内容を紹介します。

- 1枚の画像から3Dデータを生成
- プロンプト（指示文）を使って3Dデータを作成
- 作成した3Dデータの確認方法

### 事前準備

まず、`Tripo 2.0`を利用するためには、サインアップまたはログインが必要です。アカウント登録はとても簡単です。

1. **Tripo AIの公式サイトにアクセス**
[**https://www.tripo3d.ai/**](https://www.tripo3d.ai/)にアクセスします。

2. **サインアップ/ログインを行う**
画面右上の`Sign up/Log in`ボタンをクリックします。
![](/images/turtle-20240929-tripo2-evo/common_usage_00.png)
*Sign up/Log inボタン*

3. **アカウント登録**
アカウント登録画面が表示されます。画面下部のGoogleアカウントを利用して登録することもできます。
![](/images/turtle-20240929-tripo2-evo/common_usage_01_01.png =400x)
*アカウント登録画面*

4. **TOP画面表示**
ログインすると、以下のようなTOP画面が表示されます。
![](/images/turtle-20240929-tripo2-evo/common_usage_01.png)
*Tripo TOP画面*

Basicユーザーとして登録すると、月あたり600クレジットが付与されます。これにより、24個の3Dデータを生成でき、お試しには十分です。

### 1枚の画像で3Dデータを生成

ここでは、1枚の画像データをインプットとして用意し、その内容に基づいて3Dデータを生成する手順を示します。`Tripo 2.0`の優れたユーザーインターフェースにより、簡単に3Dデータを生成できます。

1. **画像データをドラッグ＆ドロップ**
インプットとなる画像データを以下の赤枠の部分にドラッグ＆ドロップし、「Create」ボタンを押します。1回あたり25クレジットが消費されます。
![](/images/turtle-20240929-tripo2-evo/turtle_base.jpg =300x)
*インプットとなるカメ画像データ*
![](/images/turtle-20240929-tripo2-evo/image_usage_01_select.png)
*画像のドラッグ&ドロップ先*

2. **データ生成を待ち、完了したら編集画面を開く**
「Create」ボタンを押すと、3Dデータ生成中の画面が表示されるので、少し待ちます。
![](/images/turtle-20240929-tripo2-evo/creating.png =300x)
*データ生成中画面*
3Dデータの生成が完了すると、次の画面が表示されます。ここで3次元的に結果を確認できます。編集画面を開くために、赤枠で囲った箇所をクリックします。
![](/images/turtle-20240929-tripo2-evo/create_done.png =300x)
*データ生成完了画面*

3. **内容を確認して、3Dデータをダウンロード**
次のような編集画面が表示されます。編集画面では様々な操作が可能ですが、ここでは3Dデータをダウンロードします。赤枠の「Download」ボタンを押すとダウンロードが開始します。デフォルトの形式は`glb`す。
![](/images/turtle-20240929-tripo2-evo/image_usage_02_select.png)
*編集画面・ダウンロードボタン*

4. **3Dプリントなど用途に応じて利用**
ダウンロードした3Dデータは、用途に応じて利用します。私の場合は3Dプリントを行うため、curaというツールを利用してプリント用のスライスを行います。

![](/images/turtle-20240929-tripo2-evo/image_usage_03.png)
*スライサによる編集*

このようにして、無事に3Dプリンタで目的のカメを出力することができました。そのリアルさにはただ驚かされます！ 

![](/images/turtle-20240929-tripo2-evo/3dp_kame.png)
*3Dプリンタにより出力されたカメ*

### プロンプト(指示文)で3Dデータを作成

ここでは、プロンプト（指示文）を使って3Dデータを生成する手順を示します。

1. **プロンプトを考える**
まず、作成したい3Dデータを思い浮かべながら、プロンプトを考えます。

```text:走行できる夢のソファ
革張りのソファ型の4輪車。
まるで家具のソファのようだが、タイヤが4つついており楽に移動できる乗り物。
見た目は完全にソファ。
```

2. **プロンプト入力**
プロンプトを以下の赤枠の部分に入力し、「Create」ボタンを押します。1回あたり60クレジットが消費され、一度に4つの3Dデータが生成されます。
![](/images/turtle-20240929-tripo2-evo/prompt_usage_01.png)
*プロンプトの入力先*

3. **データ生成を待ち、完了したら編集画面を開く**
3Dデータが生成されるのを少し待ちます。生成が完了すると、次のように4つの結果が表示されます。それぞれを確認し、編集画面を開くために、目的の3Dデータの赤枠で囲った箇所をクリックします。

![](/images/turtle-20240929-tripo2-evo/prompt_usage_02.png)
*プロンプトによる3Dデータの生成結果*

以降の手順は画像データで生成する場合と同様のため省略しますが、プロンプトからも3Dデータが生成され、3Dプリントすることができました。
![](/images/turtle-20240929-tripo2-evo/sofa_gif.gif)
*生成されたソファカーの3Dデータ*
![](/images/turtle-20240929-tripo2-evo/3dp_sofa.png)
*3Dプリンタにより出力されたソファカー*

### 作成した3Dデータの確認方法

生成した3Dデータは、TOP画面の赤枠で囲った「My Models」を選択することで確認できます。

![](/images/turtle-20240929-tripo2-evo/my_models.png)
*My Models画面*

以上で、基本機能の説明は終了です。引き続き、特徴的な機能をご覧ください。

## 特徴的な機能

ここでは、`Tripo 2.0`の特徴的な機能として、TOP画面と3Dデータ編集画面から使える以下の内容を紹介します。

- **TOP画面**
  - 関連度の高い既存3Dデータのオススメ
  - Popcorn（ポップコーン）機能
- **編集画面**
  - リギング（骨格3Dデータ）とアニメーション
  - Stylize（スタイライズ）による3Dデータ様式指定
  - 再トポロジ化と保存フォーマット

### 関連度の高い既存3Dデータお勧め表示 [TOP]

基本機能の手順を試された方はお気づきかもしれませんが、入力欄に画像データやプロンプトを入力すると、関連する既存の3Dデータが表示されます。

例えば、入力欄に「かわいい猫が座っている」と入力してみてください。
※ この時に`Create`ボタンを押さないように注意してください。
すると、たくさんの猫の3Dデータが表示されます😍 これはリアルタイムにデータを生成しているのではなく、既にある関連度の高い3Dデータを表示しているのだと思います。

![](/images/turtle-20240929-tripo2-evo/cat_usage_01.png)
*関連度の高い既存3Dデータ表示*

気に入った猫の画像をクリックすると、編集画面が開きます。高度な編集はできませんが、データのダウンロードは可能です。既存の3Dデータのため、5クレジットで利用できます。

![](/images/turtle-20240929-tripo2-evo/cat_usage_02.png =500x)
*オススメ3Dデータの編集画面*

データは`glb`形式なので、3Dプリンタで印刷することも可能です。

![](/images/turtle-20240929-tripo2-evo/cat_usage_03.png =400x)
*3Dプリント スライサで確認（既存3Dデータ猫）*

生成AIは、どのような結果が得られるかやってみるまで分からないというリスクがあります。そのため、商用サービスでこの機能が提供されているのは本当に親切だと思いました。

### Popcorn（ポップコーン）機能 [TOP]

名前からは機能が想像できなかったので、実際に使ってみることにしました。この機能はプロンプトを利用する場合のみ使用できるようです。次のようなプロンプトを入力して、ポップコーン機能を試してみました。

```text:入力するプロンプト（SFの鉱山で採掘していそうなロボット）
採掘用のずんぐり太った旧型ロボット。
旧式採掘ロボットは、旧式で工事現場の設備のようで、ダサくて、カッコ悪い。 
金属製の質感を持ち、機械的なディテールがリアルに描写、色は黄色やオレンジがぼやけた色。
```

「Create」ボタンの横にある「Popcorn」ボタンを押します。
![](/images/turtle-20240929-tripo2-evo/popcorn_01.png)
*ポップコーン機能*

生成結果は次のように表示されました。

![](/images/turtle-20240929-tripo2-evo/popcorn_02.png)
*ポップコーン機能の使用して生成した結果*

```text:ポップコーン生成結果のプロンプト
愛らしい顔つきの太った旧式採掘ロボット、
錆びた黄色とオレンジの外装に、機械的な歯車や配管が露出。
大きなショベル手で宝石を掘り、目をキラキラさせながら嬉しそうに作業中
```

この機能は、どうやら「**与えたプロンプトから意外性のある結果を生むための機能**」のようです。ちなみに、ポップコーン機能を使わなければ、次のようにいかにもSFな感じで鉱山で稼働していそうなロボットが生成されます。

![](/images/turtle-20240929-tripo2-evo/popcorn_03.png)
*ポップコーン機能を使用せずに生成した結果*

### リギング（骨格モデル）とアニメーション [編集]

高精度な3Dデータが生成されるだけでも十分凄いのですが、さらにそのモデルに動きをつけて、歩いたり、走らせたりすることができます。

編集画面を開き、「Rigging & Animation」の項目を選択します。この機能を利用するためには20クレジットが必要です。リギングが完了すると、立つ（動きはありません）、歩く、走る、ダイブするなどの動作を行うことができます。

![](/images/turtle-20240929-tripo2-evo/rig01.png)
*リギング Stand選択*

「歩く（Walk）」を選択します。すると3Dデータが動き始めます。こちらはブログの冒頭で紹介したものと同じです。なお、モデルが銃器などのオブジェクトを持っている場合、このように分割されて表示されてしまうことがあります。

![](/images/turtle-20240929-tripo2-evo/rig_walk_gif.gif)
*リギング Walk選択*

次に「走る（Run）」を選択します。より活発な動作になりました。

![](/images/turtle-20240929-tripo2-evo/rig_run_gif.gif)
*リギング run選択*

最後に「ダイブ（Dive）」を選択します。少しごちゃっとしていますが、それでも動きのイメージはつくのではないでしょうか。

![](/images/turtle-20240929-tripo2-evo/rig_dive_gif.gif)
*リギング Dive選択*

リギングモードから通常の編集モードに戻るには、「Original」ボタンを押します。

![](/images/turtle-20240929-tripo2-evo/rig_return.png)
*リギングモードを抜ける*

なお、このロボットのように骨格モデルを適用できないと判断された3Dデータは、アニメーションを表示させることができませんので、ご注意ください。

![](/images/turtle-20240929-tripo2-evo/rig_nouse.png =400x)
*リギングができない3Dデータ*

### Stylize（スタイライズ）による3Dデータ様式指定 [編集]

Stylize（スタイライズ）は、3Dデータの様式を変更する面白い機能です。3Dデータをレゴブロック調にしたり、3Dピクセル風（小さな立方体の集合）にしたり、ボロノイ図にすることもできます。この機能を利用するには、それぞれのStylizeに対して10クレジットが必要です。必要なものを選んでご利用ください。

**Lego**（レゴブロック調）

![](/images/turtle-20240929-tripo2-evo/style_lego.png)
*Legoを選択*

**Voxelize**（3Dピクセル風）

![](/images/turtle-20240929-tripo2-evo/style_vox.png)
*Voxelizeを選択*

**Voronoi**（ボロノイ図）

![](/images/turtle-20240929-tripo2-evo/style_voronoi.png)
*Voronoiを選択*

生成されたデータは、この表示された状態のまま`glb`形式でダウンロードすることができます。

### 再トポロジ化と保存フォーマット [編集]

`Tripo 2.0`は、生成した3Dデータを再トポロジ化（Retopology）することができます。これはアニメーションやゲームなどで、低ポリゴンにすることでデータ量を減らし、効率的に利用する際に行います。以下の赤枠で囲った項目で設定できます。

![](/images/turtle-20240929-tripo2-evo/retop_setting.png)
*再トポロジ化と保存フォーマット*

カスタム設定により、自由に組み合わせて設定することもできます。また、対象のソフトウェアやゲームタイトルを選択することで、適切な再トポロジ化設定と保存フォーマットを自動で選択してくれます。例えば、有名なタイトルである`Roblox`を選択すると、「game asset 3000」にチェックが入り、フォーマットが`fbx`形式に設定されました。

![](/images/turtle-20240929-tripo2-evo/settings_02.png)
*タイトル選択による設定の自動設定*

私はこれらのタイトルで自らデータを作成したことはありませんが、よく利用される方にとっては便利な機能だと思います。

以上で、便利な機能の説明は終了です。ここまでの章を読んでいただければ、`Tripo 2.0`をすぐにでも使いこなせるのではないでしょうか？引き続き、気になる内容の検証を行っていますので、ぜひご覧ください。

## 気になる内容の検証

この章では、「こんな場合はどうなる？」という内容を検証します。現状は2つだけですが、今後さらに面白そうな内容があれば更新していきたいと思います。扱う内容は次の通りです。

- フォトリアルな画像は3Dデータにできるか？
- 人物の全身画像を正確に3Dデータ生成し、プリントできるか？

### フォトリアルな画像は3Dデータにできるか？

以前の`Tripo`では、フォトリアルな画像は平面的に出力され、3D形状が正確に再現されることはありませんでした。新しい`Tripo 2.0`ではどうなるのか確認してみました。検証に利用する画像は、私が以前書いたブログで使用した画像です。

https://zenn.dev/safubuki/articles/turtle-20240916-klingai

![](/images/turtle-20240929-tripo2-evo/turtle_study.jpg =450x)
*ブログで利用したサンプル画像*

この画像を3Dデータにした結果は次の通りです。一見すると失敗しているように見えますが、いくつか驚くべきポイントがあります。

- 人物の特徴（服装・髪型、姿勢）を大まかにとらえることができている
- 人物の3Dデータとして、成立している
- 背景を正確に取り除き、対象者のみを3Dデータにしている

この写真は、構図が独特なのでこのような結果になりましたが、普通に人物が立っているような写真なら、より良い3Dデータが生成されるのではと思います。

![](/images/turtle-20240929-tripo2-evo/study_girl_data.png)
*3Dデータ生成結果*

期待以上の結果でした👆

### 人物の全身画像は、3Dデータ生成してプリントできる？

人物の全身画像をどこまで正確に3Dデータにできるか、そして3Dプリンタでの印刷に耐えられるかを検証してみました。検証に使う画像は3Dデータ生成しやすいよう、ややデフォルメしてカートゥーン調にしました。以前のTripoでもかなりデフォルメした画像であれば、3Dデータ生成やプリントはうまくいっていましたが、今回はその時よりもリアルさを増し、構成要素も複雑にしました。

![](/images/turtle-20240929-tripo2-evo/stand_knight.jpg =300x)
*甲冑女性のカートゥーンデフォルメ画像*

この画像を3Dデータにした結果は次の通りです。機能説明で何度も取り上げたのでややネタバレ感がありますが、優秀な出力結果だと思います。

![](/images/turtle-20240929-tripo2-evo/knight_girl_data.png)
*3Dデータ生成結果*

私が良いと思った内容は次の3点です。

- ライフル銃や甲冑など、かなり細かい部分まで正確に再現できている
- マントなどの布がカスれたり、穴が開いたりする不完全な部分がなく、厚さも一定程度確保されている
- 見えていない部分もバランス良く3Dデータ化されている

生成された3Dデータが非常に綺麗だったため、3Dプリンタによる印刷もとてもうまくいきました。

![](/images/turtle-20240929-tripo2-evo/3dp_knight.png)
*3Dプリンタによる印刷結果*

大変満足度の高い結果となりました👍

気になる内容の検証は以上となります。

## まとめ

3Dデータを生成する「**Tripo 2.0**」の基本および特徴的な機能と、気になる内容の検証を行いました。

以前の`Tripo`がリリースされたとき、一部は不完全ながらもその可能性に大いに期待を膨らませました。そして、今回の`Tripo 2.0`です。この技術・ツールは革新的であり、モノづくりの現場やゲーム開発、VR（仮想現実）など、様々なシーンに大きなインパクトを与えるのではないかと思います（個人の感想です）。現状は単独の3Dデータ生成だけですが、次のような機能のリリースも予定されているようです。ますます目が離せません。

![](/images/turtle-20240929-tripo2-evo/add_func.png)
*Tripoの今後追加予定の機能*

商用サービスとして使いやすいインターフェースが用意されており、無料でも利用できるため、少しでも気になった方は、ぜひ触ってみてその凄さを体感してみてください！

もし、分からないことなどありましたら、遠慮なくコメント欄に書き込んでください🐢
このブログの内容が、読んでくださった方のお役に立てたなら幸いです。
最後まで読んでいただき、ありがとうございました。

## 付録

付録では、ブログ記事を書いた後にさらに付け足したい内容を書きます。お時間があれば、ぜひご覧ください。

### コンテスト

「2024/10/08 - 2024/10/22」の期間中に、次のようなコンテストが開催されています。簡単に説明すると、Tripoを利用して独創的な「チェスの駒」を作るという内容です。

![](/images/turtle-20240929-tripo2-evo/contest.png =500x)
*コンテストの案内*

私も早速応募してみました。家電が好きなので、掃除機や掃除をテーマにしました。タイトルページの下部に並んでいるものが、Tripoで生成した3Dデータです。公式サイトに行くと、あらゆる角度から確認できますので、チェックしてみてください。

![](/images/turtle-20240929-tripo2-evo/chess_title.jpg)
*応募作品のタイトルページ*

公式サイトにアクセスするとトップページにイベントへのリンクが表示されます。画面上部のEventタブからもアクセスできます。

https://www.tripo3d.ai/

今回のイベントに限らず、今後も似たような形式でコンテストが定期的に開催される可能性が高いです。また、このようなお題に取り組むことで、コツを早くつかむことができます。解説していきますので、楽しみながらチャレンジしてみてください。

#### ●インプット画像作成

インプット画像の作成について、どのサービス選択し、どのように目的の画像を生成したかを解説します。

画像生成AIについては、DALL-E3、Flux1、ImageFXを比較した結果、掃除機や掃除用具の品質が高かったGoogleのImageFXを選択しました。

![](/images/turtle-20240929-tripo2-evo/image_fx_input.png =500x)
*ImageFXの画面*

一例として、この画像を作るためには次のようなプロンプトを用意しました。
※プロンプトはスペースをとるため、折りたたみ表示にしています。

:::details ナイト掃除機のプロンプト（クリックして開く）
```text:ナイト掃除機のプロンプト
英語プロンプト：
Create a chess piece in a vacuum cleaner consisting of a main unit and a hose.
White background.
Design chess piece s with a vacuum cleaner consisting of a main unit and a hose as the main object.
The design should be easily recognisable as a vacuum cleaner consisting of a main unit and a hose.
The vacuum cleaner , consisting of the main unit and the hose , is the star of the game.
The vacuum cleaner should be suitable for a knight and should be designed like a piece of iron armour to represent strength.
Underneath the vacuum cleaner , which consists of the body and hose , is a circular base.
The circular pedestal is made of plain wood like flooring, slightly thicker in size and does not interfere with the design of the vacuum cleaner.
The vacuum cleaner should be the main focus and the pedestal should not be too large.
The pieces are realistic 3DCG and the images are photorealistic.
---
日本語訳：
本体とホースで構成された掃除機でチェスの駒を作ります。
白い背景です。
本体とホースで構成された掃除機をメインにチェスの駒をデザインしてください。
本体とホースで構成された掃除機であることが一目でわかるデザインにしてください。
本体とホースで構成された掃除機が主役です。
掃除機はナイトのように、強さを表現するために鉄の甲冑のようなデザインです。
本体とホースで構成された掃除機の下には円形の台座がある。
円形の台座はフローリングのような無地の木材でできており、サイズはやや厚めで、掃除機のデザインを邪魔しません。
掃除機が主役なので、台座は大きすぎない方がよいです。
作品はリアルな3DCGで、画像は写実的です。
```
- AIが期待する結果を生成しないときは、同じ文章で繰り返してみる、邪魔している文言がないかを確認するなどを行ってください。
:::

また、今回のように「駒のメイン部分 + 台座部分」のように複数の要素からなる画像を生成する場合、「駒の部分は良いのに、台座の生成がイマイチだなぁ...」ということがあると思います。そのような場合は、編集モードでの部分生成が便利です。次のように台座の部分だけを選択して、再生成することが可能です。必要に応じて活用してみてください。

![](/images/turtle-20240929-tripo2-evo/image_fx_parts.png =500x)
*ImageFXの編集モード画面*

ちなみに、目的の画像はなかなかできるものではなく、今回私は初めてImageFXの1日上限まで使い切りました。1、2回だけやって「AIはダメだなぁ。言うことを聞かないなぁ。」とあきらめるのではなく、根気強くやることが大切です。

![](/images/turtle-20240929-tripo2-evo/image_fx_never.png)
*多数の生成試行実施（一部抜粋）*

画像ができたら「1枚の画像で3Dデータを生成」の章で確認した手順に従って、3Dデータを作成します。Tripoによる3Dデータ出力結果がイマイチということありますが、これは複数回試行しても結果は大きく変わりませんから、インプット画像を差し替えるのが良いかと思います。

また、イベント期間中は「**Free Retry**」が通常時よりも多くできるように感じます（気のせいかもしれませんが）。Free Retryで2～3回再生成できますので、それで確認するのも良いと思います。

#### ●応募方法

応募は、その回ごとのルールをよく確認してください。
まず「Submit Here」のような投稿ボタンを探します。

![](/images/turtle-20240929-tripo2-evo/submit.png)
*submitボタン*

このボタンを押すと、必要事項の入力画面が表示されるので、適宜入力していきます。カバーイメージは簡易的なものでも良いですが、少しキレイなものを用意すると世界観などを伝えやすくなります。

![](/images/turtle-20240929-tripo2-evo/submit_input_01.png)
*submit 入力画面1*

続いて、各駒を登録しますが、私はここで少し戸惑いました。このURL入力欄には何を入れたら良いのだろうと。

![](/images/turtle-20240929-tripo2-evo/submit_input_02.png)
*submit 入力画面2*

ここについては、3Dデータの編集画面の赤枠で囲ったリンク共有ボタンを押すことで入手可能です。このURLを先ほどのSubmit入力画面2に入力します。

![](/images/turtle-20240929-tripo2-evo/submit_input_url.png)
*submit リンク共有ボタン*

赤い*マークがついていない項目は、通常時は利用しないので無視して構いません。あとは利用規約をよく読み、同意チェックをした上で提出してください。提出すると、3Dデータは共有され、誰でもアクセス可能になります。

以上で説明は終了です。ぜひイベントにチャレンジして、楽しみながらコツを掴んでください！

### セブンティーンアイス

私はセブンティーンアイス（特にカラフルチョコ）が大好きです！3Dデータにしてみたところ、想像以上にセブンティーンアイスだったので、嬉しくなってこのようなものを作成しました。

![](/images/turtle-20240929-tripo2-evo/17ice.png)
*セブンティーンアイスの楽しみ方*

元となったのは、駐車場の車の中で何気なく撮った1枚の写真です。この写真を見ると、アイスの上部が少し欠けているのですが、それもTripoは見逃さず、非常に高い再現性です。

![](/images/turtle-20240929-tripo2-evo/real_17ice.jpg =400x)
*元のリアルなセブンティーンアイス*

このように色々な楽しみ方ができるのも、Tripoならではだと思いました。

## リンク

私が書いたAI関連ツールの記事のリンクを紹介します。興味があればぜひご覧ください。

私が書いた、GitHub CopilotというAIを利用したコーディングツールに関する記事です。プログラミングに興味がある方は、ぜひこちらの記事も読んでみてください。AIをうまく活用し、Copilotでコードの中身を、Tripoで3Dデータの外側を生成するなどと分業させると、モノづくりの速度が劇的に改善するのではと思っています。

https://zenn.dev/safubuki/articles/turtle-20240223-gitcopilot

Googleの動画生成AI「Veo2」は、Geminiなど、私たちが普段利用しているGoogleのプラットフォームから手軽に試せます。基本的な操作はシンプルですが、いくつかのコツを押さえることで、より魅力的な動画を作成できます。この記事では、Geminiの強力なカスタマイズ機能「Gem」を活用した動画生成テクニックなど、実践的な内容を解説しています。
https://zenn.dev/safubuki/articles/turtle-20250417-veo2

画像1枚から動画を生成するAIツール『Kling AI』の使い方やコツを紹介します。さらに、CM風の動画を作成することで、実際のシーンでの活用例も示しました。うまく融合させれば、モノづくりとプロモーションが画像1枚から可能になりそうです。

https://zenn.dev/safubuki/articles/turtle-20240916-klingai

TripoSRがリリースされたのは2024年3月頃でしたが、そこから約半年で劇的に進化しました。技術の変遷を確認する意味でも、読んでみると良いかもしれません。3Dプリントも絡めつつ、3Dモデル作成における画像生成のコツや成功・失敗事例なども記載しており、楽しんでいただけると思います。

https://zenn.dev/safubuki/articles/turtle-20240721-tripo-3dp

## 更新履歴

更新履歴は折りたたみ表示にしています。
確認したい場合は、以下のバーをクリック（タップ）してください。

:::details 更新履歴（最終更新日：2025/04/17）
**更新履歴**

- **2025/04/17**
  - Veo2のブログへのリンクを追加しました。

- **2024/09/30**
  TripoSRリンク及び、説明文をリンク欄にも追加しました。
  一部画像のサイズを調整

- **2024/10/11**
  コンテストについて「付録」の章に追加しました。

- **2024/11/02**
  セブンティーンアイスのいろいろな楽しみ方を追加しました。
:::