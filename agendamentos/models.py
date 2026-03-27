from django.db import models

# 👤 Cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


# 📅 Agendamento
from django.db import models

class Agendamento(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    data = models.DateField()
    horario = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nome} - {self.data} {self.horario}"