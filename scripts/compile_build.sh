# copy source code to bin services
cp -r ./src/services/service1  ./build/service1;
cp -r ./src/services/service2  ./build/service2;
cp -r ./src/api-gateway        ./build/api-gateway;

# copy requirements.txt to build services
cp ./src/services/resources/requirements.txt ./build/service1/requirements.txt
cp ./src/services/resources/requirements.txt ./build/service2/requirements.txt

# copy app to build services
cp ./src/services/resources/app.py ./build/service1/app.py;
cp ./src/services/resources/app.py ./build/service2/app.py;

# copy config to build services
cp ./src/services/resources/config.py ./build/service1/config.py;
cp ./src/services/resources/config.py ./build/service2/config.py;

# Copy uwsgi.ini to build services
cp ./src/services/resources/uwsgi.ini ./build/service1/uwsgi.ini;
cp ./src/services/resources/uwsgi.ini ./build/service2/uwsgi.ini;

# copy models to build services
cp -r ./src/services/resources/models ./build/service1/models;
cp -r ./src/services/resources/models ./build/service2/models;

# copy Dockerfiles to build services 
cp ./docker/flask/Dockerfile ./build/service1/Dockerfile;
cp ./docker/flask/Dockerfile ./build/service2/Dockerfile;
cp ./docker/node/Dockerfile  ./build/api-gateway/Dockerfile;

# copy docker-compose files to build
cp ./docker/docker-compose.yml  ./build/docker-compose.yml