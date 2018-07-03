from django.urls import path
from django.conf.urls import url

from . import views

from ceramics.views import CeramicsListView

urlpatterns = [
    #ceramics

    #url(r'^""$', CeramicsListView.as_view(template_name="ceramics/allceramics.html"), name='allceramics'),
    path('ceramics/', CeramicsListView.as_view(template_name="ceramics/allceramics.html"), name='allceramics'),


    path('ceramics/<int:sample_id>/', views.detailceramics, name='detailceramics'),
    url(r'^ceramics/edit/(?P<pk>\d+)/edit/$', views.editceramics, name='editceramics'),
    url(r'^ceramics/createceramics/$', views.createceramics, name='createceramics'),


]
