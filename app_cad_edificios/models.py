from django.db import models
from django.contrib.auth.models import User

class Edificio(models.Model):
    id_edificio = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    tipo = models.TextField(max_length=255)
    saturado = models.TextField(max_length=255)
    fac = models.TextField(max_length=255)

class Mensagem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.data_envio.strftime('%d/%m/%Y %H:%M')}"    
    
    
