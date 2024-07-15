# webj/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),  # Обновите путь для главного приложения
    path('main_1/', include('main_1.urls')),
    path('', include('main.urls')),  # Обновите путь для главной страницы
]
