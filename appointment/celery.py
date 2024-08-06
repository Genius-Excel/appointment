from __future__ import absolute_import, unicode_literals
import os
from decouple import config
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from datetime import timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appointment.settings')


# REDIS HOSTED SERVE CREDENTIALS 
redis_pass = config("REDIS_PASS")
redis_host = config("REDIS_HOST")
redis_port = config("REDIS_PORT")


# REDER REDIS HOST CREDENTIALS

render_redis_host = config("RENDER_REDIS_HOST")
app = Celery('appointment', broker=f'redis://:{redis_pass}@{redis_host}:{redis_port}/0', backend='django-db', include=['appointment.tasks'])

app.conf.enable_utc = False

app.conf.update(timezone='Africa/Lagos')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    # 'loop-numbers-in-3': {
    #     'task': 'reminder.tasks.test_func',
    #     'schedule': timedelta(minutes=1),
    # },

    'send-email-reminder': {
        'task': 'reminder.tasks.send_email_reminder',
        'schedule': timedelta(seconds=50)
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
