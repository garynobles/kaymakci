from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('processing/', views.processing3dpage, name='processing3dpage'),
    path('processing/<int:id>/', views.detailprocessing3d, name='detailprocessing3d'),

    url(r'^processing/create$', views.createprocessing3d, name='createprocessing3d'),
    url(r'^processing/edit/(?P<pk>\d+)/edit/$', views.editprocessing3d, name='editprocessing3d'),
]
