from django.db import models
from datetime import datetime

# Create your models here.

class Modelo(models.Model):
    model_codigo= models.BigIntegerField()
    model_nome = models.CharField(max_length=255)
    model_texto = models.TextField()
    model_tipo = models.CharField(max_length=1)
    model_data_atualizacao = models.DateTimeField(default= datetime.now()) 