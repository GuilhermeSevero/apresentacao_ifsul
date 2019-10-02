from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import UsuarioSerializer, Usuario


class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['nome', 'cpf', 'data_nascimento']
    ordering_fields = ['id', 'nome', 'cpf', 'data_nascimento', 'created_at', 'updated_at']
    ordering = ['nome', 'id']
