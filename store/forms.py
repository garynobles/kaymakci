from django import forms

from .models import Store
from .models import Location
from .models import Container



class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = (
        #'id',
        'store_id',
        'store_name',
        'address_1',
        'address_2',
        'region',
        'city',
        'country',
        )

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = (
        #'id',
        'location_id',
        'location_identifier',
        'store_id',
        'location_type',
        'current_location_tmp',
        'location_name',
        )






class ContainerForm(forms.ModelForm):

    class Meta:
        model = Container
        fields = (
        'container_id',
        'container_name',
        'container_type',
        'location_id',
        'sample_id',
        'current_location_tmp'
        )
