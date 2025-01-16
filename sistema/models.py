from django.db import models


class Tecnico(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)

class Veiculo(models.Model):
    placa = models.CharField(max_length=8)
    marca = models.CharField(max_length=8)
    modelo = models.CharField(max_length=8)
    cor = models.CharField(max_length=8)

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)

class Servico(models.Model):
    peca = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    defeito = models.CharField(max_length=100)
    descricao_problema = models.TextField()
    tecnico = models.ForeignKey(Tecnico, on_delete=models.PROTECT)
    descricao_solucao = models.TextField()