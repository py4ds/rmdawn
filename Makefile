.PHONY: clean clean-test clean-pyc clean-build docs help env test lint git patch minor major dist release

ENV = venv
PYTHON = .venv/bin/python3
LINTER = black
DOCS = $(wildcard docs/source/*.rst docs/source/*.md docs/source/*.ipynb)
TESTS = $(wildcard tests/*.py)
SRC = $(wildcard src/rmdawn/*.py)


init: .git/
env: .venv/bin/activate
docs: docs/index.html
patch-release: patch release


.venv/bin/activate: requirements_dev.txt
ifneq ($(ENV), $(filter $(ENV),conda venv))
	pip install $(ENV)
endif
ifeq ($(ENV), $(filter $(ENV),virtualenv venv))
	test -d .venv || python -m $(ENV) .venv
endif
ifeq ($(ENV), conda)
	test -d .venv || conda create -yp .venv python=3
endif
ifeq ($(ENV), pipenv)
	test -d .venv || pipenv --three
	pipenv install pip
	pipenv install --requirement requirements_dev.txt
else
	${PYTHON} -m pip install --requirement requirements_dev.txt
endif
	touch .venv/bin/activate

test: env
ifeq ($(ENV), pipenv)
	pipenv install pytest-mypy
else
	${PYTHON} -m pip install pytest-mypy
endif
	${PYTHON} -m pytest src tests

lint: env
ifeq ($(ENV), pipenv)
	pipenv install $(LINTER)
else
	${PYTHON} -m pip install $(LINTER)
endif
	${PYTHON} -m $(LINTER) src tests

travis: .travis.yml
	.venv/bin/travis encrypt --add deploy.password

docs/index.html: $(DOCS) $(TESTS) $(SRC) ## generate Sphinx HTML documentation, including API docs
	mv docs html
	sphinx-apidoc -fo html/source src/rmdawn
	sphinx-apidoc -fo html/source --tocfile tests tests
	sphinx-build -M html html/source .
	mv html docs
	open docs/index.html

git:
	git add --all
	[ -z "`git status --porcelain`" ] || git commit -am "Bump version from `python setup.py --version`"
	git push


patch: git
	bumpversion patch
	git push

minor: git
	bumpversion minor
	git push

major: git
	bumpversion major
	git push



clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source rmdawn -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python setup.py sdist bdist_wheel

install: clean ## install the package to the active Python's site-packages
	python setup.py install
