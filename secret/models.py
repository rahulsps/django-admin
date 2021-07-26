from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager

# Create your models here.

class Friends(models.Model):
    class Meta:
        db_table = "friends"
    id                = models.AutoField(primary_key=True)
    name              =  models.CharField(max_length=100, blank=False, null=False)
    age               = models.IntegerField(blank=False,null=False)
    department        = models.CharField(max_length=100, blank=False, null=False)
    is_active = models.BooleanField(blank=True, null=True)
    created_on        = models.DateTimeField(auto_now_add=True)
    updated_on        = models.DateTimeField(auto_now=True)
    