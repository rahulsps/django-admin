from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from secret.views import Dashboard, Login, Register, ForgotPassword, SampleReports, SampleListing, Logout, Settings, ChangePassword, Profile
from secret.angular_crud import list_users, get_user_data, delete_user,add_edit_user

urlpatterns = [
    path('', Dashboard),
	path('login/', Login, name="secretLogin"),
	path('register/', Register),
	path('forgot-password/', ForgotPassword),
	path('sample-listing/', SampleListing),
	path('sample-reports/', SampleReports),
	path('settings/', Settings),
	path('profile/', Profile),
	path('change-password/', ChangePassword),
	path('logout/', Logout),

	path('list_users/', list_users),
    path('get_user_data/', get_user_data),
    path('delete_user/', delete_user),
    path('add_edit_user/', add_edit_user),

]
urlpatterns = format_suffix_patterns(urlpatterns)






