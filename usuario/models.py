from django.db import models
from django.contrib.auth.models import User 

class Usuario(models.Model):
    plano = models.ForeignKey('Plano', on_delete=models.SET_NULL, null=True, related_name="usuarios")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    picture = models.ImageField(upload_to="usuarios/", null=True, blank=True)
    is_activate = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class Plano(models.Model):
    nome = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    prazo = models.DateTimeField()
    data_assinatura = models.DateTimeField()

    def __str__(self):
        return self.nome