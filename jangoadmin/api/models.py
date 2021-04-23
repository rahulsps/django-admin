from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager 
from .enums import TokenType 
class UserManager(BaseUserManager):
    def create_superuser(self,email,username,password):
        '''
        '''
        user=self.model(email=email)
        user.username=username 
        user.set_password(password)
        user.is_superuser=True 
        user.is_active=True 
        user.is_staff=True 
        user.save(using=self._db)
        return user 
class User(AbstractBaseUser,PermissionsMixin):
    '''
    models for the user 
    '''
    latitude=models.CharField("Latitude",blank=True,null=True,max_length=100,default=None)
    longitude=models.CharField("Latitude",blank=True,null=True,max_length=100,default=None)
    my_description=models.CharField("Latitude",blank=True,null=True,max_length=1024,default=None)
    twitter_handle=models.CharField("Twitter Handle",null=True,blank=True,max_length=255,default=None)
    facebook_handle=models.CharField("Facebook Handle",null=True,blank=True,max_length=255,default=None)
    instagram_token=models.CharField("Instagram Handle",null=True,blank=True,max_length=255,default=None)
    paypal_email=models.CharField("Paypal email",null=True,blank=True,max_length=255,default=None)
    device_token=models.CharField("Device Token",null=True,blank=True,max_length=255,default=None)
    onetime_token=models.CharField("OneTime token",null=True,blank=True,max_length=255,default=None)
    created_on=models.DateTimeField("Created On",auto_now_add=True)
    updated_on=models.DateTimeField("Updated On",auto_now_add=True)
    email=models.EmailField("Email",null=False,blank=False,unique=True,error_messages={"unique":"OOPS,An account with this email is already regisgtered"})
    avatar=models.FileField("Avatar",null=True,blank=True,upload_to="avatars",default=None) 
    username=models.CharField("UserName",null=False,blank=False,max_length=100,unique=True,error_messages={"unique":"An UserName with this username is already regisgtered"})
    objects=UserManager()
    REQUIRED_FIELDS=['username']
    USERNAME_FIELD='email'
    def save(self,*args,**kwargs):
        self.email=self.email.lower()
        self.username=self.username.lower()
        super(User,self).save(*args,**kwargs)   
class Token(models.Model):
    token_type=models.CharField("Token Type",max_length=100,choices=((type,type.value) for type in TokenType))
    token=models.CharField("Token",max_length=100,null=True,blank=True,default=None)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField("Created At",null=True,blank=True,default=None)
    expiry_minutes=models.IntegerField("Expiry Minutes",default=30)
    def __str__(self):
        return str(self.token) + "_" + str(self.token)