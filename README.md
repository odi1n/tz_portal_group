# Tz portal groups

[Service Kinopoisk](https://kinopoisk.dev/)

## Run

1. Git clone: `git clone PATH`
2. Open directory: `cd PATH`
3. Docker build-run: `docker-compose up --build`

### Warning

`WebSocket` - does not have authorization for convenient verification via a web page

## Infomation

Link - `localhost:8000`

|Link|Request|Info|
|:---|:---|:---|
|/|get|Main page - test websocket|
|/docs|get|Swagger docs project|
|/api/v1/numbers|get|Get remains value with list|
|/api/v1/number|get|Get remains value|
|/api/v1/kinopoisk|get|Get kinopoisk top5 movie|
|/api/v1/signup|post|Create new user|
|/api/v1/login|post|Create access_token for user|
|/api/v1/user|get|Get information user|
