from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, render_to_response
from store.models import Store #, Container, Location,  Samples #Storage,
import datetime
from .forms import StoreForm #, ContainerForm, LocationForm #StorageForm,  SamplesForm

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
