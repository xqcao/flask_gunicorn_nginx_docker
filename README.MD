# create python flask app
```
--static/
--templates/
  index.html
__init__.py
my_app.py
users.py
requirements.txt
```
# create wsgi.py
```
create wsgi.py or just use my_app.py
and call my_app:app to execute it
```

# gunicorn_start.sh for command execute
```
gunicorn -w 2 --bind 0.0.0.0:5001 wsgi:app 
```

# create Dockerfile and docker-compose.yaml

# build and run
```
docker-compose up --build
docker-compose rm
```