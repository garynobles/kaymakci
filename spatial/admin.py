#from django.contrib import admin

# Register your models here.
from django.contrib.gis import admin
from .models import WorldBorder
from .models import Trench_99_528

admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(Trench_99_528, admin.GeoModelAdmin)
