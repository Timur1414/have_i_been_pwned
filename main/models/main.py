"""
This file contains the models for the application.
"""
from __future__ import annotations
import logging
from typing import Optional
from django.contrib.auth.models import User
from django.db import models
from django.db.models import QuerySet
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

    def __str__(self) -> str:
        return str(self.url)

    @staticmethod
    def get(offset=0, limit=1000) -> Optional[Account]:
        """
        Get account data.
        """
        logger.debug('Getting account data with offset: %s and limit: %s', offset, limit)
        return Account.objects.get(offset=offset, limit=limit)

    @staticmethod
    def get_accounts_by_user(user: User) -> QuerySet:
        """
        Get accounts data by user.
        """
        logger.debug('Getting accounts data for user: %s', user.username)
        return Account.objects.filter(user=user).all()

class EmailData(Data):
    """
    Model for email data.
    """
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return str(self.email)

    @staticmethod
    def get(offset=0, limit=1000) -> Optional[EmailData]:
        """
        Get email data.
        """
        logger.debug('Getting email data with offset: %s and limit: %s', offset, limit)
        return EmailData.objects.get(offset=offset, limit=limit)

    @staticmethod
    def get_emails_by_user(user: User) -> QuerySet:
        """
        Get emails data by user.
        """
        logger.debug('Getting emails data for user: %s', user.username)
        return EmailData.objects.filter(user=user).all()

class PasswordData(Data):
    """
    Model for password data.
    """
    password = models.CharField(max_length=255)  # ToDo: encrypt password

    def __str__(self) -> str:
        return str(self.password)

    @staticmethod
    def get(offset=0, limit=1000) -> Optional[PasswordData]:
        """
        Get password data.
        """
        logger.debug('Getting password data with offset: %s and limit: %s', offset, limit)
        return PasswordData.objects.get(offset=offset, limit=limit)

    @staticmethod
    def get_passwords_by_user(user: User) -> QuerySet:
        """
        Get passwords data by user.
        """
        logger.debug('Getting passwords data for user: %s', user.username)
        return PasswordData.objects.filter(user=user).all()

class PhoneData(Data):
    """
    Model for phone data.
    """
    phone = PhoneNumberField(unique=True, region='RU')

    def __str__(self) -> str:
        return str(self.phone)
    
    @staticmethod
    def get(offset=0, limit=1000) -> Optional[PhoneData]:
        """
        Get phone data.
        """
        logger.debug('Getting phone data with offset: %s and limit: %s', offset, limit)
        return PhoneData.objects.get(offset=offset, limit=limit)

    @staticmethod
    def get_phones_by_user(user: User) -> QuerySet:
        """
        Get phones data by user.
        """
        logger.debug('Getting phones data for user: %s', user.username)
        return PhoneData.objects.filter(user=user).all()
