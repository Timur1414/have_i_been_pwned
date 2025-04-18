"""
Routers for the main application.
"""
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import Account, EmailData, PasswordData, PhoneData
from main.serializers import UserSerializer, AccountSerializer, EmailDataSerializer, PasswordDataSerializer, \
    PhoneDataSerializer


class UsersViewSet(APIView):
    """
    ViewSet for User model.
    """
    def get(self, request, format=None):
        """
        Get all users.
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        data = {
            'count': len(users),
            'users': serializer.data
        }
        return Response(data)


class AccountsViewSet(APIView):
    """
    ViewSet for Account model.
    """
    def get(self, request, format=None):
        """
        Get all accounts.
        """
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        data = {
            'count': len(accounts),
            'accounts': serializer.data
        }
        return Response(data)


class EmailDataViewSet(APIView):
    """
    ViewSet for EmailData model.
    """
    def get(self, request, format=None):
        email_data = EmailData.objects.all()
        serializer = EmailDataSerializer(email_data, many=True)
        data = {
            'count': len(email_data),
            'email_data': serializer.data
        }
        return Response(data)


class PasswordDataViewSet(APIView):
    """
    ViewSet for PasswordData model.
    """
    def get(self, request, format=None):
        password_data = PasswordData.objects.all()
        serializer = PasswordDataSerializer(password_data, many=True)
        data = {
            'count': len(password_data),
            'password_data': serializer.data
        }
        return Response(data)


class PhoneDataViewSet(APIView):
    """
    ViewSet for PhoneData model.
    """
    def get(self, request, format=None):
        phone_data = PhoneData.objects.all()
        serializer = PhoneDataSerializer(phone_data, many=True)
        data = {
            'count': len(phone_data),
            'phone_data': serializer.data
        }
        return Response(data)
