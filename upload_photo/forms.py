
from django import forms

from multiupload.fields import MultiFileField
from .models import Attachment


class UploadForm(forms.Form):
    # attachments = MultiFileField(min_num=1, max_num=500, max_file_size=1024*1024*5)
    attachments = MultiFileField(min_num=1, max_num=500)

    class Meta:
        model = Attachment
        fields = (
        'photobatch',
        )
