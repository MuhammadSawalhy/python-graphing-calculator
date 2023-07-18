.PHONY: run
run:
	python main.py

.PHONY: tests
tests:
	PYTHONPATH="$(shell pwd)" pytest tests

