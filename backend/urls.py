from django.contrib import admin
from django.urls import path
from agendamentos.views import (
    home,
    clientes,
    criar_cliente,
    listar_agendamentos,
    criar_agendamento
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # rota principal
    path('', home),

    # clientes
    path('clientes', clientes),
    path('clientes/criar', criar_cliente),

    # agendamentos
    path('agendamentos', listar_agendamentos),
    path('agendamentos/criar', criar_agendamento),
]