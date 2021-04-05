FROM python:3.8

#créer un répertoire pour le projet
WORKDIR /app

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
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000



