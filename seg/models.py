from ipaddress import ip_address
from operator import mod
from django.db import models
from datetime import datetime
from pandas import Timestamp
# Create your models here.
class Sessao(models.Model):
    id = models.CharField(max_length=128,primary_key=True)
    ip_address = models.CharField(max_length=45,unique=True)
    timestamp = models.BigIntegerField()
    data = models.TextField()
    
 
class Log(models.Model):
    cod_log = models.BigIntegerField()
    log_data = models.DateTimeField(default= datetime.now())
    log_rotina = models.CharField(max_length=255)
    log_retorno = models.TextField()   
    

class Oauth(models.Model):
    auth_codigo  = models.BigIntegerField(primary_key=True)
    auth_name = models.CharField(max_length=255)
    auth_provider = models.CharField(max_length=255)
    auth_scope = models.CharField(max_length=255)
    auth_application_id = models.CharField(max_length=255)
    auth_application_secret = models.CharField(max_length=255)
    auth_redirects_uri = models.TextField()
    auth_client_uri = models.CharField(max_length=255)
    auth_allowed_grant_types= models.TextField()
    auth_allowed_response_types = models.TextField()
    auth_token_ednpoint_auth_method = models.CharField(max_length=255)
    auth_options = models.TextField()  