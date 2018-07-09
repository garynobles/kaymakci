from django.contrib import admin
from django.contrib.gis import admin as gisadmin

from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

import jobs.views




from depot.views import SamplesListView
#from ceramics.views import CeramicsListView
from django.conf.urls import url
#import store.views
#import zooarch.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', jobs.views.home, name='home'),
    path('blog/', include('blog.urls')),
    #path('store/', include('store.urls')),
    path('depot/', include('depot.urls')),

    path('pdal/', include('pdal.urls')),

    path('excavation/', include('excavation.urls')),
    path('spatial/', include('spatial.urls')),
    path('spatial3d/', include('spatial3d.urls')),
    path('zooarch/', include('zooarch.urls')),

    path('ceramics/', include('ceramics.urls')),

    url(r'^gallery/', include('gallery.urls')),
    #path('samples/', include('samples.urls')),
    #path('test/', include('test_pagefilter.urls')),

    #url(r'^test_pagefilter/test_filter/$', SamplesListView.as_view(template_name="currencies/currency_filter.html")),
    ##url(r'^depot/samples/$', SamplesListView.as_view(template_name="currencies/currency_filter.html")),
    #specialist


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "GYGAIA Admin"
admin.site.site_title = "Gygaia Admin Portal"
admin.site.index_title = "Welcome to GYGAIA Excavation Database"
