run:
	docker-compose build
	docker-compose up -d
stop:
	docker-compose down
# `python-template` below should be renamed according to the corresponding service name in docker-compose.yml
enter:
	docker-compose exec python-template /bin/bash
start:
	docker-compose exec python-template poetry run start
test:
	docker-compose exec python-template poetry run test
lint:
	docker-compose exec python-template poetry run lint
format:
	docker-compose exec python-template poetry run format
log:
	docker-compose logs -f python-template
