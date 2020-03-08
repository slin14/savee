from django.shortcuts import render
from django.http import HttpResponse
from .models import roomEnergy
from rest_framework.decorators import api_view
from .serializers import EnergySerializer
from rest_framework.response import Response

# Create your views here.

# fetches 
@api_view(['get'])
def fetch_roomEnergy(request):
    roomEnergyUse = roomEnergy.objects.all()
    #serialize
    serializer = EnergySerializer(roomEnergyUse, many=True)
    #return Response using rest_framework's response
    return Response(serializer.data)