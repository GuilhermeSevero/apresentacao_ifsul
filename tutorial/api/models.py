import datetime
import math
from django.db import models


# Create your models here.


class Usuario(models.Model):
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuários'
        verbose_name_plural = 'usuarios'
        ordering = ('id',)

    nome = models.CharField(db_column='nome', max_length=255, null=False, blank=False)
    cpf = models.CharField(db_column='cpf', max_length=11, null=True, blank=True, default=None)
    data_nascimento = models.DateField(db_column='data_nascimento', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=True)

    @property
    def idade(self):
        if self.data_nascimento:
            delta = datetime.date.today() - self.data_nascimento
            return math.trunc(delta.days / 365)
        return None


class Partida(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='partidas')
    vencedor = models.BooleanField(blank=True, null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=False)
