# from django.shortcuts import render
#
# def upload(request):
#
#     return render(request, 'upload_photo/upload_photo.html', {upload:upload})
#

# from datetime import datetime



# views.py
from django.views.generic.edit import FormView
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from .forms import UploadForm
from .models import Attachment


class UploadView(FormView):
    template_name = 'upload_photo/upload_photo.html'
    form_class = UploadForm
    success_url = '/upload/photo2/'


    def form_valid(self, form):
        photobatch_id=1
        # time=datetime.now()
        for each in form.cleaned_data['attachments']:
            Attachment.objects.create(file=each, photobatch=photobatch_id)


        return super(UploadView, self).form_valid(form)

def allimages(request):
    allimages = Attachment.objects
    return render(request, 'upload_photo/images.html', {'attachment':allimages})


# def allstorage(request):
#     allstorage = Storage.objects
#     return render(request, 'storage/allstorage.html', {'storage':allstorage})
