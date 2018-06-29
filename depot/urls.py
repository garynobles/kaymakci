from django.urls import path
from django.conf.urls import url

from . import views

from depot.views import SamplesListView

urlpatterns = [
    #samples
    #path('samples/', views.SamplesListView, name='SamplesListView'),
    url(r'^samples/$', SamplesListView.as_view(template_name="samples/allsamples.html"), name='SamplesListView'),

    #url(r'^$', CurrencyListView.as_view()),
    #url(r'^createstore/$', views.createstore, name='createstore'),

    #url(r'^samples/$', SamplesListView.as_view(template_name="currencies/currency_filter.html")),




    url(r'^currencies/edit/(?P<pk>\d+)/edit/$', views.editsample, name='editsample'),






    #url(r'^samples/$', views.allsamples, name='allsamples'),
    path('samples/<int:sample_id>/', views.detailsamples, name='detailsamples'),

    url(r'^currencies/createsample/$', views.createsample, name='createsample'),




    #store
    path('store/', views.allstore, name='allstore'),
    path('<int:store_id>/', views.detailstore, name='detailstore'),

    url(r'^createstore/$', views.createstore, name='createstore'),
    url(r'^editstore/(?P<pk>\d+)/editstore/$', views.editstore, name='editstore'),

    #locations
    url(r'^location/$', views.alllocation, name='alllocation'),
    path('location/<int:location_id>/', views.detaillocation, name='detaillocation'),

    url(r'^createlocation/$', views.createlocation, name='createlocation'),
    url(r'^location/edit/(?P<pk>\d+)/edit/$', views.editlocation, name='editlocation'),

    #container
    url(r'^container/$', views.allcontainer, name='allcontainer'),
    path('container/<int:container_id>/', views.detailcontainer, name='detailcontainer'),

    url(r'^container/createcontainer/$', views.createcontainer, name='createcontainer'),
    url(r'^container/edit/(?P<pk>\d+)/edit/$', views.editcontainer, name='editcontainer'),
    url(r'^container/search/edit/(?P<pk>\d+)/edit/$', views.editcontainersearch, name='editcontainersearch'),


    url(r'^samples/search/edit/(?P<pk>\d+)/edit/$', views.editsamplesearch, name='editsamplesearch'),

    #storage
    url(r'^storage/$', views.allstorage, name='allstorage'),
    path('storage/<int:store_id>/', views.detailstorage, name='detailstorage'),

    url(r'^storage/createstorage/$', views.createstorage, name='createstorage'),
    url(r'^storage/edit/(?P<pk>\d+)/edit/$', views.editstorage, name='editstorage'),

    #samples
    #url(r'^samples/$', views.allsamples, name='allsamples'),
    #path('samples/<int:sample_id>/', views.detailsamples, name='detailsamples'),

    #url(r'^samples/createsample/$', views.createsample, name='createsample'),
    #url(r'^samples/edit/(?P<pk>\d+)/edit/$', views.editsample, name='editsample'),


    #filtering and pagination
    #url(r'^container/search/$', views.containerfilterpage, name='containerfilterpage'),

    #pagination only
    #url(r'^users/page/$', views.index, name='index'),
    #filtering only

    url(r'^samples/filter/$', views.samplesearch, name='samplesearch'),
    url(r'^container/filter/$', views.containersearch, name='containersearch'),

    url(r'^container/page/$', views.containerpage, name='containerpage'),

    url(r'^samples/listing/$', views.listing, name='listing'),

]
