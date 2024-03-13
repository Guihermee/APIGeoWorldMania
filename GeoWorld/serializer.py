from rest_framework import serializers
from GeoWorld.models import Bandeira, Pais

class BandeiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bandeira
        fields = '__all__'

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class ListaPorContinenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'