# Docker stuff

- _linting_ - `docker-compose run --rm app sh -c "flake8"`
- _create django project_ - `docker-compose run --rm app sh -c "django-admin startproject app ."`
- _run tests_ - `docker-compose run --rm app sh -c "python manage.py test"`
