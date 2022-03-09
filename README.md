# Brixner Inschriften

## about
The project **The inscriptions of Brixen / Bressanone. Survey of the epigraphic testimonies of the Middle Ages and the Early Modern Period** (2011-2013) aimed at photographing, transcribing and describing all inscriptions on the territory of the municipality of Brixen/Bressanone (South Tyrol) from the period between the 13th century and the year 1665. As a second step, we make the results of this work accessible in an online database.
The current repo holds the source code of the application.

## install

The application is build with [django](https://www.djangoproject.com/) and based upon [djangobaseproject](https://github.com/acdh-oeaw/djangobaseproject).

### step by step

Brin is configured to work with a Postgresql database. Connection settings, as well as e.g. `DEBUG`, `ALLOWED_HOSTS` or `SECRET_KEY` can be configured with environment variables. See `brin/settings.py` for more information.

1. clone the repo `git clone https://github.com/acdh-oeaw/brin.git`
2. recomended: create a virtual environment
3. install needed packages `pip install -r requirements.txt`
4. makemigrations: `python manage.py makemigrations`
5. migrate: `python manage.py migrate`
5. start the server: `python manage.py runserver`

## docker

### building the image

* `docker build -t brin:latest .`
* `docker build -t brin:latest --no-cache .`

### running the image

To run the image you should provide an `.env` file to pass in needed environment variables; see example below:

* `docker run -it -p 8020:8020 --env-file env.secret --name brin brin:latest`

# import legacy data

run ipython notebooks
1. `import_somedatafrommain` to import information about Inschriften
2. `re_import` to link images and inschriften as well as adding gps-info to places
