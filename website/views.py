from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from cos.models import Ordem

def home(request):
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
		return render(request, 'website/home.html')

def services(request):
	return render(request, 'website/services.html')

def mapa(request):
	return render(request, 'website/mapa.html')