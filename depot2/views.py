from django.shortcuts import render
from django import forms
from django.utils.translation import ugettext
import django_filters
from django_filters.filterset import ORDER_BY_FIELD
# Create your views here.

from .models import Samples
from filters.views import FilterMixin

#from .forms import LocationFilterForm

#from depot2.forms import SamplesFilterForm
#from depot2.filters import SamplesFilter

class SamplesFilterForm(forms.ModelForm):
    class Meta:
        model = Samples
        fields = (
        #'sample_id',
        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        'material',
        'specific_material',
        'exterior_color_hue',
        'exterior_color_lightness_value',
        'exterior_color_chroma',
        'interior_color_hue',
        'interior_color_lightness_value',
        'interior_color_chroma',
        'weight_kilograms',
        'sample_description',
        'category',
        'subcategory',
        'count',
        'current_location',
        'recovery_type',
        'problems',
        'image_files',
        'number_3d_files',
        'chronology',
        'analysis_request',
        'detailed_sample_description',
        'bureaucratic_status',
        'subjective_significance',
        'museum_inventory_number',
        'bureaucratic_status_identifier',

        )


class SamplesFilter(django_filters.FilterSet):

    class Meta:  # pylint: disable=C1001
        form = SamplesFilterForm
        model = Samples
        fields = [
        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        'material',
        'specific_material',
        'exterior_color_hue',
        'exterior_color_lightness_value',
        'exterior_color_chroma',
        'interior_color_hue',
        'interior_color_lightness_value',
        'interior_color_chroma',
        'weight_kilograms',
        'sample_description',
        'category',
        'subcategory',
        'count',
        'current_location',
        'recovery_type',
        'problems',
        'image_files',
        'number_3d_files',
        'chronology',
        'analysis_request',
        'detailed_sample_description',
        'bureaucratic_status',
        'subjective_significance',
        'museum_inventory_number',
        'bureaucratic_status_identifier',

        ]
        order_by = (
            ('sample_number', ugettext("A-Z")),
            ('-sample_number', ugettext("Z-A")),
        )





class SamplesListView(FilterMixin, django_filters.views.FilterView):
    model = Samples
    paginate_by = 10
    filterset_class = SamplesFilter

def editcontainersearch(request):
    pass






def allsamples(request):
    pass

def detailsamples(request):
    pass

def createsample(request):
    pass


def editsample(request, pk):
    pass
