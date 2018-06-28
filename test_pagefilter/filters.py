from django.shortcuts import render
from django import forms
from django.utils.translation import ugettext
import django_filters
from django_filters.filterset import ORDER_BY_FIELD
# Create your views here.

from test_pagefilter.models import Samples
from filters.views import FilterMixin

#from .forms LocationFilterForm

class SamplesFilter(django_filters.FilterSet):

    def __init__(self, data={}, *args, **kwargs):
        super(SamplesFilterForm, self).__init__(data, *args, **kwargs)  # NOQA
        try:
            self.fields[ORDER_BY_FIELD].widget.attrs = {
                'onchange': "this.form.submit();",
            }
        except KeyError:
            pass

    class Meta:  # pylint: disable=C1001
        form = SamplesFilterForm
        model = Samples
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
