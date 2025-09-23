from django.db import models
from django.contrib.auth.models import User 
from usuario.models import Usuario

# Create your models here.
class Conta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="contas")
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, related_name="contas")
    servico = models.ForeignKey('Servico', on_delete=models.SET_NULL, null=True, blank=True, related_name="contas")
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True, related_name="contas")
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    tipo = models.CharField(max_length=50)
    data_vencimento = models.DateTimeField()
    data_pagamento = models.DateTimeField(null=True, blank=True)
    resultado = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.descricao} - {self.usuario.user.username}"

class Empresa(models.Model):
    nome = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    servico = models.CharField(max_length=50)
    endereco = models.TextField()
    numero_celular = models.DecimalField(max_digits=9, decimal_places=0)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    slug = models.SlugField(unique=True)
    tipo_servico = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_servico

class Categoria(models.Model):
    slug = models.SlugField(unique=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome