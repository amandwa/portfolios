from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin do Django
    path('', include('core.urls')),  # Conectar com as URLs do app core
]
