# import sys, os, json, io, boto3, base64, hashlib
# from boto3.s3.transfer import S3Transfer
# from datetime import datetime
# from decouple import config

# from django.conf import settings
# from django.contrib import auth
# from django.contrib.auth.models import User
# from django.core import serializers
# from django.core.files.storage import FileSystemStorage
# from django.core.mail import EmailMessage
# from django.core.mail import EmailMultiAlternatives
# from django.http.response import JsonResponse
# from django.shortcuts import render
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags

# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from api.models import Profile, Timezones

# def checkAuth(request):
#     if Token.objects.filter(key=request.META.get('HTTP_TOKEN')):
#         return Token.objects.filter(key=request.META.get('HTTP_TOKEN'))[0]
#     else:
#         return 0

# # Create your views here.
# @api_view(['POST'])
# def Login(request):
#     reqdata = json.loads(request.body.decode('utf-8'))
#     if(int(reqdata['google']) == 0):
#         user = auth.authenticate(username=reqdata['username'], password=reqdata['secret'])
#     else:
#         user = User.objects.filter(email=reqdata['email'])
#         if user:
#             user = user[0]
#         else:
#             user = None

#     if user:
#         token = Token.objects.get_or_create(user=user)
#         u = {}
#         u['token']      = token[0].key
#         u['id']         = user.id
#         u['username']   = user.username
#         u['first_name'] = user.first_name
#         u['last_name']  = user.last_name
#         u['email']      = user.email
#         u['is_staff']   = user.is_staff
#         u['is_active']  = user.is_active
#         u['timezone']   = user.profile.timezone.tz_name if user.profile.timezone else None
#         data = {"status":200,"data":u}
#     else:
#         if(int(reqdata['google']) != 0):
#             data = {"status":400,"data":{"message":"Account not registered"}}
#         else:
#             user = User.objects.filter(username=reqdata['username'])
#             if user:
#                 data = {"status":400,"data":{"message":"Invalid password"}}
#             else:
#                 data = {"status":400,"data":{"message":"Invalid username"}}
#     return JsonResponse(data)

# @api_view(['POST'])
# def Register(request):
#     try:

#         reqdata = json.loads(request.body.decode('utf-8'))
#         usrname = reqdata['username'] if (int(reqdata['google']) == 0) else reqdata['email']
#         if(reqdata['password'] != reqdata['confirm-password']):
#             data = {"status":400,"data":{"message":"Passwords did not match!"}}
#             return JsonResponse(data)
#         # check existing username
#         if User.objects.filter(username=usrname):
#             data = {"status":500,"data":{"message":"Username already exists!"}}
#             return JsonResponse(data)
#         # check existing email
#         if User.objects.filter(email=reqdata['email']):
#             data = {"status":500,"data":{"message":"Account already exists!"}}
#             return JsonResponse(data)
#         # create user
#         if(int(reqdata['google']) == 0):
#             user = User(username=usrname,email=reqdata['email'])
#             user.set_password(reqdata['password'])
#             user.save()
#         else:
#             # .split('@')[0]
#             user = User(username=usrname,email=reqdata['email'],first_name=reqdata['first_name'],last_name=reqdata['last_name'])
#             user.set_unusable_password()
#             user.save()
#         # send welcome email
#         subject, from_email, to = "Hey there - we're flipping upside down that you've joined us!", settings.EMAIL_HOST_USER, user.email
#         html_content = render_to_string('email/welcome.html', {'name':user.username})
#         text_content = strip_tags(html_content)
#         msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()
#         # save user profile
#         p = Profile.objects.get_or_create(user=user,latitude=reqdata['latitude'],longitude=reqdata['longitude'],device_token=reqdata['device_token'])
#         if 'timezone' in reqdata:
#             t = Timezones.objects.filter(tz_name=reqdata['timezone'])
#             if t:
#                 user.profile.timezone = t[0]
#                 user.profile.save()

#         token = Token.objects.get_or_create(user=user)

#         u = {}
#         u['token']      = token[0].key
#         u['id']         = user.id
#         u['username']   = user.username
#         u['first_name'] = user.first_name
#         u['last_name']  = user.last_name
#         u['email']      = user.email
#         u['is_staff']   = user.is_staff
#         u['is_active']  = user.is_active
#         u['timezone']   = None
#         if user.profile.timezone:
#             u['timezone']   = user.profile.timezone.tz_name

#         data = {"status":200,"data":u}
#         return JsonResponse(data)
#     except Exception as e:
#         exc_type, exc_obj, exc_tb = sys.exc_info()
#         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#         data = {"status":500,"data":{"message":"Something went wrong!","trace":str(e)}}
#         return JsonResponse(data)

# @api_view(['PUT','GET'])
# def MyProfile(request):

#     token = checkAuth(request)
#     if token == 0:
#         data = {"status":403,"data":{"message":"Not Logged In!"}}
#         return JsonResponse(data)
#     try:

#         AWS_STORAGE_URL = config('AWS_STORAGE_URL', default='')
#         if request.method == 'PUT':
#             reqdata = json.loads(request.body.decode('utf-8'))
#             User.objects.filter(id=token.user.id).update(first_name=reqdata['first_name'],last_name=reqdata['last_name'],email=reqdata['email'],username=reqdata['username'])
#             Profile.objects.filter(user=token.user.id).update(latitude=reqdata['latitude'],longitude=reqdata['longitude'],my_description=reqdata['my_description'],twitter_handle=reqdata['twitter_handle'],facebook_handle=reqdata['facebook_handle'],instagram_handle=reqdata['instagram_handle'],paypal_email=reqdata['paypal_email'])
#             token = checkAuth(request)

#         p = {}
#         p['latitude']           = token.user.profile.latitude
#         p['longitude']          = token.user.profile.longitude
#         p['my_description']     = token.user.profile.my_description
#         p['twitter_handle']     = token.user.profile.twitter_handle
#         p['facebook_handle']    = token.user.profile.facebook_handle
#         p['instagram_handle']   = token.user.profile.instagram_handle
#         p['paypal_email']       = token.user.profile.paypal_email
#         p['avatar']             = AWS_STORAGE_URL+str(token.user.profile.avatar)
#         p['first_name']         = token.user.first_name
#         p['last_name']          = token.user.last_name
#         p['email']              = token.user.email
#         p['username']           = token.user.username

#         data = {"status":200,"data":p}
#         return JsonResponse(data)
#     except Exception as e:
#         exc_type, exc_obj, exc_tb = sys.exc_info()
#         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#         data = {"status":500,"data":{"message":"Something went wrong!","trace":str(e)}}
#         return JsonResponse(data)
# @api_view(['PUT'])
# def ChangePassword(request):
#     token = checkAuth(request)
#     if token == 0:
#         data = {"status":403,"data":{"message":"Not Logged In!"}}
#         return JsonResponse(data)
#     try:
#         if request.method=="PUT":
#             u = token.user
#             reqdata = json.loads(request.body.decode('utf-8'))
#             opwd  = reqdata['opwd']
#             npwd  = reqdata['npwd']
#             cnpwd = reqdata['cnpwd']
#             if u.check_password(opwd) == True:
#                 if npwd == cnpwd:
#                     u.set_password(npwd)
#                     u.save()
#                     msg  = "Password Updated!"
#                     data = {"status":200,"data":{"message":msg}}
#                     return JsonResponse(data)
#                 else:
#                     err  = "New password(s) didn't match!"
#                     data = {"status":400,"data":{"message":err}}
#                     return JsonResponse(data)
#             else:
#                 err  = "Incorrect Old Password!"
#                 data = {"status":400,"data":{"message":err}}
#                 return JsonResponse(data)
#         else:
#             data = {"status":405,"data":{"message":"Only PUT method accepted!"}}
#             return JsonResponse(data)
#     except Exception as e:
#         exc_type, exc_obj, exc_tb = sys.exc_info()
#         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#         data = {"status":500,"data":{"message":"Something went wrong!","trace":str(e)}}
#         return JsonResponse(data)
# @api_view(['POST'])
# def ForgotPassword(request):
#     reqdata = json.loads(request.body.decode('utf-8'))
#     if "email" in reqdata:
#         user = User.objects.filter(email=reqdata['email']).first()
#         if user:
#             if user.has_usable_password():
#                 # create token
#                 web_url = config('WEBURL', default='http://192.168.0.124:8000/')
#                 strfortoken = user.email+'/'+str(datetime.now().timestamp())
#                 token = hashlib.md5(strfortoken.encode()).hexdigest()
#                 user.profile.onetime_token=token
#                 user.profile.save()
#                 # send email
#                 subject, from_email, to = "Reset your password", settings.EMAIL_HOST_USER, user.email
#                 html_content = render_to_string('email/reset-password.html', {'name':user.username,'reset_link':web_url+'reset-password/'+token+"/"})
#                 text_content = strip_tags(html_content)
#                 msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#                 msg.attach_alternative(html_content, "text/html")
#                 msg.send()
#                 data = {"status":200,"data":{"message":"Please check your email!"}}
#                 return JsonResponse(data)
#             else:
#                 data = {"status":400,"data":{"message":"Login with Google!"}}
#                 return JsonResponse(data)
#         else:
#             data = {"status":400,"data":{"message":"Account not found!"}}
#             return JsonResponse(data)
#     elif "npwd" in reqdata and "cnpwd" in reqdata and "token" in reqdata:
#         p = Profile.objects.filter(onetime_token=reqdata['token']).first()
#         if p:
#             u = p.user
#             npwd  = reqdata['npwd']
#             cnpwd = reqdata['cnpwd']
#             if npwd == cnpwd:
#                 u.set_password(npwd)
#                 u.save()
#                 p.onetime_token = None
#                 p.save()
#                 msg  = "Password Updated!"
#                 data = {"status":200,"data":{"message":msg}}
#                 return JsonResponse(data)
#             else:
#                 err  = "New password(s) didn't match!"
#                 data = {"status":400,"data":{"message":err}}
#                 return JsonResponse(data)
#         else:
#             data = {"status":200,"data":{"message":"Password reset token has expired!"}}
#             return JsonResponse(data)
#     else:
#         data = {"status":400,"data":{"message":"Invalid request!"}}
#         return JsonResponse(data)

# @api_view(['POST','GET'])
# def Avatar(request):

#     token = checkAuth(request)
#     if token == 0:
#         data = {"status":403,"data":{"message":"Not Logged In!"}}
#         return Response(data)
#     try:
#         AWS_STORAGE_URL = config('AWS_STORAGE_URL', default='')
#         user   = token.user
#         if request.method == 'POST':
#             avatar = request.FILES['file']
#             AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='')
#             AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='')
#             AWS_STORAGE_BUCKET_RGN = config('AWS_STORAGE_BUCKET_RGN', default='us-east-1')
#             AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default='')
#             fs          = FileSystemStorage(os.getcwd()+'/static/img/avatars')
#             fname       = avatar.name
#             filename    = fs.save(fname,avatar)
#             s3_path     = 'avatars/'+fname
#             local_path  = os.getcwd()+'/static/img/avatars/'+fname
#             transfer    = S3Transfer(boto3.client('s3', AWS_STORAGE_BUCKET_RGN,  aws_access_key_id = AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY,use_ssl=False))
#             client      = boto3.client('s3')

#             transfer.upload_file(local_path, AWS_STORAGE_BUCKET_NAME, s3_path,extra_args={'ACL': 'public-read'})
#             Profile.objects.filter(user=token.user.id).update(avatar=s3_path)

#             os.remove(local_path)
#             token = checkAuth(request)
#             user  = token.user
#         if str(token.user.profile.avatar) != '':
#             data = {"status":200,"data":{"url":AWS_STORAGE_URL+str(token.user.profile.avatar)}}
#         else:
#             data = {"status":404,"data":{"message":"avatar missing!"}}
#         return Response(data)
#     except Exception as e:
#         print(e)
#         data = {"status":500,"data":{"message":"Something went wrong!","trace":str(e)}}
#         return JsonResponse(data)

# @api_view(['POST'])
# def Logout(request):

#     if checkAuth(request) == 0:
#         data = {"status":403,"data":{"message":"Not Logged In!"}}
#         return JsonResponse(data)

#     Token.objects.filter(key=request.META.get('HTTP_TOKEN')).delete()
#     data = {"status":200,"data":{"message":"Logged out!"}}
#     return JsonResponse(data)

# @api_view(['POST'])
# def Dashboard(request):

#     if checkAuth(request) == 0:
#         data = {"status":403,"data":{"message":"Not Logged In!"}}
#         return JsonResponse(data)

#     data = {"status":200,"data":{"message":1}}
#     return JsonResponse(data)

import logging,traceback 
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status 
from .models import User 
from .serializers import UserSerializer
from django.contrib.auth import authenticate,login 
from rest_framework.authtoken.models import Token 
logger=logging.getLogger(__name__)
class UserSignUp(APIView):
    '''
    API FOR SIGNUP 
    DEVELOPER: Dheeraj_Rajput (dheeraj_rajput@softprodigy.com)
    Remarks: Don't Change anything without disucssion with developing team 
    '''
    def post(self,request): 
        try:
            params=request.data 
            try:
                password=params.pop("password") 
            except Exception:
                password=None 
            if not password:
                return Response({"status":True,"message":"Password Not Found"},status=status.HTTP_400_BAD_REQUEST)
            params.update(password=password)
            try:
                serializer=UserSerializer(data=params)
                if serializer.is_valid(raise_exception=True):
                    user=serializer.save() 
                    user.set_password(password)
                    user.save()
                    return Response({"status":True,'message':"Signup Successful","data":serializer.data},status=status.HTTP_201_CREATED)     
            except Exception:
                return Response({"status":"False","message":"Something went wrong","errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
        except Exception:
            logger.exception(traceback.format_exc())
            logger.exception("Something went wrong while Signup")
            return Response({"status":False,"message":"OOPS,Something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class LoginView(APIView): 
    '''
    API FOR SIGIN 
    '''  
    def post(self,request):
        try:
            params=request.data 
            try:
                email=params.pop("email") 
            except Exception:
                email=None 
            if not email:
                return Response({"status":False,"message":"Email Not Found"},status=status.HTTP_400_BAD_REQUEST) 
            try:
                password=params.pop("password") 
            except Exception:
                password=None 
            if not password:
                return Response({"status":False,"message":"Password Not Found"},status=status.HTTP_400_BAD_REQUEST)
            params.update(email=email)
            params.update(password=password)
            try:
                user=User.objects.get(email=params['email'].lower()) 
            except Exception:
                return Response({"status":False,"message":"OOPS,We are unable to recognise you"},status=status.HTTP_400_BAD_REQUEST)
            user.is_active=True 
            user.save()
            user=authenticate(email=params['email'].lower(),password=params['password'])
            if user:
                serializer=UserSerializer(user)
                login(request,user)
                token,created=Token.objects.get_or_create(user=user)
                return Response({"status":True,"message":"Loged In Successful","data":serializer.data,"token":token.key},status=status.HTTP_200_OK)  
            else:
                return Response({"status":False,"message":"OOPS,It seems credentials are invalid"},status=status.HTTP_400_BAD_REQUEST)  
        except Exception:
            logger.exception(traceback.format_exc())
            logger.exception("Something went wrong in " + "Post" + "login")
            return Response({"status":True,"message":"Something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)