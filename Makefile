build:
	docker build -t server .

test:
	docker-compose up -d
	pytest --disable-warnings || true
	docker-compose down

coverage:
	docker-compose up -d	
	pytest --cov-report term-missing --cov=src tests/
	docker-compose down
