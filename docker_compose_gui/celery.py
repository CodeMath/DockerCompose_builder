import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'docker_compose_gui.settings')

app = Celery('docker_compose_gui', broker=os.getenv('APP_BROKER_URI'))

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))