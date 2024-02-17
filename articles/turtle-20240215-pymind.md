---
title: "【Python】VSCode拡張機能で自信をもってコーディングする方法！"
emoji: "🐢"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [python,vscode,vscode拡張機能]
published: false
---
プログラミングで、自分の書いたコードに自信が持てないことってありませんか？
他人にコードを見せることが恥ずかしくて嫌だという経験、あるのではないでしょうか。

私も以前はそうでした。

コードが汚いと思われたり、能力が低いと思われたりするのではないかと不安になり、また自らの内面をさらけ出すようで何とも恥ずかしいものでした。

しかし、プログラミング能力向上にとって、コードを他人に見せてフィードバックを受けることは大切です。

そこで試していただきたいのが、VSCodeエディタとその拡張機能を使う方法です。
コードのエラーチェック、整形、補完などを拡張機能によって自動でできるので、読みやすさや品質を高めることが簡単にできます。

今回は、Pythonのコーディングに役立つ拡張機能をいくつか紹介します。
それぞれの拡張機能のインストール方法や設定方法、使い方のポイントなどを詳しく説明します。

#### ブログ対象者

- 自分のコードの読みやすさや品質に自信が持てない方
- コードのレビューやテストを行う、チームで開発するなど、コードの読みやすさや品質を高める必要がある方
- Pythonを扱う方
説明をPython言語で行うため。ただし、他の言語でも似たような仕組みがありますので、本ブログで雰囲気は感じ取っていただけると思います。

#### 得られる効果

このブログを読むことで、次のような効果が得られます。

- Pythonのコーディングルールに準拠し、読みやすいコードを作成できるようになります。
- コードのエラーチェックや整形、補完などを自動で行う環境を構築でき、コードの品質を高めることができます。
- 他人にコードを見せることが苦にならなくなり、フィードバックを受けやすくなることで、能力向上が期待できます。

**これらの効果により、自信をもってコーディングができるようになります！**

## 環境の準備

コーディングするとき、VSCodeはとても便利なエディタですが、標準の機能だけではコードを効率的に書くことができません。そこで、VSCodeには様々な機能を追加できる拡張機能というものがあり、これをインストールして使用します。さらに、それらを便利に使うための設定を行います。

それでは早速、環境構築を進めましょう。

### ① 拡張機能のインストール

次の図に示すような各種便利な機能を提供する**6つの拡張機能**を使います。まずこれらをインストールしてください。似たような名前の拡張機能もありますので、拡張機能の名前や作者の名前を正しく確認して、作業を行ってください。

![ext_list.png](/images/turtle-20240215-pymind/ext_list.png)
*自信をもってコーディンするための拡張機能一覧*

上記は画像として表示されていますので、拡張名をコピー&ペーストしてミスなく検索できるように、以下にテキストを用意しました。ご活用ください。

```text
Pylint, Pylance, Mypy Type Checker, yapf, isort, autoDocstring
```

もし、拡張機能のインストール方法がわからない場合は、以前私が書いた次の記事を参考にしてみてください。

https://zenn.dev/safubuki/articles/turtle-20240121-vscode#%E6%8B%A1%E5%BC%B5%E6%A9%9F%E8%83%BD%EF%BC%9A%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%96%B9%E6%B3%95

### ② Google Style Guides ダウンロード・編集

#### Google Style Guidesとは

Google Style Guidesとは、Googleが公開しているプログラミング言語ごとのコーディングスタイルガイドのことです。これらのガイドは、Googleのコードの品質や可読性を高めるために作られたもので、世界中の開発者から高い評価を得ています。私は、Googleの人や、関連サービスを作っている人たちと同じスタイルで、記述することができるというのは、とても素敵だと思います😊
Pythonの場合、Pylint向けの設定ファイルとして提供されています。

#### ダウンロードの手順

1. 次のサイトにアクセスします。

https://google.github.io/styleguide/

2. 各種言語のスタイルガイドがあります。
今回はPythonを対象にしますので**Python Style Guide**のリンクをクリックします。

![py_style](/images/turtle-20240215-pymind/py_style.png =500x)
*Google Style Guidesのページ*

3. 2.1 Lintの**pylintrc**のリンクをクリックします。
すると、ファイルのダウンロードが始まります。

![py_style_py](/images/turtle-20240215-pymind/py_style_py.png =500x)
*Google Python Style Guideのページ*

4. ダウンロードした`pylintrc`ファイルを次の場所に移動します。
   なお、{ユーザー名}は、自身の環境にあわせて書き換えてください。
   ```text
   C:\Users\{ユーザー名}\AppData\Roaming\Code\User
   ```
   ※ pylintrc はどこに保存しても良いのですが、分かりやすいようにVSCodeの設定ファイル(settings.json)と同じ場所に保存しておきます。これは、後でVSCodeの設定でpylintrcのパスを指定するときに、同じフォルダ内にあると便利だからです。

#### 編集の手順
1. pylintrcをVSCodeなどのエディタで開き、次の項目を編集します。
   - **max-line-length**
   **1行あたりの最大文字数**
   PEP8に従うなら1行は79文字ですから、無理して変更する必要はないです。が、プロジェクトの規約や個人の好みによっては変更したいというケースもあるでしょうから、ここでは変更しています。
        ```diff text:pylintrc 240行目付近
        + max-line-length=100
        - max-line-length=80
        ```
        ::::message
        ワンポイント 💡
        :::details 1行の文字数はPEP8で決められているのに変更していいの？（クリックで開く）
        Pythonのコードを書くとき、1行の長さはどのくらいが適切なのでしょうか？PEP8では79文字と決められていますが、それに従う必要はあるのでしょうか？
        PEP8スタイルガイドに次の記述があります。

        >すべての行の長さを、最大79文字までに制限しましょう。

        その理由は次の通りです。

        >ほとんどのツールのデフォルトの折り返し動作は、コードの見た目の構造を壊し、理解するのを難しくします。79文字という制限は、ウィンドウの幅を80に制限し、行を折り返すときにツールが行末にマーカーを置いたとしても、エディタに折り返す動作をさせない目的で選ばれています。

        ですが、実際にこの規約の通りにコーディングすると、頻繁に改行が入り逆に見づらくなることもあります。さらに読み進めると、

        >1行を79文字より長くするのを好むチームもあります。この問題について合意できるチームが独占的に、もしくは重点的にメンテナンスするコードについては、1行99文字まで制限を緩めてもOKです。ただし、コメントや docstring については72文字で折り返すようにすることが条件です。

        また、PEP8の冒頭には次のような記述があります。

        >多くのプロジェクトには、自分たちのコーディングスタイルに関するガイドラインがあります。それとこの文書の規約の内容が矛盾した場合は、そのプロジェクトのガイドラインが優先します。

        >一貫性を崩すべき場合があることも知っておいてください - つまり、このスタイルガイドが適用されない場合があります。疑問に思ったときは、あなたの判断を優先してください。

        とあります。つまり、プロジェクトにおいてメンバ間で合意をとることができる場合や、可読性が下がると自身が判断した場合には、1行79文字に固執しなくてもいいです。意外な事実が分かりました。

        PEP8の行長は、コードの品質や可読性を向上させるためのものです。しかし、それはあくまでガイドラインであり、プロジェクトや個人の状況に応じて柔軟に対応することができます。自分のコードを書くときは、1行の長さについても意識してみてください。
        
        参考情報：
        https://pep8-ja.readthedocs.io/ja/latest/

        :::
        ::::
   - **indent-string**
   **インデントのスペース数**
   一般的には4スペースなのですが、Googleのスタイルガイドでは2スペースになっているため、4スペースに変更します。
        ```diff text:pylintrc 260行目付近
        + indent-string='    '
        - indent-string='  '
        ```
        ::::message
        ワンポイント 💡
        :::details Googleのスタイルガイドはなぜ2スペースなの？（クリックで開く）
        PEP 8では4スペースと決められていますが、Googleのスタイルガイドでは2スペースになっています。なぜこの違いがあるのでしょうか？
        pylintrcのindent-stringの設定項目のすぐ上に次のような記述があります。

        > **原文：**
        String used as indentation unit.  The internal Google style guide mandates 2 spaces. Google's externaly-published style guide says 4, consistent with PEP 8. Here, we use 2 spaces, for conformity with many open-sourced Google projects (like TensorFlow).
        **日本語訳：**
        インデント単位となる文字列。 グーグル社内のスタイルガイドでは、スペース2個が義務付けられています。 Googleが社外に公開しているスタイルガイドでは、PEP 8に準拠して4スペースとなっています。ここでは、多くのオープンソースのGoogleプロジェクト（TensorFlowなど）に準拠するため、2スペースを使用しています。

        インデントは一般的には4スペースが用いられることが多いですが、オープンソースプロジェクトに対する姿勢や、コードの可読性や品質に関する考え方によって異なることが分かりました。
        インデントの幅についても意識してみると、色々なことが見えてきます。
        :::
        ::::

2. 編集したpylintrcファイルを保存したら、この項目の作業は完了です。

### ③ VSCodeの設定（Settings.json）

続いてVSCodeの設定を行います。
この設定が終わると、すべての設定は完了です。あともう少し頑張ってください。

1. `Ctrl + Shift + p`を入力し、コマンドパレットを表示します。
2. 入力欄に「setting」と入力し、候補の中から`Preferences: Open User Settings(JSON)`を選択します。すると`settings.json`というファイルが開きます。
3. 次の内容をsettings.jsonにコピー＆ペーストしてください。
      ```json:settings.jsonにコピーする内容
      {
          "[python]": {
              "editor.insertSpaces": true,
              "editor.tabSize": 4,
              "editor.formatOnType": true
          },
          "pylint.args": [
              "--rcfile=C:\\Users\\{ユーザー名}\\AppData\\Roaming\\Code\\User\\pylintrc"
          ],
          "yapf.args": [
              "--style",
              "{based_on_style: google, column_limit: 100, indent_width: 4}"
          ],
          "mypy-type-checker.args": [
              "--ignore-missing-imports",
              "--check-untyped-defs"
          ],
          "editor.formatOnSave": true,
          "editor.codeActionsOnSave": {
              "source.organizeImports": "explicit"
          }
      }
      ```
      それぞれの設定項目の意味は次の通りです。
      - "[**python**]"：python言語に対する設定です
        - "**editor.insertSpaces**"：タブキーを押したときに、スペースを挿入します
        - "**editor.tabSize**"：タブのサイズを 4 に設定します
        - "**editor.formatOnType**"：コードを入力したとき、自動でフォーマットを整えます
      - "**pylint.args**"：pylintの設定です
      先ほどダウンロード・編集したpylintrcファイルを設定ファイルとして使います。
      - "**yapf.args**"：yapfの設定です
      Googleのスタイルガイドに基づき、コード幅を100 、インデント幅を4にします。
      - "**mypy-type-checker.args**"：mypyの設定です
        - "**--ignore-missing-imports**"：インポートしたモジュールの型情報がなくてもエラーにしない
        - "**--check-untyped-defs**"：型注釈のない関数もチェックする
      - "**editor.formatOnSave**"：ファイルを保存時、自動的にフォーマットを整えます
      - "**editor.codeActionsOnSave**"：ファイルを保存時、自動的に実行するコードアクションを指定します
        - "**source.organizeImports**"：ファイルの先頭にあるインポート文を整理します

      :::message
      - pylint.argsの{ユーザー名}は、自身の環境にあわせて書き換えてください。
      - 既にいくつか設定項目が`settings.json`ある場合は、前の設定に続ける形で追加してください。その場合は、上記の先頭と末尾の{}中カッコは不要です。`"[python]":` 以降をコピーしてください。
      :::
4. 設定が完了したら、ファイルを保存して閉じてください。
5. `Ctrl + Shift + p`を入力し、コマンドパレットを表示します。
6. 入力欄に「reload」と入力し、候補の中から`Developer: Reload Window`を選択します。

以上で全ての環境設定は完了です。お疲れさまでした🎉
これで、あなたは自信をもってコーディングをするスタートラインに立ちました！

## 効果を体感しよう

ここからは、拡張機能の効果を体感します。
悪いコードの例を示しますので、それが拡張機能を駆使してどのように改善していくか、自身の環境で確かめてみてください。

### 悪いコード降臨

私がAIと協力しながら作成した、サンプルコードを以下に示します。
お世辞にも良いとは言えない、悪いコードの例になります。
コード上には、青や黄色、赤など多くの**警告**や**エラー**が表示されています。
これらは拡張機能が全て指摘をしています。
この警告やエラーを無くすことが、きれいなコードを書くポイントになります。

![ext_sample](/images/turtle-20240215-pymind/ext_sample.gif)
*悪いコードのエラー確認gif動画*

悪いところが多々あるプログラムですが、意図したとおりに動作はします。

![ext_execute](/images/turtle-20240215-pymind/ext_execute.png)
*プログラムの実行結果*

::::message
ブレークタイム（時間があれば読んでみてください）☕
:::details 悪いコード作成秘話（クリックで開く）
悪いコードを書くのも一苦労です。
最近は、コーディングする際にAIの力を借りることもしばしば。
そこで、悪いコードを書くお手伝いをしてもらいました。

プロンプト（指示文章）は次のような感じです。

```text
以下の条件のpythonコードを生成してください。 
・プログラムとして正しく動作し、不自然さがない
・ランダムに5つの数値を出力し、その合計を出力する処理とする
・関数は3つ程度用いる。実行契機があること
・処理の内容が誰から見ても平易である
・インポートするモジュールの順序がでたらめである
・yapfなどのフォーマッタが自動整形しなければならないほどでたらめである
・型ヒントを守らずmypyから指摘を受けるコード
　戻り値の型ヒントがリスト型なのに、実際はリストではない型を返す 
・pylintから複数の要因で指摘を受ける
・pylanceからも指摘を受ける
なお、上記は悪い例のコードを元に学習するために行っています。
協力をお願いします。
```

AIのCopilotさんは少々不満げですが、ちゃんと仕事をこなしてくれます。

![copilot_work](/images/turtle-20240215-pymind/copilot_work.png)

ただ、生成されたコードは、悪いコードとしては不十分でしたので、ここから私がさらに磨きをかけて悪いコードを完成に導きました。

そこそこの時間を溶かして「一体何をやっているんだ」と思うこともありましたが、無事完成したときは達成感がありました！👿

以上、悪いコード秘話でした🤭
:::
::::

### 悪いコードをキレイに

それでは、先ほど降臨した悪いコードをキレイにしていきます。

1. **VSCodeの開発環境に`sample.py`という空のファイルを作成します。**
2. **次の悪いコードをコピーして、`sample.py`にペーストします。**

```python:sample.py（これをコピーしてください）
from typing import List
import random
import math

def g_rand() -> List[int]:
  num_list = []
  for i in range(5):
      num_list.append(random.randint(1, 100))
  return num_list

def g_sums(numbers: List[int]) -> int:
  total = 0
  for n in numbers:
      total += n
  return total

def p_res(prt_numbers: int, prt_total: List[int]) -> None:
    print("The random numbers are:", prt_numbers)
    print("The sum is:", prt_total)

if __name__ == "__main__":
    numbers = g_rand()
    total = g_sums(numbers)
    p_res(numbers, total)
```

3. **画面を注意深く見つめながら`Ctrl + s`を入力してファイルを保存します。**
この時、コードに変化が起こったと思います。
もし、見逃した方は`Ctrl + z`で戻して、再び`Ctrl + s`してみてください。
これは、yapf、isortの働きによりコードが自動的に整形されたのです。
yapfはコードのインデントや改行などのスタイルを自動で整え、isortはインポートの順序を自動で整えました。yapfは、この他にも1行あたりの文字数が99文字を超えていた場合、範囲内に収まるように適切に改行します。

```python:sample.py（yapfとisortによる自動整形後）
import math
import random
from typing import List


def g_rand() -> List[int]:
    num_list = []
    for i in range(5):
        num_list.append(random.randint(1, 100))
    return num_list


def g_sums(numbers: List[int]) -> int:
    total = 0
    for n in numbers:
        total += n
    return total


def p_res(prt_numbers: int, prt_total: List[int]) -> None:
    print("The random numbers are:", prt_numbers)
    print("The sum is:", prt_total)


if __name__ == "__main__":
    numbers = g_rand()
    total = g_sums(numbers)
    p_res(numbers, total)
```

![format](/images/turtle-20240215-pymind/format.png)
*フォーマッタの効果(yapf, isort)*
::::message
ワンポイント 💡
:::details 派生開発（既存コードに機能追加や改善する開発）でのフォーマッタ使用注意（クリックで開く）

自動で整形してくれるyapfやisortのようなフォーマッタは大変便利ですが、派生開発での使用には注意が必要です。開発にもよりますが、中にはPEP8のスタイルガイドに準拠していないコードがベースの開発もあると思います。そのようなコードに数行変更を加えただけのつもりで`Ctrl + s`を入力しようものなら、フォーマッタが容赦なく全体をキレイにしていきます。以下に、私がプライベートで開発しているコードでフォーマッタを実行した例を示します。

![caution_hasei](/images/turtle-20240215-pymind/caution_hasei.png)
*フォーマッタによる多数の修正*

ご覧の通り、`Ctrl + s`を入力しただけで、結構な量のコードが修正されました。加えて、既存で動作していたコードに手を加えることになるので、再度テストが必要になるケースがあります。自動でテストをする仕組みがあれば良いですが、そうではない場合は、一時的に無効にしておくことも選択肢の一つになるかと思います。派生開発でもゆとりがあり、リファクタリングをするようなフェーズでは、フォーマッタに頼ってきれいにしながらテストをしていくのも良いですが、開発が佳境のときのフォーマッタによる思いもよらない変更には注意が必要です。
:::
::::

4. **Pylint、Pylance、mypyの指摘を修正します。**
   ここでは代表的なものを見ていきます。まず、1行目の`import math`に指摘があります。マウスカーソルを当てると次のような表示が出力されます。
   ![shiteki](/images/turtle-20240215-pymind/shiteki.png =550x)
   *拡張機能による指摘*
   mathモジュール使われておらず、不要ということのようです。今回はこのメッセージの一文だけで指摘内容が分かりましたが、場合によっては内容を理解できないことがあります。その時は、赤線の青い文字のリンクをクリックしてみてください。すると、次のようなWebページに移動します。
   ![pylint_page](/images/turtle-20240215-pymind/pylint_page.png =550x)
   *Pylintドキュメントサイト*
   このページには、問題のあるコードと正しいコードのサンプルを交えた解説があります。指摘内容の理解と改善の助けとなります。そして、さらに便利な機能がQuick Fixです。以下の赤線をクリックします。
   ![quick_fix](/images/turtle-20240215-pymind/quick_fix.png =550x)
   *Quick fix*
   すると、さらに次のような表示がされます。この中からRemove unused importsを選択すると選択した使っていないimportが削除されます。all unusedの方を選択すると全ての使っていないimportが削除されます。ただし、このQuick Fix、指摘内容によっては使えないことがあります。その場合は、先ほどのページを参照しながら修正を行ってください。
   :::details 補足説明：Fix using CopilotとExplain using Copilotとは？
   ちなみに、皆さんの環境ではRemove～など💡マークがついた2つしか表示されていないかもしれません。それでは残りのFix using CopilotとExplain using Copilotは何？ということにになりますが、これは有料サービスの「GitHub Copilot」を利用していたら表示される項目です。AIが指摘内容を修正や説明し、今までのQuick Fixでは修正できかなった内容もAIが修正してくれます。「GitHub Copilot」契約されている方は、便利な機能ですので、ぜひ使ってみてください。
   :::
   ![quick_fix_sel](/images/turtle-20240215-pymind/quick_fix_sel.png =200x)
   *Quick fix選択画面*
   このような形で、残りの指摘も修正していきます。

5. **関数にコメントをつけて、さらに分かりやすくしていきます。**
   以下のように"(ダブルクォーテーション)を3回入力するだけで、関数コメントの概要、引数、戻り値のテンプレートが完成しました。こちらは拡張機能autoDocstringの働きによるものです。
   ![docstring](/images/turtle-20240215-pymind/docstring.gif)
   *関数コメント(docstring)の雛形生成*
   あとは、このひな形に説明文を記載していきます。完成すると次のような形になります。
   ![func_comment](/images/turtle-20240215-pymind/func_comment.png)
   *関数コメント(docstring)*
   関数のコメントについて、関数名の上に#コメントで記載するケースを見ますがこれはオススメしません。一般的な方法ではないですし、ヒント機能で関数コメントの内容が表示されないからです。ヒント機能は次のように、マウスカーソルをコールする関数に当てるとその内容が表示される機能です。
   ![hint](/images/turtle-20240215-pymind/hint.png)
   *ヒント機能*
   せっかく書いたコメントをよりよく活用するために、ぜひこの書き方を使って見てください。

6. 関数名も分かりやすい名称に修正します。
g_rand、g_sums、p_resですとパッ関数名を見て分かりにくいと感じる方もいると思いますので、get_random_numbers、get_sum、print_resultに修正します。
こちらは、プロジェクトによっては命名ルールが決まっている場合もあると思いますので、その場合はプロジェクトのルール等に従ってください。

以上で完成です！お疲れさまでした。
完成後のコードは次のようになります。

```python:sample.py
"""ランダムな数値を生成して、それらを加算、出力する"""

import random
from typing import List


def get_random_numbers() -> List[int]:
    """1から100までのランダムな整数を5つ生成し、それらをリストとして返す関数。

    Returns:
        List[int]: 生成されたランダムな整数のリスト
    """
    num_list = []
    for _ in range(5):
        num_list.append(random.randint(1, 100))
    return num_list


def get_sum(number_list: List[int]) -> int:
    """整数のリストを引数として受け取り、その合計値を返す関数。

    Args:
        number_list (List[int]): 合計値を求める整数のリスト

    Returns:
        int: リストの合計値
    """
    sum_total = 0
    for n in number_list:
        sum_total += n
    return sum_total


def print_result(prt_numbers: List[int], prt_total: int) -> None:
    """ランダムな整数のリストとその合計値を引数として受け取り、それらを出力する関数。

    Args:
        prt_numbers (List[int]): 出力するランダムな整数のリスト
        prt_total (int): 出力する合計値
    """
    print("The random numbers are:", prt_numbers)
    print("The sum is:", prt_total)


if __name__ == "__main__":
    numbers = get_random_numbers()
    total = get_sum(numbers)
    print_result(numbers, total)
```

## まとめ
いかがでしたでしょうか？
今回VSCodeと拡張機能を使って、Pythonのコーディングルールに準拠し、読みやすいコードを作成できるようになりました。また、コードのエラーチェックや整形、補完などを自動で行う環境を構築することができ、コードの品質を高めることができました。
このように世間一般的な方法に則ってコーディングを行うと「自分のコーディングは世の中のエンジニアと同じようにできているんだ！」「細かなミスもなく、品質を保てている！」と思えるようになり、自分のコーディングに自信が湧いてきます。そして、他人にコードを見せることが苦にならなくなり、フィードバックもどんどん受けられるようになります。
また、フィードバックをする側もフィードバックをしやすくなり、細かなミスの指摘ではなく、もっと根本的なロジックなど本質的な部分の指摘ができるようになります。

このページを読んでくださった方が、少しでも自信をもってコーディングすることができるようになった、あるいはその気持ちになっていただけたなら幸いです。最後までお付き合いくださり、ありがとうございました。