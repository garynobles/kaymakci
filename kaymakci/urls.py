from django.contrib import admin
from django.contrib.gis import admin as gisadmin

from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

import jobs.views
#import store.views
#import zooarch.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', jobs.views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('store/', include('store.urls')),
    path('excavation/', include('excavation.urls')),
    path('spatial/', include('spatial.urls')),
    path('spatial3d/', include('spatial3d.urls')),
    path('zooarch/', include('zooarch.urls')),
    #path('samples/', include('samples.urls')),

    #specialist


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "GYGAIA Admin"
admin.site.site_title = "Gygaia Admin Portal"
admin.site.index_title = "Welcome to GYGAIA Excavation Database"
