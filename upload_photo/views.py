from django.shortcuts import render

def upload(request):

    return render(request, 'upload_photo/upload_photo.html', {upload:upload})
