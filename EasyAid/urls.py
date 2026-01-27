from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from django.shortcuts import render


# ДОБАВЬТЕ ЭТУ СТРОКУ

# Создайте функции прямо здесь
def index(request):
    """Главная страница"""
    return render(request, 'main/index.html')
def health_check(request):
    return HttpResponse("OK", status=200)

urlpatterns = [
    path('', index, name='index'),
    path('health/', health_check, name='health_check'),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]