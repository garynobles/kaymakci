import datetime
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from .models import Processing3d
from .forms import Processing3dForm
from .filters import Processing3dFilter
from . import filters

# Create your views here.
def processing3dpage(request):
    processing3d_list = Processing3d.objects.all()
    filtered_qs = filters.Processing3dFilter(request.GET, queryset=processing3d_list).qs
    paginator = Paginator(filtered_qs, 10)

    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)
    return render(request,'spatial3d/processing3d.html',{'response': response})

def detailprocessing3d(request, id):
    detailprocessing3d = get_object_or_404(Processing3d, pk=id)
    return render(request, 'spatial3d/detailprocessing3d.html', {'detailprocessing3d':detailprocessing3d})




def createprocessing3d(request):
    if request.method == "POST":
        form = Processing3dForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.created_by = request.user
            #post.modified_by = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('processing3dpage')
    else:
        form = Processing3dForm()
    return render(request, 'spatial3d/create_processing3d.html', {'form': form})

def editprocessing3d(request, pk):
    post = get_object_or_404(Processing3d, pk=pk)
    if request.method == "POST":
        form = Processing3dForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('processing3dpage')
            #, pk=post.pk)
    else:
        form = Processing3dForm(instance=post)
    return render(request, 'spatial3d/create_processing3d.html', {'form': form})
