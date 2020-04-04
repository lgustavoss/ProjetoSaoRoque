from django.contrib import admin
from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('registrar_usuario/', registrar_usuario, name='registrar_usuario'),
    path('listar_usuario/', listar_usuario, name='listar_usuario'),
    path('logar/', logar, name='logar'),
    re_path(r'^remover_usuario/(?P<pk>[0-9]+)', remover_usuario, name='remover_usuario'),
    path('deslogar/', deslogar, name='deslogar'),
]

