from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from . import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
