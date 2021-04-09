from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import Register, Login, Logout, Dashboard, MyProfile, Avatar, ChangePassword, ForgotPassword

urlpatterns = [
    path('register/', Register,name="register"),
    path('login/', Login,name="login"),
    path('profile/', MyProfile),
    path('avatar/', Avatar),
    path('change-password/', ChangePassword),
    path('forgot-password/', ForgotPassword),
    path('logout/', Logout),
    path('home/', Dashboard),
]
urlpatterns = format_suffix_patterns(urlpatterns)
