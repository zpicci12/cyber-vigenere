make:
	@echo To encode: \"make encode plaintext key\"
	@echo To decode: \"make decode ciphertext key\"

run:
	python3 Vigenere.py $(ARGS)
