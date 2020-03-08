from django.contrib import admin
from .models import house

class HouseObjectsAdmin(admin.ModelAdmin):
    list_display = ('house_name', 'electricity_use', 'logged_date')

# Register your models here.
admin.site.register(house, HouseObjectsAdmin)
