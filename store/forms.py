from django import forms

from .models import Store
from .models import Location

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
