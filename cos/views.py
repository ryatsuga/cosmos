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

def ordens(request):
	ordens = Ordem.objects.filter(autor=request.user)
	return render(request, 'cos/ordem_lista.html', {'ordens': ordens})

def marca_criar(request):
	if request.method =='POST':
		form=MarcaCriarForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Marca cadastrada com sucesso!')
			return redirect('home')
	else:
		form=MarcaCriarForm()

	return render(request, 'cos/ordem_criar.html', {'form': form})

def ordem_criar(request):
	if request.method =='POST':
		form=OrdemCriarForm(request.POST)
		if form.is_valid():
			form.instance.autor = request.user
			form.save()
			messages.success(request, f'Ordem de Serviço cadastrada com sucesso!')
			return redirect('ordem_lista')
	else:
		form=OrdemCriarForm()

	return render(request, 'cos/ordem_criar.html', {'form': form})
