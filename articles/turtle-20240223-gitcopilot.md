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

このブログでは、GitHub Copilotが初めてという方のために**使い方の基本**や**便利な使い方**を図解と例を交えながら丁寧に説明し、**品質向上のポイント**など少し発展した内容も紹介します。このブログを読んで、GitHub Copilotの魅力を感じてみてください👍

また、**2025年5月**に本ブログの内容を大幅に見直しました！ GitHub Copilotの料金プランが新しくなり、選べるAIモデルの種類も増え、さらに「**プレミアムリクエスト**」という新しい仕組み（こちらは2025年6月4日から課金開始予定です）も登場しています。これらの最新情報を分かりやすく解説していますので、ぜひチェックしてみてください。
※2025/5/31に「エディタ上でのAgentモード利用とプレミアムリクエスト消費の考え方」についても追加しました。

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

## ブログの構成

このブログは、大きく分けて6つの章から成ります。各章の概要については、以下の図をご覧ください。

![blog_struct](/images/turtle-20240223-gitcopilot/blog_struct.png)

`New`や`Update`のマークが付いた項目は、GitHub CopilotやVSCodeの更新に伴い、2024年11月に本ブログを大幅に追加・更新した部分です。これまでにこのブログをご覧になった方も、ぜひ再度ご確認してみてください。

## GitHub Copilotとは

GitHub Copilotは、AIがコードを自動的に生成し、開発者の生産性を向上させる画期的なツールです。それでは、GitHub Copilotの機能の一覧と利用することによるメリットを見ていきましょう。

### 機能一覧

GitHub Copilotには、多くの機能がありますが、その中でも代表的な機能の一部を紹介します。

![func_list](/images/turtle-20240223-gitcopilot/func_list.png)
*GitHub Copilot機能一覧(代表例)*

コーディングに必要な各種機能が組み込まれており、AIの力を借りて効率的かつスムーズに開発を進めることができます。何だかワクワクしてきませんか？これらの機能を使ってみたくなったでしょうか。

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

GitHub Copilotを始めてみたいけれど、料金プランや導入方法が気になる方もいらっしゃるのではないでしょうか。
GitHub Copilotには、手軽に試せる無料の**Freeプラン**（AIモデルや使用回数に制限あり）や、より多機能な**有償プラン**があります。学生や教員、対象OSSのメンテナーの方向けの無料特典も利用可能です。この章では、これらの導入方法について説明します。

なお、既に導入済みの方や、企業などの組織で利用手順が別途定められている場合は、**この章をスキップ**して構いません。

この章では、これからGitHub Copilotを個人で使ってみようという方を対象にしています。必要に応じて「**GitHub Copilotの導入手順**」の各項目をクリックして、詳細をご確認ください。

::::message
**GitHub Copilotの導入手順**
:::details ① アカウント作成（クリックで開く）

### アカウント作成

GitHub Copilotの利用には、**GitHub**のアカウント作成が必要になります。既にGitHubアカウントを保持されている方は、スキップしてください。
ちなみに、GitHubは、web上にプログラムコードを保存し、バージョン管理やメンバで共有するためのサービスです。こちらも開発には無くてはならないものですから、まだの方は、この機会に個人のGitHubアカウントを作成しましょう。

1.  GitHubのサイトにアクセスします。
    [https://github.com/](https://github.com/)
2.  ページ右上のSign upをクリックします。
    ![hub_page](/images/turtle-20240223-gitcopilot/hub_page.png =400x)
3.  メールアドレスやパスワードなど必要事項を入力します。
    ![hub_regist](/images/turtle-20240223-gitcopilot/hub_regist.png =400x)
4.  メールが送られてきますので、必要な対応を行って、アカウント作成完了となります。

※ ここで示している入力画面は一例です。実際の画面とは細部が異なる場合がありますが、同様の情報（メールアドレス、パスワードなど）を入力してアカウントを作成する流れとなります。
※ 私は、途中まで入力していますが、実際の登録は行っていません。
　 個人が無料のアカウントを複数持つことは利用規約違反となるためです。
　 個人用、業務用(有償organization所属)をそれぞれ分けて使うのは問題ないようです。
　 (参考URL)[複数のGitHubアカウントを保持していいの？GitHubサポートに問い合わせてみた](https://www.timedia.co.jp/tech/20221025-tech/)
:::

:::details ② 料金プラン（クリックで開く） ★ 2025.5.14 Update ★

### 料金プラン

GitHub Copilotを利用するには、いくつかの料金プランがあります。ご自身の使い方に合わせて最適なプランを選ぶことができます。以下に主なプランをご紹介します。（2025年5月現在）

| プラン名          | 月額料金（1ユーザー） | 年額料金（1ユーザー） | 主な対象ユーザー                                 | 月間プレミアムリクエスト目安 |
| ----------------- | ------------------- | ------------------- | ------------------------------------------------ | -------------------------- |
| **Copilot Free** | 無料                | -                   | 個人開発者（機能・利用回数制限あり）             | 50回                       |
| **Copilot Pro** | \$10                | \$100               | 個人開発者                                       | 300回                      |
| **Copilot Pro+** | \$39                | \$390               | 高度なAIモデルや機能を求める個人開発者             | 1,500回                    |
| **Copilot Business**| \$19                | -                   | 企業、チーム                                     | 300回/ユーザー             |
| **Copilot Enterprise**| \$39                | -                   | 大規模組織（高度なセキュリティと管理機能が必要） | 1,000回/ユーザー           |

**各プランの主な特徴：**

* **Copilot Free**:
    * 基本的なコード補完やチャット機能を限定的にお試しいただけます。
    * 月間の利用回数には制限があります。
* **Copilot Pro**:
    * 個人開発者向けの標準プランで、コード補完やチャット機能を存分に利用できます。
    * VS CodeやJetBrains製IDEなど、多くのエディタに対応しています。
    * **無料対象**: 認証済みの学生、教師、人気のあるオープンソースプロジェクトのメンテナーの方は、Proプランを無料で利用できる場合があります。
* **Copilot Pro+**:
    * Proプランの全機能に加え、より多くの「プレミアムリクエスト」と、GPT-4.5のような最新・高性能なAIモデルへのアクセスが可能です。
    * より複雑なコード生成や高度な機能を求める個人の方におすすめです。
* **Copilot Business**:
    * チームや小〜中規模の組織での利用に適したプランです。
    * Copilot Proの全機能に加え、ユーザー管理機能、組織内での利用ポリシー設定、利用状況の監査ログ、組織向けの保護機能などが提供されます。
    * 組織のセキュリティとプライバシーに配慮し、コードスニペット（コードの断片）が製品改善のために収集されないように設定できます。
* **Copilot Enterprise**:
    * 大規模な組織向けの最上位プランです。
    * Copilot Businessの全機能に加え、組織が持つ独自のコードベースやドキュメントを学習させ、より組織の状況に合わせたカスタマイズされたコード提案や回答を得られます。
    * プロジェクトごとのコーディング規約設定や、さらに高度なセキュリティ機能が利用可能です。
    * GitHub Enterprise Cloudとの連携が前提となります。

**プレミアムリクエストについて：**

2025年6月4日以降に、「プレミアムリクエスト」という仕組みが導入されます。これは、標準のAIモデルよりもさらに高性能なAIモデル（例えばGPT-4.5やClaude 3.7 Sonnetなど）をチャットなどで利用する際に消費される、ポイントのようなものです。各プランには毎月一定数のプレミアムリクエストが付与されており、より高度なAIの力を活用できます。Pro+以上のプランでは追加購入も可能です。**このプレミアムリクエストの詳細については、後述の章で改めて詳しくご説明します。**

**契約にあたっての注意点：**

* 上記の情報は、本ブログ執筆時点（2025年5月）のものです。料金やプラン内容は変更される可能性があるため、契約前には必ず[GitHub Copilotの公式サイト](https://github.com/features/copilot/plans)で最新情報をご確認ください。
* GitHub Copilotで生成されたコードは、必ずご自身で内容を確認し、プロジェクトの要件やセキュリティに適合しているか検証することが大切です。
* 無料トライアルについては、期間終了後に自動で有料プランに移行する場合があるため、利用規約をよく確認し、必要に応じて事前に解約手続きを行ってください。

**GitHub Copilot登録・契約手順：**

1.  githubサイトにアクセスしてサインインします。
2.  画面右上のアイコンをクリックして、メニュー一覧を表示します。
    ![cop_kei1](/images/turtle-20240223-gitcopilot/cop_kei1.png =300x)
3.  メニュー一覧からCopilotを選択します。
    ![cop_kei2](/images/turtle-20240223-gitcopilot/cop_kei2.png =200x)
4.  その後は画面の指示に従い、ご希望のプランを選択（トライアルで始める場合は月額プランを選択しておくと安心です）、支払い情報（クレジットカードまたはPayPal）の入力、公開コードの提案範囲や自身のコードスニペットの製品改善への利用許可などのアカウント設定を行い、登録を完了します。

    詳細な手順や画面は変更される可能性があるため、公式サイトの指示に従って進めるのが最も確実です。

:::

:::details ③ 拡張機能インストール（クリックで開く）

### 拡張機能インストール

GitHub Copilotを利用するためには、まずエディタが必要になります。エディタはVisual Studio Code(VSCode)、Visual Studio、JetBrains、Neovimに対応しています。
そして、このエディタにGitHub Copilotのアプリケーションを拡張機能としてインストールすることで、使えるようになります。今回は、VSCodeを用いて、拡張機能のインストール手順を示します。

1.  VSCodeを開き、拡張機能タブで「GitHub Copilot」を検索して、インストールします。
    GitHub Copilotをインストールすると「GitHub Copilot Chat」も自動で一緒にインストールされます。
    ![cop_kei8](/images/turtle-20240223-gitcopilot/cop_kei8.png =250x)
    インストールの仕方が分からない方は、次のサイトの手順を参考にしてみてください。
    (参考URL) [拡張機能：インストール方法 (ブログ記事)](https://zenn.dev/safubuki/articles/turtle-20240121-vscode#%E6%8B%A1%E5%BC%B5%E6%A9%9F%E8%83%BD%EF%BC%9A%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%96%B9%E6%B3%95)
2.  インストールするとVSCodeの右下に、ポップアップで「GitHub Copilotとの連携認証」が表示されるので、クリックして認証画面を開き、承認します。

以上で、全ての導入手順は完了です。お疲れさまでした🎉

:::
::::

## 使い方の基本

この章では、GitHub Copilotの基本的な使い方を説明します。初めての方は、まずここで紹介する3つの基本機能から試してみることをお勧めします。これらの機能を使いこなすことで、GitHub Copilotの便利さを実感できると思います。

- **インラインチャット**
- **コードサジェスチョン**
- **チャット**

これらの使い方を、Pythonのプログラムを実際に作成しながら、説明していきます。

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

チャットは、**エディタ上**でコードの生成や関数の説明、その他プログラム開発に関する質問など**自然言語により対話する**機能です。チャット機能は、**エディタ上部の検索バー右横のCopilotボタン**をクリックすることで使うことができます。

![new_cop_start](/images/turtle-20240223-gitcopilot/new_cop_start.png)
*Copilot ボタン*

起動すると、エディタ右側のセカンダリサイドバーにチャット欄が表示されます。以前から使っている方は、位置が移動して最初は慣れないかもしれませんが、慣れてくるとチャット欄を常時表示したままファイル操作やソース管理ができるため、とても便利です。

![new_cop_start](/images/turtle-20240223-gitcopilot/new_cop_sec.png)
*チャット欄のセカンダリサイドバー表示*

実際に対話を行いながらプログラムを作成した様子を示します。インラインチャットで行った円を描画するプログラムの作成を、チャット機能でも同じように行うことができました。

![cop_c_1](/images/turtle-20240223-gitcopilot/new_cop_turtle.gif)
*(gif動画) チャット機能で対話によるプログラム作成*

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

## 便利な使い方

まずは、「使い方の基本」で紹介した機能を、自然な言葉で試してみてください。そして、これらの基本機能に慣れてきたら、次に示す「便利な使い方」にも挑戦してみてください。より効率的に、目的に応じた使い方ができるようになります。

- ショートカットキー
- チャットパーティシパンツ（Chat Participants）
- スラッシュコマンド（Slash Commands）
- コンテキスト変数（Context Variables）
- AIモデルの選択

これらを活用することで、さらにGitHub Copilotが身近な存在になると思います。

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

### チャットパーティシパンツ（Chat Participants）

チャットパーティシパンツは、日本語では「チャット参加者」と訳されます。解説サイトによっては、エージェントと呼ばれることもあります。チャット欄に`@workspace`や`@terminal`のようなタグを入力し、その後に続く指示を行うことで、ワークスペースやターミナルなど特定の内容について質問を行うことができます。このタグ付けを行うことで、質問の範囲を広げ、より良い回答を得ることができます。

※「Chat participants」という表記は、GitHub DocsやVSCode拡張機能「GitHub Copilot Chat」の説明に基づいています。
(参考URL) [GitHub Docs - Chat participants (公式)](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide#chat-participants)

#### タグ一覧

チャットパーティシパンツのタグ一覧を示します。

| 変数名        | 内容                              | よく使う(★) |
|------------|---------------------------------|---------|
| @workspace | ワークスペース全体に関する質問をする。          | ★★★     |
| @terminal  | ターミナルでの操作に関する質問をする。          | ★★☆     |
| @vscode    | Visual Studio Codeに関する質問をする。 | ★★☆     |
| @github    | GitHubに関する質問をする。             | ★☆☆     |

#### タグの詳細な使い方

一覧で示したタグに付いて、詳細に説明します。

##### @workspace

@workspaceは、ワークスペース全体に関する質問を行うためのタグで、私が最もよく使うタグです。例えば、`@workspace フォルダ、ファイルを一覧にして項目ごとに分類して説明し、全体の目的を教えて下さい。` と入力します。すると、まずワークスペース全体の情報を収集し、その後に指示内容を実行して、各ファイルの説明とワークスペースの目的を教えてくれます。

![pat_workspace](/images/turtle-20240223-gitcopilot/pat_workspace.gif)
*(gif動画) @workspaceによるワークスペースの解説*

さらに、`@workspace UI処理を別ファイルで行いたい。`と入力すると、ワークスペースからUI処理を探し出し、処理を別ファイルで行う提案を行ってくれます。

![pat_workspace_ui](/images/turtle-20240223-gitcopilot/pat_workspace_ui.png =600x)
*ワークスペースの情報収集と処理提案*

このタグのポイントは、まずワークスペース全体の情報を収集することです。これにより、精度の高い回答を得ることができます。

GitHub CopilotのAIモデルがGPT-3の頃は、扱える情報量が少なく、あまり利用することはありませんでした。しかし、現在はAIモデルがGPT-4oになり、扱える情報量が大幅に増え、精度が向上したため、とてもよく使うようになりました。

##### @terminal

@terminalは、ターミナルでの操作に関する質問をする際に使用します。例えば、`@terminal ディスクの使用状況を表示したい`や`@terminal ubuntuでフォルダの一覧を示して、特定のフォルダを削除したい`と入力すると、目的のターミナルコマンドを教えてくれます。コマンドを忘れてしまったときにとても便利です。

![pat_terminal](/images/turtle-20240223-gitcopilot/pat_terminal.png =500x)
*ターミナルコマンドの提示*

##### @vscode

@vscodeは、Visual Studio Codeに関する質問をする際に使用します。例えば、`@vscode ターミナルを開きたい`や`@vscode フォントサイズを16に設定したい`と入力すると、Visual Studio Codeに関する具体的な回答を得ることができます。

![pat_vscode](/images/turtle-20240223-gitcopilot/pat_vscode.png)
*vscodeの回答*

##### @github

@githubは、GitHubに関する質問をする際に使用します。例えば、`@github codespaceについて教えてほしい`や`@github コミットをリバートする方法を知りたい`と入力することで、具体的な回答を得ることができます。ただし、`@github`を使わなくても似たような回答を得られるため、現状では使い方を模索している段階です。良い利用方法が見つかりましたら、ブログで更新します。

### スラッシュコマンド（Slash Commands）

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
| /help        | GitHub Copilotの使い方のヘルプを表示する                       |                     | 〇                 | ★☆☆     |
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

### コンテキスト変数（Context Variables）

特定のファイルやコードの一部を指定して、より具体的で関連性の高い回答を得るために**コンテキスト変数**があります。チャット欄に`#file` や `#selection`、`#terminalSelection` などを入力して、情報を与えることで利用できます。私は、Copilotを用いたAIコーディングで、このコンテキスト変数を本当によく使います。スラッシュコマンド同様、一覧を示し、よく使うものについてはさらに詳細な使い方の説明を行います。

#### 変数一覧

コンテキスト変数の一覧を示します。

| 変数名                  | 内容                                              | よく使う(★) |
|----------------------|-------------------------------------------------|---------|
| #selection           | アクティブなエディタのカーソル選択した範囲                           | ★★★     |
| #terminalSelection   | アクティブなターミナルのカーソル選択した範囲                          | ★★★     |
| #file                | ワークスペース内の選択したファイル                               | ★★☆     |
| #codebase            | プロジェクト全体のコード                                  | ★★☆     |
| #editor              | アクティブなエディタ                                      | ★☆☆     |
| #terminalLastCommand | アクティブなターミナルの最後実行したコマンド                          | ★☆☆     |
| #vscodeApi           | VS Code APIリファレンスを使用し、<br/>VS Code拡張開発に関する質問に回答 | ☆☆☆     |

#### 変数の詳細な使い方

一覧で示したコマンドのうち、**★が２つ以上**のよく使うものについて、詳細に説明します。

##### #selection

#selectionは、アクティブなエディタでカーソル選択した範囲を示す変数です。エディタ上でコード選択し、`#selection 処理内容を説明してください`や`#selection 処理を簡略化してください`と入力することで、選択範囲のコードについてのみ説明や修正を行うことができます。

![selection](/images/turtle-20240223-gitcopilot/selection.gif)
*(gif動画) #selectionによる選択範囲の説明*

なお、300行程度のコードは省略せずに回答されますが、それ以上の長いコードでは説明が一部省略されることがあります。長いコードは数関数ずつに分けて選択し、回答を得るようにしてください。

##### #terminalSelection

#terminalSelectionは、アクティブなターミナルでカーソル選択した範囲を示す変数です。VSCodeでは`Ctrl + @`でターミナルを起動できます。この変数は、プログラム実行時にエラーが発生するシーンでよく利用します。ターミナルに表示されたエラーを選択し、`#terminalSelection エラーの原因と対策を教えてください`と入力すると、エラーの原因と対策を教えてくれます。

![terminal_selection](/images/turtle-20240223-gitcopilot/terminal_selection.gif)
*(gif動画) #terminalSelectionによるエラー原因と対策*

インターネット等でエラーコードを検索するよりも速く、エラー解決の糸口を得ることができます。本当によく使うオススメの変数です。

##### #file

#fileは、ワークスペース内で選択したファイルを示す変数です。ファイルの概要や関数の一覧、ファイル同士の関係性を知りたいときに便利です。例えば、`#file:sample.py ファイルの概要と関数の一覧を示してください`や`#file:kame.py #file:turtle.py これらのファイルの関係性を示してください`と入力します。

![file](/images/turtle-20240223-gitcopilot/file.gif)
*(gif動画) #fileによるファイルの説明*

また、`#file`と似た「**ファイルをコンテキストとしてアタッチする**」という機能もあります。ファイルを選択してチャット欄にドラッグ&ドロップするだけで簡単に利用できます。以下の動画でその使い方を確認できます。

![cop_file_attach](/images/turtle-20240223-gitcopilot/cop_file_attach.gif)
*(gif動画) ファイルをコンテキストとしてアタッチする*

一見すると、`#file`とこの機能はほぼ同じように見えるかもしれません。しかし、`#file`はプロンプト内で変数として使用できる点が異なります。例えば、`#file:test_kame.pyと同じような形式でmockを利用し、#file:test_turtle.pyにテストケースを追加してください`というように使います。

どちらの機能も似たようなシーンで使えるため、使いやすい方を選んで利用すると良いと思います。

なお、巨大なファイルなど情報量が多すぎる場合、一部の回答が省略されることがあります。その際は、ファイルを開いて`#selection`を使い、少しずつ回答を得るようにしてください。

##### #codebase

#codebaseは、プロジェクト全体のソースコードを示す変数です。プロジェクト内の実装詳細や具体的な使用例を調べるのに有効です。例えば、`#codebase Turtleメソッドの使用例と呼び出し元を教えてください`というように使います。このコマンドはワークスペース全体の情報を収集してから実行されます。

![cop_codebase](/images/turtle-20240223-gitcopilot/cop_codebase.gif)
*(gif動画) #codebaseによるメソッドの検索・利用方法*

このコマンドは、`@workspace`と似ていますが、次のように使い分けると良いと思います。

- **#codebase**: コードの実装や機能に関する質問をするときに使用。
  - 例: メソッドの使用例、実装パターンの検索、コール方法など。
- **@workspace**: 開発環境の構造や設定に関する質問をするときに使用。
  - 例: フォルダ構成、設定ファイルの配置、プロジェクト構成など。

（注：ここでの「プロジェクト」はソフトウェア開発のためのソースと関連ファイルの集合体を、「ワークスペース」は複数のプロジェクトを含む開発者の作業環境を指します。）

### AIモデルの選択
**★ 2025.5.14 Update ★**

GitHub Copilotの特に魅力的な機能の一つとして、特性の異なる様々なAIモデルを利用できること、そして、それらをチャット画面ですぐに切り替えて使い分けられる点が挙げられると、私は感じています。

以前、AIが時折見せるハルシネーション（実際には存在しないことを本当のように述べる）への対策として、私は複数のモデルで結果を比較し、情報の正確性を確認する「セカンドオピニオン」的な使い方をすることがありました。

しかし、昨今のAIモデルの進化は本当に目覚ましく、特に高性能なモデルではハルシネーションもかなり低減されてきました。そのため、AIモデル間のクロスチェックの必要性は相対的に下がり、それぞれのAIモデルが持つ個性や得意分野を理解し、**目的に応じて使い分けることの重要性**が高まってきたと思います。例えば、いつものコーディング作業やドキュメントの生成、ちょっとした質問にはバランス・汎用型のモデルを選び、複雑なコードや高度な分析・提案を求める際には高性能・推論型のモデルを選ぶ、というように使い分けができます。

もちろん、あるモデルでは解決が難しい課題に対して別のモデルのアプローチを試したり、多角的な視点を得るためのセカンドオピニオンとして活用したりといった、**AIモデル間の相互補完的な役割**は依然として大切です。

それでは、チャット欄にある選択欄から、使いたいAIモデルを選んでみてください。

![ai_models](/images/turtle-20240223-gitcopilot/ai_models.png)
*AIモデルの選択*

※ 個人契約の方は、同意にOKするとすぐに使えますが、企業などでEnterpriseライセンスを利用している方は、Organization管理者が有効設定していないと使えません。もし使えない場合は、管理者に問い合わせてください。

利用可能なAIモデルの主な特徴は次の通りです。

**GitHub Copilot 主要AIモデルの開発元・タイプ・特徴**

| AIモデル名                     | 開発元    | タイプ        | 特徴                                                                                                                                                                |
| ------------------------------ | --------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GPT-4.1 (ベースモデル)         | OpenAI    | バランス・汎用  | GitHub Copilotの現デフォルトベースモデル。コーディング支援からチャットまで広範なタスクに対応し、GPT-4oから推論能力・理解力が向上。                                                    |
| Claude 3.5 Sonnet              | Anthropic | バランス・汎用  | Anthropic社のClaude 3ファミリーモデル。知能・速度・コストのバランスに優れ、特に長文理解、コンテンツ生成、コーディング支援で高性能を発揮。                                                |
| Claude 3.7 Sonnet              | Anthropic | バランス・汎用  | Claude 3.5 Sonnetの後継または上位版。高速性と知能のバランスを重視しつつ、さらなる性能向上や新機能の追加が見込まれる。                                                                  |
| Claude 3.7 Sonnet Thinking     | Anthropic | 高性能・推論    | Claude 3.7 Sonnetをベースに対話と思考プロセス、複雑な指示への応答、推論能力を強化。深い理解や多角的な検討が求められるタスク向け。                                                          |
| Gemini 2.0 Flash               | Google    | 高速・効率    | Google社Geminiファミリーの速度・効率特化型軽量モデル。迅速な応答や大量リクエスト処理に適応。                                                                                        |
| Gemini 2.5 Pro (Preview)       | Google    | 高性能・推論    | Google社の最新世代の高性能プレビュー版モデル。複雑な推論、長文理解、コーディング、多言語対応において特に優れた能力を発揮。                                                                     |
| GPT-4.5                        | OpenAI    | 高性能・推論    | OpenAI社の最先端モデルの一つ。非常に高度な推論能力と複雑な問題解決能力、専門知識の理解に優れる。Copilot内では最高の性能ですがプレミアムリクエスト消費も大きい。                                            |
| o1 (Preview)                   | OpenAI    | 高性能・推論    | OpenAIが提供するプレビュー版で、特に複雑な推論能力に優れる。コード最適化、難解なバグ修正、構造化されたコード生成、ログや結果の分析的要約といったタスクで高い性能を示す。                                         |
| o3-mini                        | OpenAI    | 高速・効率    | OpenAI提供の比較的小規模で効率的なモデル。「mini」の名称通り、応答速度やコスト効率を重視した設計。                                                                                       |
| o4-mini (Preview)              | OpenAI    | 高速・効率    | OpenAI提供の新世代小規模・効率モデルのプレビュー版。o3-mini同様の効率性を重視しつつ、最新アーキテクチャ等による性能向上が図られています。                                                       |

**補足:**

* **タイプの凡例:**
    * **高速・効率**: 主に応答速度を重視し、比較的軽量で、迅速なフィードバックやシンプルなタスク処理に適したモデルを指します。
    * **バランス・汎用**: 性能と応答速度、リソース消費のバランスが良く、日常的なコーディング支援から一般的なチャットまで、幅広い用途に対応できるモデルを指します。
    * **高性能・推論**: 複雑な問題解決や高度なコード生成、そして特に推論能力が求められる難易度の高いタスクに適したモデルを指します。
* ここでの「タイプ」分類は、各モデルの一般的な特性やGitHub Copilot内での想定される役割に基づいたものです。実際の性能や挙動は、利用状況やチューニングによって変わる可能性があります。
* **(Preview)** と記載されているモデルは、まだ正式リリース前のプレビュー段階であり、機能や性能が変更されたり、提供が一時的であったりする可能性があります。
* **GPT-4oについて**: 以前は主要なモデルの一つとして利用されていましたが、現在は新しいベースモデル（GPT-4.1）への移行に伴い、非推奨となる予定です。そのため、上記表からは除外しています。
* 各モデルのより詳細な技術的仕様や最新情報については、開発元（OpenAI, Google, Anthropic）やGitHubの公式発表をご参照ください。

おすすめの機能ですので、ぜひ活用してみてください。

### プレミアムリクエストとは？～仕組みとプラン・モデル別の扱い～
**★ 2025.5.15 Update ★**

前の章「AIモデルの選択」では、GitHub Copilotで様々なAIモデルを切り替えて利用できる魅力について触れました。また、「料金プラン」の章でも少しだけ「プレミアムリクエスト」という言葉が出てきました。

「プレミアムリクエストって何だろう？」「どういう時に、どれくらい消費するの？」といった疑問をお持ちの方もいらっしゃるかもしれません。
この章では、その**プレミアムリクエスト**について、もう少し詳しく解説していきます。この仕組みをご理解いただくことで、GitHub Copilotの各AIモデルをより効果的に、そしてご自身の使い方に合わせて活用できるようになると思います。

#### プレミアムリクエストの基本

まず、プレミアムリクエストとは何か、基本的な情報から確認していきます。

* **プレミアムリクエストの定義**
    GitHub Copilotにおけるプレミアムリクエストとは、簡単に言うと、より高性能なAIモデルや特定の機能に特化したAIモデルを利用する際に消費される「**利用枠**」や「**クレジット**」のようなものです。
* **導入の目的**
    この仕組みは、ユーザーが、Anthropic社のClaudeモデル、Google社のGeminiモデル、OpenAI社の高性能なGPTモデルといった、様々な最先端AIモデルの中から必要に応じて選択し利用できるようにしつつ、その利用量に応じた公平で持続可能なコスト負担を実現するために導入されたものです。
* **課金開始予定日**
    GitHubの公式情報によると、このプレミアムリクエストに対する実際の課金は、すべてのプランにおいて**2025年6月4日から開始される予定**です（2025年5月14日時点の情報）。

#### プレミアムリクエストの仕組みと消費量

プレミアムリクエストの具体的な仕組みの中心となるのが、AIモデルごとに設定された「**乗数 (Multiplier)**」という考え方です。

* **AIモデルごとの「乗数」**
    利用できる各AIモデルには、その性能や計算コストに応じて「乗数」が設定されています。
    プレミアムリクエストを消費する操作、例えばCopilot Chatで特定のAIモデルを選んで質問や指示を行った場合、選択したモデルの乗数分だけプレミアムリクエストが消費されます。一般的に、高性能なモデルほど乗数が高く設定されています。

    主要なAIモデルごとのプレミアムリクエスト消費量は以下の通りです。

    **GitHub Copilot AIモデル別 プレミアムリクエスト消費量 (2025年5月14日時点)**

    | AIモデル名                     | プレミアムリクエスト乗数 |
    | :------------------------- | :----------------------- |
    | **ベースモデル (GPT-4.1)** | **0** (有料プランの場合) |
    |                            | **1** (Freeプランの場合) |
    | Claude 3.5 Sonnet          | 1                        |
    | Claude 3.7 Sonnet          | 1                        |
    | Claude 3.7 Sonnet Thinking | 1.25                     |
    | Gemini 2.0 Flash           | 0.25                     |
    | Gemini 2.5 Pro (Preview)   | 1                        |
    | GPT-4.5                    | 50                       |
    | o1 (Preview)               | 10                       |
    | o3-mini                    | 0.33                     |

    少しイメージしづらいかもしれませんので、具体的な例を挙げてみます。
    例えば、Copilot Chatで特定のAIモデルを選択し、AIと5回ほどメッセージのやり取り（質問や指示など）をした場合に消費されるプレミアムリクエストは、おおよそ以下のようになります。

    * **GPT-4.5** を利用した場合:
        * 50 (乗数) × 5回 = **250** プレミアムリクエスト
    * **Claude 3.7 Sonnet Thinking** を利用した場合:
        * 1.25 (乗数) × 5回 = **6.25** プレミアムリクエスト
    * **ベースモデル (GPT-4.1)** を有料プランで利用した場合:
        * 0 (乗数) × 5回 = **0** プレミアムリクエスト （消費しません）
    * **ベースモデル (GPT-4.1)** をFreeプランで利用した場合:
        * 1 (乗数) × 5回 = **5** プレミアムリクエスト

    このように、選択するAIモデルによって、消費されるプレミアムリクエストの量が大きく変わることが分かります。

#### プランごとの月間プレミアムリクエスト目安

「料金プラン」の章でも一度触れましたが、各プランで毎月利用できるプレミアムリクエストの目安を以下の表で改めて確認します。この表を基に、プランごとの扱いを詳しく見ていきます。

| プラン名          | 月額料金（1ユーザー） | 年額料金（1ユーザー） | 主な対象ユーザー                                 | 月間プレミアムリクエスト目安 |
| ----------------- | ------------------- | ------------------- | ------------------------------------------------ | -------------------------- |
| **Copilot Free** | 無料                | -                   | 個人開発者（機能・利用回数制限あり）             | 50回                       |
| **Copilot Pro** | \$10                | \$100               | 個人開発者                                       | 300回                      |
| **Copilot Pro+** | \$39                | \$390               | 高度なAIモデルや機能を求める個人開発者             | 1,500回                    |
| **Copilot Business**| \$19                | -                   | 企業、チーム                                     | 300回/ユーザー             |
| **Copilot Enterprise**| \$39                | -                   | 大規模組織（高度なセキュリティと管理機能が必要） | 1,000回/ユーザー           |

この表を踏まえて、プランごとの扱いを説明します。

* **有料プラン (Pro, Pro+, Business, Enterprise) をご利用の方**
    * 通常のコード補完やチャットで標準的に使われるAIモデル（現在のベースモデルはGPT-4.1）の利用は、プラン料金の範囲内で**無制限**となっており、プレミアムリクエストを消費しません。これは、個人的にも嬉しいポイントだと感じています。
    * 上記の表で示した月間プレミアムリクエストは、主に高性能なAIモデルを選んで利用する場合のために付与されています。
    * BusinessプランやEnterpriseプランでは、組織単位で管理されたり、ユーザーごとに利用ルールが設定されたりします。

* **Freeプランをご利用の方**
    * Freeプランの場合は、コード補完やチャットなど、ベースモデルを利用する際にも、上記表に示された月間のプレミアムリクエスト上限までの中で消費していく形になります。

#### エディタ上でのAgentモード利用とプレミアムリクエスト消費の考え方
**★ 2025.5.31 Update ★**

GitHub CopilotをVSCodeなどのエディタ上でチャット機能やインラインチャットを使って利用する際、特に少し複雑な修正や機能追加をお願いすると、「一体どれくらいのプレミアムリクエストを消費するのだろう？」と気になることがあるかもしれません。

例えば、ユーザーが「この変数定義の箇所を、現状のレイアウトを可能な限り維持しつつ、すべての変数を表示できるようにしてほしい」といった、ある機能の修正をCopilotに1回お願いしたとします。私たちユーザーにとっては1回の要求ですが、Copilotの内部では、その要求を実現するために、関連するコードを分析したり、複数の箇所を修正したりと、いくつもの処理を連続して実行してくれることがあります。

![premium](/images/turtle-20240223-gitcopilot/cop_premium.png)
*ユーザーの1回の要求に対し、Copilot内部で複数処理実行例*

上の図は、まさにそのような状況を示しています。ユーザーが一つの明示的な要求（図中の「ユーザーによる明示的な要求」）を出したのに対し、GitHub Copilotがその要求に応えるために、内部的に複数の処理（図中の「GitHub Copilotが、内部で行う複数回の処理」）を行っている様子が分かります。

では、このような場合、プレミアムリクエストはCopilotが内部で行った処理の回数分、つまり図の例で言えば5回分消費されてしまうのでしょうか？

ご安心ください！GitHub Copilotのプレミアムリクエスト消費に関する基本的な考え方として、**ユーザーによる1回の明示的な要求（例えば、チャットでの1回の送信や、インラインチャットでの1回の実行指示など）に対して、選択したAIモデルの乗数分のプレミアムリクエストが消費される**というルールになっています。
つまり、Copilotが内部的にどれだけ多くの処理ステップを踏んだとしても、それがユーザーの最初の1回の要求に応えるための一連の動作であれば、消費されるプレミアムリクエストの計算に使われる「要求回数」は1回としてカウントされる、ということです。

具体的な例で見てみましょう。

* ユーザーの要求回数：**1回** （例：「この関数の処理内容を変更して、返り値の型も修正してください」という一連の指示）
* GitHub Copilotが内部で行った処理ステップの数：仮に**5ステップ** （例：関数の理解、ロジック変更、型定義の修正、関連部分の修正、コメント修正など）
* 選択したAIモデル：Claude 3.7 Sonnet Thinking （プレミアムリクエスト乗数：**1.25**）

この場合、消費されるプレミアムリクエストは、Copilot内部の処理ステップ数（5ステップ）ではなく、あくまで**ユーザーの要求回数（1回）に、選択したAIモデルの乗数を掛けた値**となります。

計算：1 (ユーザーの要求回数) × 1.25 (Claude 3.7 Sonnet Thinkingの乗数) = **1.25 プレミアムリクエスト**

この例では、1.25プレミアムリクエストの消費で済むわけです。これは、一度の指示で複雑な修正や広範囲な変更を依頼する場合に、プレミアムリクエストを効率的に使える可能性があることを示しています。

#### 公式情報

プレミアムリクエストに関する詳細については、以下のGitHub Copilotの公式ドキュメントでご確認いただくのが最も確実です。

* GitHub Copilot プレミアムリクエストに関する公式ドキュメント:

https://docs.github.com/ja/copilot/managing-copilot/monitoring-usage-and-entitlements/about-premium-requests

このプレミアムリクエストの仕組みを理解した上で、**普段使いに適したベースモデルと、ここぞという時に頼りになる高性能なプレミアムモデルとを状況に応じて使い分けながら**、ご自身の開発スタイルに最適な使い方を見つけてみてください。

お疲れさまでした！以上で「使い方の基本」「便利な使い方」の説明を終わります。
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

GitHub Copilotを使ってみたい、これなら使えそうだ！と思っていただけたでしょうか。少しでも、この記事を読んでくださった方に、そう思っていただけたなら幸いです。 もし、分からないことや、分かりにくい部分がありましたら遠慮なくコメント欄に書き込んでください。🐢

私は、GitHub Copilotを使い始めたその日から、その魅力に魅了されました。他にも多くの詳細な記事がありますが、私の経験を通じて、私の言葉で、皆さんにその魅力を伝えたいと思い、この記事を書きました。このブログが、皆さんの開発に少しでも役立つことを願っています。

今後も魅力的な機能が追加されると思いますので、その都度ブログを更新していきたいと思います。

最後まで読んでいただき、ありがとうございました！

## リンク

これらの記事では、たった一枚の画像からAIを活用し、3Dプリンタでリアルな造形物を作成する技術を紹介しています。外側の造形部分はリンク先の記事の内容で、内側のソフトウェアはGitHub Copilotを使って開発することで、近い将来、AIをベースにした家電のようなモノづくりができるかもしれません。そんな未来に興味がある方は、ぜひ記事を読んでみてください👍

**Tripo 2.0**は、TripoSRの後継モデルで、劇的に精度が向上しました。モノづくり、ゲーム、VRなど幅広い分野に広がりそうな勢いを感じました。進化が止まりません！
https://zenn.dev/safubuki/articles/turtle-20240929-tripo2-evo

**Stable Fast 3D**は、TripoSRの後継モデルで、さらに素早くキレイな3Dデータを生成できるようになりました。AIの世界は進化がすごいです。
https://zenn.dev/safubuki/articles/turtle-20240803-stable-fast

**TripoSR**は、少し古い技術になりましたが、インプット画像生成のコツや成功・失敗事例なども記載しています。参考になる部分もいろいろあります。
https://zenn.dev/safubuki/articles/turtle-20240721-tripo-3dp

## 更新履歴

更新履歴は折りたたみ表示にしています。
確認したい場合は、以下のバーをクリック（タップ）してください。

:::details 更新履歴（最終更新日：2025/05/31）
**更新履歴**

- **2025/05/31**
  - エディタ上でのAgentモード利用とプレミアムリクエスト消費の考え方のサブセクションを新規追加

- **2025/05/15**
  - 「プレミアムリクエストとは？～仕組みとプラン・モデル別の扱い～」の章を新規追加。

- **2025/05/14**
  - 「導入方法」の章を最新情報（2025年5月時点）に基づき全体的に更新。
    - Freeプランに関する記述を明確化。
    - 料金プランの情報（プレミアムリクエスト導入予定を含む）を更新。
    - アカウント作成、登録・契約手順、拡張機能インストールに関する説明や注釈を調整。
  - 「AIモデルの選択」サブセクションを最新情報に基づき更新。
    - 導入文の表現やニュアンスを調整。
    - 記載するAIモデルの種類、各モデルの特徴、タイプ分類の名称と定義を見直し。
    - GPT-4oに関する情報を表から補足へ移動。

- **2024/11/11**
  - 導入部分の文章を見直し
  - ブログ構成の図の一部不正確な内容を修正
  - リンク章の文章を一部修正
  - タイポを修正

- **2024/11/09**
  - 導入の文章にCopilotアップデートに対応した旨を追加
  - ブログの構成の章を追加して、ブログの一覧性を向上
  - チャット機能の起動方法や表示位置について記載
  - チャット機能のgif動画を更新
  - 便利な使い方の章を追加して、コンテキスト変数などを移動
  - チャットパーティシパンツ（Chat Participants）章を新規追加
  - コンテキスト変数の#fileにファイルをアタッチする機能を新規追加
  - コンテキスト変数#codebaseを追加更新
  - AIモデルの選択を新規追加
  - まとめの文章に更新追従する旨の一文を追加
  - 変更履歴の表示を折りたたみ表示に変更

- **2024/09/30**
  - Tripo 2.0リンク及び、説明文を追加

- **2024/08/04**
  - AI関連のStable Fast 3Dの記事を追加し、説明文を追加修正

- **2024/08/02**
  - 記事紹介のリンクを追加し、AI関連のTripoSRの記事を紹介

- **2024/07/10**
  - コンテキスト変数の説明を追加

- **2024/03/04**
  - 説明に使用した一部の画像やgif動画の文字が見づらいため、画像サイズを大きくした
:::
