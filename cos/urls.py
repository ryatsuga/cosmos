from django.urls import path
from cos.apps import CosConfig
from . import views
from .views import *

urlpatterns = [
    path('ordens/', views.ordens, name='ordem_lista'),
    path('nova-os/', views.nova_ordem, name='nova_ordem'),
    path('ordem-criar/', views.ordem_criar, name='ordem_criar'),
    path('ordem-consulta/', views.ordem_consultar, name='ordem_consultar'),
    path('ordem-info/<str:pk>', views.ordem_info, name='ordem_info'),
    path('ordem-remover/<str:pk>', OrdemRemover.as_view(), name='ordem_remover'),
    path('ordem-atualizar/<str:pk>', OrdemAtualizar.as_view(), name='ordem_atualizar'),
    path('ordem-imprimir/<str:pk>', OrdemImprimir.as_view(), name='ordem_imprimir'),
    path('ordem-atualizar-status/<str:pk>', OrdemStatusAtualizar.as_view(), name='ordem_status_atualizar'),

    path('marca-criar/', views.marca_criar, name='marca_criar'),


]
