from django.conf import settings
from django.conf.urls import url, include, static
from django.contrib import admin

urlpatterns = [
	url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    # meus apps
    url(r'^', include('src.urls')),
]
urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
