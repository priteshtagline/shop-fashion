# shop-fashion

## Setup Project using Docker

First make sure you have installed `docker` and `docker-compose` on your machine.
https://docs.docker.com/get-docker/

1. Clone the project from git repository and move into the project directory.

```sh
git clone https://github.com/priteshtagline/shop-fashion.git
cd shop-fashion/
```

2. Then run the following command to setup project using docker:

```sh 
docker-compose up -d --build
```

3. Migrate the database

```sh
docker-compose exec web python manage.py migrate
```

4. Create a super user with following command; So you can login into the admin site:

```sh
docker-compose exec web python manage.py createsuperuser
```

5. Run the project in localhost

```sh 
docker-compose up
```

You can go to the http:///127.0.0.1:8000 to view the application running.