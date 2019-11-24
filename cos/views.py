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


def ordens(request):
	ordens = request.user.controle.ordens_todas
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
	#elif request.POST['action'] == 'consultaPorId':
	else:
		cid = request.POST.get('clienteID', None)
		if cid == '':
			cid='00000000000'

		cliente = Cliente.objects.get(identificacao=cid)
		empresa = Empresa.objects.get(dono=request.user)

		request.session['cliente'] = cliente.id
		request.session['empresa'] = empresa.id

		return redirect('ordem_criar')

def ordem_criar(request):
	cliente = Cliente.objects.get(pk=request.session['cliente'])
	empresa = Empresa.objects.get(pk=request.session['empresa'])
	if request.method =='POST':
		form=OrdemCriarForm(request.POST)
		if form.is_valid():
			form.instance.autor = request.user
			form.instance.empresa = empresa
			form.instance.cliente = cliente
			form.save()
			messages.success(request, f'Ordem de Serviço cadastrada com sucesso!')
			return redirect('ordem_lista')
	else:
		form=OrdemCriarForm()

	cxt= {}
	cxt['form']= form
	cxt['cliente']= cliente
	cxt['empresa']= empresa
	return render(request, 'cos/ordem_criar.html', cxt)
