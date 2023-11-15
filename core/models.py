from django.db import models


class Empresa(models.Model):
    cnpj = models.CharField(max_length=14, unique=True)
    logradouro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.cnpj


class Departamento(models.Model):
    centro_custo = models.CharField(max_length=50)
    nome = models.CharField(max_length=255)
    codigo_integracao = models.CharField(max_length=20, unique=True)
    ativo = models.BooleanField(default=True)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, related_name='departamento')

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=255)
    email_contato = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    data_ingresso = models.DateField()
    data_desligamento = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)
    cidade = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING, related_name='pessoa')
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, related_name='pessoa_empresa')


    def __str__(self):
        return self.nome_completo
