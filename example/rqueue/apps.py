from django.apps import AppConfig

from rqueue.schedule import schedule


class RqueueConfig(AppConfig):
    name = "rq"

    def ready(self):
        schedule()
