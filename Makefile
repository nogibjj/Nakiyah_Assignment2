install:
	pip install --upgrade pip && pip install -r Requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

test:
	python3 -m pytest -cov=main_file test_file.py

all: install format lint test