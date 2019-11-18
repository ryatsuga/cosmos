from django.urls import path
from empresa.apps import EmpresaConfig
from . import views

urlpatterns = [
    path('dashboard/', views.empresa_dashboard, name='empresa_dashboard'),
    path('ativar/', views.empresa_criar, name='empresa_criar'),
    path('empresas/', views.empresas, name='empresa_lista'),
    path('painel/<int:pk>', views.empresa_painel, name='empresa_painel'),
    path('inativa/', views.empresa_inativa, name='empresa_inativa'),

    path('cliente-criar/', views.cliente_criar, name='cliente_criar'),

]
