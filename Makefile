
COMPOSE = docker-compose -f docker-compose.yaml

help:
	@echo "help               -- Print this help showing all commands.         "
	@echo "build              -- Build containers.                             "
	@echo "up                 -- Run the webserver.                            "
	@echo "manage             -- Run django 'manage.py' command.               "
	@echo "                      Ex. make manage CMD=\"migrate\"               "
	@echo "flake8             -- Run flake8 tool.                              "
	@echo "pytest             -- Run pytest tool.                              "

rmpyc:
	find . | grep -E "__pycache__|\.pyc|\.pyo" | xargs sudo rm -rf

build: rmpyc
	$(COMPOSE) build

up:
	$(COMPOSE) up

manage:
	$(COMPOSE) run --rm web python manage.py ${CMD}

flake8:
	$(COMPOSE) run --rm web /bin/bash -c "flake8 . --exclude migrations,settings.py --max-line-length 90"

pytest:
	$(COMPOSE) run --rm web /bin/bash -c "pytest ."

.PHONY: help rmpyc build up manage flake8 pytest
