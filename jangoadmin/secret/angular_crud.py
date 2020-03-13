from __future__ import unicode_literals
from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib.auth.models import User
import sys, os, json, io,  base64, hashlib,re
from secret.models import Friends
from secret.serializers import adding_friends
entries_per_page = 10

def pagination(request,friends):
    try:
        
        page      = request.GET.get('page', 1)
        paginator = Paginator(friends, entries_per_page)
        friends     = paginator.page(page)
        
        if not friends:
            msg="No Data Found"
    except PageNotAnInteger:
        friends = {}
        msg="No Data Found"
    except EmptyPage:
        friends = {}
        msg="No Data Found"
    except Exception as e :
        print(e)
    friends_array=[]
    friends_array.append(friends)
    pages=[]
    for x in range(1,paginator.num_pages+1):
        pages.append(x)
    friends_array.append(pages)
    return friends_array

@api_view(['GET'])
def get_user_data(request):
    try:
        # finding if there is search param
        search=request.GET.get('search')
        friends = list(Friends.objects.filter(name__icontains=search).values('id','name', 'age', 'department', 'is_active' ).order_by('-id'))
        friends_array=pagination(request,friends)
        friends=list(friends_array[0])
        data  = {"status":"200","msg":"success",'friends':friends,'total_pages':friends_array[1],'entries_per_page':entries_per_page}
    except Exception as E:
        print(E)
        try:
            friends = Friends.objects.filter().values('id','name', 'age', 'department', 'is_active' ).order_by('-id')
            friends_array=pagination(request,friends)
            friends=list(friends_array[0])
            data  = {"status":"200","msg":"success",'friends':friends,'total_pages':friends_array[1],'entries_per_page':entries_per_page}
        except Exception as E:
            print(E)
            data = {"status":"500","msg":"Failure"}
    return JsonResponse(data,safe=False)

@login_required
def list_users(request):
    msg=""
    return render(request,'angular_crud/list_users.html',{'msg':msg})
    
@api_view(['GET'])
def delete_user(request):
    msg=""
    id=request.GET.get('id')
    Friends.objects.filter(id=id).delete()
    friends = Friends.objects.filter().values('id','name', 'age', 'department', 'is_active' ).order_by('-id')
    friends_array=pagination(request,friends)
    friends=list(friends_array[0])
    data  = {"status":"200","msg":"success",'friends':friends,'total_pages':friends_array[1],'entries_per_page':entries_per_page}
    return JsonResponse(data,safe=False)

@api_view(['GET'])
def add_edit_user(request):
    msg=""
    # user=request.POST['user']
    id=request.GET.get('id')
   
    name=request.GET.get('name')
    age=request.GET.get('age')
    department=request.GET.get('department')
    if id!="":
        instance =Friends.objects.get(id=id) 
        data={
            'id'        :id,
            'name'      :name,
            'age'       : age,
            'department':department ,
        }
    else:
        data={
            'name'      :name,
            'age'       : age,
            'department':department ,
        }
    print(id,age,name,department)
    form = adding_friends(data=data)
    if form.is_valid():
        if id!="":
            form.update(instance=instance,validated_data=data)
        else:
            form.save()
        friends = Friends.objects.filter().values('id','name', 'age', 'department', 'is_active' ).order_by('-id')
        friends_array=pagination(request,friends)
        friends=list(friends_array[0])
        data  = {"status":"200","msg":"success",'friends':friends,'total_pages':friends_array[1],'entries_per_page':entries_per_page}
    else:
        friends = Friends.objects.filter().values('id','name', 'age', 'department', 'is_active' ).order_by('-id')
        friends_array=pagination(request,friends)
        friends=list(friends_array[0])
        print(form.errors)
        error_msg={}
        for key, value in form.errors.items() :
            error_msg[key] = value[0]
        data  = {"status":"500","msg":"failure",'friends':friends,'total_pages':friends_array[1],'error_msg':error_msg,'entries_per_page':entries_per_page}
    return JsonResponse(data,safe=False)