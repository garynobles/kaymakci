import django_filters

from .models import Container, Samples

class ContainerFilter(django_filters.FilterSet):
    class Meta:
        model = Container
        fields = [
        'container_id',
        'container_name',
        'container_type',
        'location_id',
        'sample_id',
        'current_location_tmp',
        ]

class SamplesFilter(django_filters.FilterSet):
    class Meta:
        model = Samples
        fields = [
        'sample_id',
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
        'container_id',


    ]
