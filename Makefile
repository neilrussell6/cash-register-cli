-include .env
include ./_make/print.lib.mk

#------------------------------
# vars
#------------------------------

SHELL := /bin/bash
REQUIREMENTS_FILE := requirements
STR_TO_LOWERDASH := sed -e 's/\([A-Z]\)/-\L\1/g' -e 's/^-//' -e 's/\s-/-/g'
SOURCE_DIR := src
ENTRY_POINT := cli

#------------------------------
# help
#------------------------------

.PHONY: help
help:
	@$(call print_h1,"AVAILABLE","OPTIONS")
	@$(call print_space)
	@$(call print_options,"init","Install initial requirements and install script etc")
	@$(call print_space)
	@$(call print_h2,"dependency")
	@$(call print_options,"pipcompile","Compile requirements")
	@$(call print_options,"pipinstall","Install requirements")
	@$(call print_space)
	@$(call print_h2,"test")
	@$(call print_options,"test","Run all tests.")
	@$(call print_space)
	@$(call print_h2,"linting")
	@$(call print_options,"lint","Run Flake PEP8 linter.")
	@$(call print_space)
	@$(call print_h2,"cli")
	@$(call print_options,"version","Display app version.")

#------------------------------
# initialize
#------------------------------

.PHONY: init
init: initprint copyenv initpip pipcompile pipinstall install
	@$(call print_h1,"... success")

.PHONY: initprint
initprint:
	@$(call print_h1,"initializating ...")

.PHONY: copyenv
copyenv:
ifeq (,$(wildcard '.env'))
	@$(call print_h2,"creating env file")
	@cp .env.local .env
endif

.PHONY: initpip
initpip:
	@$(call print_h2,"installing pip")
	@pip install --upgrade pip
	@$(call print_h2,"installing piptools")
	@pip install pip-tools

#------------------------------
# dependency
#------------------------------

.PHONY: pipcompile
pipcompile:
# if called directly
ifeq ($(MAKECMDGOALS),pipcompile)
	@$(call print_h1,"compiling requirements ...")
	@pip-compile $(REQUIREMENTS_FILE).in
	@$(call print_h1,"... success")
# if called as dependency
else
	@$(call print_h2,"compiling requirements")
	@pip-compile $(REQUIREMENTS_FILE).in
endif

.PHONY: pipinstall
pipinstall:
# if was not called called directly (called as dependency)
ifneq ($(MAKECMDGOALS),pipinstall)
	@$(call print_h2,"installing requirements ...")
	@pip install -r $(REQUIREMENTS_FILE).txt
# requirements txt does not exists, so prompt user to run compile
else ifeq (,$(wildcard $(REQUIREMENTS_FILE).txt))
	$(error Requirements are not compiled run make pipcompile first)
# requirements txt exists, so install
else
	@$(call print_h1,"installing requirements ...")
	@pip install -r $(REQUIREMENTS_FILE).txt
	@$(call print_h1,"... success")
endif

#------------------------------
# cli
#------------------------------

.PHONY: install
install:
# if called directly
ifeq ($(MAKECMDGOALS),install)
	@$(call print_h1,"installing script ...")
	@pip install --editable .
	@$(call print_h1,"... success")
# if called as dependency
else
	@$(call print_h2,"installing script")
	@pip install --editable .
endif

#------------------------------
# test
#------------------------------

.PHONY: test
test:
	@$(call print_h1,"running all tests ...")
	@PYTHONPATH=./ py.test || true
	@$(call print_h1,"... complete")

#------------------------------
# linting
#------------------------------

.PHONY: lint
lint:
	@$(call print_h1,"linting code ...")
	@flake8 || true
	@$(call print_h1,"... complete")

#------------------------------
# cli
#------------------------------

.PHONY: version
version:
ifeq (,$(APP_COMMAND))
	$(error please set APP_COMMAND in .env)
else ifeq (myapp,$(APP_COMMAND))
	$(error please first run make init)
else
	@$(APP_COMMAND) --version
endif
