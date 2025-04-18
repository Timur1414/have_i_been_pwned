"""
Serializers for models.
"""
from django.contrib.auth.models import User
from rest_framework import serializers
from main.models import Account, EmailData, PasswordData, PhoneData


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']


class AccountSerializer(serializers.ModelSerializer):
    """
    Serializer for Account model.
    """
    class Meta:
        model = Account
        fields = ['id', 'url', 'login', 'password', 'user', 'pwned']
        read_only_fields = ['id']


class EmailDataSerializer(serializers.ModelSerializer):
    """
    Serializer for EmailData model.
    """
    class Meta:
        model = EmailData
        fields = ['id', 'email', 'user', 'pwned']
        read_only_fields = ['id']


class PasswordDataSerializer(serializers.ModelSerializer):
    """
    Serializer for PasswordData model.
    """
    class Meta:
        model = PasswordData
        fields = ['id', 'password', 'user', 'pwned']
        read_only_fields = ['id']


class PhoneDataSerializer(serializers.ModelSerializer):
    """
    Serializer for PhoneData model.
    """
    class Meta:
        model = PhoneData
        fields = ['id', 'phone', 'user', 'pwned']
        read_only_fields = ['id']
