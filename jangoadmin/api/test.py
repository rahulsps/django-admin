import json,requests,ast
from api.models import User 
from rest_framework import status 
from django.urls import reverse 
from rest_framework import response 
from rest_framework.test import APITestCase 
from api.serializers import UserSerializer
class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data="{'username' :'dhee1903','email':'dheeraj_4@gmail.com','password':'test@123'}"
        my_dict=ast.literal_eval(data)
        response=self.client.post(reverse('register'),data=my_dict,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    def test_registration_without_data(self):
        data='{"username":"dhee1904"}'
        my_dict=ast.literal_eval(data)
        response=self.client.post(reverse('register'),data=my_dict,format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
    def test_login_without_data(self):
        self.data='{"email":"dheeraj_4@gmail.com"}'
        my_dict=ast.literal_eval(self.data)
        response=self.client.post(reverse("login"),data=my_dict,format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
