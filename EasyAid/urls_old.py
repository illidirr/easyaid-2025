from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from main import views

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
    # ЗАКОММЕНТИРУЙТЕ эту строку временно:
    # path('', include('main.urls')),
]
