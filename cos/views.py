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
from empresa.models import *

def ordem_criada(request):
	return render(request, 'cos/ordem_criada.html')

def ordens(request):
	ordens = Ordem.objects.filter(autor=request.user)
	return render(request, 'cos/ordem_lista.html', {'ordens': ordens})

def marca_criar(request):
	if request.method =='POST':
		form=MarcaCriarForm(request.POST)
		if form.is_valid():
			form.instance.empresa = request.user.empresa
			form.save()
			messages.success(request, f'Marca cadastrada com sucesso!')
			return redirect('home')
	else:
		form=MarcaCriarForm()

	return render(request, 'cos/marca_criar.html', {'form': form})

def nova_ordem(request):
	if request.method == 'GET':
		clientes = Cliente.objects.all()
		return render(request, 'cos/nova_ordem.html', {'clientes': clientes})
	else:
		cid = request.POST.get('clienteID', None)
		if cid == '':
			cid='00000000000'		

		cliente = Cliente.objects.get(identificacao=cid)
		empresa = Empresa.objects.get(dono=request.user)
		marcas = Marca.objects.filter(empresa=request.user.empresa)
		data_context = {'cliente': cliente, 'empresa': empresa, 'marcas': marcas}
		return ordem_criar(request, dcxt=data_context)

def ordem_criar(request, dcxt = None):
	if request.method =='POST':
		form=OrdemCriarForm()
		if form.is_valid():
			form.instance.autor = request.user
			form.instance.empresa = empresa
			form.instance.cliente = cliente
			form.save()
			messages.success(request, f'Ordem de Serviço cadastrada com sucesso!')
			return redirect('nova_ordem')
	else:
		form=OrdemCriarForm()

	dcxt['form']= form
	return render(request, 'cos/ordem_criar.html', dcxt)
