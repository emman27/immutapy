test:
	pipenv run pytest

cover:
	pipenv run pytest --cov=immutable

build:
	pipenv run python setup.py sdist
