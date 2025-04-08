# app_cad_edificios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edificios/', views.edificios, name='listagem_edificios'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
    path('sadm/', views.sadm, name='sadm'),
    path('edificios/', views.listar_edificios, name='listar_edificios'), # Exemplo da sua listagem
    path('edificios/apagar/<int:id_edificio>/', views.apagar_edificio, name='apagar_edificio'),
    path('logout/', views.fazer_logout, name='logout')
    
    
]