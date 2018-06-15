from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import store.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', jobs.views.home, name='home'),
    #path('blog/', include('blog.urls')),
    path('store/', include('store.urls')),
    #path('samples/', include('samples.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "GYGAIA Admin"
admin.site.site_title = "Gygaia Admin Portal"
admin.site.index_title = "Welcome to GYGAIA Excavation Database"
