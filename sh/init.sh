docker compose up -d
sleep 3
docker ps
sleep 2
docker compose exec api python manage.py makemigrations 
sleep 2
docker compose exec api python manage.py migrate
sleep 2
docker compose exec -T api python manage.py shell < setup