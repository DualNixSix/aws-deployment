# makefile - some adjustments might be needed based on computer speed when testing. I used WSL and Docker desktop. 

# make reset
reset:
	docker compose down -v
	sleep 2.5
	docker system prune -a
	sleep 2.5
	docker compose up -d 
	sleep 3.5
	docker compose exec api python manage.py makemigrations
	sleep 2
	docker compose exec api python manage.py migrate
	sleep 2
	docker compose exec -T api python manage.py shell < setup_data.py
	sleep 2
	docker ps
	sleep 1
	docker compose exec api python manage.py createsuperuser

# make run
run:
	docker compose up -d
	sleep 3
	docker ps
#	sleep 1
#   docker ps -a 

# make migrations
migrate:
	docker compose exec api python manage.py makemigrations 
	sleep 2
	docker compose exec api python manage.py migrate

# make seed
seed:
	docker compose exec -T api python manage.py shell < setup