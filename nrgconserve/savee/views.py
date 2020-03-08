from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializers import EnergySerializer, houseSerializer
from rest_framework.response import Response
from django.shortcuts import render

import json
from rest_framework.parsers import JSONParser
import pickle

from .models import house

# Create your views here.

# fetches 
@api_view(['get'])
def fetch_neighbourhood(request):
    house_energy_use = house.objects.all()
    #serialize
    serializer = EnergySerializer(house_energy_use, many=True)
    #return Response using rest_framework's response
    return Response(serializer.data)

@api_view(['get'])
def fetch_rankings(request):
    houses = house.objects.all().filter(logged_date="2020-02-20").order_by('-electricity_use')
    serializer = houseSerializer(houses, many=True)
    return Response(serializer.data)


def main_home(request):
    """View function for home page of site."""

    field_name = 'electricity_use'
    houses = house.objects.filter(house_name = 'house1', logged_date = '2020-02-21').get()
    
    context = {
        'energy_consumption': getattr(houses, field_name)
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, '3-main_home.html', context=context)
