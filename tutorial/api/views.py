from rest_framework import viewsets

from .serializers import UsuarioSerializer, Usuario


class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
