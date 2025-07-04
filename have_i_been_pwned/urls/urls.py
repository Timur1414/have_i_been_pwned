"""
URL configuration for the Have I Been Pwned project.
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from cipher.views import download
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexPage.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'
         ),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'
         ),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'
         ),

    path('registration/', include('django_registration.backends.activation.urls')),
    path('profile/', views.ProfilePage.as_view(), name='profile'),

    path('create/email/', views.EmailCreatePage.as_view(), name='create_email'),
    path('create/password/', views.PasswordCreatePage.as_view(), name='create_password'),
    path('create/phone', views.PhoneCreatePage.as_view(), name='create_phone'),
    path('create/account', views.AccountCreatePage.as_view(), name='create_account'),

    path('cipher/', views.CipherPage.as_view(), name='cipher'),
    path('cipher/download_result/<int:id>', download, name='download_result'),
]
