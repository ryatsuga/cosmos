from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import (
	ListView, 
	DetailView, 
	UpdateView, 
	CreateView,
	DeleteView,
	TemplateView
	)
from .forms import *
from .models import *

def empresa_dashboard(request):
	result = 0
	try:
		if request.user.empresa is None:
			result = 0
		else:
			result = 1
	except:
		msg = 'Não funciona!'
	finally:
		if result == 0:
			return render(request, 'empresa/empresa_inativa.html')
		else:
			return redirect('home')
	return 0

def empresa_criar(request):
	if request.method =='POST':
		form=EmpresaCriarForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.dono = request.user
			form.instance.ativo = True
			form.save()
			messages.success(request, f'Empreendimento cadastrado com sucesso!')
			return redirect('home')
	else:
		form=EmpresaCriarForm()

	return render(request, 'empresa/empresa_ativar.html', {'form': form})


def negocio_atualizar(request):
	return 0

def negocio_desativar(request):
	return 0

def colaboradores(request):
	return 0

def clientes(request):
	return 0





