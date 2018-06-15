from django.contrib import admin

# Register your models here.
from .models import Store
from .models import Container, Location

admin.site.register(Store)
admin.site.register(Container)
admin.site.register(Location)
