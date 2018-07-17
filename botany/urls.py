from django.urls import path

from . import views

urlpatterns = [
    path('', views.allbotany, name='allbotany'),
    #path('<int:blog_id>/', views.detail, name='detail'),


    path('fraction/', views.allfraction, name='allfraction'),

    path('fractioncomposition/', views.allfractioncomposition, name='allfractioncomposition'),
    path('fractionmaterialpresent/', views.allfractionmaterialpresent, name='allfractionmaterialpresent'),

    path('createfraction/', views.createfraction, name='createfraction'),
    path('createbotany/', views.createbotany, name='create_botany'),
    path('botany/<int:botany_id>/', views.detailbotany, name='detailbotany'),
    path('fraction/<int:fraction_id>/', views.detailfraction, name='detailfraction'),


    path('createfractioncomposition/', views.createfractioncomposition, name='create_fractioncomposition'),
    path('createfractionmaterialpresent/', views.createfractionmaterialpresent, name='create_fractionmaterialpresent'),

    path('detailfractioncomposition/<int:fract_comp_id>/', views.detailfractioncomposition, name='detailfractioncomposition'),
    path('detailfractionmaterialpresent/<int:material_id>/', views.detailfractionmaterialpresent, name='detailfractionmaterialpresent'),


    path('fraction/edit/(?P<pk>\d+)/edit/$', views.editfraction, name='editfraction'),
]
