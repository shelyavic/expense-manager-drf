import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
app = Celery("main")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "every": {
        "task": "users.tasks.distribute_email_tasks",
        "schedule": crontab(),
        # "schedule": crontab(hour=8, minute=0),
    },
}
