from django.shortcuts import render
from django import forms
from django.utils.translation import ugettext
import django_filters
from django_filters.filterset import ORDER_BY_FIELD
# Create your views here.

from depot.models import Samples, Container, Location
from filters.views import FilterMixin

#from .forms import LocationFilterForm

# def detailsamples(request, sample_id):
#     detailsamples = get_object_or_404(Samples, pk=sample_id)
#     return render(request, 'samples/detailsamples.html', {'samples':detailsamples})
#
def allstore(request):
    pass

def detailstore(request):
    pass

def createstore(request):
    pass

def editstore(request):
    pass

def alllocation(request):
    pass

def detaillocatiob(request):
    pass

def detaillocation(request):
    pass

def createlocation(request):
    pass

def editlocation(request):
    pass

def allcontainer(request):
    pass

def detailcontainer(request):
    pass

def createcontainer(request):
    pass

def editcontainer(request):
    pass

def editsamplesearch(request):
    pass

def allstorage(request):
    pass

def detailstorage(request):
    pass

def createstorage(request):
    pass

def editstorage(request):
    pass

def samplesearch(request):
    pass

def containerpage(request):
    pass

def listing(request):
    pass

#def allsamples(request):
#    return render(request,'samples/allsamples.html',{})

def detailsamples(request):
    pass






def containersearch(request):
    container_list = Container.objects.all()
    container_filter = ContainerFilter(request.GET, queryset=container_list)
    return render(request, 'search/container_filter.html', {'filter': container_filter})



def editcontainersearch(request, pk):
    post = get_object_or_404(Container, pk=pk)
    if request.method == "POST":
        form = ContainerForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('containersearch')
            #, pk=post.pk)
    else:
        form = ContainerForm(instance=post)
    return render(request, 'container/create_container.html', {'form': form})



def createsample(request):
    if request.method == "POST":
        form = SamplesForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('allsamples')
    else:
        form = SamplesForm()
    return render(request, 'currencies/create_samples.html', {'form': form})


def editsample(request, pk):
    post = get_object_or_404(Samples, pk=pk)
    if request.method == "POST":
        form = SamplesForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('allsamples')
            #, pk=post.pk)
    else:
        form = SamplesForm(instance=post)
    return render(request, 'currencies/create_samples.html', {'form': form})

#
# #all storages
# def allstorage(request):
#     allstorage = Storage.objects
#     return render(request, 'storage/allstorage.html', {'storage':allstorage})
#
# def detailstorage(request, store_id):
#     detailstorage = get_object_or_404(Storage, pk=store_id)
#     return render(request, 'storage/detailstorage.html', {'storage':detailstorage})
#
# def createstorage(request):
#     if request.method == "POST":
#         form = StorageForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             #post.user = request.user
#             #post.datetime = datetime.datetime.now()
#
#             post.save()
#             return redirect('allstorage')
#     else:
#         form = StorageForm()
#     return render(request, 'storage/create_storage.html', {'form': form})
#
# def editstorage(request, pk):
#     post = get_object_or_404(Storage, pk=pk)
#     if request.method == "POST":
#         form = StorageForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             #post.user = request.user
#             #post.datetime = datetime.datetime.now()
#             post.save()
#             return redirect('allstorage')
#             #, pk=post.pk)
#     else:
#         form = StorageForm(instance=post)
#     return render(request, 'storage/create_storage.html', {'form': form})





class SamplesFilterForm(forms.ModelForm):
    class Meta:
        model = Samples
        fields = (
        #'sample_id',
        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        'material',
        'specific_material',
        'exterior_color_hue',
        'exterior_color_lightness_value',
        'exterior_color_chroma',
        'interior_color_hue',
        'interior_color_lightness_value',
        'interior_color_chroma',
        'weight_kilograms',
        'sample_description',
        'category',
        'subcategory',
        'count',
        'current_location',
        'recovery_type',
        'problems',
        'image_files',
        'number_3d_files',
        'chronology',
        'analysis_request',
        'detailed_sample_description',
        'bureaucratic_status',
        'subjective_significance',
        'museum_inventory_number',
        'bureaucratic_status_identifier',

        )

class ContainerFilterForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = (
        'container_id',
        'container_name',
        'container_type',
        #'location_id',
        #'sample_id',
        'current_location_tmp',
        )

class LocationFilterForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = (

        'location_id',
        'location_identifier',
        #'store_id',
        'location_type',
        'current_location_tmp',
        'location_name',
        #'icon_desc'

        )




class SamplesFilter(django_filters.FilterSet):

    class Meta:  # pylint: disable=C1001
        form = SamplesFilterForm
        model = Samples
        fields = [
        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        'material',
        'specific_material',
        'exterior_color_hue',
        'exterior_color_lightness_value',
        'exterior_color_chroma',
        'interior_color_hue',
        'interior_color_lightness_value',
        'interior_color_chroma',
        'weight_kilograms',
        'sample_description',
        'category',
        'subcategory',
        'count',
        'current_location',
        'recovery_type',
        'problems',
        'image_files',
        'number_3d_files',
        'chronology',
        'analysis_request',
        'detailed_sample_description',
        'bureaucratic_status',
        'subjective_significance',
        'museum_inventory_number',
        'bureaucratic_status_identifier',

        ]
        order_by = (
            ('sample_number', ugettext("A-Z")),
            ('-sample_number', ugettext("Z-A")),
        )

class ContainerFilter(django_filters.FilterSet):

    class Meta:  # pylint: disable=C1001
        form = ContainerFilterForm
        model = Container
        fields = [
        'container_id',
        'container_name',
        'container_type',
        #'location_id',
        #'sample_id',
        'current_location_tmp',
        #'icon_desc'



        ]
class LocationFilter(django_filters.FilterSet):

    class Meta:  # pylint: disable=C1001
        form = LocationFilterForm
        model = Location
        fields = [
        'location_id',
        'location_identifier',
        #'store_id',
        'location_type',
        'current_location_tmp',
        'location_name',
        #'icon_desc'

        ]


class SamplesListView(FilterMixin, django_filters.views.FilterView):
    model = Samples
    paginate_by = 16
    filterset_class = SamplesFilter

class ContainerListView(FilterMixin, django_filters.views.FilterView):
    model = Container
    paginate_by = 16
    filterset_class = ContainerFilter

class LocationListView(FilterMixin, django_filters.views.FilterView):
    model = Location
    paginate_by = 16
    filterset_class = LocationFilter
