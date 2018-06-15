from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    #store
    url('', views.allstore, name='allstore'),
    path('<int:store_id>/', views.detailstore, name='detailstore'),

    url(r'^createstore/$', views.createstore, name='createstore'),
    url(r'^edit/(?P<pk>\d+)/edit/$', views.editstore, name='editstore'),

]
