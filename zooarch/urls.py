from django.urls import path
from django.conf.urls import url

from . import views

from zooarch.views import ZooarchListView, QnispListView

urlpatterns = [
    #zooarch

    path('', ZooarchListView.as_view(template_name="zooarch/allzooarch.html"), name='allzooarch'),
    path('qnisp/', QnispListView.as_view(template_name="zooarch/allqnisp.html"), name='allqnisp'),

    path('zooarch/<int:sample_id>/', views.detailzooarch, name='detailzooarch'),
    url(r'^zooarch/edit/(?P<pk>\d+)/edit/$', views.editzooarch, name='editzooarch'),
    url(r'^zooarch/createzooarch/$', views.createzooarch, name='createzooarch'),

    #url(r'^qnisp/$', views.allqnisp, name='allqnisp'),
    path('qnisp/<int:sample_id>/', views.detailqnisp, name='detailqnisp'),
    url(r'^qnisp/createqnisp/$', views.createqnisp, name='createqnisp'),
    url(r'^qnisp/edit/(?P<pk>\d+)/edit/$', views.editqnisp, name='editqnisp'),

]
