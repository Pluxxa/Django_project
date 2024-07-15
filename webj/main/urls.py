# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# main_1/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new, name='new'),
]

# project_name/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('main_1/', include('main_1.urls')),
]
