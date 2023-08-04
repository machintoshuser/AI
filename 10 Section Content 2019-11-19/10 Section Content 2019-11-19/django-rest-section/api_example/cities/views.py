from django.shortcuts import render
from rest_framework import viewsets
from .models import City
from .serializers import CitySerializer
# Create your views here.


class CityView(viewsets.ModelViewSet):
    '''
    retrieve:
        Return a city instance

    list:
    		Return all cities
    '''
    queryset = City.objects.all()
    serializer_class = CitySerializer