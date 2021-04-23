from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import UserSignUp,LoginView,ChangePassWord,AvatarView 
urlpatterns = [
    path('register/', UserSignUp.as_view(),name="register"),
    path('login/', LoginView.as_view(),name="login"),
    path('change-password/', ChangePassWord.as_view(),name="ChangePassWord"),
    # path('profile/', MyProfile),
    path('avatar/', AvatarView.as_view(),name="AvatarView"),
    
    # path('forgot-password/', ForgotPassword),
    # path('logout/', Logout),
    # path('home/', Dashboard),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
