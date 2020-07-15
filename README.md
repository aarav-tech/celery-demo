# Celery with Django

## Introduction
This project is just to demonstrate how celery can be integrated with django project to call task asynchronously as well as synchronously if required. Tasks can also be executed on schedule as well as periodically.

## Learning points
- Celery configuration
- Write celery task in django app
- Call task asynchronously
- Execute task periodically

## Installation Steps
### Step 1 - Install python dependencies
`pip install -r requirements.txt`

### Step 2 - Migrate database
`python manage.py migrate`

### Step 3 - Run celery worker to receive tasks and execute
`celery -A celery_demo worker -l info -Q celery,high`

### Step 4 - Run celery beat for sending task periodically to workers
`celery -A celery_demo beat`

### Step 5 - Run command line events monitor
`celery -A celery_demo events`

### Step 6 - Monitor celery tasks and workers using flower third party web tool
- `pip install flower`
- `celery -A celery_demo flower`

Now go to browser and access flower real time monitoring web tool by using following url
http://localhost:5555
