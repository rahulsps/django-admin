"""jangoadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.views.generic.base import TemplateView

#from frontend.views import Home, ForgotPassword, ResetPassword

#from kuldeep.views import *

#router = routers.DefaultRouter()

#router.register(r'harvest', HarvestViewSet),
#router.register(r'bread', BreadViewSet),

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include(router.urls)),
    #path('secret/', include('secret.urls')),
    path('api/', include('api.urls')),
    #path('forgot-password/', ForgotPassword),
    #path('reset-password/<str:token>/', ResetPassword),
    #path('', Home),
    #path('users/', include('users.urls'))
]
