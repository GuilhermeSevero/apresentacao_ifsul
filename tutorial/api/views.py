from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .serializers import UsuarioSerializer, PartidaSerializer
from .models import Usuario, Partida


class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['nome', 'cpf', 'data_nascimento']
    ordering_fields = ['id', 'nome', 'cpf', 'data_nascimento', 'created_at', 'updated_at']
    ordering = ['nome', 'id']

    @action(methods=['GET'], detail=True)
    def historico(self, request, pk, *args, **kwargs):
        serializer = self.get_serializer()
        return Response(data=serializer.get_historico(pk=pk), status=status.HTTP_200_OK)


class PartidaView(viewsets.ModelViewSet):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = ['-created_at']

    @action(methods=['GET'], detail=False)
    def ranking(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response(data=serializer.get_ranking(), status=status.HTTP_200_OK)
