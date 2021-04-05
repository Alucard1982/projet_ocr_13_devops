FROM python:3.8

#créer un répertoire pour le projet
WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=config.settings.production \
    PORT=8000 \
    WEB_CONCURRENCY=3

ADD . /app

#récup les dépendances
COPY requirements.txt .

#install les dépendances
RUN pip install -r requirements.txt

#copy le code source
COPY . /app
#port
EXPOSE 8000

#run le projet
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT



