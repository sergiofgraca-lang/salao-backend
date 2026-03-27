from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cliente, Agendamento


# ✅ ROTA PRINCIPAL
def home(request):
    return JsonResponse({"status": "API rodando"})


# =========================
# 👤 CLIENTES
# =========================

@api_view(['GET'])
def clientes(request):
    lista = Cliente.objects.all()
    data = [
        {
            "id": c.id,
            "nome": c.nome,
            "telefone": c.telefone
        }
        for c in lista
    ]
    return Response(data)


@csrf_exempt
@api_view(['POST'])
def criar_cliente(request):
    cliente = Cliente.objects.create(
        nome=request.data.get('nome'),
        telefone=request.data.get('telefone')
    )

    return Response({
        "id": cliente.id,
        "nome": cliente.nome,
        "telefone": cliente.telefone
    })


# =========================
# 📅 AGENDAMENTOS
# =========================

@api_view(['GET'])
def listar_agendamentos(request):
    ags = Agendamento.objects.all()
    data = [
        {
            "id": a.id,
            "nome": a.nome,
            "telefone": a.telefone,
            "data": str(a.data),
            "horario": a.horario
        }
        for a in ags
    ]
    return Response(data)


@csrf_exempt
@api_view(['POST'])
def criar_agendamento(request):
    ag = Agendamento.objects.create(
        nome=request.data.get("nome"),
        telefone=request.data.get("telefone"),
        data=request.data.get("data"),
        horario=request.data.get("horario"),
    )

    return Response({
        "id": ag.id,
        "nome": ag.nome
    })