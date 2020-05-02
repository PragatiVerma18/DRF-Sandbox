from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

class UserAPITestCase(TestCase):
  def setUp(self):
    user = User.objects.create(username='cfe', email='hello@cfe.com')
    user.set_password("yeahhhcfe")
    user.save()

  def test_created_user_std(self):
    qs = User.objects.filter(username='cfe')
    self.assertEqual(qs.count(), 1)

  def test_register_user_api(self):
    url = api_reverse('api-auth:register')
    data = {
      'username': 'cfe.doe',
      'email': 'cfe.doe@gmail.com',
      'password': 'learncode',
      'password2': 'learncode',
    }
    response = self.client.post(url, data, format="json")
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_register_user_api_fail(self):
    url = api_reverse('api-auth:register')
    data = {
      'username': 'cfe.doe',
      'email': 'cfe.doe@gmail.com',
      'password': 'learncode',
    }
    response = self.client.post(url, data, format="json")
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_login_user_api(self):
    url = api_reverse('api-auth:login')
    data = {
      'username': 'cfe',
      'password': 'yeahhhcfe',
    }
    response = self.client.post(url, data, format="json")
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_login_user_api_fail(self):
    url = api_reverse('api-auth:login')
    data = {
      'username': 'cfe.abc',
      'password': 'yeahhhcfe',
    }
    response = self.client.post(url, data, format="json")
    self.assertEqual(response.status_code, status.HTTP_200_OK)