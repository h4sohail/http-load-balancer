build:
	docker build -t server .

test:
	docker-compose up -d
	pytest --disable-warnings || true
	docker-compose down