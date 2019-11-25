from django import forms
from django.contrib.auth.models import User
from localflavor.br.forms import *
from .models import *

class OrdemCriarForm(forms.ModelForm):

	class Meta:
		model = Ordem
		fields = ['valor', 'previsao', 'marca', 'modelo', 'identificacao', 'defeito', 'q_molhou', 'q_liga', 'observacao', 'status']

class OrdemAtualizarForm(forms.ModelForm):

	class Meta:
		model = Ordem
		fields = ['valor', 'previsao', 'marca', 'modelo', 'identificacao', 'defeito', 'q_molhou', 'q_liga', 'observacao', 'status']

class OrdemStatusAtualizarForm(forms.ModelForm):

	class Meta:
		model = Ordem
		fields = ['status']

class MarcaCriarForm(forms.ModelForm):

	class Meta:
		model = Marca
		fields = ['nome']