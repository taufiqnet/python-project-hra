from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

handler404 = 'core.views.error_404_view'

urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Change the Admin Panel Header
admin.site.site_header = "HR & Administration"
admin.site.index_title = "Management"
