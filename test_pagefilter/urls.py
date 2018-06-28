from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    #store
    path('test/', views.LocationListView, name='LocationListView'),
    #url(r'^$', CurrencyListView.as_view()),
    #url(r'^createstore/$', views.createstore, name='createstore'),
]
