from django.urls import path
from empresa.apps import EmpresaConfig
from . import views
from .views import *

urlpatterns = [
    path('ativar/', views.empresa_criar, name='empresa_criar'),
    path('empresas/', views.empresas, name='empresa_lista'),
    path('painel/<int:pk>', views.empresa_painel, name='empresa_painel'),

    path('cliente-criar/', views.cliente_criar, name='cliente_criar'),
    path('cliente-criar-extendido/', views.cliente_criar_ex, name='cliente_criar_ex'),
    path('novo-cliente/', views.novo_cliente, name='novo_cliente'),
    path('cliente-remover/<int:pk>', ClienteRemover.as_view(), name='cliente_remover'),
    path('clientes/', views.clientes, name='cliente_lista'),

]
