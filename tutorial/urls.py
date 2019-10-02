from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tutorial.api import views


router = DefaultRouter()
router.register(r'usuarios', views.UsuarioView)

urlpatterns = [
    path('', include(router.urls)),
]