
from django.contrib import admin
from django.urls import path, include 
from GeoWorld.views import BandeiraViewSet, PaisViewSet
from rest_framework import routers

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('Bandeiras', BandeiraViewSet, basename='Bandeiras')
router.register('Paises', PaisViewSet, basename='Paises')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

# Configuração de rota para servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)