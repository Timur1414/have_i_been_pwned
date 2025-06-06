"""
This module contains tasks related to the cipher application.
"""
from django.utils import timezone
from have_i_been_pwned.celery import app
from main.models import CipherResults


@app.task
def delete_files():
    """
    This task is used to delete files from the media directory if more than 1 day old.
    """
    objects = CipherResults.objects.all()
    now = timezone.now()
    for obj in objects:
        if (now - obj.date_created).days > 1:
            obj.delete()
