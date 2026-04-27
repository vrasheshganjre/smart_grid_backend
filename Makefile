PYTHON ?= python3.13
VENV_DIR := .venv
PIP := $(VENV_DIR)/bin/pip
PY := $(VENV_DIR)/bin/python

.PHONY: venv install run test clean

venv:
	$(PYTHON) -m venv $(VENV_DIR)

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements-dev.txt

run: install
	$(VENV_DIR)/bin/uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

test: install
	$(VENV_DIR)/bin/pytest tests -q

clean:
	rm -rf $(VENV_DIR)
