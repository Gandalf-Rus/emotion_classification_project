VENV = venv
PYTHON = python3
PIP = $(VENV)/bin/pip
JUPYTER = $(VENV)/bin/jupyter

.PHONY: venv install freeze activate clean start_jupyter

venv:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip

install: venv
	test -f requirements.txt && $(PIP) install -r requirements.txt || echo "requirements.txt not found"

freeze:
	$(PIP) freeze > requirements.txt

activate:
	@echo "To activate the virtual environment, run: source $(VENV)/bin/activate"

clean:
	rm -rf $(VENV)

start_jupyter: venv
	$(JUPYTER) notebook --no-browser