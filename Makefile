.PHONY: build run test

build:
	docker build -t myapp .

run: build
	docker run --rm myapp

lint: build
	docker run --rm myapp flake8 ./calculator_cli

format: build
	docker run --rm myapp black ./calculator_cli

test: build
	docker run --rm myapp pytest -c tox.ini

coverage: build
	docker run --rm myapp pytest -c tox.ini --cov=./calculator_cli

before_commit: lint test
