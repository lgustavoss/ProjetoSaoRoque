from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('cadastrar_adquirente/', cadastrar_adquirente, name='cadastrar_adquirente'),
    path('listar_adquirentes/', listar_adquirente, name='listar_adquirentes')
]


