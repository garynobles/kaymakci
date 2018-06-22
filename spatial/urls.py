from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    #store
    path('spatial/', views.allspatial, name='allspatial'),
#    path('<int:store_id>/', views.detailstore, name='detailstore'),

#    url(r'^createstore/$', views.createstore, name='createstore'),
#    url(r'^editstore/(?P<pk>\d+)/editstore/$', views.editstore, name='editstore'),


]
