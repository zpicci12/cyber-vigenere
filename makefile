make:
	@echo To encode: make run ARGS=\"encode plaintext key\"
	@echo To decode: make run ARGS=\"decode ciphertext key\"

run:
	python3 Vigenere.py $(ARGS)
