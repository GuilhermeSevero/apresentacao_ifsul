from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tutorial.api import views


router = DefaultRouter()
router.register(r'usuarios', views.UsuarioView)
router.register(r'partidas', views.PartidaView)

urlpatterns = [
    path('', include(router.urls)),
]