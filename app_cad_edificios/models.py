from django.db import models


class Edificio(models.Model):
    id_edificio = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    tipo = models.TextField(max_length=255)
    saturado = models.TextField(max_length=255)
    fac = models.TextField(max_length=255)
    
    
