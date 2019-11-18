from django.urls import path
from website.apps import WebsiteConfig
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services-list', views.services, name='services'),
    path('mapa', views.mapa, name='mapa'),

]
