from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.user_login, name='login'),
    # path('edificios/editar/<int:id_edificio>/', views.editar_edificio, name='editar_edificio'), # Removido
    # path('edificios/', views.edificios, name='listagem_edificios'), # Removido (se não pertencer a este app)
]