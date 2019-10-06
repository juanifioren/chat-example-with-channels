[![N|Solid](https://i.postimg.cc/1zkVbLV8/test.png)](#)

This project is chat real-time application using websockets on Django. Is only implementing a few features, use it for learning purposes. The main software stack used to build the chat application is:
 - Python 3 (latest stable version).
 - Django 2.2 (latest stable version).
 - Postgres 11.
 - Redis 5.

For setting up all these requirements I use docker​ and docker-compose​ . Also create a ​ Makefile to easily manage the most useful docker-compose commands. To provide a real-time chat experience I implement Django-channels to support not only HTTP, but also WebSocket communications between clients browsers and our server.

## Features

Most important features are:
 - Login and logout re-using Django auth views.
 - List of all users to chat with.
 - Real time chat with another user and save every message on database to keep the history.

## Usage

You just need ​Docker​ and ​docker-compose​ installed on your machine then:

```
$ make build
$ make up
```

Now go to ​http://localhost:8000/​ or ​http://127.0.0.1:8000/. Now the site is running but we need create run our django migrations and create some users (I recommend you to create at least 3) to really test the chat app, so:

```
$ make manage CMD="migrate"
$ make manage CMD="createsuperuser"
$ make up
```

## Testing

Also includes Pytest suite already configured with a simple test trying to connect to the websocket and flake8 as a linter for analyzing source code to flag programming errors, bugs or any stylistic errors:

```
$ make pytest
$ make flake8
```

_Created by Juan Ignacio Fiorentino. 2019_
