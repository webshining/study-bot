run: 
	python app.py
compose: 
	docker-compose up -d
logs: 
	docker-compose logs app
rebuild: 
	docker-compose up -d --build --no-deps --force-recreate
mongosh: 
	docker-compose exec mongo mongosh