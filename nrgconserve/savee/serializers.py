from rest_framework.serializers import ModelSerializer
from .models import house


class EnergySerializer(ModelSerializer):
    class Meta:
        model = house
        fields = '__all__'