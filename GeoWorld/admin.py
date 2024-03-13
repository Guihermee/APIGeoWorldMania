from django.contrib import admin
from GeoWorld.models import Pais,Bandeira

# Register your models here.

class Bandeiras(admin.ModelAdmin):
    list_display = ('id', 'nome', 'imagem', 'descricao')
    list_display_links = ('nome', 'id')
    search_fields = ('imagem',)
    ordering = ('nome',)

admin.site.register(Bandeira, Bandeiras)

class Paises(admin.ModelAdmin):
    list_display = ('id', 'nome', 'capital', 'continente')
    list_display_links = ('nome', 'id')
    search_fields = ('nome',)
    ordering = ('nome',)
    
admin.site.register(Pais, Paises)
