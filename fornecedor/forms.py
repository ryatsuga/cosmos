from django import forms
from django.contrib.auth.models import User
from localflavor.br.forms import *
from .models import *
from fornecedor.models import Fornecedor

class FornecedorCriarForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = Fornecedor
		fields = ['empresa', 'logo', 'dono', 'nome_fantasia', 
		'identificacao', 'telefone',
		'celular', 'email', 'cep',
		'endereco', 'numero',
		'complemento', 'bairro',
		'cidade', 'uf',]

