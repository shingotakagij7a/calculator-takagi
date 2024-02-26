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

#### Run

```bash
# EXPR: 計算式
# SCALE: 結果の小数点以下の桁数
make run EXPR=<expression>
make run_scale EXPR=<expression> SCALE=<scale>
make run_interactive
make run_interactive_scale SCALE=<scale>
```

#### Static Lint

```bash
make lint
```

#### Format Code

```bash
make format
```

#### Test

```bash
make test
```

#### Output Coverage

```bash
make coverage
```

#### Before Commit Checks

lint, format, test を実行します。

```bash
make before_commit
```

`make before_commit` は、コミット前に実行するためのフックを設定することを推奨します。

```bash
git config --local core.hooksPath .githooks
chmod +x .githooks/pre-commit
```

### Architecture

このアプリケーションは、以下のコンポーネントで構築されています。

- **Controller**: エントリーポイントからの指示を受け取り、他のコンポーネントを呼び出します。
- **Service**: 算術演算のロジックを担当します。
- **View**: ユーザーの指定したオプションに応じて表示を整形し、結果を返却します。

依存関係は [アーキテクチャ図](docs/architecture.drawio) を参照。

### Testing

#### Unit Test Strategy

テスト容易性の高い Service 層に対してはユニットテストを実装しています。
Service 層以下のコンポーネント(CalculatorService, Parser, Operator)に関してはカバレッジが 100% になるようにテストを実装しています。

```bash
make coverage

# Coverage Output on `0479c71` commit
---------- coverage: platform linux, python 3.8.18-final-0 -----------
Name                                                 Stmts   Miss  Cover
------------------------------------------------------------------------
calculator_cli/__init__.py                               0      0   100%
calculator_cli/__main__.py                              32     32     0%
calculator_cli/controller/__init__.py                    0      0   100%
calculator_cli/controller/calculator_controller.py      11     11     0%
calculator_cli/service/__init__.py                       0      0   100%
calculator_cli/service/calculator_service.py            36      0   100%
calculator_cli/service/lib/__init__.py                   0      0   100%
calculator_cli/service/lib/operator.py                  12      0   100%
calculator_cli/service/lib/parser.py                    33      0   100%
calculator_cli/view/__init__.py                          0      0   100%
calculator_cli/view/calculator_view.py                  12     12     0%
------------------------------------------------------------------------
TOTAL                                                  136     55    60%
```

#### Thought of Test Cases

入出力に関して以下の観点の組み合わせでテストケースを決定しています。また、これらのテストケースに含まれない要求を満たすために確認が必要なテストケースは別途追加しています。

- (入力)オペランド: 数字以外/定義域内の整数/定義域内の小数/定義域外の数値
- (入力)オペレータ: 加算/減算/乗算/除算/複数の組み合わせ/不適切な算術記号
- (入力)括弧の有無: 不適切な形式/有り/無し
- (出力)計算結果: 定義域内の整数/定義域内の小数/定義域外の数値/ゼロ除算

| 入力: オペランドの型 | 入力: 括弧の使用 | 入力: 算術記号               | 出力: 値の範囲 | テストケースの例  | 結果 |
| -------------------- | ---------------- | ---------------------------- | -------------- | ----------------- | ---- |
| 整数                 | なし             | 加算                         | 値域内         | "1 + 2"           | 成功 |
| 整数                 | なし             | 減算                         | 値域内         | "1 - 2"           | 成功 |
| 整数                 | なし             | 乗算                         | 値域内         | "2 \* 3"          | 成功 |
| 整数                 | なし             | 除算                         | 値域内         | "10 / 2"          | 成功 |
| 整数                 | あり、適切       | 複数の算術記号               | 値域内         | "(1 - 2) \* 3"    | 成功 |
| 小数                 | なし             | 加算                         | 値域内         | "0.1 + 0.2"       | 成功 |
| 小数                 | なし             | 乗算                         | 値域内         | "2.5 \* 4"        | 成功 |
| 不正な文字列         | -                | -                            | -              | "a"               | 失敗 |
| 整数                 | あり、不適切     | 任意の算術記号               | -              | "(1 + 2"          | 失敗 |
| 整数                 | なし             | 不適切な算術記号（比較など） | -              | "1 > 0"           | 失敗 |
| 整数                 | なし             | 除算                         | ゼロ除算       | "1 / 0"           | 失敗 |
| 整数                 | なし             | 加算                         | 値域外         | "1 + 1000000001"  | 失敗 |
| 整数                 | なし             | 減算                         | 値域外         | "1 + -1000000001" | 失敗 |
