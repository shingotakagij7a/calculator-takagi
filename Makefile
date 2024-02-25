.PHONY: build run test

build:
	docker build -t myapp .

run: build
	docker run --rm myapp python -m calculator_cli.main "$(EXPR)"

run_scale: build
	docker run --rm myapp python -m calculator_cli.main --scale "$(SCALE)" "$(EXPR)"

run_interactive: build
	docker run --rm -it myapp python -m calculator_cli.main --interactive

run_interactive_scale: build
	docker run --rm -it myapp python -m calculator_cli.main --interactive --scale "$(SCALE)"

lint: build
	docker run --rm myapp flake8 ./calculator_cli

format: build
	docker run --rm myapp black ./calculator_cli

test: build
	docker run --rm myapp pytest -c tox.ini

coverage: build
	docker run --rm myapp pytest -c tox.ini --cov=./calculator_cli

before_commit: lint test
