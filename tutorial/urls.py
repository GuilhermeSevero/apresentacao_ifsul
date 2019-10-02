from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tutorial.api import views

urlpatterns = [
    path('usuarios/', views.usuario_list),
    path('usuarios/<int:pk>', views.usuario_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
