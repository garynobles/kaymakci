from django.shortcuts import render

# Create your views here.
# def gallery(request):
#     pass

def gallery(request):
    return render(request, 'gallery/base.html', {'gallery':gallery})
