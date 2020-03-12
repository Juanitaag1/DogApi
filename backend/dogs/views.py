#from django.shortcuts import render

# Create your views here.
#dogs/views.py
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Dog
from .models import Breed
from .serializers import DogSerializer
from .serializers import BreedSerializer
from rest_framework import generics
#from rest_framework.response import Response
#from rest_framework.reverse import reverse


class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    #name = 'dog-list'


class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    #name = 'dog-detail'

class BreedList(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    #name = 'breed-list'


class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
#    name = 'breed-detail'
