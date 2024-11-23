run_server:
	poetry run python manage.py runserver 0.0.0.0:8080

migrate:
	poetry run python manage.py migrate

run_migrations_server: migrate run_server
#
#.PHONY: help
#
#help: # Run `make help` to get help on the make commands
#	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'