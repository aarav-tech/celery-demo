from __future__ import absolute_import, unicode_literals

from celery import shared_task
import time


@shared_task
def send_email(email_id, message):
    time.sleep(10)
    print(f"Email is sent to {email_id}. Message sent was - {message}")