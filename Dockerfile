FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /home/tree_menu/

COPY . /home/tree_menu/

RUN pip3 install poetry==1.2.1
RUN poetry install
RUN poetry run python manage.py collectstatic
CMD poetry run -vvv python3 manage.py migrate
CMD poetry run -vvv python3 manage.py loaddata db.json

CMD poetry run gunicorn --bind 0.0.0.0:8000 tree_menu.wsgi
