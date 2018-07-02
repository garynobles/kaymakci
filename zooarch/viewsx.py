from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from zooarch.models import Qnisp
import datetime
from .forms import QnispForm
from .filters import QnispFilter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . import filters

#https://tutorial.djangogirls.org/en/django_forms/

#https://tutorial.djangogirls.org/en/django_forms/
#from django.contrib.auth.models import User

# Create your views here.
#allqnisp's
def allqnisp(request):
    qnisp_list = Qnisp.objects.all()
    filtered_qs = filters.QnispFilter(request.GET, queryset=qnisp_list).qs
    paginator = Paginator(filtered_qs, 10)

    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)
    return render(request,'qnisp/allqnisp.html',{'response': response})
    #store = Store.objects
    #return render(request, 'store/allstorage.html', {'containerpage':containerpage})

def detailqnisp(request, qnisp_id):
    detailqnisp = get_object_or_404(Qnisp, pk=qnisp_id)
    return render(request, 'qnisp/detailqnisp.html', {'qnisp':detailqnisp})

def createqnisp(request):
    if request.method == "POST":
        form = QnispForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('allqnisp')
    else:
        form = QnispForm()
    return render(request, 'qnisp/create_qnisp.html', {'form': form})

def editqnisp(request, pk):
    post = get_object_or_404(Qnisp, pk=pk)
    if request.method == "POST":
        form = QnispForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('allqnisp')
            #, pk=post.pk)
    else:
        form = QnispForm(instance=post)
    return render(request, 'qnisp/create_qnisp.html', {'form': form})
