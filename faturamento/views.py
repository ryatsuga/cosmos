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
from .models import *

def faturamento_dashbord(request):
	return 0

def faturamento_ordens(request):
	return 0

def faturamento_cliente(request):
	return 0

def faturamento_mes(request):
	return 0