---
title: "VSCodeのはじめ方：Pythonで楽しく学びながら時短ショートカットと拡張機能で広がる世界！"
emoji: "🐢"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [vscode]
published: false
---


## VSCodeでPythonを動かす準備をする

https://gammasoft.jp/blog/how-to-start-visual-studio-code-for-python/

## VSCodeでPythonプログラム楽しむ

## ショートカットと拡張機能で広がる世界

### ショートカット

| キー入力               | 説明                                                                                                                               | 解説画像<br>（クリックで拡大表示）                          |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Ctrl + l（エル）       | **現在の行を選択**<br>カーソルが当たっている行を即選択できる。                                                                     | ![l](/images/turtle-20240121-vscode/s_ctrl_l.gif)           |
| Ctrl + /               | **現在の行をコメントアウト/解除**<br>動作確認時コメントアウトによく使う。<br>複数行一括でコメントアウトできる。                    | ![slash](/images/turtle-20240121-vscode/s_commnet.gif)      |
| Ctrl + c,<br>Ctrl + v  | **現在の行をコピー/貼り付け**<br>前の処理を残しつつ、新しい処理を追加する際によく使う。                                            | ![cv](/images/turtle-20240121-vscode/s_ctrl_cv.gif)         |
| Ctrl + d               | **選択した文字と同じ文字を次々に選択**<br>選択した文字は一括編集できる！<br>限られたスコープで文字を置換したいとに重宝。           | ![d](/images/turtle-20240121-vscode/s_ctrl_d.gif)           |
| Alt + <br>上下キー     | **現在の行を上下に移動**<br>処理やデータ順序を変更したいときに使用。                                                               | ![arrow](/images/turtle-20240121-vscode/s_alt_arrow.gif)    |
| Ctrl + <br>Shift + p   | **コマンドパレットを開く**<br>(＝設定などVSCodeの各種機能へのアクセスツール)<br>慣れると様々な機能に即アクセスできる！             | ![set](/images/turtle-20240121-vscode/s_settings.png)       |
| Ctrl + @               | **ターミナルを開く**<br>(＝プログラム実行やファイル管理等のコマンド実行ツール)<br>ソフトを切り替えることなくターミナルを利用可能。 | ![atmark](/images/turtle-20240121-vscode/s_ctrl_atmark.png) |
| Ctrl + <br>Shift + o   | **指定シンボル(関数、定義等)に移動**<br>サクッと目的の関数や定義にアクセスできる。                                                 | ![o](/images/turtle-20240121-vscode/s_ctrl_shift_o.png)     |
| Ctrl + k,<br>Ctrl + 0  | **すべての領域を折りたたみ**<br>関数をざっと眺めたいとき、<br>集中して目的の関数に取り組みたいときに使う。                         | ![k0j](/images/turtle-20240121-vscode/s_ctrl_k0j.gif)       |
| Ctrl + k,<br> Ctrl + j | **すべての領域を展開**                                                                                                             | (同上)                                                      |
| Ctrl + k,<br>Ctrl + [  | **現在の領域を折りたたみ**<br>(選択した関数、メソッドのみ折りたたみ)                                                               | ![close](/images/turtle-20240121-vscode/s_ctrl_close.png)   |
| Ctrl + k,<br>Ctrl + ]  | **現在の領域を展開**<br>(選択した関数、メソッドのみ展開)                                                                           | ![open](/images/turtle-20240121-vscode/s_ctrl_open.png)     |

### 拡張機能

#### プログラミング言語とAI支援

プログラミング言語に関連する拡張機能と、AIを活用したコード生成や補完などの機能を提供する拡張機能です。

| 拡張名                                                                     | 説明                                                                                             | 解説画像<br>（クリックで拡大表示）                  |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------- |
| ![e](/images/turtle-20240121-vscode/e_python.png)<br>Python                | Pythonコードの実行やデバッグなど開発に必要な基本機能を提供する。必須の拡張機能。                 | －                                                  |
| ![e](/images/turtle-20240121-vscode/e_python.png)<br>Pylint                | Pythonコードのスタイル(見やすさ)やエラーチェック、リファクタリング提案をし品質を向上する。       | ![l](/images/turtle-20240121-vscode/ee_pylint.png)  |
| ![e](/images/turtle-20240121-vscode/e_python.png)<br>Pylance               | Pythonコードの入力補完やエラーチェックの高速化など、開発体験を向上する。                         | ![l](/images/turtle-20240121-vscode/ee_pylance.png) |
| ![e](/images/turtle-20240121-vscode/e_python.png)<br>yapf                  | Pythonコードをスタイル(見やすさ)に沿って、保存時に自動で整形する。                               | ![l](/images/turtle-20240121-vscode/ee_yapf.gif)    |
| ![e](/images/turtle-20240121-vscode/e_python.png)<br>Mypy<br>Type Checker  | Pythonコードの変数や引数の型チェックを行い、エラーを警告表示する。                               | ![l](/images/turtle-20240121-vscode/ee_mypy.png)    |
| ![e](/images/turtle-20240121-vscode/e_python.png)<br>isort                 | Pythonコードのインポート文を整理し、保存時に自動で整形する。                                     | ![l](/images/turtle-20240121-vscode/ee_isort.gif)   |
| ![e](/images/turtle-20240121-vscode/e_pilot.png)<br>GitHub Copilot         | AIがコードを記述する際に学習データに基づいて自動的にコードを提案、表示する。                     |                                                     |
| ![e](/images/turtle-20240121-vscode/e_pilot.png)<br>GitHub Copilot<br>Chat | AIとチャットしながらコードに対して質問、要求できる。また、コードの提案も行い、すぐに反映できる。 |

#### リモート開発とGit

リモートサーバーや仮想マシンに接続して、VSCode上でコードを編集や実行ができる拡張機能と、Gitと連携して、バージョン管理やコミット履歴などの機能を提供する拡張機能です。

| 拡張名                                                             | 説明                                                                                         | 解説画像<br>（クリックで拡大表示）                   |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| ![e](/images/turtle-20240121-vscode/e_graph.png)<br>Git Graph      | Gitのコードの変更の履歴や、ブランチやコミットなどをグラフィカルに表示、操作できる。          | ![l](/images/turtle-20240121-vscode/ee_gitgraph.png) |
| ![e](/images/turtle-20240121-vscode/e_lens.png)<br>Git Lens        | Git Graph同様グラフィカルな表示が可能。コード上で1行ごとに誰がいつ変更したかの確認もできる。 | ![l](/images/turtle-20240121-vscode/ee_gitlens.png)  |
| ![e](/images/turtle-20240121-vscode/e_ssh.png)<br>Remote<br> - SSH | SSHという仕組みで遠隔PCに接続し、VSCode上で遠隔PC上のコードを編集できる。                    | －                                                   |

#### ドキュメンテーション

Markdownファイルの編集やプレビューなどの機能を提供する拡張機能です。ドキュメンテーションの作成や管理を助けることができます。

| 拡張名                                                                            | 説明                                                                             | 解説画像<br>（クリックで拡大表示）                   |
| --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------- |
| ![e](/images/turtle-20240121-vscode/e_docs.png)<br>auto<br>Docstring              | Pythonの関数やクラスにドキュメント文字列（コメント）を自動生成する。             | ![l](/images/turtle-20240121-vscode/ee_string.gif)   |
| ![e](/images/turtle-20240121-vscode/e_markall.png)<br>Markdown<br>All in One      | Markdown記法の見出しやリンク、リスト、テーブルなど編集を便利にサポートする。     | －                                                   |
| ![e](/images/turtle-20240121-vscode/e_marklint.png)<br>markdown<br>lint           | Markdown記法の文法やスタイルをチェックして、警告を表示する。                     | ![l](/images/turtle-20240121-vscode/ee_marklint.png) |
| ![e](/images/turtle-20240121-vscode/e_excel.png)<br>Excel to<br>Markdown<br>table | クリップボードにコピーしたExcelデータをMarkdown記法のテーブルに変換する。        | －                                                   |
| ![e](/images/turtle-20240121-vscode/e_uml.png)<br>PlantUML                        | テキストベースでシーケンス図やフローチャートなどのUML図を作成できる。            | ![l](/images/turtle-20240121-vscode/ee_plant.png)    |
| ![e](/images/turtle-20240121-vscode/e_zenn.png)<br>Zenn Editor                    | ブログ(Zenn)執筆をサポートする。プレビュー表示などコンテンツを快適に作成できる。 | ![l](/images/turtle-20240121-vscode/ee_zenn.png)     |

#### ユーティリティ

コードのスナップショットやタスク管理など、開発作業を補助する機能を提供する拡張機能です。開発効率や品質を向上させることができます。

| 拡張名                                                                 | 説明                                                                                     | 解説画像<br>（クリックで拡大表示）                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------- |
| ![e](/images/turtle-20240121-vscode/e_tree.png)<br>Todo Tree           | コード内TODOやFIXMEなどでコメントを残すと、それらをツリー形式で表示する。                | ![l](/images/turtle-20240121-vscode/ee_tree.png)  |
| ![e](/images/turtle-20240121-vscode/e_count.png)<br>VS Code<br>Counter | VSCodeのプロジェクト内のコードの行数(規模)や変更点を簡単に把握することができる。         | ![l](/images/turtle-20240121-vscode/ee_count.png) |
| ![e](/images/turtle-20240121-vscode/e_img.png)<br>Paste Image          | クリップボードの画像をエディタに張り付けると、画像保存し、リンクをエディタに貼り付ける。 | －                                                |

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
