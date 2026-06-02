PYTHONPATH=src

.PHONY: verify test

verify:
	PYTHONPATH=$(PYTHONPATH) python scripts/verify_runtime_safety.py
	PYTHONPATH=$(PYTHONPATH) python scripts/verify_challenge_4.py
	PYTHONPATH=$(PYTHONPATH) python scripts/verify_data_hashes.py


test:
	PYTHONPATH=$(PYTHONPATH) python -m pytest -q
