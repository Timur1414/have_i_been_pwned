"""
Abstract models for the application.
"""
from django.contrib.auth.models import User
from django.db import models


class Data(models.Model):
    """
    Abstract model for data that can be pwned.
    """
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    pwned = models.BooleanField(default=False)

    class Meta:
        abstract = True
