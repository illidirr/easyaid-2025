from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render  # Добавьте этот импорт

# Удалите лишнюю функцию tezt или исправьте её
def index_view(request):
    return render(request, 'main/index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Главные URL из приложения main
]

# В режиме DEBUG добавляем обслуживание медиафайлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)