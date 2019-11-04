from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from localflavor.br.forms import *

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', \
		 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name']

class PerfilUpdateForm(forms.ModelForm):
	cpf = BRCPFField(max_length=11)
	class Meta:
		model = Perfil
		fields = ['image', 'sexo', 'data_nascimento', 'cpf', 'cep', 'endereco', 'complemento', 'bairro', \
		'cidade', 'uf',]