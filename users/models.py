from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.models import PermissionsMixin
from PIL import Image
import qrcode
import random

def get_card_num():
		alfa = ['a', 'b', 'c', 'd', 'x', 'y','z']
		num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
		existe_no_banco = True
		while existe_no_banco == True:
			card_num_gerador = random.choice(alfa)+random.choice(num)+random.choice(alfa)+random.choice(num)+random.choice(num)
			card_num_verifica_igual = Card.objects.filter(card_number=card_num_gerador)
			if card_num_verifica_igual.count() > 0:
				return False
			else:
				return card_num_gerador

class Profile(models.Model):
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
	ESTADO_CIVIL_CHOICES = (
		('S', 'Solteiro'),
		('C', 'Casado'),
		('D', 'Divorciado'),
		('V', 'Viúvo'),
	)
	TIPO_PERFIL_CHOICES = (
		('0', 'Operador'),
		('1', 'Técnico'),
		('2', 'Cliente'),
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
	image = models.ImageField(_('Imagem Perfil'), default='default.jpg', upload_to='profile_pics')
	sexo = models.CharField(_('Sexo'),max_length=1, choices=SEXO_CHOICES)
	estado_civil = models.CharField(_('Estado Civil'),max_length=1, choices=ESTADO_CIVIL_CHOICES)
	cpf = models.CharField(_('CPF'), max_length=11, null=False, blank=False)
	data_nascimento = models.DateField(default=timezone.now)
	contato1= models.CharField(_('Telefone'), max_length=20, null=False, blank=True)
	contato2= models.CharField(_('Celular'), max_length=20, null=False, blank=False)
	endereco = models.CharField(_('Endereço'), max_length=200, null=False, blank=False)
	complemento = models.CharField(_('Complemento'),max_length=30, null=False, blank=False)
	bairro = models.CharField(_('Bairro'),max_length=100, null=False, blank=False)
	cidade = models.CharField(_('Cidade'),max_length=100, null=False, blank=False)
	uf = models.CharField(_('Estado'),max_length=2, null=False, blank=False, choices=UF_CHOICES, default='MG')
	cep = models.CharField(_('CEP'),max_length=8, null=False, blank=False)
	tipo_perfil = models.CharField(_('Tipo de Perfil'),max_length=1, null=False, blank=False, choices=TIPO_PERFIL_CHOICES, default='2')

	def __str__(self):
		return f'{self.user.username} Profile'

	def get_full_name(self):

		full_name = '%s %s' % (self.user.first_name, self.user.last_name)
		return full_name.strip()

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)


class Card(models.Model):
	STATUS_CHOICES = (
		(0, 'Inativo'),
		(1, 'Ativo'),
		(2, 'Bloqueado'),
		(3, 'Cancelado'),
	)
	user_ref = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Cliente')
	status = models.IntegerField(_('Status'), null=False, blank=False, default=0, choices=STATUS_CHOICES)
	card_number = models.CharField(_('Número do Cartão'), max_length=6, null=True, blank=True, default=get_card_num)

	def get_qrcode(self):
		img = qrcode.make(self.card_number)
		return img

	def __str__(self):
		return f'{self.user_ref.username} Card'
