# dogs/urls.py
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from django.conf.urls import url
#from . import views
from dogs import views
from .controllers import DogList, DogDetails, BreedList, BreedDetails


urlpatterns = [
    path(r'dogs/', views.DogList.as_view()),
        #name=views.DogList.name),
    path(r'dogs/<int:pk>/', views.DogDetail.as_view()),
        #name=views.DogDetail.name),
    path(r'breeds/', views.BreedList.as_view()),
        #name=views.BreedList.name),
    path(r'breeds/<int:pk>/', views.BreedDetail.as_view()),
        #name=views.BreedDetail.name),
]
urulpatterns = format_suffix_patterns(urlpatterns)
