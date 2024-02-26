.PHONY: build run run_scale run_interactive run_interactive_scale run_help test lint format coverage before_commit

build:
	docker build -t myapp .

run: build
	docker run --rm myapp python -m calculator_cli "$(EXPR)"

run_scale: build
	docker run --rm myapp python -m calculator_cli --scale "$(SCALE)" "$(EXPR)"

run_interactive: build
	docker run --rm -it myapp python -m calculator_cli --interactive

run_interactive_scale: build
	docker run --rm -it myapp python -m calculator_cli --interactive --scale "$(SCALE)"

run_help: build
	docker run --rm myapp python -m calculator_cli --help

lint: build
	docker run --rm myapp flake8 ./calculator_cli

format: build
	docker run --rm myapp black ./calculator_cli

test: build
	docker run --rm myapp pytest -c tox.ini

coverage: build
	docker run --rm myapp pytest -c tox.ini --cov=./calculator_cli

before_commit: lint test
