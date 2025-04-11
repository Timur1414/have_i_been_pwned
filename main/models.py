"""
This file contains the models for the application.
"""
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Data(models.Model):
    """
    Abstract model for data that can be pwned.
    """
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    pwned = models.BooleanField(default=False)

    class Meta:
        abstract = True

class EmailData(Data):
    """
    Model for email data.
    """
    email = models.EmailField(unique=True)

    def __str__(self):
        return str(self.email)

class PasswordData(Data):
    """
    Model for password data.
    """
    password = models.CharField(max_length=255)

    def __str__(self):
        return str(self.password)

class PhoneData(Data):
    """
    Model for phone data.
    """
    phone = PhoneNumberField(unique=True, region='RU')

    def __str__(self):
        return str(self.phone)
