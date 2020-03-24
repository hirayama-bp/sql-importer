.PHONY: lint fmt

lint:
	poetry run flake8 .
	@echo -e "\e[32;1mlint ok\e[m"

fmt:
	poetry run black .
	poetry run isort -y -rc .
	@echo -e "\e[32;1mfmt ok\e[m"
