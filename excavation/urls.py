from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('context/', views.contextpage, name='contextpage'),
    path('context/<int:context_id>/', views.detailcontext, name='detailcontext'),

    #url(r'^excavation/createcontext/$', views.createcontext, name='createcontext'),
    url(r'^context/editcontext/(?P<pk>\d+)/editcontext/$', views.editcontext, name='editcontext'),
    url(r'^context/search/edit/(?P<pk>\d+)/edit/$', views.editcontextsearch, name='editcontextsearch'),


    ]
