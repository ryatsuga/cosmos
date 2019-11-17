from django.urls import path
from cos.apps import CosConfig
from . import views

urlpatterns = [
    path('ordens/', views.ordens, name='ordem_lista'),
    path('nova-os/', views.nova_ordem, name='nova_ordem'),
    path('os-criar/', views.ordem_criar, name='ordem_criar'),
    path('marca-criar/', views.ordem_criar, name='marca_criar'),


]
