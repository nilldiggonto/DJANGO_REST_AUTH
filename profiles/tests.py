# from django.test import TestCase
import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from profiles.api.serializers import ProfileSerializer

from .models import Profile, ProfileStatus

# Create your tests here.
class RegistrationTestCase(APITestCase):
    
    def test_registration(self):
        data = {
            'username':'testcase',
            'email':'test@gmail.com',
            'password1':'nill1234',
            'password2':'nill1234',
        }

        response = self.client.post('/api/rest-auth/registration/',data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)



class ProfileViewSetTestCase(APITestCase):
    list_url = reverse('profile-list')
    def setUp(self):
        self.user = User.objects.create_user(username='diggonto',password='nill1234')

        self.token = Token.objects.create(user=self.user)


    def api_authentication(self):
        self.client.credentitals(HTTP_AUTHORIZATION = 'Token' + self.token)

    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)