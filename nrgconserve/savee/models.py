from django.db import models

# Create your models here.

class house(models.Model):
    house_name = models.CharField(max_length=30)
    electricity_use = models.FloatField()
    logged_date = models.DateField()




    
    