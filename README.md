![GitHub last commit](https://img.shields.io/github/last-commit/shingotakagij7a/calculator-takagi)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-pr/shingotakagij7a/calculator-takagi)
![GitHub top language](https://img.shields.io/github/languages/top/shingotakagij7a/calculator-takagi)
![GitHub repo size](https://img.shields.io/github/repo-size/shingotakagij7a/calculator-takagi)
[![ci](https://github.com/shingotakagij7a/calculator-takagi/actions/workflows/ci.yml/badge.svg)](https://github.com/shingotakagij7a/calculator-takagi/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/shingotakagij7a/calculator-takagi/graph/badge.svg?token=42UWIQY2RI)](https://codecov.io/gh/shingotakagij7a/calculator-takagi)

# Calculator

このアプリケーションは、コーディング面接の課題のために開発されたシンプルな計算機です。基本的な算術演算を行い、コマンドラインインターフェースを介してユーザーの入力に応じて計算結果を表示します。

## Functionality

- 基本的な算術演算（足し算、引き算、掛け算、割り算）
- コマンドラインインターフェースを通じた式の入力と結果表示
- 結果の小数点以下の桁数指定（スケールオプション）

## For Users

### Requirements

動作確認済みの環境:

- Python 3.8

他は `requirements.txt` を参照してください。

### Setup

プロジェクトをローカルで実行するためには、以下の手順に従ってください。

```bash
git clone https://github.com/your-username/calculator-takagi.git
cd calculator-takagi
```

必要なライブラリをインストールします。

```bash
pip install -r requirements.txt
```

### Usage

```bash
python -m calculator_cli <expression> [--scale <scale>] [--interactive]

positional arguments:
  expression                Mathematical expression to evaluate

optional arguments:
  -h, --help                show this help message and exit
  -i, --interactive         Run in interactive mode
  -s SCALE, --scale SCALE   Scale for rounding the result
```

## For Developers

### Requirements

動作確認済みの環境:

- Docker v20.10.16

### Setup

プロジェクトをローカルで実行するためには、以下の手順に従ってください。

```bash
git clone https://github.com/your-username/calculator-takagi.git
cd calculator-takagi
```

### Usage

#### 実行

```bash
# EXPR: 計算式
# SCALE: 結果の小数点以下の桁数
make run EXPR=<expression>
make run_scale EXPR=<expression> SCALE=<scale>
make run_interactive
make run_interactive_scale SCALE=<scale>
```

#### コードの静的解析（Lint）

```bash
make lint
```

#### コードのフォーマット

```bash
make format
```

#### テストの実行

```bash
make test
```

#### カバレッジレポートの生成

```bash
make coverage
```

#### コミット前のチェック

lint, format, test を実行します。

```bash
make before_commit
```

`make before_commit` は、コミット前に実行するためのフックを設定することを推奨します。

```bash
git config --local core.hooksPath .githooks
chmod +x .githooks/pre-commit
```

### アーキテクチャ

このアプリケーションは、以下のコンポーネントで構築されています。

- **Controller**: エントリーポイントからの指示を受け取り、他のコンポーネントを呼び出します。
- **Service**: 算術演算のロジックを担当します。
- **View**: ユーザーの指定したオプションに応じて表示を整形し、結果を返却します。

依存関係は [アーキテクチャ図](docs/architecture.drawio) を参照。
