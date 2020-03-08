from django.db import models

# Create your models here.

# each room uses a different amount of energy, so it's useful if we can keep track of the individual energy usage per room
class roomEnergy(models.Model):
    room_name = models.CharField(max_length=30)
    heat_use = models.FloatField()
    electricity_use = models.FloatField()