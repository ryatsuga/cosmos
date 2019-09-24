from django.urls import path
from website.apps import WebsiteConfig
from . import views

urlpatterns = [
    path('', views.home, name='home'),

]
