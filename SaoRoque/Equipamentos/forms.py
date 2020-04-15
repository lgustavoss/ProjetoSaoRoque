from django import forms
from .models import *


# Cadastro de Adquirente
class AdquirentesForm(forms.ModelForm):
    class Meta:
        model = Adquirentes
        fields = ('adquirente',)


# Cadastro de Colaborador
class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ('nome', 'funcao')


# Cadastro de Computador
class ComputadorForm(forms.ModelForm):
    class Meta:
        model = Computador
        fields = ('tipo', 'colaborador', 'estabelecimento', 'marca', 'modelo', 'processador', 'memoria', 'armazenamento',
                  'service_tag', 'observacoes')


# Cadastro de Dispositivo
class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivos
        fields = ('tipo', 'colaborador', 'estabelecimento', 'marca', 'modelo', 'service_tag', 'observacoes')


# Cadastro de Estabelecimento
class EstabelecimentoForm(forms.ModelForm):
    class Meta:
        model = Estabelecimento
        fields = ('nome', 'cnpj')


# Cadastro de Maquininhas
class MaquininhaForm(forms.ModelForm):
    class Meta:
        model = Maquininha
        fields = ('tipo', 'adquirente', 'estabelecimento', 'n_serie', 'n_logico', 'mensalidade', 'status',
                  'data_ativacao', 'data_inativacao', 'observacoes')

