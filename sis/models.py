from django.db import models

# Create your models here.

class Aplicativo(models.Model):
    apl_codigo = models.IntegerField(primary_key=True)
    apl_nome = models.CharField(max_length=50)
    apl_versao = models.CharField(max_length=10)
    apl_link_download = models.CharField(max_length=255)
    apl_link_imagem = models.CharField(max_length=255)
    apl_disponivel_download = models.CharField(max_length=1)
    apl_projeto = models.CharField(max_length=125)
    apl_data_lancamento = models.DateField()