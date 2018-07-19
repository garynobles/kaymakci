# from django.shortcuts import render
#
# def upload(request):
#
#     return render(request, 'upload_photo/upload_photo.html', {upload:upload})
#

# views.py
from django.views.generic.edit import FormView

from .forms import UploadForm
from .models import Attachment


class UploadView(FormView):
    template_name = 'upload_photo/upload_photo.html'
    form_class = UploadForm
    success_url = '/upload/photo/'

    def form_valid(self, form):
        for each in form.cleaned_data['attachments']:
            Attachment.objects.create(file=each)
        return super(UploadView, self).form_valid(form)
