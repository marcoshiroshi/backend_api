from rest_framework import viewsets, permissions, status
from core.serializers import *
from rest_framework.response import Response


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance = self.get_object()
        instance.ativo = False
        instance.save()
        return Response(status=status.HTTP_200_OK)


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance = self.get_object()
        instance.ativo = False
        instance.save()
        return Response(status=status.HTTP_200_OK)


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Pessoa.objects.all()

        cidade = self.request.query_params.get('cidade', None)
        empresa = self.request.query_params.get('empresa', None)
        departamento = self.request.query_params.get('departamento', None)

        if cidade:
            queryset = queryset.filter(cidade__icontains=cidade)
        if empresa:
            queryset = queryset.filter(empresa__cnpj__icontains=empresa)
        if departamento:
            queryset = queryset.filter(departamento__centro_custo__icontains=departamento)
        return queryset

    def perform_destroy(self, instance):
        instance = self.get_object()
        instance.ativo = False
        instance.save()
        return Response(status=status.HTTP_200_OK)