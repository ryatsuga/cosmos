from django.urls import path
from empresa.apps import EmpresaConfig
from . import views

urlpatterns = [
    path('dashboard/', views.empresa_dashboard, name='empresa_dashboard'),
    path('ativar/', views.empresa_criar, name='empresa_criar'),

]
