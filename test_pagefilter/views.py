from django.shortcuts import render
from django import forms
from django.utils.translation import ugettext
import django_filters
from django_filters.filterset import ORDER_BY_FIELD
# Create your views here.

from test_pagefilter.models import Location
from filters.views import FilterMixin


class LocationFilterForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = (
        #'sample_id',
        'location_id',
        'location_identifier',
        'location_name',
        'location_type',
        'current_location_tmp',

        )

class LocationFilter(django_filters.FilterSet):

    class Meta:  # pylint: disable=C1001
        form = LocationFilterForm
        model = Location
        fields = [
        'location_id',
        'location_identifier',
        'location_name',
        'location_type',
        'current_location_tmp',

        ]
        order_by = (
            ('location_name', ugettext("A-Z")),
            ('-location_name', ugettext("Z-A")),
        )

class LocationListView(FilterMixin, django_filters.views.FilterView):
    model = Location
    paginate_by = 22
    filterset_class = LocationFilter
