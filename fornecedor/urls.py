from django.urls import path
from empresa.apps import EmpresaConfig
from . import views

urlpatterns = [
    path('dashboard/', views.fornecedor_dashboard, name='fornecedor_dashboard'),
    path('ativar/', views.fornecedor_criar, name='fornecedor_criar'),
    path('fornecedores/', views.fornecedores, name='fornecedor_lista'),
    path('painel/<int:pk>', views.fornecedor_painel, name='fornecedor_painel'),
    path('inativo/', views.fornecedor_inativo, name='fornecedor_inativo'),
    
]
