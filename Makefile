start:
	docker-compose --env-file .env.prod up -d
	docker-compose exec django poetry run python manage.py makemigrations
	docker-compose exec django poetry run python manage.py migrate
	docker-compose exec django poetry run python manage.py collectstatic --noinput
stop:
	docker-compose down
build:
	docker-compose build
restart:
	docker-compose down
	docker-compose up -d
	docker-compose exec django poetry run python manage.py makemigrations
	docker-compose exec django poetry run python manage.py migrate
	docker-compose exec django poetry run python manage.py collectstatic --noinput
admin:
	docker-compose exec django poetry run python manage.py createsuperuser
sync: 
	docker-compose exec django poetry run python manage.py search_index --rebuild -f
