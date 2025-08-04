# python_cevc_lam-dang-khoa

## Database command:
- Make migration: `python booking_tours/manage.py makemigrations api --name "<migration name>"`
- Command Run migration: `python booking_tours/manage.py migrate api`

## Server command:
- Command start server: `python booking_tours/manage.py runserver`

## Show setting:
- Enable virtual enviroment: `source env/bin/activate`
- Install packages: `pip install -r .requirements`
- Get urls: `python booking_tours/manage.py show_urls`

## Create reauirement by pip-chill:
- Install pip-chill: `pip install pip-chill`
- Create file requirement: `pip-chill > .requirements`

## Run auto check syntax before commit:
- Command auto check: `pycodestyle --exclude=__pycache__,migrations,env,*.pyc,.git,venv booking_tours/`

## Document: https://docs.google.com/document/d/1E_SfrfkqCZ__Lq68Jb9IWpFJa7gRNry9usQeJABkt8Y/edit?usp=sharing
