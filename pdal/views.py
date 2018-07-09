from django.shortcuts import render

# Create your views here.
def pdal(request):
    #detailcontainer = get_object_or_404(Container, pk=container_id)
    return render(request, 'pdal/pdal.html', {pdal:pdal})
