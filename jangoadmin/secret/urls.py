from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from secret.views import Dashboard, Login, Register, ForgotPassword, SampleReports, SampleListing, Logout, Settings, ChangePassword, Profile

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
]
urlpatterns = format_suffix_patterns(urlpatterns)
