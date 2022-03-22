from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
		valida_id = len(cid)
		if valida_id == 11 or valida_id == 14:

			if Cliente.objects.filter(identificacao=cid, vinculo=request.user.controle.empresa_selecionada):

				cliente = Cliente.objects.get(identificacao=cid)
				empresa = Empresa.objects.get(pk=request.user.controle.empresa_selecionada.pk)

				request.session['cliente'] = cliente.id
				request.session['empresa'] = empresa.id

				return redirect('ordem_criar')

			else:
				request.session['cid'] = cid
				return redirect('cliente_criar_ex')
		else:
			messages.success(request, f'CPF/CNPJ Inválido')
			return redirect('nova_ordem')


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

class OrdemRemover(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Ordem
	login_required = True
	template_name = 'cos/ordem_remover.html'

	def test_func(self):
		if self.request.user == self.request.user.empresa.dono:
			return True
		if Colaborador.objects.get(user=self.request.user):
			return True
		return False

	def get_success_url(self):
		return reverse('ordem_lista')

class OrdemAtualizar(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Ordem
	login_required = True
	form_class = OrdemAtualizarForm
	template_name = 'cos/ordem_atualizar.html'

	def test_func(self):
		if self.request.user == self.request.user.empresa.dono:
			return True
		if Colaborador.objects.get(user=self.request.user):
			return True
		return False

	def get_success_url(self):
		return reverse('ordem_lista')

class OrdemStatusAtualizar(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Ordem
	login_required = True
	form_class = OrdemStatusAtualizarForm
	template_name = 'cos/ordem_status_atualizar.html'

	def test_func(self):
		if self.request.user == self.request.user.empresa.dono:
			return True
		if Colaborador.objects.get(user=self.request.user, empresa=ordem.empresa):
			return True
		return False

	def get_success_url(self):
		return reverse('ordem_lista')

class OrdemImprimir(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = Ordem
	login_required = True
	template_name = 'cos/ordem_cliente_print.html'

	def test_func(self):
		if self.request.user == self.request.user.empresa.dono:
			return True
		if Colaborador.objects.get(user=self.request.user, empresa=ordem.empresa):
			return True
		return False

def ordem_consultar(request):
	if request.method == 'POST':
		search_cid = request.POST.get('clienteID', None)
		search_osid = request.POST.get('osID', None)
		if Ordem.objects.filter(codigo=search_osid):
			ordem = Ordem.objects.get(codigo=search_osid)
			if ordem.cliente.identificacao == search_cid:
				return redirect('ordem_info', search_osid)
		else:
			messages.success(request, f'Não há resultados para essa pesquisa!')
			return render(request, 'cos/ordem_consultar.html')
	else:
		return render(request, 'cos/ordem_consultar.html')

def ordem_info(request, pk):
	ordem = Ordem.objects.get(codigo=pk)
	cxt = {'ordem': ordem}
	return render(request, 'cos/ordem_info.html', cxt)


