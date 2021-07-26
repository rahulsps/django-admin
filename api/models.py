from django.db import models
from django.contrib.auth.models import User
from decouple import config

class Timezones(models.Model):
    class Meta:
        db_table  = "hs_timezones"
    
    id = models.AutoField(primary_key=True)
    county_code = models.CharField(blank=True, null=True, max_length=2, default=None)
    lat_long = models.CharField(blank=True, null=True, max_length=12, default=None)
    tz_name = models.CharField(blank=True, null=True, max_length=50, default=None)
    country_portion = models.CharField(blank=True, null=True, max_length=50, default=None)
    status = models.CharField(blank=True, null=True, max_length=10, default=None)
    utc_offset = models.CharField(blank=True, null=True, max_length=6, default=None)
    utc_dst_offset = models.CharField(blank=True, null=True, max_length=6, default=None)
    notes = models.TextField(blank=True, null=True, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    class Meta:
        db_table  = "hs_user_profile"
    
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    latitude = models.CharField(blank=True, null=True, max_length=100, default=None)
    longitude = models.CharField(blank=True, null=True, max_length=100, default=None)
    my_description = models.CharField(blank=True, null=True, max_length=1024, default=None)
    twitter_handle = models.CharField(blank=True, null=True, max_length=255, default=None)
    facebook_handle = models.CharField(blank=True, null=True, max_length=255, default=None)
    instagram_handle = models.CharField(blank=True, null=True, max_length=255, default=None)
    paypal_email = models.CharField(blank=True, null=True, max_length=255, default=None)
    device_token = models.CharField(blank=True, null=True, max_length=255, default=None)
    onetime_token = models.CharField(blank=True, null=True, unique=True, max_length=255, default=None)
    timezone = models.ForeignKey(Timezones, on_delete=models.CASCADE, blank=True, null=True, default=None)
    avatar = models.FileField(blank = True, null=True, upload_to='avatars', default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

