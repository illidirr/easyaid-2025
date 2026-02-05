from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from main import views
from django.conf import settings
# ДОБАВЬТЕ ЭТУ СТРОКУ

# Создайте функции прямо здесь
def index(request):
    """Главная страница"""
    return render(request, 'main/index.html')
def health_check(request):
    return HttpResponse("OK", status=200)

urlpatterns = [
    path('', views.index, name='index'),
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('', index, name='index'),
    path('health/', health_check, name='health_check'),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)