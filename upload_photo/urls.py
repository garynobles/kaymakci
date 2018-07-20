from django.urls import path

from . import views


urlpatterns = [
    path('photo/', views.UploadView.as_view(), name='photo_upload'),
    path('photo2/', views.allimages, name='allimages'),
]
