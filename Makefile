.PHONY: run
run:
	python main.py

.PHONY: tests
tests:
	PYTHONPATH="$PYTHONPATH:$(shell pwd)" pytest

