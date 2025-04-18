"""
This file contains the models for the application.
"""
from __future__ import annotations
import logging
from typing import Optional
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from main.models.abstract import Data

logger = logging.getLogger('models')

class Account(Data):
    """
    Model for account data.
    """
    url = models.URLField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  # ToDo: encrypt password

    def __str__(self):
        return str(self.url)

    @staticmethod
    def get_account_by_user(user: User) -> Optional[Account]:
        """
        Get account data by user.
        """
        logger.debug('Getting account data for user: %s', user.username)
        return Account.objects.filter(user=user).first()

class EmailData(Data):
    """
    Model for email data.
    """
    email = models.EmailField(unique=True)

    def __str__(self):
        return str(self.email)

    @staticmethod
    def get_email_by_user(user: User) -> Optional[EmailData]:
        """
        Get email data by user.
        """
        logger.debug('Getting email data for user: %s', user.username)
        return EmailData.objects.filter(user=user).first()

class PasswordData(Data):
    """
    Model for password data.
    """
    password = models.CharField(max_length=255)  # ToDo: encrypt password

    def __str__(self):
        return str(self.password)

    @staticmethod
    def get_password_by_user(user: User) -> Optional[PasswordData]:
        """
        Get password data by user.
        """
        logger.debug('Getting password data for user: %s', user.username)
        return PasswordData.objects.filter(user=user).first()

class PhoneData(Data):
    """
    Model for phone data.
    """
    phone = PhoneNumberField(unique=True, region='RU')

    def __str__(self):
        return str(self.phone)

    @staticmethod
    def get_phone_by_user(user: User) -> Optional[PhoneData]:
        """
        Get phone data by user.
        """
        logger.debug('Getting phone data for user: %s', user.username)
        return PhoneData.objects.filter(user=user).first()
