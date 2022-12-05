# REST-API-Flask


Build Rest API using the lightweight python framework **Flask**.


To run the code:

```
docker build -t flaskapi_image .
docker run -d --rm -v "${PWD}:/app" --name flaskapi_container flaskapi_image
```


Or you can use ```docker-compose```
```
docker-compose up -d
```
Note: ```-d``` to put the model in the detached mode.

