from rest_framework.test import APITestCase
from django.urls import reverse 
class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url=reverse("register")
        self.login_url=reverse("login")
        self.user_data={
            "username":"rahulsps",
            "email":"rahulbhola.softprodigy@gmail.com",
            "password":"rahul123",
            "confirm-password":"rahul123",
            "latitude":"37.456",
            "longitude":"72.123",
            "google":0,
            "timezone":"Asia/Kolkata",
            "device_token":"qwerty"
        }
        print("===user data is: ",self.user_data)
        self.login_data={"username":"rahulsps","secret":"rahul123","google":0}
        print("===== login in data is: ",self.login_data)
        return super().setUp()
    def tearDown(self):
        return super().tearDown()
