PYTHONPATH := $(shell pipenv --where)

install-dev-dependencies:
	@pipenv check && pipenv install

install-prod-dependencies:
	@pipenv check && pipenv install --dev

install-pre-commit:
	@pipenv run pre-commit install

configure-prod:
	@DJANGO_ENV=production pipenv run python manage.py check --deploy --fail-level WARNING
	@sed 's~workdir~$(CURDIR)~g;s~venvpath~$(PYTHONPATH)~g' \
	./config_templates/gunicorn.service.in > ./production/gunicorn.service

.env:
	@test ! -f .env && pipenv run dump-env -t config_templates/env.template -p 'SECRET_' > .env

check-env: .env
	@pipenv run dotenv-linter .env config_templates/env.template

setup-dev: install-dev-dependencies install-precommit .env
	@pipenv run python manage.py check

setup-prod: install-prod-dependencies .env

test:
	@pipenv run pytest

run-dev-server:
	@pipenv run manage.py runserver

shell:
	@pipenv run manage.py shell

.PHONY: setup-dev setup-prod run-dev-server shell test
