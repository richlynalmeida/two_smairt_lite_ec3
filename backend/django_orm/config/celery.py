# config/celery.py

import os

from celery import Celery

# Set default Django settings module for 'celery' CLI programs
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("2smairt")

# Load task settings from Django settings using 'CELERY_' namespace
app.config_from_object("django.conf:settings", namespace="CELERY")

# Autodiscover tasks across all registered Django app configs
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
