from django.urls import include, path
from .views import HarvestAPIView, BreadAPIView
urlpatterns = [
    path('all-harvest/',HarvestAPIView.as_view()),
    path('all-bread/', BreadAPIView.as_view())

    ]