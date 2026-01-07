WEB=web

up:
	docker compose up -d

up-dev:
	docker compose up

down:
	docker compose down

build:
	docker compose build

makemigrations:
	docker compose exec $(WEB) python manage.py makemigrations

migrate:
	docker compose exec $(WEB) python manage.py migrate

superuser:
	docker compose exec $(WEB) python manage.py createsuperuser

logs:
	docker compose logs -f $(WEB)

test:
	docker compose exec $(WEB) python manage.py test

shell:
	docker compose exec $(WEB) bash

collectstatic: 
	docker compose exec $(WEB) python manage.py collectstatic --noinput
