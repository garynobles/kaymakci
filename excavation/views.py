from .models import Context
# Create your views here.

from django.shortcuts import render, get_object_or_404, render_to_response, redirect

import datetime
from .forms import ContextForm
from .filters import ContextFilter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . import filters

#https://tutorial.djangogirls.org/en/django_forms/

#https://tutorial.djangogirls.org/en/django_forms/
from django.contrib.auth.models import User



#def contextpage(request):
#    context = Context.objects
#    return render(request, 'excavation/context_filter.html', {'context':context})


def contextpage(request):
    # BTW you do not need .all() after a .filter()
    # local_url.objects.filter(global_url__id=1) will do
    context_list = Context.objects.all()
    filtered_qs = filters.ContextFilter(request.GET, queryset=context_list).qs
    paginator = Paginator(filtered_qs, 10)

    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)
    return render(request,'context/context_page.html',{'response': response})
    #store = Store.objects
    #return render(request, 'store/allstore.html', {'containerpage':containerpage})



def detailcontext(request, context_id):
    detailcontext = get_object_or_404(context, pk=context_id)
    return render(request, 'context/detailcontext.html', {'context':detailcontext})

#def createcontext(request):

    #return render(request, '')

def editcontextsearch(request, pk):
    post = get_object_or_404(Context, pk=pk)
    if request.method == "POST":
        form = ContextForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('contextsearch')
            #, pk=post.pk)
    else:
        form = ContextForm(instance=post)
    return render(request, 'context/create_context.html', {'form': form})

def editcontext(request, pk):
    post = get_object_or_404(context, pk=pk)
    if request.method == "POST":
        form = contextForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('contextpage')
            #, pk=post.pk)
    else:
        form = contextForm(instance=post)
    return render(request, 'context/create_context.html', {'form': form})
