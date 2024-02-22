.PHONY: build run test

build:
	docker build -t myapp .

run: build
	docker run myapp

lint: build
	docker run myapp flake8 ./app

format: build
	docker run myapp black ./app

test: build
	docker run myapp pytest

coverage: build
	docker run myapp pytest --cov=./app

before_commit: lint test
