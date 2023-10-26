# Makefile for the Machine Learning Project of Group "group03_ett"

# The default target.
.DEFAULT_GOAL := run

# Mark these as non-files.
.PHONY: build run gen-docs clean dbuild drun dbash

# Define Variables.
# ?= is used to only fill variable once.
# TAG ?= group03
# VERSION ?= latest
# IMAGE_NAME ?= predict-ett
# CONTAINER_NAME ?= predict-ett
# CONTAINER_INSTANCE ?= default

# docker build -t $(TAG)/$(IMAGE_NAME):$(VERSION) --file dockerfile .

# docker run parameters:
# -it: access container in an interactive mode.
# --rm: remove container after exit (currently not implemented).
# --volume: mount host machine folder. Syntax: hostFolder:containerFolder.
# --name: Give container a specific name.

# docker run -dit --rm --name ett-httpd -p 8080:80 533b0770883d
# docker run -it --rm --name $(CONTAINER_NAME) $(TAG)/$(IMAGE_NAME):$(VERSION)
# docker run -it --rm --name $(CONTAINER_NAME) $(TAG)/$(IMAGE_NAME):$(VERSION) bash

# Switched to docker-compose to better manage more then one container.
dbuild:
	docker-compose build

drun:
	docker-compose up

dbash:
	docker-compose run base bash


# "Normal" non-docker build settings to more quickly test things.
# Check the OS by searching for a Windows flag.
ifeq ($(OS),Windows_NT)
# Windows

# Has to be python NOT python3, otherwise normal python installations won't
# work correctly.
# To fix python2 and python3 errors, uninstall python2 or change the path
# variable to exclude python2.
build:
	if exist .venv rmdir /S /Q .venv
	python -m venv .venv
	.venv\Scripts\activate.bat
	pip3 install poetry
	poetry install

run:
	.venv\Scripts\activate.bat
	poetry run python3 group03_ett\main.py

gen-docs:
	.venv\Scripts\activate.bat
	pip3 install -r requirements-documentation.txt
	sphinx-apidoc -o docs group03_ett
	docs\make.bat html

clean:
	if exist .venv rmdir /S /Q .venv
	if exist docs\_build rmdir /S /Q docs\_build
else
# Linux

build:
	( \
		rm -rf .venv; \
		python3 -m venv .venv; \
		source .venv/bin/activate; \
		pip3 install poetry; \
		poetry install; \
	)

run:
	( \
		source .venv/bin/activate; \
		poetry run python3 group03_ett/main.py; \
	)

# Creating the Documentation within the docker container seems unwise as it
# would be very hard to read it without hosting a web server with port
# forwarding so we create a local python virtual enviroment for that.
gen-docs:
	( \
		source .venv/bin/activate; \
		pip3 install -r requirements-documentation.txt; \
		cd docs; \
		sphinx-apidoc -o . ../group03_ett/; \
		make html; \
	)

clean:
	rm -rf .venv
	rm -rf docs/_build/
endif
