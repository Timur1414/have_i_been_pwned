from django.contrib import admin

from main.models import EmailData, PasswordData, PhoneData, Account


@admin.register(EmailData)
class EmailDataModelAdmin(admin.ModelAdmin):
    """
    Admin interface for EmailData model.
    """
    list_display = ('email', 'pwned', 'user')
    search_fields = ('email',)
    list_filter = ('pwned',)
    ordering = ('email',)
    list_display_links = ('email', 'pwned')

@admin.register(PasswordData)
class PasswordDataModelAdmin(admin.ModelAdmin):
    """
    Admin interface for PasswordData model.
    """
    list_display = ('password', 'pwned', 'user')
    list_filter = ('pwned',)
    ordering = ('user',)
    list_display_links = ('password', 'pwned')

@admin.register(PhoneData)
class PhoneDataModelAdmin(admin.ModelAdmin):
    """
    Admin interface for PhoneData model.
    """
    list_display = ('phone', 'pwned', 'user')
    search_fields = ('phone',)
    list_filter = ('pwned',)
    ordering = ('phone',)
    list_display_links = ('phone', 'pwned')

@admin.register(Account)
class AccountModelAdmin(admin.ModelAdmin):
    """
    Admin interface for Account model.
    """
    list_display = ('user', 'url',)
    search_fields = ('url',)
    list_filter = ('pwned',)
    ordering = ('user',)
    list_display_links = ('user', 'url',)
