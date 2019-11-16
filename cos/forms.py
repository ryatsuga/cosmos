from django import forms
from django.contrib.auth.models import User
from localflavor.br.forms import *
from .models import *

class OrdemCriarForm(forms.ModelForm):

	class Meta:
		model = Ordem
		fields = ['valor', 'modelo']

class MarcaCriarForm(forms.ModelForm):

	class Meta:
		model = Marca
		fields = ['nome']