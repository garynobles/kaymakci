from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    #store
    path('test/', views.SamplesListView, name='SamplesListView'),
    #url(r'^$', CurrencyListView.as_view()),
    #url(r'^createstore/$', views.createstore, name='createstore'),
]
