from django.urls import path
from . import views

urlpatterns = [
    # Основные страницы
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # Группы материалов
    path('group1/', views.group1, name='group1'),
    path('group2/', views.group2, name='group2'),

    # Страницы с материалами
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
    path('page4/', views.page4, name='page4'),
    path('internet-fraud/', views.internet_fraud, name='internet_fraud'),

    # Тесты - одна функция обрабатывает и показ теста и результаты
    path('test/', views.test, name='test'),
    path('test-internet/', views.test_internet, name='test_internet'),
    path('test-internet-result/', views.test_internet, name='test_internet-result'),
    path('test-resuit/', views.test, name='test-resuit'),
]