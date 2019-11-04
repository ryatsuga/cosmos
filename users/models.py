from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.models import PermissionsMixin
from PIL import Image
import random


class Perfil(models.Model):
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
	SEXO_CHOICES = (
		('M', 'Masculino'),
		('F', 'Feminino'),
		('O', 'Outro'),
	)

	user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
	image = models.ImageField(_('Imagem Perfil'), default='default.jpg', upload_to='profile_pics')
	sexo = models.CharField(_('Sexo'),max_length=1, choices=SEXO_CHOICES)
	cpf = models.CharField(_('CPF'), max_length=11, null=True, blank=False)
	data_nascimento = models.DateField(default=timezone.now)
	telefone = models.CharField(_('Telefone'), max_length=20, null=True, blank=True)
	celular = models.CharField(_('Celular'), max_length=20, null=True, blank=False)
	cep = models.CharField(_('CEP'),max_length=8, null=True, blank=False)
	endereco = models.CharField(_('Endereço'), max_length=200, null=True, blank=False)
	numero = models.IntegerField(_('Número'), null=True, blank=False)
	complemento = models.CharField(_('Complemento'),max_length=30, null=True, blank=False)
	bairro = models.CharField(_('Bairro'),max_length=100, null=True, blank=False)
	cidade = models.CharField(_('Cidade'),max_length=100, null=True, blank=False)
	uf = models.CharField(_('Estado'),max_length=2, null=True, blank=False, choices=UF_CHOICES, default='MG')
	#Metadata
	completo = models.BooleanField(_('Completo'), default=False)

	def __str__(self):
		return f'{self.user.username} Perfil'

	def nome_completo(self):

		full_name = '%s %s' % (self.user.first_name, self.user.last_name)
		return full_name.strip()

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

