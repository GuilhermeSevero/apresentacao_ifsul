from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Usuario
from .serializers import UsuarioSerilizer


@api_view(['GET', 'POST'])
def usuario_list(request):
    if request.method == 'GET':
        usuario = Usuario.object.all()
        serializer = UsuarioSerilizer(usuario, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UsuarioSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detail(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerilizer(usuario)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = UsuarioSerilizer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
