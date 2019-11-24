from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.models import PermissionsMixin
from PIL import Image
from empresa.models import Empresa
import random

UF_CHOICES = (
		('AC', 'Acre'), 
		('AL', 'Alagoas'),
		('AP', 'Amapá'),
		('BA', 'Bahia'),
		('CE', 'Ceará'),
		('DF', 'Distrito Federal'),
		('ES', 'Espírito Santo'),
		('GO', 'Goiás'),
		('MA', 'Maranão'),
		('MG', 'Minas Gerais'),
		('MS', 'Mato Grosso do Sul'),
		('MT', 'Mato Grosso'),
		('PA', 'Pará'),
		('PB', 'Paraíba'),
		('PE', 'Pernanbuco'),
		('PI', 'Piauí'),
		('PR', 'Paraná'),
		('RJ', 'Rio de Janeiro'),
		('RN', 'Rio Grande do Norte'),
		('RO', 'Rondônia'),
		('RR', 'Roraima'),
		('RS', 'Rio Grande do Sul'),
		('SC', 'Santa Catarina'),
		('SE', 'Sergipe'),
		('SP', 'São Paulo'),
		('TO', 'Tocantins'),
	)


class Fornecedor(models.Model):
	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa', null=True, blank=True)
	dono = models.CharField(_('Dono'), max_length=40, null=False, blank=False)
	logo = models.ImageField(_('Logo'), default='default.jpg', upload_to='negocio_pics')
	nome_fantasia = models.CharField(_('Nome fantasia'), max_length=40, null=False, blank=False)
	identificacao = models.CharField(_('CPF/CNPJ'), max_length=18, null=False, blank=False)
	telefone = models.CharField(_('Telefone'), max_length=20, null=False, blank=True)
	celular = models.CharField(_('Celular'), max_length=20, null=False, blank=False)
	email = models.CharField(_('E-mail'), max_length=60, null=True, blank=True)
	cep = models.CharField(_('CEP'),max_length=8, null=False, blank=False)
	endereco = models.CharField(_('Endereço'), max_length=200, null=False, blank=False)
	numero = models.IntegerField(_('Número'), null=False, blank=False)
	complemento = models.CharField(_('Complemento'),max_length=20, null=True, blank=True)
	bairro = models.CharField(_('Bairro'),max_length=100, null=False, blank=False)
	cidade = models.CharField(_('Cidade'),max_length=100, null=False, blank=False)
	uf = models.CharField(_('Estado'),max_length=2, null=False, blank=False, choices=UF_CHOICES, default='MG')
	#Metadata
	data = models.DateField(default=timezone.now)
	completo = models.BooleanField(_('Completo'), default=False)

	def __str__(self):
		return f'{self.nome_fantasia} - {self.identificacao}'

	def endereco_completo(self):
		return f'{self.endereco}, {self.numero}, {self.bairro} - {self.cidade}/{self.uf}'

