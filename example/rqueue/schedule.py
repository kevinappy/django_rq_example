"""Define RQ periodic tasks. This is executed on runtime by apps.py"""
import django_rq

from rqueue import tasks

scheduler = django_rq.get_scheduler("default")


def schedule():
    # Delete any existing jobs in the scheduler when the app starts up
    for job in scheduler.get_jobs():
        job.delete()

    scheduler.cron("* * * * *", func=tasks.idempotent_method)
    scheduler.cron("*/2 * * * *", func=tasks.idempotent_method2)
