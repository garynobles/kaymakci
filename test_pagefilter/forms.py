from django.shortcuts import render
from django import forms
from django.utils.translation import ugettext
import django_filters
from django_filters.filterset import ORDER_BY_FIELD
# Create your views here.

from test_pagefilter.models import Samples
from filters.views import FilterMixin




class SamplesFilterForm(forms.ModelForm):
    class Meta:
        model = Samples
        fields = (
        #'sample_id',
        'location_id',
        'location_identifier',
        'location_name',
        'location_type',
        'current_location_tmp',

        )
