SHELL=/bin/bash -euo pipefail

install-python:
	poetry install

install-node:
	npm install

pre-commit-hook:
	cp scripts/pre-commit .git/hooks/pre-commit

install: install-node install-python pre-commit-hook

lint:
	npm run lint
	find . -name '*.py' -not -path '**/.venv/*' | xargs poetry run flake8

clean:
	rm -rf build
	rm -rf dist

publish: clean
	mkdir -p build
	npm run publish 2> /dev/null

serve:
	npm run serve

check-licenses:
	npm run check-licenses
	scripts/check_python_licenses.sh

format:
	poetry run black **/*.py

start-sandbox:
	cd sandbox && npm run start

build-proxy:
	scripts/build_proxy.sh

copy-examples:
	#cp -r  specification/examples docker/receiver/src/routes/examples

_dist_include="pytest.ini poetry.lock poetry.toml pyproject.toml Makefile build/. tests"

release: clean copy-examples publish build-proxy
	mkdir -p dist
	for f in $(_dist_include); do cp -r $$f dist; done

test:
#	this target should be used for local unit tests ..  runs as part of the build pipeline
	#make --no-print-directory -C sandbox test

smoketest:
#	this target is for end to end smoketests this would be run 'post deploy' to verify an environment is working
	poetry run pytest -v --junitxml=smoketest-report.xml -s -m smoketest
