import django_filters

from .models import Container

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
