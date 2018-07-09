from django.shortcuts import render
from django import forms
from django.utils.translation import ugettext
import django_filters
from django_filters.filterset import ORDER_BY_FIELD
# Create your views here.


from .models import Storage, Container, Location, Samples, JoinSampleContainer
from filters.views import FilterMixin


class SamplesForm(forms.ModelForm):

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

        #'container_id'

        )


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = (
        #'id',
        'location_id',
        'store_id',
        'icon_desc',
        'location_identifier',
        'location_type',
        'current_location_tmp',
        'location_name',
        'orderby',

        )

class StorageForm(forms.ModelForm):

    class Meta:
        model = Storage
        fields = (
        #'id',
        'store_id',
        'store_name',
        'address_1',
        'address_2',
        'region',
        'zip',
        'city',
        'country',
        'icon_desc',

        )



class ContainerForm(forms.ModelForm):

    class Meta:
        model = Container
        fields = (
        'container_id',
        'container_name',
        'container_type',
        'location_id',
        'icon_desc'
        )


class JoinSampleContainerForm(forms.ModelForm):

    class Meta:
        model = JoinSampleContainer
        fields = (
        'id',
        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        #container_id = models.ForeignKey(Container, db_column='container_id', on_delete = models.PROTECT)
        'container_id',
        )
