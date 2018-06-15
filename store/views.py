from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, render_to_response
from store.models import Store, Container, Location,  Samples, Storage
import datetime
from .forms import StoreForm, ContainerForm, LocationForm, StorageForm, SamplesForm

#https://tutorial.djangogirls.org/en/django_forms/


#filters
##from django.contrib.auth.models import User
#from .filters import ContainerFilter
#from .filters import  ContainerFilter, SampleFilter #UserFilter,

# Create your views here.








#stores
def allstore(request):
    store = Store.objects
    return render(request, 'store/allstore.html', {'store':store})

def detailstore(request, store_id):
    detailstore = get_object_or_404(Store, pk=store_id)
    return render(request, 'store/detailstore.html', {'store':detailstore})

def createstore(request):
    if request.method == "POST":
        form = StoreForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('allstore')
    else:
        form = StoreForm()
    return render(request, 'store/create_store.html', {'form': form})

def editstore(request, pk):
    post = get_object_or_404(Store, pk=pk)
    if request.method == "POST":
        form = StoreForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('allstore')
            #, pk=post.pk)
    else:
        form = StoreForm(instance=post)
    return render(request, 'store/create_store.html', {'form': form})




#all locations
def alllocation(request):
    alllocation = Location.objects
    return render(request, 'location/alllocation.html', {'location':alllocation})

def detaillocation(request, location_id):
    detaillocation = get_object_or_404(Location, pk=location_id)
    return render(request, 'location/detaillocation.html', {'location':detaillocation})

def createlocation(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('alllocation')
    else:
        form = LocationForm()
    return render(request, 'location/create_location.html', {'form': form})

def editlocation(request, pk):
    post = get_object_or_404(Location, pk=pk)
    if request.method == "POST":
        form = LocationForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('alllocation')
            #, pk=post.pk)
    else:
        form = LocationForm(instance=post)
    return render(request, 'location/create_location.html', {'form': form})





#allcontainers
def allcontainer(request):
    allcontainer = Container.objects
    return render(request, 'container/allcontainer.html', {'container':allcontainer})

def detailcontainer(request, container_id):
    detailcontainer = get_object_or_404(Container, pk=container_id)
    return render(request, 'container/detailcontainer.html', {'container':detailcontainer})

def createcontainer(request):
    if request.method == "POST":
        form = ContainerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('allcontainer')
    else:
        form = ContainerForm()
    return render(request, 'container/create_container.html', {'form': form})

def editcontainer(request, pk):
    post = get_object_or_404(Container, pk=pk)
    if request.method == "POST":
        form = ContainerForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('allcontainer')
            #, pk=post.pk)
    else:
        form = ContainerForm(instance=post)
    return render(request, 'container/create_container.html', {'form': form})


#all samples
def allsamples(request):
    samples = Samples.objects
    return render(request, 'samples/allsamples.html', {'samples':samples})

def detailsamples(request, sample_id):
    detailsamples = get_object_or_404(Samples, pk=sample_id)
    return render(request, 'samples/detailsamples.html', {'samples':detailsamples})

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
    return render(request, 'samples/create_samples.html', {'form': form})


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
    return render(request, 'samples/create_samples.html', {'form': form})


#all storages
def allstorage(request):
    allstorage = Storage.objects
    return render(request, 'storage/allstorage.html', {'storage':allstorage})

def detailstorage(request, store_id):
    detailstorage = get_object_or_404(Storage, pk=store_id)
    return render(request, 'storage/detailstorage.html', {'storage':detailstorage})

def createstorage(request):
    if request.method == "POST":
        form = StorageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('allstorage')
    else:
        form = StorageForm()
    return render(request, 'storage/create_storage.html', {'form': form})

def editstorage(request, pk):
    post = get_object_or_404(Storage, pk=pk)
    if request.method == "POST":
        form = StorageForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('allstorage')
            #, pk=post.pk)
    else:
        form = StorageForm(instance=post)
    return render(request, 'storage/create_storage.html', {'form': form})
