from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    #store
    url('', views.allstore, name='allstore'),
    path('<int:store_id>/', views.detailstore, name='detailstore'),

    url(r'^createstore/$', views.createstore, name='createstore'),
    url(r'^edit/(?P<pk>\d+)/edit/$', views.editstore, name='editstore'),

    #locations
    url(r'^location/$', views.alllocation, name='alllocation'),
    path('<int:location_id>/', views.detaillocation, name='detaillocation'),

    url(r'^createlocation/$', views.createlocation, name='createlocation'),
    url(r'^edit/(?P<pk>\d+)/edit/$', views.editlocation, name='editlocation'),

]
