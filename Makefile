.PHONY: test test-lf lint fmt

test:
	poetry run pytest tests
	@echo -e "\e[32;1mtest ok\e[m"

test-lf:
	poetry run pytest --lf tests
	@echo -e "\e[32;1mtest-lf ok\e[m"

lint:
	poetry run flake8 .
	poetry run mypy --no-color .
	@echo -e "\e[32;1mlint ok\e[m"

fmt:
	poetry run black .
	poetry run isort -y -rc .
	@echo -e "\e[32;1mfmt ok\e[m"
