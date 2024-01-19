FROM python:3.8-buster

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY app/templates /app/templates
COPY app/models.py /app/models.py
COPY app/app.py app/app.py
COPY app/migrations app/migrations
COPY gunicorn.config.py  gunicorn.config.py

WORKDIR /app

ENV FLASK_APP app.py
EXPOSE 5000

CMD sleep 2 && flask db upgrade && gunicorn -c ../gunicorn.config.py app:app
