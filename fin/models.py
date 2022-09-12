from django.db import models
from datetime import datetime
# Create your models here.


class Promocao(models.Model):
    promo_codigo=models.BigIntegerField()
    promo_chave = models.CharField(max_length=255)
    promo_tipo = models.CharField(max_length=255)
    promo_valor = models.DecimalField( max_digits=10, decimal_places=2)
    promo_dhinicio = models.DateTimeField(default= datetime.now())
    promo_dhfim = models.DateTimeField(default= datetime.now())
    promo_situacao = models.CharField(max_length=255)