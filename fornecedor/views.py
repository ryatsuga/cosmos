from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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
from empresa.models import Empresa
from users.models import Controle

def fornecedor_inativo(request):
	return render(request, 'fornecedor/fornecedor_inativo.html')

def fornecedor_dashboard(request):
	result = 0
	try:
		if request.user.empresa.fornecedor is None:
			result = 0
		else:
			result = 1
	except:
		msg = 'Usuário sem fornecedor cadastrado.'
	finally:
		if result == 0:
			return render(request, 'fornecedor/fornecedor_inativo.html')
		else:
			return redirect('home')
	return 0

def fornecedor_criar(request):
	if request.method =='POST':
		form=FornecedorCriarForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.empresa = request.user.empresa
			form.instance.ativo = True
			form.save()
			messages.success(request, f'Fornecedor cadastrado com sucesso!')
			return redirect('fornecedor_lista')
	else:
		form=FornecedorCriarForm()

	return render(request, 'fornecedor/fornecedor_ativar.html', {'form': form})


def fornecedor_atualizar(request):
	return 0

def fornecedor_painel(request, pk):
	
	empresa = Empresa.objects.get(pk=pk)
	Controle.objects.filter(user=request.user).update(empresa_selecionada=empresa)
	fornecedor = Fornecedor.objects.filter(empresa=request.user.empresa)	

	return render(request, 'fornecedor/fornecedor_painel.html')

def fornecedor_desativar(request):
	return 0

def fornecedores(request):

	fornecedores = Fornecedor.objects.filter(empresa=request.user.empresa)

	return render(request, 'fornecedor/fornecedor_lista.html', {'fornecedores': fornecedores})


