from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tutorial.api import views

urlpatterns = [
    path('usuarios/', views.UsuarioList.as_view()),
    path('usuarios/<int:pk>', views.UsuarioDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
