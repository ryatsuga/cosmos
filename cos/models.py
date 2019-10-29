from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import random
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.urls import reverse
from localflavor.br.models import *
from empresa.models import *

def gerar_os_cod():
	alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'X']
	num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

	existe_no_banco = True
	while existe_no_banco == True:
		os_gerador = random.choice(alfa)+random.choice(num)+random.choice(alfa)+random.choice(alfa)+random.choice(num)+random.choice(num)
		os_verifica_igual = Ordem.objects.filter(os_cod=os_gerador)
		if len(os_verifica_igual) <= 0:
			return os_gerador

STATUS_CHOICES = (
		(0, 'Orçamento'),
		(1, 'Liberado para manutenção'),
		(2, 'Em manutenção'),
		(3, 'Aguardando pagamento'),
		(4, 'Finalizado'),
		(9, 'Cancelado'),
	)

class Marca(models.Model):
	nome=models.TextField(_('Nome'), max_length=50)
	#Metadata
	empresa = models.ForeignKey(Empresa, verbose_name='Empresa', on_delete=models.SET_NULL, null=True)

class Ordem(models.Model):
	#Dados básicos OS
	codigo = models.CharField(_('Código'), max_length=14, primary_key=True, null=False, blank=False, default=gerar_os_cod)
	cliente = models.ForeignKey(Cliente, verbose_name='Cliente', on_delete=models.SET_NULL, null=True)
	valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	#Dados situação
	status = models.CharField(_('Status'), max_length=1, null=False, blank=False, default=0, choices=STATUS_CHOICES,)
	previsao = models.DateTimeField(_('Previsão Entrega'),default=timezone.now)
	#Dados dispositivo
	marca = models.ForeignKey(Marca, verbose_name='Marca', on_delete=models.SET_NULL, null=True)
	modelo = modelo=models.CharField(_('Modelo'), max_length=40, null=False, blank=False)
	identificacao=models.CharField(_('Identificação'), max_length=40, null=True, blank=True)
	#Questionário
	q_molhou =models.BooleanField(_('O dispositivo molhou?'), max_length=1, null=True, blank=True, default=0)
	q_liga = models.BooleanField(_('O dispositivo liga?'), max_length=1, null=True, blank=True, default=0)
	#Metadata
	empresa = models.ForeignKey(Empresa, verbose_name='Empresa', on_delete=models.SET_NULL, null=True)
	autor = models.ForeignKey(Colaborador, verbose_name='Colaborador', on_delete=models.SET_NULL, null=True)
	data = models.DateField(_('Data'),default=timezone.now)

