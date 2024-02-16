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
コードのエラーチェック、整形、補完などを自動でできるので、読みやすさや品質を高めることが簡単にできます。

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

## 環境構築

まず、実際に触ってもらって効果を体感していただきたいので、拡張機能の細かい説明は後回しにして、実際に動かせる環境を作っていきたいと思います。

### ① 拡張機能のインストール

次の図に示す、**6つの拡張機能**をVSCodeにインストールしてください。
似たような名前の拡張機能がありますから、拡張名や作者名をよく確認して、作業を行ってください。

![ext_list.png](/images/turtle-20240215-pymind/ext_list.png)
*自信をもってコーディンするための拡張機能一覧*

もし、拡張機能のインストール方法がわからない場合は、以前私が書いた次の記事を参考にしてみてください。

https://zenn.dev/safubuki/articles/turtle-20240121-vscode#%E6%8B%A1%E5%BC%B5%E6%A9%9F%E8%83%BD%EF%BC%9A%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%96%B9%E6%B3%95

### ② Google Style Guides ダウンロード・編集

Google Style Guidesとは、Googleが公開しているプログラミング言語ごとのコーディングスタイルガイドのことです。これらのガイドは、Google内部でのプロジェクト開発において、コードの一貫性を保ち、理解しやすく、保守しやすくするために使われています。つまり、Googleの人や、関連サービスを作っている人たちと同じスタイルで、記述することができるわけですね😊
Pythonの場合、Pylint向けの設定ファイルとして提供されています。
それでは、手順に従って、ダウンロード・編集します。

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
   ※ pylintrc はどこに保存しても良いのですが、分かりやすいようにVSCodeの設定ファイル(settings.json)と同じ場所に保存しておきます。

5. pylintrcをVSCodeなどのエディタで開き、次の項目を編集します。
   - **max-line-length**
   **1行あたりの最大文字数**
   PEP8に従うなら1行は79文字ですから、無理して変更する必要はないです。が、プロジェクトの規約や個人の好みによっては変更したいというケースもあるでしょうから、ここでは変更しています。
        ```diff text:pylintrc 240行目付近
        + max-line-length=100
        - max-line-length=80
        ```
        ::::message
        ワンポイント
        :::details 1行の文字数はPEP8で決められているのに変更していいの？（クリックで開く）

        PEP8スタイルガイドの次の項目に、1行の長さについて記述があります。

        https://pep8-ja.readthedocs.io/ja/latest/#id8

        ここには、

        >すべての行の長さを、最大79文字までに制限しましょう。

        と明確に書かれています。
        そして、その理由は次の通りです。

        >ほとんどのツールのデフォルトの折り返し動作は、コードの見た目の構造を壊し、理解するのを難しくします。79文字という制限は、ウィンドウの幅を80に制限し、行を折り返すときにツールが行末にマーカーを置いたとしても、エディタに折り返す動作をさせない目的で選ばれています。

        しかし、実際にこの規約の通りにコーディングすると、頻繁に改行が入り逆に見づらくなったというケースも、経験ある方、いらっしゃるかもしれません。さらに読み進めると、次のような記述があります。

        >1行を79文字より長くするのを好むチームもあります。この問題について合意できるチームが独占的に、もしくは重点的にメンテナンスするコードについては、1行99文字まで制限を緩めてもOKです。ただし、コメントや docstring については72文字で折り返すようにすることが条件です。

        また、PEP8の冒頭には次のような記述があります。

        https://pep8-ja.readthedocs.io/ja/latest/#id1

        >多くのプロジェクトには、自分たちのコーディングスタイルに関するガイドラインがあります。それとこの文書の規約の内容が矛盾した場合は、そのプロジェクトのガイドラインが優先します。

        >一貫性を崩すべき場合があることも知っておいてください - つまり、このスタイルガイドが適用されない場合があります。疑問に思ったときは、あなたの判断を優先してください。

        つまり、プロジェクトにおいてメンバ間で合意をとることができる場合や、コードの可読性が下がると自身が判断した場合には、必ずしも1行79文字に固執する必要はないと思います。

        一貫性にこだわりすぎず、柔軟に対応していけば良いのだと思います。
        とはいえ「じゃあ、1行200文字だ！」というのは現実的ではないですから、そこはうまくバランスをとってください👍
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
        ワンポイント
        :::details Googleのスタイルガイドはなぜ2スペースなの？（クリックで開く）
        pylintrcのindent-stringの設定項目のすぐ上の文章に次のような記述があります。

        > **原文：**
        String used as indentation unit.  The internal Google style guide mandates 2 spaces. Google's externaly-published style guide says 4, consistent with PEP 8. Here, we use 2 spaces, for conformity with many open-sourced Google projects (like TensorFlow).
        **日本語訳：**
        インデント単位となる文字列。 グーグル社内のスタイルガイドでは、スペース2個が義務付けられています。 Googleが社外に公開しているスタイルガイドでは、PEP 8に準拠して4スペースとなっています。ここでは、多くのオープンソースのGoogleプロジェクト（TensorFlowなど）に準拠するため、2スペースを使用しています。

        上記のような理由から2スペースになっているのですね。
        :::
        ::::

6. 保存したら、この項目の作業は完了です。

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

### 悪いソースコード降臨

私がAIと協力しながら作成した、サンプルコードを以下に示します。
お世辞にも良いとは言えない、悪いコードの例になります。
コード上には、青や黄色、赤など多くのニョロニョロが表示されています。
これらは拡張機能が指摘している問題点です。
このニョロを無くすことが、きれいなコードを書くポイントになります。

![ext_sample](/images/turtle-20240215-pymind/ext_sample.gif)
*bad_sample_org.pyのエラー確認gif動画*

悪いところは多々あるプログラムですが、意図したとおりに動作します。

![ext_execute](/images/turtle-20240215-pymind/ext_execute.png)
*プログラムの実行結果*

::::message
ブレークタイム
:::details 悪いコード作成秘話（ネスト）
ネストされた要素
:::
::::

```python:bad_sample.py
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

## 拡張機能解説
## まとめ
## リンク

