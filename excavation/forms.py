
from django import forms
from .models import Contexts

class ContextForm(forms.ModelForm):
    class Meta:
        model = contexts
        fields = (
        'context_id',
        'area_easting',
        'area_northing',
        'context_number',
        'context_type',
        'description',
        'deposition_interpretation',
        'subtable',
        'chronology',
        'chronology_source',
        'stratigraphic_narrative',
        )
