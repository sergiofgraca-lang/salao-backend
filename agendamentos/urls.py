from django.urls import path
from . import views
from .views import listar_agendamentos, criar_agendamento, clientes

urlpatterns = [
    path('', views.home),
    
    path('clientes', views.clientes),
    path('clientes/criar', views.criar_cliente),
     path('clientes', clientes),
    path('agendamentos', listar_agendamentos),
    path('agendamentos/criar', views.criar_agendamento),
    
    
    
    
]