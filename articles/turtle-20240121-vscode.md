---
title: "VSCodeのはじめ方：Pythonで楽しく学びながら時短ショートカットと拡張機能で広がる世界！"
emoji: "🐢"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [vscode]
published: false
---
テストテスト

## 環境を作ろう

### Pythonのインストール

### VSCodeのインストール

https://gammasoft.jp/blog/how-to-start-visual-studio-code-for-python/

## 使ってみよう

## 便利その１：ショートカット

| キー入力                   | 説明                                           | 解説画像（クリックで拡大表示）                                             |
|------------------------|----------------------------------------------|-------------------------------------------------------------|
| Ctrl + l（エル）           | 現在の行を選択                                      | ![l](/images/turtle-20240121-vscode/s_ctrl_l.gif)           |
| Ctrl + /               | 現在の行をコメントアウト/解除                              | ![slash](/images/turtle-20240121-vscode/s_commnet.gif)      |
| Ctrl + c,<br>Ctrl + v  | 現在の行をコピー/貼り付け<br>(**行選択不要でコピーできる！**)         | ![cv](/images/turtle-20240121-vscode/s_ctrl_cv.gif)         |
| Ctrl + d               | 選択した文字と同じ文字を次々に選択<br>(**選択した文字はまとめて編集できる！**) | ![d](/images/turtle-20240121-vscode/s_ctrl_d.gif)           |
| Alt + <br>上下キー         | 現在の行を上下に移動                                   | ![arrow](/images/turtle-20240121-vscode/s_alt_arrow.gif)    |
| Ctrl + <br>Shift + p   | コマンドパレットを開く<br>(設定などVSCodeの各種機能へのアクセスツール)    | ![set](/images/turtle-20240121-vscode/s_settings.png)       |
| Ctrl + @               | ターミナルを開く<br>(プログラム実行やファイル管理等のコマンド実行ツール)      | ![atmark](/images/turtle-20240121-vscode/s_ctrl_atmark.png) |
| Ctrl + <br>Shift + o   | 指定シンボル(関数、定義等)に移動                            | ![o](/images/turtle-20240121-vscode/s_ctrl_shift_o.png)     |
| Ctrl + k,<br>Ctrl + 0  | すべての領域を折りたたみ                                 | ![k0j](/images/turtle-20240121-vscode/s_ctrl_k0j.gif)       |
| Ctrl + k,<br> Ctrl + j | すべての領域を展開                                    | (同上)                                                        |
| Ctrl + k,<br>Ctrl + [  | 現在の領域を折りたたみ<br>(選択した関数、メソッドのみ折りたたみ)          | ![close](/images/turtle-20240121-vscode/s_ctrl_close.png)   |
| Ctrl + k,<br>Ctrl + ]  | 現在の領域を展開<br>(選択した関数、メソッドのみ展開)                | ![open](/images/turtle-20240121-vscode/s_ctrl_open.png)     |

## 便利その２：拡張機能

### プログラミング言語とAI支援

プログラミング言語に関連する拡張機能と、AIを活用したコード生成や補完などの機能を提供する拡張機能です。

| 拡張名                                                                        | 説明                                          | 解説画像<br>（クリックで拡大表示）                               |
|----------------------------------------------------------------------------|---------------------------------------------|---------------------------------------------------|
| ![e](/images/turtle-20240121-vscode/e_python.png)<br>Python                | コードの補完やフォーマット、デバッグ、テストなどPythonの開発をサポートする。   | ![l](/images/turtle-20240121-vscode/s_ctrl_l.gif) |
| ![e](/images/turtle-20240121-vscode/e_c.png)<br>C/C++                      | コードの補完やフォーマット、デバッグ、テストなどC/C++の開発をサポートする。    |                                                   |
| ![e](/images/turtle-20240121-vscode/e_ros.png)<br>ROS                      | ROSというロボット開発のための拡張機能。プロジェクトの作成、デバッグなどを支援する。 |                                                   |
| ![e](/images/turtle-20240121-vscode/e_python.png)<br>Pylint                | コードのスタイルやエラー、リファクタリングの提案など品質をチェックする         |                                                   |
| ![e](/images/turtle-20240121-vscode/e_python.png)<br>Pylance               | Pythonのコードの補完やエラーチェックを高速化してくれる拡張機能          |                                                   |
| ![e](/images/turtle-20240121-vscode/e_python.png)<br>yapf                  | Pythonのコードを保存時に自動で整形してくれる便利なツール。            |                                                   |
| ![e](/images/turtle-20240121-vscode/e_python.png)<br>Mypy<br>Type Checker  | 型エラーや警告が表示し、 Pythonの型チェックをする。               |                                                   |
| ![e](/images/turtle-20240121-vscode/e_python.png)<br>isort                 | Pythonのインポート文を整理し、保存時に保存時に自動で整形する。          |                                                   |
| ![e](/images/turtle-20240121-vscode/e_pilot.png)<br>GitHub Copilot         | AIがコードを自動生成、候補として表示する。一度使いだすと手放せません！        |                                                   |
| ![e](/images/turtle-20240121-vscode/e_pilot.png)<br>GitHub Copilot<br>Chat | AIとチャットしながらコードを書ける。この機能の充実によりさらに使いやすくなりました。 |

### リモート開発とGit

リモートサーバーや仮想マシンに接続して、VSCode上でコードを編集や実行ができる拡張機能と、Gitと連携して、バージョン管理やコミット履歴などの機能を提供する拡張機能です。

| 拡張名                                                                                        | 説明                                                    | 解説画像<br>（クリックで拡大表示）                               |
|--------------------------------------------------------------------------------------------|-------------------------------------------------------|---------------------------------------------------|
| ![e](/images/turtle-20240121-vscode/e_ssh.png)<br>Remote<br> - SSH                         | SSHという仕組みで遠隔のPCに接続し、VSCode上でコードを編集できる。よく使います！         | ![l](/images/turtle-20240121-vscode/s_ctrl_l.gif) |
| ![e](/images/turtle-20240121-vscode/e_ssh.png)<br>Remote<br> - SSH<br>Editing<br>Configura | 上記同様、SSHで遠隔のPCに接続し、VSCode上でファイルを編集できる。                |                                                   |
| ![e](/images/turtle-20240121-vscode/e_remote.png)<br>Remote<br>Explorer                    | リモート開発のための拡張機能の一覧を表示する。                               |                                                   |
| ![e](/images/turtle-20240121-vscode/e_graph.png)<br>Git Graph                              | コードの履歴や変更点、ブランチやコミットなどをグラフィカルに表示、操作できる。コレ無しは考えられませ！   |                                                   |
| ![e](/images/turtle-20240121-vscode/e_lens.png)<br>Git Lens                                | こちらもGitのコミット履歴をグラフ表示します。私は、コード上で誰が変更したか確認する機能をよく使います。 |

### ドキュメンテーション

Markdownファイルの編集やプレビューなどの機能を提供する拡張機能です。ドキュメンテーションの作成や管理を助けることができます。

| 拡張名                                                                               | 説明                                                           | 解説画像<br>（クリックで拡大表示）                               |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------|---------------------------------------------------|
| ![e](/images/turtle-20240121-vscode/e_uml.png)<br>PlantUML                        | テキストベースでUML図を作成できる。作図の際に配置に頭を悩ませる必要ないので便利！                   | ![l](/images/turtle-20240121-vscode/s_ctrl_l.gif) |
| ![e](/images/turtle-20240121-vscode/e_markall.png)<br>Markdown<br>All in One      | テーブルやリスト、見出し、リンクなど、Markdownの編集を楽にする。                         |                                                   |
| ![e](/images/turtle-20240121-vscode/e_marklint.png)<br>markdown<br>lint           | Markdownの文法やスタイルをチェックしてくれる。                                  |                                                   |
| ![e](/images/turtle-20240121-vscode/e_excel.png)<br>Excel to<br>Markdown<br>table | クリップボードにコピーしたExcelのデータをMarkdownのテーブルに変換する。今まさにこの表づくりに使っています。 |                                                   |
| ![e](/images/turtle-20240121-vscode/e_docs.png)<br>auto<br>Docstring              | Pythonの関数やクラスにドキュメント文字列を自動生成する。                              |                                                   |
| ![e](/images/turtle-20240121-vscode/e_zenn.png)<br>Zenn Editor                    | Markdownで記述した内容をZenn記事プレビューする。この拡張のおかげでこうしてVSCodeでブログ書けています。 |

### ユーティリティ

コードのスナップショットやタスク管理など、開発作業を補助する機能を提供する拡張機能です。開発効率や品質を向上させることができます。

| 拡張名                                                                    | 説明                                               | 解説画像<br>（クリックで拡大表示）                               |
|------------------------------------------------------------------------|--------------------------------------------------|---------------------------------------------------|
| ![e](/images/turtle-20240121-vscode/e_tree.png)<br>Todo Tree           | コード内のTODOやFIXMEなどでコメントを残すと、それらをツリー形式で表示する。       | ![l](/images/turtle-20240121-vscode/s_ctrl_l.gif) |
| ![e](/images/turtle-20240121-vscode/e_count.png)<br>VS Code<br>Counter | VSCodeのプロジェクト内のコードの行数や文字数などを瞬時にカウントする。           |                                                   |
| ![e](/images/turtle-20240121-vscode/e_img.png)<br>Paste Image          | クリップボードの画像をVSCodeのエディタに貼り付ける。ブログやReadme作成で活躍します。 |

## まとめ

:::message alert
記載する
:::

## リンク

### 環境

WindowsのVSCode、Python環境についてもう少し掘り下げてみたい方は、次のサイトを見てみてください。私も知らないことが色々とあり、勉強になりました！

https://qiita.com/SAITO_Keita/items/ddcde4fdcdf5e5eaa933

### Python学習

Pythonの知識を深めたい方は、次のサイトがオススメです。  
私は会社などでPythonを初めて触る人に教える場合、こちらのサイトを見ながら勉強会を行っています。入門、基礎から応用へと段階を踏んで学習できます。初めての方は、まず入門、基礎を一通りやるとPythonがどういうものか分かってくると思います！

https://www.python-izm.com/

私はこちらの本でPythonの知識を習得しました。  
最近は、各種テックブログや上記のような学習サイトありますが、やはりいつでもサクッと読め、体系的にまとまった書籍は1冊手元にあると便利です！

https://amzn.asia/d/3Ipg0EM
