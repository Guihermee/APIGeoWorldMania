from rest_framework import viewsets, filters
from GeoWorld.models import Bandeira, Pais
from GeoWorld.serializer import BandeiraSerializer, PaisSerializer

# Imports para Autenticação
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Imports para filtro
from django_filters.rest_framework import DjangoFilterBackend

# Imports para aceitar list no POST
from rest_framework.response import Response
from rest_framework import status


class BandeiraViewSet(viewsets.ModelViewSet):
    """Exibindo todas as bandeiras"""
    queryset = Bandeira.objects.all()
    serializer_class = BandeiraSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome']
    ordering_fields = ['nome']

    def create(self, request, *args, **kwargs):
            data = request.data
            if isinstance(data, list):
                serializer = self.get_serializer(data=data, many=True)
            else:
                serializer = self.get_serializer(data=data)

            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PaisViewSet(viewsets.ModelViewSet):
    """Exibindo todos os paises"""
    queryset = Pais.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome', 'capital', 'continente']
    ordering_fields = ['nome']

    def create(self, request, *args, **kwargs):
        data = request.data
        if isinstance(data, list):
            serializer = self.get_serializer(data=data, many=True)
        else:
            serializer = self.get_serializer(data=data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
