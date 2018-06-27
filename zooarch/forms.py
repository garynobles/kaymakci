from django import forms
from .models import Qnisp

class QnispForm(forms.ModelForm):

    class Meta:
        model = Qnisp
        fields = (
        'qnisp_id',
        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        'collection_method',
        'mandible_with_teeth',
        'bt',
        'ss',
        'oc_tje',
        'ch',
        'oa',
        'equid',
        'cer',
        'lp',
        'meles',
        'pesc',
        'brd',
        'canis',
        'unio',
        'cerastoderma',
        'landsnail',
        'shell_other',
        'rodent',
        'comments',
        'ursus',
        'big_feline_lynx_size',
        )
