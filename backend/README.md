# Robot Agent System - Phase 1 Backend Infrastructure

## 概要

自然言語でロボットを操るAIエージェントシステムのバックエンドAPI。Google Gemini 2.5 Flash、LangChain、ChromaDBを使用したRAGシステムの基盤となるFastAPIサーバーです。

## 技術スタック

- **Backend**: Python 3.8+, FastAPI
- **LLM**: Google Gemini 2.5 Flash
- **RAG Framework**: LangChain
- **Vector Database**: ChromaDB
- **OS**: Windows/Linux/macOS対応

## 必要な前提条件

- Python 3.8以上
- Google Cloud APIアカウント
- Git

## セットアップ手順

### 1. プロジェクトのクローン

```bash
git clone <repository-url>
cd zenn-contents/backend
```

### 2. 仮想環境の構築

#### Windows

```cmd
# 自動セットアップスクリプトの実行
setup_env.bat

# または手動セットアップ
python -m venv venv
venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
```

#### Linux/macOS

```bash
# 自動セットアップスクリプトの実行
./setup_env.sh

# または手動セットアップ
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. 環境変数の設定

1. `.env.example`を`.env`にコピー

```bash
cp .env.example .env
```

2. `.env`ファイルを編集し、必要なAPIキーを設定

```env
# Google Cloud API Configuration
GOOGLE_API_KEY=your_actual_google_api_key_here

# Server Configuration
HOST=0.0.0.0
PORT=8000
DEBUG=True

# CORS Configuration (フロントエンド接続用)
CORS_ORIGINS=["http://localhost:3000", "http://localhost:8080"]

# ChromaDB Configuration
CHROMA_PERSIST_DIRECTORY=./chroma_db
CHROMA_COLLECTION_NAME=robot_commands

# LangChain Configuration (オプション)
LANGCHAIN_TRACING_V2=false
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=your_langchain_api_key_here
LANGCHAIN_PROJECT=robot-agent-system
```

### 4. Google Cloud API設定

1. [Google Cloud Console](https://console.cloud.google.com/)にアクセス
2. 新しいプロジェクトを作成または既存のプロジェクトを選択
3. Gemini APIを有効化
4. APIキーを生成
5. 生成されたAPIキーを`.env`ファイルの`GOOGLE_API_KEY`に設定

## 開発サーバーの起動

### 自動起動スクリプト

#### Windows
```cmd
start_server.bat
```

#### Linux/macOS
```bash
./start_server.sh
```

### 手動起動

```bash
# 仮想環境をアクティベート
source venv/bin/activate  # Linux/macOS
# または
venv\Scripts\activate.bat  # Windows

# サーバー起動
python main.py
```

サーバーが起動すると、以下のURLでアクセスできます：

- API: http://localhost:8000
- インタラクティブドキュメント: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API エンドポイント

### Health Check
- **GET** `/health`
- システムの状態を確認

### Natural Language Processing
- **POST** `/process-instruction`
- 自然言語指示を処理してロボット制御コマンドに変換

#### リクエスト例

```json
{
  "instruction": "move forward",
  "context": "living room",
  "robot_id": "robot_001"
}
```

#### レスポンス例

```json
{
  "status": "success",
  "processed_instruction": "move forward",
  "robot_commands": {
    "action": "move",
    "direction": "forward",
    "distance": 1.0
  },
  "timestamp": "2024-01-01T12:00:00",
  "message": "Instruction 'move forward' processed successfully"
}
```

## プロジェクト構成

```
backend/
├── main.py                 # FastAPIアプリケーション
├── config.py              # 設定管理
├── requirements.txt       # Pythonパッケージ依存関係
├── .env.example          # 環境変数テンプレート
├── .env                  # 環境変数（作成必要）
├── setup_env.sh          # Linux/macOS用セットアップスクリプト
├── setup_env.bat         # Windows用セットアップスクリプト
├── start_server.sh       # Linux/macOS用起動スクリプト
├── start_server.bat      # Windows用起動スクリプト
├── venv/                 # Python仮想環境
└── chroma_db/            # ChromaDBデータ（自動生成）
```

## 開発時の注意事項

1. **仮想環境の使用**: 必ず仮想環境を使用してください
2. **環境変数**: 実際のAPIキーを設定してください
3. **CORS設定**: フロントエンドのURLを適切に設定してください
4. **デバッグモード**: 本番環境では`DEBUG=False`に設定してください

## トラブルシューティング

### Python仮想環境の問題

```bash
# 仮想環境を削除して再作成
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### パッケージインストールの問題

```bash
# pipをアップグレード
pip install --upgrade pip

# 依存関係を再インストール
pip install -r requirements.txt --force-reinstall
```

### APIキーの設定問題

1. `.env`ファイルが正しく作成されているか確認
2. Google Cloud APIキーが有効か確認
3. 必要なAPIが有効化されているか確認

## 次のフェーズ

Phase 2では以下の機能を実装予定：

- LangChainとGoogle Geminiの統合
- ChromaDBを使用したRAGシステム
- 実際のロボット制御コマンド生成
- 高度な自然言語理解機能

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 貢献

バグ報告や機能要求は、GitHubのIssuesにお願いします。