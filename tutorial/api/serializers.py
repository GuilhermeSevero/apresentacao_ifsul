from rest_framework import serializers
from django.db.models import Count, Max

from .models import Usuario, Partida


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'cpf', 'data_nascimento', 'idade', 'created_at', 'updated_at')

    def get_historico(self, pk):
        vitorias = Partida.objects \
            .filter(usuario__pk=pk, vencedor=True) \
            .aggregate(qtd_vitoria=Count('*'), ultima_vitoria=Max('created_at'))
        derrotas = Partida.objects \
            .filter(usuario__pk=pk, vencedor=False) \
            .aggregate(qtd_derrota=Count('*'), ultima_derrota=Max('created_at'))
        return {**vitorias, **derrotas}


class PartidaSerializer(serializers.ModelSerializer):
    id_usuario = serializers.IntegerField(source='usuario_id', write_only=True)
    usuario = UsuarioSerializer(many=False, read_only=True)

    class Meta:
        model = Partida
        fields = ('id', 'id_usuario', 'usuario', 'vencedor', 'created_at')

    def get_ranking(self):
        usuarios = Partida.objects \
            .filter(vencedor=True) \
            .values('usuario') \
            .order_by('usuario') \
            .annotate(qtd_vitorias=Count('*')) \
            .order_by('-qtd_vitorias')
        return RankingSerializer(usuarios, many=True).data


class RankingSerializer(serializers.Serializer):
    usuario = serializers.SerializerMethodField(method_name='get_usuario')
    qtd_vitorias = serializers.IntegerField(read_only=True)

    def get_usuario(self, data):
        return UsuarioSerializer(Usuario.objects.get(pk=data.get('usuario', None))).data
