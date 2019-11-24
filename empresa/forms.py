from django import forms
from django.contrib.auth.models import User
from localflavor.br.forms import *
from .models import *

class EmpresaCriarForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = Empresa
		fields = ['logo', 'nome_fantasia', 
		'identificacao', 'telefone',
		'celular', 'email', 'cep',
		'endereco', 'numero',
		'complemento', 'bairro',
		'cidade', 'uf',]

class ColaboradorNivelForm(forms.ModelForm):

	class Meta:
		model = Colaborador
		fields = ['nivel']

class ClienteForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = Cliente
		fields = ['nome', 
		'telefone', 'celular',
		'email', 'cep',
		'endereco', 'numero',
		'complemento', 'bairro',
		'cidade', 'uf',]