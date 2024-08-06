#!/usr/bin/env bash

set -o errexit

echo "Running custom script.."

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

celery -A appointment worker --pool=solo -l info

celery -A appointment beat -l info

echo "Script successfully run."
