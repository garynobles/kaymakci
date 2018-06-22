from django.shortcuts import render

# Create your views here.
def allspatial(request):
    #allspatial = Spatial.objects
    return render(request, 'spatial/allspatial.html', {'allspatial':allspatial})
