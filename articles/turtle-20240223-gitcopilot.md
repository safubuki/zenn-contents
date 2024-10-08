---
title: "【GitHub Copilot】実践ガイド：図解と例で学ぶ使い方とコード品質向上のポイント"
emoji: "🐢"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [githubcopilot,github,vscode,vscode拡張機能,python]
published: true
---
AIがコードを書いてくれる画期的なツール、**GitHub Copilot**をご存知ですか？

私は2024年1月から使い始めましたが、驚くほど便利です。GitHub Copilotは、自然言語による指示やコードの一部を入力するだけで、目的のコードを生成してくれます。そして、エディタ上で、すぐに反映できるので、開発をとてもスムーズに行うことができます。

私は、GitHub Copilotのおかげで、小規模ながらも個人のOSS(オープンソースソフトウェア)開発にチャレンジすることができました。効率よく開発ができたのは言うまでもありませんが、Copilotが提案するコードから多くのことを学びました。そして、何より、**楽しくコーディング**でき、**モノづくりに集中すること**ができました！

このブログでは、GitHub Copilotが初めてという方のために**使い方の基本**を図解と例を交えながら丁寧に説明し、**品質向上のポイント**など少し発展した内容も紹介します。このブログを読んで、あなたもぜひGitHub Copilotの魅力を感じてみてください👍

#### ブログ対象者

このブログでは、次のような方を対象に分かりやすく説明します。

- **GitHub Copilotについて知りたい**
  - 始めたばかりで概要を知りたい方や、新しいツールを試してみたい方
- **GitHub Copilotの使い方に困っている**
  - 実際にGitHub Copilotを使ってみたが、活用する方法がわからない方
  - コーディングの効率を上げたいが、どうすればいいか悩んでいる方
- **GitHub Copilotを使いこなしたい**
  - すでにGitHub Copilotを使用しているが、さらにスキルを向上したい方
  - 便利なショートカットキーやコマンドで、生産性を高めたい方

なお、説明は**VSCode**エディタ、**Python**言語を用いて行いますが、環境が準備できない、Pythonは普段使わないという方にも読みやすく、内容を理解できるようにしています。

#### 得られる効果

このブログを読むことで、次のような効果が得られます。

- **開発効率の向上**
  - GitHub Copilotの基本機能をマスターし、コーディング速度をアップできます。
  - 日々の開発をよりスムーズに進めることができるます。
- **品質向上のポイント**
  - 静的解析ツールとの組み合わせにより、コードの品質を向上させる方法が得られます。
- **注意点の理解**
  - GitHub Copilotの使用時に気をつけるべきポイントを把握できます。

## GitHub Copilotとは

GitHub Copilotは、AIがコードを自動的に生成し、開発者の生産性を向上させる画期的なツールです。それでは、GitHub Copilotの機能の一覧と利用することによるメリットを見ていきましょう。

### 機能一覧

GitHub Copilotには、多くの機能がありますが、その中でも代表的な機能の一部を紹介します。

![func_list](/images/turtle-20240223-gitcopilot/func_list.png)
*GitHub Copilot機能一覧(代表例)*

コーディングに必要な各種機能が組み込まれており、AIの力を借りて効率的かつスムーズに開発を進めることができます。何だかワクワクしてきませんか？これらの機能を使いたくなってきましたでしょうか。

### ChatGPTとの比較とメリット

しかし、機能の一覧を見て、こう感じた方もいるのではないでしょうか？

「無料版のChatGPTでも同じことできるのでは？」

ChatGPTは、お馴染みの方もいらっしゃるかもしれませんが、頼りになる対話型の生成AIです。確かに、一部の機能は、ChatGPTでも行うことができます。では、どのような違いがあるのでしょうか？実際にプログラムを生成する際の手順を比較してみましょう。まずは、ChatGPTの手順を示します。

![coding_gpt](/images/turtle-20240223-gitcopilot/coding_gpt.png)
*ChatGPTによるプログラム作成手順*

このように**Web上のChatGPTサービスとエディタ間を行き来しながら**、手順を進めていきます。次にGitHub Copilotの手順を示します。

![coding_cop](/images/turtle-20240223-gitcopilot/coding_cop.png =550x)
*GitHub Copilotによるプログラム作成手順*

こちらは全ての手順が**エディタの中で完結**します。

今回は「指示したプログラムを作成する」というシンプルなケースです。しかし、実際の開発では、バグの修正や部分的な処理の追加、関数コメントの作成、テストの実施など行うことが多岐にわたります。Webブラウザとエディタを行き来する1回あたりの時間は僅かかもしれませんが、これが**積み重なると無視できない時間**になってきます。

GitHub Copilotは、AIが提示するコードの精度の高さなど多くの魅力がありますが、何よりも**エディタの中で全てが完結し、ストレスなく快適に開発ができる**、これが一番のメリットだと思います。

## 導入方法

GitHub Copilotは、**有償**（**学生ほか一部対象者は無料**）のツールです。利用するためには、アカウントの作成や契約、エディタの拡張機能をインストールする必要があります。これらの方法について説明します。

なお、既に導入済みの方や、企業などの組織で利用される方（組織で提供される利用手順書等を参照いただくのが確実です）は、**この章をスキップ**して構いません。

この章は、これから使ってみようという**個人の利用者を対象**にしています。
対象者が限られるので、デフォルトでは、説明の表示を閉じています。
必要に応じて「**GitHub Copilotの導入手順**」の**各項目をクリック**して、詳細な説明をご確認ください。
::::message
**GitHub Copilotの導入手順**
:::details ① アカウント作成（クリックで開く）

### アカウント作成

GitHub Copilotの利用には、**GitHub**のアカウント作成が必要になります。既にGitHubアカウントを保持されている方は、スキップしてください。
ちなみに、GitHubは、web上にプログラムコードを保存し、バージョン管理やメンバで共有するためのサービスです。こちらも開発には無くてはならないものですから、まだの方は、この機会に個人のGitHubアカウントを作成しましょう。

1. GitHubのサイトにアクセスします。
   [https://github.com/](https://github.com/)
2. ページ右上のSign upをクリックします。
   ![hub_page](/images/turtle-20240223-gitcopilot/hub_page.png =400x)
3. メールアドレスやパスワードなど必要事項を入力します。
   ![hub_regist](/images/turtle-20240223-gitcopilot/hub_regist.png =400x)
4. メールが送られてきますので、必要な対応を行って、アカウント作成完了となります。

※ 入力画面は、2024年2月現在のものです。
※ 私は、途中まで入力していますが、実際の登録は行っていません。
　 個人が無料のアカウントを複数持つことは利用規約違反となるためです。
　 個人用、業務用(有償organization所属)をそれぞれ分けて使うのは問題ないようです。
　 (参考URL)[複数のGitHubアカウントを保持していいの？GitHubサポートに問い合わせてみた](https://www.timedia.co.jp/tech/20221025-tech/)
:::

:::details ② 有償プラン契約（クリックで開く）

### 有償プラン契約

GitHub Copilotの利用には料金がかかります。そのため、クレジットカードまたはPayPal(paypayではありません)を用いて、利用手続きを行う必要があります。まず、利用料金については、次のようになっています。

| プラン   | 料金      | 備考                               |
|-------|---------|----------------------------------|
| 月額プラン | 10ドル / 月  |                                  |
| 年額プラン | 100ドル / 年 | 月あたり2ドル弱、年間で20ドル(2か月分)お得💰 |

(参考URL) [GitHub Copilot の課金について (公式)](https://docs.github.com/ja/billing/managing-billing-for-github-copilot/about-billing-for-github-copilot)

なお、期間限定で無料で利用する仕組みがあります。

- **1か月の無料トライアル**
どのようなものだろう？と気になる方は、トライアルで**実際に触って確かめてみるのがオススメ**です。その際、作ってみたいもの、開発テーマなど軽く決めてから使うとより効果が実感できると思います。なお、1か月経過後は、**自動で課金されるので注意**してください。事前に解約申請をしても1か月間は使えますので、まず1か月だけという方は、早めに解約申請をしておくと安心です。
(参考URL) [GitHub Copilot 解約方法/手順を3分で解説！ (ブログ記事)](https://yakiimosan.com/github-copilot-cancellation/)
- **学生など無料利用プログラム**
学生、教師、メジャーなオープンソースプロジェクトのメンテナーは無料で利用できます。**学生**は、次のブログ記事が参考になりますので、ぜひチャレンジしてみてください。
(参考URL) [Github Education の申請方法 (ブログ記事)](https://zenn.dev/iizuka0000/articles/how-to-apply-for-github-education)

※上記の情報は、本ブログ執筆時点の2024年2月の情報に基づきます。

それでは、登録・契約の手順を示します。

#### GitHub Copilot登録・契約手順

1. githubサイトにアクセスしてサインインします。
2. 画面右上のアイコンをクリックして、メニュー一覧を表示します。
![cop_kei1](/images/turtle-20240223-gitcopilot/cop_kei1.png =300x)
3. メニュー一覧からCopilotを選択します。
![cop_kei2](/images/turtle-20240223-gitcopilot/cop_kei2.png =200x)
4. 次の画面が表示されるので、プランを選択します。
選択したら、緑の「Get access to GitHub Copilot」ボタンを押します。
トライアルで始める場合は、月額プランを選択しておいた方が安心です。
![cop_kei3](/images/turtle-20240223-gitcopilot/cop_kei3.png)
5. 住所、支払い登録情報が無い場合、次のように住所や支払い情報の登録が求められますので、必要な項目を入力して、緑の「Save」や「Save payment infomation」ボタンを押します。
※既に登録情報がある場合、本画面は表示されず、次の手順6画面が表示されます。
![cop_kei4](/images/turtle-20240223-gitcopilot/cop_kei4.png)
6. 支払いの確認画面が表示されるので、内容に問題なければ、緑の「Submit」ボタンを押します。
![cop_kei5](/images/turtle-20240223-gitcopilot/cop_kei5.png =450x)
7. アカウントの設定画面が表示されますので、設定を行います。
それぞれの設定項目は次の通りです。なお、これらの設定は後から変更可能です。
![cop_kei6](/images/turtle-20240223-gitcopilot/cop_kei6.png =450x)

- **Suggestions matching public code**
GitHub Copilotが提案しようとしたコードがGitHub上の公開コードと一致した場合に、そのまま提案するかどうかを設定する項目です。推奨設定は**Block**です。理由は、他社の著作権の侵害を防ぐためです。
  - Allow
  公開コードと同じコードが提案される可能性があります。
  - Block
  Copilotがアレンジしたコードが提案されます。
- **Allow GitHub to use my code snippets for product improvements**
自分のコードをGitHub Copilotの学習データとして利用させるかどうかの設定です。この設定は、個人の好みやプライバシーによって設定してください。
  - チェックを入れる
  自分のコードがGitHubに送信されます。送信時のプライバシーなどは保証されるようです。
  - チェックを外す
  送信されません。

8. 準備が整いましたのような画面が表示されます。
![cop_kei7](/images/turtle-20240223-gitcopilot/cop_kei7.png =300x)

以上で、GitHub Copilot登録・契約手順は完了です。
次の項目で拡張機能のインストールについて説明します。

:::

:::details ③ 拡張機能インストール（クリックで開く）

### 拡張機能インストール

GitHub Copilotを利用するためには、まずエディタが必要になります。エディタはVisual Studio Code(VSCode)、Visual Studio、JetBrains、Neovimに対応しています。
そして、このエディタにGitHub Copilotのアプリケーションを拡張機能としてインストールすることで、使えるようになります。今回は、VSCodeを用いて、拡張機能のインストール手順を示します。

1. VSCodeを開き、拡張機能タブで「GitHub Copilot」を検索して、インストールします。
GitHub Copilotをインストールすると「GitHub Copilot Chat」も自動で一緒にインストールされます。
![cop_kei8](/images/turtle-20240223-gitcopilot/cop_kei8.png =250x)
インストールの仕方が分からない方は、次のサイトの手順を参考にしてみてください。
(参考URL) [拡張機能：インストール方法 (ブログ記事)](https://zenn.dev/safubuki/articles/turtle-20240121-vscode#%E6%8B%A1%E5%BC%B5%E6%A9%9F%E8%83%BD%EF%BC%9A%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%96%B9%E6%B3%95)
※こちらは、以前私が書いた記事になります🐢

1. インストールするとVSCodeの右下に、ポップアップで「GitHub Copilotとの連携認証」が表示されるので、クリックして認証画面を開き、承認します。

以上で、全ての導入手順は完了です。お疲れさまでした🎉

:::
::::

## 使い方の基本

この章では、GitHub Copilotの基本となる使い方を説明します。まず、GitHub Copilotの基本機能である3つの機能を紹介します。

- **インラインチャット**
- **コードサジェスチョン**
- **チャット**

これらの使い方を、Pythonのプログラムを実際に作成しながら、説明していきます。
そして、**ショートカットキー**や、目的の機能を簡単に呼び出すための**スラッシュコマンド**について説明を行います。

### 機能①：インラインチャット

インラインチャットとは、**コードを書いているファイルの中**でチャット機能を呼び出し、コードの生成や修正などを行う機能です。次のような開発シーンを想定して説明します。

1. プログラムのベースを新規作成
2. 部分的に処理を追加
3. 冗長な処理を修正

#### 1.プログラムのベースを新規作成

まず、ベースとなる「緑の円の中に、黄色い円を描画する」プログラムを新規作成します。

![cop_i_new](/images/turtle-20240223-gitcopilot/cop_i_new.gif =600x)
*(gif動画) 処理の新規作成*

pyファイルの中でインラインチャットが呼び出され、指示を行うことでプログラムが作成されました。行ったことを順に説明します。

1. pyファイル(circle.py)を作成します。
2. **Ctrl + I** (アイ) キーでインラインチャットを呼び出します。
コード上の✨**アイコン**をクリックでも、インラインチャットを呼び出すことができます。
![cop_i_star](/images/turtle-20240223-gitcopilot/cop_i_star.png)
*✨アイコン*
3. チャット欄に「緑の円の中に、黄色い円を描画するプログラムを作成して」と入力して、Enterキーを押します。
4. 候補となるプログラムが出力されるので、次の3つのボタンの中から1つを選択します。
![cop_i_btn](/images/turtle-20240223-gitcopilot/cop_i_btn.png)
*インラインチャット ボタン*
   - **Accept**：候補を受け入れて、提案を決定します
   - **Discard**:候補を受け入れず、提案を破棄します
   - **Regenerate**(矢印マーク)：別の候補を再度生成します
5. Acceptで提案を受け入れて確定し、ファイルを保存します。

ちなみに、作成したブログラムは、次のように期待する動作をします。
![cop_i_res](/images/turtle-20240223-gitcopilot/cop_i_res.png =350x)
*プログラム実行結果*

#### 2.部分的に処理を追加

ベースとなるプログラムに、さらに「赤い円を描画する」処理を追加します。

![cop_i_fix](/images/turtle-20240223-gitcopilot/cop_i_fix.gif =600x)
*(gif動画) 処理の追加*

赤い円を描画する処理が追加され、さらにメイン処理で描画処理を呼び出す箇所も追加されました。基本的な流れは「1.プログラムのベースを新規作成」と同じですが、**異なる点**があります。それは、インラインチャットを呼び出す前、**処理を追加する箇所にカーソルを移動**し、さらに**修正が必要なメイン処理も選択**している点です。こうすることで、必要な箇所に、必要な処理を追加することができます。

#### 3.冗長な処理を修正

円を描画するいくつかの関数ができましたが、これらは汎用性がなく冗長です。関数を一つにまとめて、汎用的でシンプルな処理に修正します。

![cop_i_imp](/images/turtle-20240223-gitcopilot/cop_i_imp.gif =600x)
*(gif動画) 処理の修正*

複数の円を描画する処理が削除され、代わりに円を描画する共通関数が追加されました。メイン処理のコール部分も、共通関数でコールされるようになりました。
今回は、**全体的に修正が必要**なので「2.部分的に処理を追加」ように**部分的な選択ではなく、全てを選択**してから、インラインチャットで指示を行います。

このように、インラインチャットで複数回指示をするだけで、円を描画するシンプルなプログラムを作成することができました。

### 機能②：コードサジェスチョン

コードサジェスチョンとは、コードを書いているときに、1行または複数行の**最適なコードを提案（サジェスチョン）する**機能です。これと似たような機能は、今までもありましたが、GitHub Copilotが優れているのは**精度の高さ**です。利用者のコーディング環境を学習をして、**コードの記述の仕方を合わせて**くれます。また、提案するコードも**期待するコードである割合が非常に高い**です。
それでは「赤い円を異なる箇所に3つ描画する処理」の追加をコードサジェスチョンで行ってみましょう。

![cop_s_1](/images/turtle-20240223-gitcopilot/cop_s_1.gif =600x)
*(gif動画) コードサジェスチョン*

このように、改行すると次から次にコードが提案されます。行ったことを順に説明します。

1. コメントで実行したい処理を記述します。
2. 目的の箇所で改行すると、薄い色の文字でコードが提案されます。
3. **TABキー**を押すと確定します。
4. 以降は、手順2と3を繰り返します。

なお、コードの提案が期待する内容ではなかった場合、**Ctrl + Enter キー**を入力することで、別の提案を一覧で表示することができます。期待する提案が一覧にあれば **Accept suggestion X ボタン**を押して、選択した提案を反映します。

![cop_c_list](/images/turtle-20240223-gitcopilot/cop_c_list.png =650x)
*Ctrl + Enterによる提案一覧*

今回は、コメントを記載して、分かりやすくサジェスチョンさせましたが、軽微な修正を行うときなどコメントを記載せずとも、期待する候補の提案も行ってくれるので、とても作業が捗ります。

### 機能③：チャット

チャットは、**エディタ上**でコードの生成や関数の説明、その他プログラム開発に関する質問など**自然言語により対話する**機能です。実際に対話を行いながらプログラムを作成した様子を示します。

![cop_c_1](/images/turtle-20240223-gitcopilot/cop_c_1.gif)
*(gif動画) チャット機能で対話によるプログラム作成*

インラインチャットで行った円を描画するプログラムの作成を、チャット機能でも同じように行うことができました。なお、チャット機能は、**エディタ左側のチャットタブ**を選択することで使うことができます。

![cop_c_0](/images/turtle-20240223-gitcopilot/cop_c_0.png =450x)
*チャット機能タブ*

作成したコードは、**Insert at Cursor ボタン**を押すことで、ファイルに簡単に反映することができます。

![cop_c_2](/images/turtle-20240223-gitcopilot/cop_c_2.png =450x)
*Insert at Cursor ボタンによる追加*

会話の話題を切り替えたときは、チャット画面上部の**＋のボタン**(New Chat)を押すことで、今までの会話をクリアして、新しく始めることができます。また、これまでの会話内容を確認したいときは、**時計マークのボタン**(Show Chats)を押すことで見ることができます。

![cop_c_btn](/images/turtle-20240223-gitcopilot/cop_c_btn.png =450x)
*新しい会話を始める・これまでの会話を表示する ボタン*

なお、チャット機能の注意点として、プログラミングに関する内容以外は受け付けてくれないことです。オススメの観光地は別のAIに聞いてください🙇‍♂️

![cop_c_kanko](/images/turtle-20240223-gitcopilot/cop_c_kanko.png =500x)
*オススメの観光地は教えてくれない*

このように、コード生成をサポートしてもらったり、困ったことを質問して解決したいときなどに、チャット機能は、素早くエディタ上で頼れる存在です。

### ショートカットキー

GitHub Copilotでは、次のショートカットキーを使うことができます。なお、詳細な使い方は、既に機能①～③の説明でgif動画を交えて触れていますので、そちらをご参照ください。ショートカットキーの一覧と内容を示します。

| ショートカットキー     | 内容                                                                 | よく使う(★) |
|---------------|--------------------------------------------------------------------|---------|
| Ctrl + I (アイ) | **インラインチャットを起動する**<br/>コーディングしているファイルの中で、<br/>チャットを起動し、コードの生成や質問ができる   | ★★★     |
| TAB           | **コードサジェスチョン（提案）を受け入れる**<br/>コーディングしているときに、<br/>提案してくるコードの案を受け入れて確定する  | ★★★     |
| ESC           | **コードサジェスチョン（提案）を拒否する**<br/>コーディングしているときに、<br/>提案してくるコードの案を拒否する        | ★★★     |
| Ctrl + Enter  | **コードサジェスチョン（提案）の一覧を表示する**<br/>コーディングしているときに、<br/>提案してくるコードの別案の一覧を表示する | ★★☆     |
| Alt + ]       | **次のコードサジェスチョン（提案）を表示する**                                              | ★☆☆（※）  |
| Alt + [       | **前のコードサジェスチョン（提案）を表示する**                                              | ★☆☆（※）  |

(参考URL) [GitHub Copilot の概要 (公式)](https://docs.github.com/ja/copilot/using-github-copilot/getting-started-with-github-copilot)
(※) 「次/前の提案を表示する」は、環境により動作しない可能性があります。

### スラッシュコマンド

GitHub Copilotには、目的の機能を簡単に呼び出し、素早く実行するために**スラッシュコマンド**があります。チャット欄に`/fix` や `/doc` などを入力するだけで、コード修正をしたり、関数の説明コメントを追加したりすることができます。コマンドの一覧を示し、よく使うものについてはさらに詳細な使い方の説明を行います。

#### コマンド一覧

スラッシュコマンドの一覧を示します。なお、項目の**機能①Inline**と**機能③Chat**については、それぞれ、**インラインチャット機能**と**チャット機能**を示しています。〇がついているものは、その機能のチャット欄から呼び出せるコマンドであることを表しています。

| コマンド名        | 内容                                                | 機能<br/>①<br/>Inline | 機能<br/>③<br/>Chat | よく使う(★) |
|--------------|---------------------------------------------------|:---------------------:|:-------------------:|---------|
| /fix         | 選択したコードの問題の修正案を提示する                               | 〇                   | 〇                 | ★★★     |
| /doc         | ドキュメンテーションコメント(※)を追加する<br/>(※) 関数等の概要や引数、戻り値のコメント | 〇                   |                   | ★★★     |
| /tests       | 選択したコードのテストコードを生成する                               | 〇                   | 〇                 | ★★★     |
| /explain     | 選択したコードの意味や動作を説明する                                | 〇                   | 〇                 | ★★☆     |
| /new         | 新しいワークスペースのファイル、コードを生成する                          |                     | 〇                 | ★★☆     |
| /newChat     | 新しいチャットを開始する                                      |                     | 〇                 | ★☆☆     |
| /help        | GitHub Copilotの使い方のヘルプを表示する                       |                     | 〇                 | ☆☆☆     |
| /api         | VS Codeの拡張開発について質問する                              |                     | 〇                 | ☆☆☆     |
| /newNotebook | 新しいJupyter Notebookを作成する                          |                     | 〇                 | －（※）    |

(※) /newNotebookコマンドについて、私がJupyter Notebookを使わないため無評価としました。ただ、Notebookを調べて、実際にコマンドを実行してみたところ、Jupyter Notebookを利用する方にとって、重宝しそうなコマンドだと思いましたので、補足いたします。

#### コマンドの詳細な使い方

一覧で示したコマンドのうち、**★が２つ以上**のよく使うものについて、詳細に説明します。

##### /fix

/fix は、選択したコードの問題の修正案を提示するコマンドです。構文のエラーやバグ、セキュリティのリスクなどを検出し、提案します。また、コードの効率や可読性を向上させるために、冗長な処理や不要な変数などを簡略化することもできます。例えば、`/fix 処理を簡略化して、変数xはリストにしてください` と入力すると、変数xをリストに変換するコード作成します。自身が認識していない問題があるか確認したい場合は **/fixのみ**を、修正方針などがある場合は、**/fix に続けて指示文を入力**する、というように使い分けてみてください。

![slash_fix](/images/turtle-20240223-gitcopilot/slash_fix.gif =600x)
*(gif動画) /fixコマンドによるコード修正提案*

##### /doc

/doc は、コードにドキュメンテーションコメントを追加するコマンドです。ドキュメンテーションコメントとは、関数やクラスの概要や引数、戻り値を説明するコメントのことです。なお、`/doc`のみを入力すると、**英語のコメント**が生成されますが、`/doc 日本語で`と入力すると、**日本語のコメント**が生成されます。
※ 環境によっては、`/doc`のみでも日本語のコメントが生成される場合があります。

![slash_doc](/images/turtle-20240223-gitcopilot/slash_doc.gif =600x)
*(gif動画) /docコマンドによるコメント追加*

##### /tests

/tests は、コードに対応するテストコードを生成するコマンドです。ユニットテストなどプログラムの品質を確認するためのテストケースを作成し、テストファイルに保存します。
`/tests`を入力すると、テストケースの一覧が表示されます。そして、**Create**をクリックすると、テストファイルが生成されます。**/tests の後に指示文を入力する**と、テストケースの数や内容をカスタマイズすることができます。例えば、`/tests 複数` と入力すると、必要な複数のテストケースが作成されます。

![slash_tests](/images/turtle-20240223-gitcopilot/slash_tests.gif =600x)
*(gif動画) /testsコマンドによるテストコード作成*

##### /explain

/explain は、コードの意味や動作を分かりやすく説明するコマンドです。自分でプログラムを作成するときは、あまり必要ないかもしれませんが、他の人が作成したプログラムを読む際に、コメントがない、処理のロジックがわからないなどの場合に便利なコマンドです。`/explain`のみを入力すると、**英語で説明**が表示されますが、`/explain 日本語で`と入力すると、**日本語で説明**が表示されます。

![slash_explain](/images/turtle-20240223-gitcopilot/slash_explain.gif)
*(gif動画) /explainコマンドによる関数の説明*

##### /new

/new は、新しいワークスペースのファイルやコードを生成するコマンドです。指示文に従って、ワークスペースのフォルダ構成やファイル名、各ファイルのコード内容を作成します。例えば、`@workspace /new Python TCP通信を行うアプリケーション テストフォルダを用意する`と入力すると、TCP通信を行うアプリケーションのファイルやテストフォルダを生成します。なお、チャット欄に`/new`と入力すると、自動的に`@workspace /new`と補完され、ワークスペースに対するコマンドになります。新しいプロジェクトを始めるときに使ってみてください。

![slash_new](/images/turtle-20240223-gitcopilot/slash_new.gif)
*(gif動画) /newコマンドによる新しいワークスペース作成*

### コンテキスト変数

特定のファイルやコードの一部を指定して、より具体的で関連性の高い回答を得るために**コンテキスト変数**があります。チャット欄に`#file` や `#selection`、`#terminalSelection` などを入力して、情報を与えることで利用できます。私は、Copilotを用いたAIコーディングで、このコンテキスト変数を本当によく使います。スラッシュコマンド同様、一覧を示し、よく使うものについてはさらに詳細な使い方の説明を行います。

#### 変数一覧

コンテキスト変数の一覧を示します。

| 変数名                  | 内容                                              | よく使う(★) |
|----------------------|-------------------------------------------------|---------|
| #selection           | アクティブなエディタのカーソル選択した範囲                           | ★★★     |
| #terminalSelection   | アクティブなターミナルのカーソル選択した範囲                          | ★★★     |
| #file                | ワークスペース内の選択したファイル                               | ★★☆     |
| #editor              | アクティブなエディタ                                      | ★☆☆     |
| #terminalLastCommand | アクティブなターミナルの最後実行したコマンド                          | ★☆☆     |
| #vscodeApi           | VS Code APIリファレンスを使用し、<br/>VS Code拡張開発に関する質問に回答 | ☆☆☆     |

#### 変数の詳細な使い方

一覧で示したコマンドのうち、**★が２つ以上**のよく使うものについて、詳細に説明します。

##### #selection

#selectionは、アクティブなエディタでカーソル選択した範囲を示す変数です。エディタ上でコード選択し、`#selection 処理内容を説明してください`や`#selection 処理を簡略化してください`と入力することで、選択範囲のコードについてのみ説明や修正を行うことができます。

![selection](/images/turtle-20240223-gitcopilot/selection.gif)
*(gif動画) /selectionによる選択範囲の説明*

なお、300行程度のコードは省略せずに回答されますが、それ以上の長いコードでは説明が一部省略されることがあります。長いコードは数関数ずつに分けて選択し、回答を得るようにしてください。

##### #terminalSelection

#terminalSelectionは、アクティブなターミナルでカーソル選択した範囲を示す変数です。VSCodeでは`Ctrl + @`でターミナルを起動できます。この変数は、プログラム実行時にエラーが発生するシーンでよく利用します。ターミナルに表示されたエラーを選択し、`#terminalSelection エラーの原因と対策を教えてください`と入力すると、エラーの原因と対策を教えてくれます。

![terminal_selection](/images/turtle-20240223-gitcopilot/terminal_selection.gif)
*(gif動画) /terminalSelectionによるエラー原因と対策*

インターネット等でエラーコードを検索するよりも速く、エラー解決の糸口を得ることができます。本当によく使うオススメの変数です。

##### #file

#fileは、ワークスペース内で選択したファイルを示す変数です。ファイルの概要や関数の一覧、ファイル同士の関係性を知りたいときに便利です。例えば、`#file:sample.py ファイルの概要と関数の一覧を示してください`や`#file:kame.py #file:turtle.py これらのファイルの関係性を示してください`と入力します。

![file](/images/turtle-20240223-gitcopilot/file.gif)
*(gif動画) /fileによるファイルの説明*

巨大なファイルの場合、一部回答が省略されることがあります。その場合は、ファイルを開いて#selectionで少しずつ回答を得るようにしてください。

お疲れさまでした！以上で、使い方の基本の説明を終わります。
ここまでの内容を読めば、GitHub Copilotの使い方はマスターできていると思います👍
ですが、注意して使うことがあるため、よろしければ次の章も読んでみてください。

## 注意すべきポイント

ここまで、Github Copilotのメリットや魅力的な機能を紹介してきましたが、その使用にあたっては注意も必要です。ここではそのポイントを説明します。

### 推奨言語以外では期待する結果が得られない可能性がある

GitHub Copilotの公式サイトによると、次の言語での使用が推奨されています。

- Python
- JavaScript
- TypeScript
- Ruby
- Go
- C#
- C++

その理由は、これらの言語が多くのプロジェクトや開発者に使われており、Copilotの学習データにも多く含まれているからです。他の言語でも使用できますが、期待する結果が得られないことがあります。

(参考URL) [GitHub Copilot の概要 (公式)](https://docs.github.com/ja/copilot/using-github-copilot/getting-started-with-github-copilot)

### 古いライブラリやAPIが提案されることがある

GitHub Copilotは、過去のコードから学習しているため、場合によっては古い情報に基づいた提案をすることがあります。例えば、PDFをテキストに変換するアプリを生成した際に、次のようなエラーが出力されることがありました。

> PyPDF2.errors.DeprecationErrorreader.numPages is deprecated and was removed in PyPDF2 3.0.0. Use len(reader.pages) instead.

提案されたコードは、古いバージョンのAPIを使用していました。なお、エラーが発生した場合、開発者は手動で修正してもよいですが、Copilotに任せて`/fix`コマンドに**エラー情報を指示文として与えて修正**することで、対応できる場合があります。

### Copilotはあくまで副操縦士である

GitHub Copilotはあくまで副操縦士です。これまで示したようにAIは完ぺきではないため、提案されたコードは必ず確認し、問題がないか自身でチェックすることが大切です。また、プログラミングの基本知識やスキルの習得も欠かせません。

これらのポイントを押さえて、GitHub Copilotを活用してください。

以上が、注意すべきポイントの紹介でした。
始めたばかりの方や、まずは基本をおさえたいという方は、ここまでの内容でも十分です👍
一旦、復習のために、今までの内容を振り返りながら、実際に触ってみるのも良いと思います。

次の章では少し、発展的な内容を説明します。
引き続き興味がある方は、ご覧ください。

## 品質向上のポイント

GitHub Copilotを使ったコーディングで効率よく、品質を向上させるために静的解析ツールなど従来の手法を組み合わせることが有効です。次に代表的なツール、手法を紹介します。

![syuhou](/images/turtle-20240223-gitcopilot/syuhou.png)
*品質を高めるツール・手法*

これらは、コードの一貫性を保ち、潜在的なエラーやバグを事前に検出するのに役立ちます。実際の活用方法については、私が書いた記事にまとめておりますので、もしよろしければ見てみてください。

https://zenn.dev/safubuki/articles/turtle-20240215-pymind

なお、内容はPython言語で説明していますが、他の言語にも同様の仕組みがあります。

### Copilotでさらに便利に

静的解析ツールによる指摘への対応や、型ヒントの対応は、意外と時間がかかります。そこで、GitHub Copilotを活用することで、効率的に対応を行うことができます。

#### 静的解析ツールの指摘修正

静的解析ツールには、Quick Fixという指摘内容を簡単に修正する仕組みがあります。便利な機能ですが、GitHub Copilotが導入されていない環境では、静的解析ツールの指摘は表示されても、修正案が得られないケースがあります。このようなときは、時間をかけてWebなどで調べてから、対応する必要が出てきます。

![quick_fix_none](/images/turtle-20240223-gitcopilot/quick_fix_none.png =600x)
*GitHub Copilot未導入時のQuick Fix*

しかし、GitHub Copilotが導入されていると、次のように**Quick Fix**が表示されます。これを選択すると`Fix using Copilot`という、Copilotで修正する選択肢が出てきます。さらに選択をするとGitHub Copilotによって、修正の提案が行われます。

![quick_fix](/images/turtle-20240223-gitcopilot/quick_fix.gif =600x)
*(gif動画) GitHub Copilot導入済のQuick Fix*

#### 型ヒントの追加

型ヒントも便利な仕組みですが、コーディングする際にヒントを書く作業は、以外と手間と時間がかかります。しかし、Copilotならコードの構文などを解析して、より正確に型ヒントを追加することができます。方法は、今まで説明してきたインラインチャットを使い、対象の関数を選択してから「型ヒントを追加してください。必要に応じてtypingをインクルードしてください。」と指示をするだけです。

![type_hint](/images/turtle-20240223-gitcopilot/type_hint.gif =600x)
*(gif動画) GitHub Copilotによる型ヒントの追加*

GitHub Copilotは、従来のツールや手法を組み合わせることで、より品質の高いプログラムを作成することができます。ぜひ、この方法を活用してみてください。

以上で全ての説明は完了となります！
本当にお疲れさまでした🎉

## まとめ

いかがでしたでしょうか？
GitHub Copilotを使ってみたい、これなら使えそうだ！と思っていただけたでしょうか。少しでも、この記事を読んでくださった方に、そう思っていただけたなら幸いです。 もし、分からないことや、分かりにくい部分がありましたら遠慮なくコメント欄に書き込んでください。🐢

私は、GitHub Copilotを使い始めたその日から、その魅力に魅了されました。他にも多くの詳細な記事がありますが、私の経験を通じて、私の言葉で、皆さんにその魅力を伝えたいと思い、この記事を書きました。このブログが、皆さんの開発に少しでも役立つことを願っています。

最後まで読んでいただき、ありがとうございました！

## リンク

これら記事では、たった一枚の画像からAIを活用して、3Dプリンタでリアルな造形物を作成する技術を紹介しています。外側のリアルな部分はリンク先の記事の内容で、内側のソフトウェアはGitHub Copilotを使って開発することで、近い将来、AIだけで家電のようなモノづくりができるかもしれません。そんな未来に興味がある方は、ぜひ記事を読んでみてください👍

**Tripo 2.0**は、TripoSRの後継モデルで、劇的に精度が向上しました。モノづくり、ゲーム、VRなど幅広い分野に広がりそうな勢いを感じました。進化が止まりません！
https://zenn.dev/safubuki/articles/turtle-20240929-tripo2-evo

**Stable Fast 3D**は、TripoSRの後継モデルで、さらに素早くキレイな3Dデータを生成できるようになりました。AIの世界は進化がすごいです。
https://zenn.dev/safubuki/articles/turtle-20240803-stable-fast

**TripoSR**は、少し古い技術になりましたが、インプット画像生成のコツや成功・失敗事例なども記載しています。参考になる部分もいろいろあります。
https://zenn.dev/safubuki/articles/turtle-20240721-tripo-3dp

## 更新履歴

- **2024/03/04**
  説明に使用した一部の画像やgif動画の文字が見づらいため、画像サイズを大きくしました。

- **2024/07/10**
  コンテキスト変数の説明を追加しました。

- **2024/08/02**
  記事紹介のリンクを追加し、AI関連のTripoSRの記事を紹介しました。

- **2024/08/04**
  AI関連のStable Fast 3Dの記事を追加し、説明文を追加修正しました。

- **2024/09/30**
  Tripo 2.0リンク及び、説明文を追加しました。
