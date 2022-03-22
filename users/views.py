from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic import (
	ListView, 
	DetailView, 
	UpdateView, 
	CreateView,
	DeleteView,
	TemplateView
	)


def register(request):
	if request.method =='POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request, f'{username}, sua conta foi criada com sucesso! Você já pode acessar o sistema!')
			return redirect('login')
	else:
		form=UserRegisterForm()

	return render(request, 'users/register.html', {'form': form})

@login_required
def perfil(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = PerfilUpdateForm(request.POST, request.FILES, instance=request.user.perfil)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Sua conta foi atualizada!')
			return redirect('home')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = PerfilUpdateForm(instance=request.user.perfil)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}

	return render(request, 'users/perfil.html', context)






