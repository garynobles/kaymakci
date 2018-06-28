from django.contrib import admin

# Register your models here.
from .models import Store, Container, Location, Icon

admin.site.register(Store)
admin.site.register(Container)
admin.site.register(Location)
admin.site.register(Icon)
