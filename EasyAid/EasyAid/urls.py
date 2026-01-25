from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.views.generic import TemplateView

def tezt(request):
    return HttpResponse("Django is working!")

urlpatterns = [
    path('', tezt),
    path('admin/', admin.site.urls),
   # path('', TemplateView.as_view(template_name='index.html'), name='home'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)