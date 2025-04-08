# cad_edificios/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('', include('app_cad_edificios.urls')),  # Inclua as URLs do seu app
    
]