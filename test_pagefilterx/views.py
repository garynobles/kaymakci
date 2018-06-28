from django.shortcuts import render
#from test_pagefilter.models import Currency
# Create your views here.
from django import forms
from django.utils.translation import ugettext
import django_filters
from django_filters.filterset import ORDER_BY_FIELD
from currencies.models import Currency
from filters.views import FilterMixin

#from .filters import CurrencyFilter
#from . import filters

#goes in forms
class CurrencyFilterForm(forms.Form):

    def __init__(self, data={}, *args, **kwargs):
        super(CurrencyFilterForm, self).__init__(data, *args, **kwargs)  # NOQA
        try:
            self.fields[ORDER_BY_FIELD].widget.attrs = {
                'onchange': "this.form.submit();",
            }
        except KeyError:
            pass

class CurrencyFilter(django_filters.FilterSet):

    class Meta:  # pylint: disable=C1001
        form = CurrencyFilterForm
        model = Currency
        fields = []
        order_by = (
            ('code', ugettext("A-Z")),
            ('-code', ugettext("Z-A")),
        )



class CurrencyListView(FilterMixin, django_filters.views.FilterView):
    model = Currency
    paginate_by = 12
    filterset_class = CurrencyFilter
