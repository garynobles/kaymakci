from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django import forms
from django.utils.translation import ugettext
import django_filters
from django_filters.filterset import ORDER_BY_FIELD
# Create your views here.

from .forms import CeramicsForm
from ceramics.models import Ceramics
from filters.views import FilterMixin


# Create your views here.
def createceramics(request):
    if request.method == "POST":
        form = CeramicsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('allceramics')
    else:
        form = CeramicsForm()
    return render(request, 'ceramics/create_ceramics.html', {'form': form})


def editceramics(request, pk):
    post = get_object_or_404(Ceramics, pk=pk)
    if request.method == "POST":
        form = CeramicsForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('allceramics')
            #, pk=post.pk)
    else:
        form = CeramicsForm(instance=post)
    return render(request, 'ceramics/create_ceramics.html', {'form': form})


def detailceramics(request):
    pass




class CeramicsFilterForm(forms.ModelForm):
    class Meta:
        model = Ceramics
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



class CeramicsFilter(django_filters.FilterSet):

    class Meta:  # pylint: disable=C1001
        form = CeramicsFilterForm
        model = Ceramics
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



class CeramicsListView(FilterMixin, django_filters.views.FilterView):
    def get_queryset(self, *atgs, **kwargs):
        object_list=Ceramics.objects.filter(material='Ceramic')
        return object_list
    model = Ceramics
    paginate_by = 16
    filterset_class = CeramicsFilter
