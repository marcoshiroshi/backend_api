from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Empresa, Departamento, Pessoa
from .utils import *


class EmpresaSerializer(serializers.HyperlinkedModelSerializer):

    cnpj = serializers.CharField(min_length=14, max_length=14)
    cidade = serializers.ChoiceField(choices=CIDADES_CHOICES)
    pais = serializers.ChoiceField(choices=PAISES_CHOICES)

    class Meta:
        model = Empresa
        fields = ['url', 'id', 'cnpj', 'logradouro', 'cidade', 'pais', 'ativo']

    def create(self, validated_data):
        cnpj = validated_data.get('cnpj')
        if not cnpj_verification(self, cnpj):
            raise serializers.ValidationError("CNPJ inválido")

        if Empresa.objects.filter(cnpj=cnpj).exists():
            raise serializers.ValidationError("Empresa já cadastrada com esse CNPJ")

        return Empresa.objects.create(**validated_data)

    def update(self, instance, validated_data):

        cnpj = validated_data.get('cnpj', instance.cnpj)

        if not cnpj_verification(self, cnpj):
            raise serializers.ValidationError("CNPJ inválido")

        if Empresa.objects.filter(cnpj=cnpj).exists() and cnpj != instance.cnpj:
            raise serializers.ValidationError("Empresa já cadastrada com esse CNPJ")

        instance.cnpj = validated_data.get('cnpj', instance.cnpj)
        instance.cidade = validated_data.get('cidade', instance.cidade)
        instance.pais = validated_data.get('pais', instance.pais)
        instance.logradouro = validated_data.get('logradouro', instance.logradouro)
        instance.ativo = validated_data.get('ativo', instance.ativo)

        instance.save()
        return instance


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Departamento
        fields = ['url', 'id', 'centro_custo', 'nome', 'codigo_integracao', 'ativo', 'empresa']

    def create(self, validated_data):
        return Departamento.objects.create(**validated_data)

    def update(self, instance, validated_data):

        codigo_integracao = validated_data.get('cnpj', self.instance.codigo_integracao)
        if Departamento.objects.filter(codigo_integracao=codigo_integracao).exists() and codigo_integracao != instance.codigo_integracao:
            raise serializers.ValidationError("Departamento já cadastrado com esse código de integração")

        instance.centro_custo = validated_data.get('centro_custo', instance.centro_custo)
        instance.nome = validated_data.get('nome', instance.nome)
        instance.codigo_integracao = validated_data.get('codigo_integracao', instance.codigo_integracao)
        instance.empresa = validated_data.get('empresa', instance.empresa)
        instance.ativo = validated_data.get('ativo', instance.ativo)

        instance.save()
        return instance


class PessoaSerializer(serializers.HyperlinkedModelSerializer):

    telefone = serializers.CharField(max_length=20)
    cidade = serializers.ChoiceField(choices=CIDADES_CHOICES)

    class Meta:
        model = Pessoa
        fields = [
            'url',
            'nome_completo',
            'email_contato',
            'telefone',
            'data_nascimento',
            'data_ingresso',
            'data_desligamento',
            'ativo',
            'cidade',
            'departamento',
            'empresa'
        ]
