"""
Test cases for the main app views.
"""
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client

from main.models import EmailData, PhoneData


class IndexPageTestCase(TestCase):
    """
    Test cases for the index page.
    """
    def setUp(self):
        self.client = Client()
        self.response = self.client.get('/')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'index/index.html')

    def test_context(self):
        self.assertIn('title', self.response.context)
        self.assertEqual(self.response.context['title'], 'Index')


class ProfilePageTestCase(TestCase):
    """
    Test cases for the profile page.
    """
    fixtures = [
        'data.json'
    ]
    def setUp(self):
        self.client = Client()
        self.user = User.objects.get(username='admin')
        self.client.force_login(self.user)
        self.response = self.client.get(f'/profile/{self.user.id}/')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'profile/index.html')

    def test_context(self):
        self.assertIn('user', self.response.context)
        self.assertEqual(self.response.context['user'], self.user)
        self.assertIn('is_same_user', self.response.context)
        self.assertTrue(self.response.context['is_same_user'])
        self.assertIn('title', self.response.context)
        self.assertEqual(self.response.context['title'], 'Profile')
        self.assertIn('email', self.response.context)
        email = EmailData.get_email_by_user(self.user)
        self.assertEqual(self.response.context['email'], email)
        self.assertIn('phone', self.response.context)
        phone = PhoneData.get_phone_by_user(self.user)
        self.assertEqual(self.response.context['phone'], phone)

    def test_another_user_profile(self):
        another_user = User.objects.get(username='test')
        self.response = self.client.get(f'/profile/{another_user.id}/')
        self.assertEqual(self.response.status_code, 200)
        self.assertIn('is_same_user', self.response.context)
        self.assertFalse(self.response.context['is_same_user'])
        self.assertNotIn('email', self.response.context)
        self.assertNotIn('phone', self.response.context)

    def test_no_login(self):
        self.client.logout()
        self.response = self.client.get(f'/profile/{self.user.id}/')
        self.assertEqual(self.response.status_code, 302)
