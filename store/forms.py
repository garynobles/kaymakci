from django import forms

from .models import Store



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
