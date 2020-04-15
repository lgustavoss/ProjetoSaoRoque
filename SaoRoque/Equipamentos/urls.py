from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('cadastrar_adquirente/', cadastrar_adquirente, name='cadastrar_adquirente'),
    path('cadastrar_colaborador/', cadastrar_colaborador, name='cadastrar_colaborador'),
    path('cadastrar_computador/', cadastrar_computador, name='cadastrar_computador'),
    path('cadastrar_dispositivo/', cadastrar_dispositivo, name='cadastrar_dispositivo'),
    path('cadastrar_estabelecimento/', cadastrar_estabelecimento, name='cadastrar_estabelecimento'),
    path('cadastrar_maquininha/', cadastrar_maquininha, name='cadastrar_maquininha'),
    path('listar_adquirentes/', listar_adquirente, name='listar_adquirentes'),
    path('listar_colaborador/', listar_colaborador, name='listar_colaborador'),
    path('listar_computador/', listar_computador, name='listar_computador'),
    path('listar_dispositivo/', listar_dispositivo, name='listar_dispositivo'),
    path('listar_estabelecimento/', listar_estabelecimento, name='listar_estabelecimento'),
    path('listar_maquininha/', listar_maquininha, name='listar_maquininha'),
    re_path('^editar_adquirente/(?P<pk>[0-9]+)', editar_adquirente, name='editar_adquirente'),
    re_path('^editar_colaborador/(?P<pk>[0-9]+)', editar_colaborador, name='editar_colaborador'),
    re_path('^editar_computador/(?P<pk>[0-9]+)', editar_computador, name='editar_computador'),
    re_path('^editar_dispositivo/(?P<pk>[0-9]+)', editar_dispositivo, name='editar_dispositivo'),
    re_path('^editar_estabelecimento/(?P<pk>[0-9]+)', editar_estabelecimento, name='editar_estabelecimento'),
    re_path('^editar_maquininha/(?P<pk>[0-9]+)', editar_maquininha, name='editar_maquininha'),
    re_path('remover_adquirente/(?P<pk>[0-9]+)', remover_adquirente, name='remover_adquirente'),
    re_path('remover_colaborador/(?P<pk>[0-9]+)', remover_colaborador, name='remover_colaborador'),
    re_path('remover_computador/(?P<pk>[0-9]+)', remover_computador, name='remover_computador'),
    re_path('remover_dispositivo/(?P<pk>[0-9]+)', remover_dispositivo, name='remover_dispositivo'),
    re_path('remover_estabelecimento/(?P<pk>[0-9]+)', remover_estabelecimento, name='remover_estabelecimento'),
    re_path('remover_maquininha/(?P<pk>[0-9]+)', remover_maquininha, name='remover_maquininha'),
]
