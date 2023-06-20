from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

# api urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('freelance.urls')),
]
 
# media urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


# frontend urls
urlpatterns += [
    path('', include('templates.urls'))
    
]