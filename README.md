# Brixner Inschriften

## about
The project **The inscriptions of Brixen / Bressanone. Survey of the epigraphic testimonies of the Middle Ages and the Early Modern Period** (2011-2013) aimed at photographing, transcribing and describing all inscriptions on the territory of the municipality of Brixen/Bressanone (South Tyrol) from the period between the 13th century and the year 1665. As a second step, we make the results of this work accessible in an online database.
The current repo holds the source code of the application.

## install

The application is build with [django](https://www.djangoproject.com/) and based upon [djangobaseproject](https://github.com/acdh-oeaw/djangobaseproject).

### modularized settings

This django project uses modularized settings as described in [this blog post](https://simpleisbetterthancomplex.com/tips/2017/07/03/django-tip-20-working-with-multiple-settings-modules.html) to keep sensitiv information out of GitHub. Therefore you'll have to adapt `brin/settings/dev.py` to your needs, like changing the `SECRET_KEY` or adding your specific data base settings.
To execute any `manage.py`commands, you'll have to pass in a settings parameter pointing to your custom settings file like: `python manage.py runserver --settings=brin.settings.{nameOfCustomSettingsFile}`

### step by step

1. clone the repo `git clone https://github.com/acdh-oeaw/brin.git`
2. recomended: create a virtual environment
3. install needed packages `pip install -r requirements.txt`
4. makemigrations: `python manage.py makemigrations --settings=brin.settings.dev`
5. migrate: `python manage.py migrate --settings=brin.settings.dev`
5. start the server: `python manage.py runserver --settings=brin.settings.dev`

# import legacy data

run ipython notebooks
1. `import_somedatafrommain` to import information about Inschriften
2. `re_import` to link images and inschriften as well as adding gps-info to places
