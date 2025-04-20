"""
URL patterns for the API endpoints.
"""
from django.urls import path, include
from main import routers
from cipher import views as cipher_views

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('users/', routers.UsersViewSet.as_view()),
    path('accounts/', routers.AccountsViewSet.as_view()),
    path('email_data/', routers.EmailDataViewSet.as_view()),
    path('password_data/', routers.PasswordDataViewSet.as_view()),
    path('phone_data/', routers.PhoneDataViewSet.as_view()),

    path('cipher_logic/', cipher_views.cipher, name='cipher_logic'),
]
