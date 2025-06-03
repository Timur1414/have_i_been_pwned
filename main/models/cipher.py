"""
This file contains the models for the application.
"""
from __future__ import annotations
import logging

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

logger = logging.getLogger('models')

class CipherResults(models.Model):
    file = models.FileField(upload_to='cipher_results/%Y/%m/%d/')
    date_created = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

@receiver(pre_delete, sender=CipherResults)
def delete_image(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete(False)
