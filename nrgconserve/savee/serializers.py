from rest_framework.serializers import ModelSerializer
from .models import roomEnergy


class EnergySerializer(ModelSerializer):
    class Meta:
        model = roomEnergy
        fields = '__all__'