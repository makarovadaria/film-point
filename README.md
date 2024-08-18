python manage.py dumpdata events.SurveyQuestion --indent 4 > fixtures.json

python manage.py loaddata fixtures.json