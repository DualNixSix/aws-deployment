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