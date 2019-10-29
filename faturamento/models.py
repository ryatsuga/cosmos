from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.models import PermissionsMixin

class Despesa(models.Model):
	descricao = 
	valor = 
	#Metadata
	data =
	negocio = 

class Ganho(models.Model):
	descricao = 
	valor = 
	#Metadata
	data =
	negocio = 


