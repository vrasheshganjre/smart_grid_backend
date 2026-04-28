UV ?= uv
PYTHON ?= 3.12
HOST ?= 127.0.0.1
PORT ?= 8000

.PHONY: venv install run test clean

venv:
	$(UV) venv --python $(PYTHON)

install:
	$(UV) sync

run: install
	$(UV) run uvicorn app.main:app --reload --host $(HOST) --port $(PORT)

test: install
	$(UV) run pytest tests -q

clean:
	rm -rf .venv
