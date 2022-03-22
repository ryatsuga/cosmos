from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
from users.models import Controle
from cos.models import Ordem


@login_required
def empresa_criar(request):
	if request.method =='POST':
		form=EmpresaCriarForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.dono = request.user
			form.instance.ativo = True
			form.save()
			messages.success(request, f'Empreendimento cadastrado com sucesso!')
			return redirect('empresa_lista')
	else:
		form=EmpresaCriarForm()

	return render(request, 'empresa/empresa_ativar.html', {'form': form})


def empresa_atualizar(request):
	return 0

@login_required
def empresa_painel(request, pk):
	#Seleciona empresa para tarefas
	empresa = Empresa.objects.get(pk=pk)
	Controle.objects.filter(user=request.user).update(empresa_selecionada=empresa)
	#Seleciona OSs da empresa
	ordens = Ordem.objects.filter(empresa=empresa).order_by('-data')[:3]
	colaboradores = Colaborador.objects.filter(empresa=empresa)

	cxt={'ordens':ordens, 'colaboradores':colaboradores}

	return render(request, 'empresa/empresa_painel.html', cxt)

def empresa_desativar(request):
	return 0

@login_required
def empresas(request):
	empresas_usuario = Empresa.objects.filter(dono=request.user)

	return render(request, 'empresa/empresa_lista.html', {'empresas_usuario': empresas_usuario})

def colaboradores(request):
	return 0

@login_required
def clientes(request):
	clientes = Cliente.objects.filter(vinculo=request.user.controle.empresa_selecionada)
	empresa = request.user.controle.empresa_selecionada
	numero_clientes = len(clientes)
	return render(request, 'empresa/cliente_lista.html', {'empresa': empresa, 'clientes': clientes, 'numero_clientes':numero_clientes})

@login_required
def cliente_criar_ex(request):
	if request.method =='POST':
		form=ClienteForm(request.POST)
		if form.is_valid():
			form.instance.vinculo = request.user.empresa
			form.instance.identificacao = request.session['cid']
			form.instance.ativo = True
			form.save()
			messages.success(request, f'Cliente cadastrado com sucesso!')

			cliente = Cliente.objects.get(identificacao=request.session['cid'])
			empresa = Empresa.objects.get(pk=request.user.controle.empresa_selecionada.pk)

			request.session['cliente'] = cliente.id
			request.session['empresa'] = empresa.id

			return redirect('ordem_criar')
	else:
		form=ClienteForm()
		cid = request.session['cid']
		if len(cid) < 12:
			cid = '{}.{}.{}-{}'.format(cid[:3], cid[3:6], cid[6:9], cid[9:])
		else:
			cid = '{}.{}.{}/{}-{}'.format(cid[:2], cid[2:5], cid[5:8], cid[8:12], cid [12:])

	return render(request, 'empresa/cliente_criar.html', {'form': form, 'cid': cid})

@login_required
def cliente_criar_ex(request):
	if request.method =='POST':
		form=ClienteForm(request.POST)
		if form.is_valid():
			form.instance.vinculo = request.user.empresa
			form.instance.identificacao = request.session['cid']
			form.instance.ativo = True
			form.save()
			messages.success(request, f'Cliente cadastrado com sucesso!')

			cliente = Cliente.objects.get(identificacao=request.session['cid'])
			empresa = Empresa.objects.get(pk=request.user.controle.empresa_selecionada.pk)

			request.session['cliente'] = cliente.id
			request.session['empresa'] = empresa.id

			return redirect('ordem_criar')
	else:
		form=ClienteForm()
		cid = request.session['cid']
		if len(cid) < 12:
			cid = '{}.{}.{}-{}'.format(cid[:3], cid[3:6], cid[6:9], cid[9:])
		else:
			cid = '{}.{}.{}/{}-{}'.format(cid[:2], cid[2:5], cid[5:8], cid[8:12], cid [12:])

	return render(request, 'empresa/cliente_criar_ex.html', {'form': form, 'cid': cid})

@login_required
def cliente_criar(request):
	if request.method =='POST':
		form=ClienteForm(request.POST)
		if form.is_valid():
			form.instance.vinculo = request.user.empresa
			form.instance.identificacao = request.session['new_cid']
			form.instance.ativo = True
			form.save()
			messages.success(request, f'Cliente cadastrado com sucesso!')

			cliente = Cliente.objects.get(identificacao=request.session['new_cid'])
			empresa = Empresa.objects.get(pk=request.user.controle.empresa_selecionada.pk)

			request.session['cliente'] = cliente.id
			request.session['empresa'] = empresa.id

			return redirect('cliente_lista')
	else:
		form=ClienteForm()
		new_cid = request.session['new_cid']
		if len(new_cid) < 12:
			new_cid = '{}.{}.{}-{}'.format(new_cid[:3], new_cid[3:6], new_cid[6:9], new_cid[9:])
		else:
			new_cid = '{}.{}.{}/{}-{}'.format(new_cid[:2], new_cid[2:5], new_cid[5:8], new_cid[8:12], new_cid [12:])

	return render(request, 'empresa/cliente_criar.html', {'form': form, 'new_cid': new_cid})


class ClienteRemover(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Cliente
	login_required = True
	template_name = 'empresa/cliente_remover.html'

	def test_func(self):
		if self.request.user == self.request.user.empresa.dono:
			return True
		if Colaborador.objects.get(user=self.request.user):
			return True
		return False

	def get_success_url(self):
		return reverse('cliente_lista')

@login_required
def novo_cliente(request):
	if request.method == 'GET':
		clientes = Cliente.objects.all()
		return render(request, 'empresa/novo_cliente.html', {'clientes': clientes})
	#elif request.POST['action'] == 'consultaPorId':
	else:
		new_cid = request.POST.get('clienteID', None)
		valida_id = len(new_cid)
		if valida_id == 11 or valida_id == 14:
			if Cliente.objects.filter(identificacao=new_cid, vinculo=request.user.controle.empresa_selecionada):

				cliente = Cliente.objects.get(identificacao=new_cid)
				empresa = Empresa.objects.get(pk=request.user.controle.empresa_selecionada.pk)

				request.session['cliente'] = cliente.id
				request.session['empresa'] = empresa.id

				return redirect('ordem_criar')

			else:
				request.session['new_cid'] = new_cid
				return redirect('cliente_criar')
		else:
			messages.success(request, f'CPF/CNPJ Inválido')
			return redirect('novo_cliente')