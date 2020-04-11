from django import forms
from .models import *


# Cadastro de Adquirente
class AdquirentesForm(forms.ModelForm):
    class Meta:
        model = Adquirentes
        fields = ('adquirente',)
