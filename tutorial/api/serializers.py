from rest_framework import serializers

from .models import Usuario


class UsuarioSerilizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=255)
    cpf = serializers.CharField(required=False, allow_null=True, allow_blank=True, max_length=11)
    data_nascimento = serializers.DateField(required=False, allow_null=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    idade = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Usuario.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.data_nascimento = validated_data.get('data_nascimento', instance.data_nascimento)
        instance.save()
        return instance
