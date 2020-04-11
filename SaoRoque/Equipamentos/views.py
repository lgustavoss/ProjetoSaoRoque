import post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.

# Cadastro de Adquirente

def cadastrar_adquirente(request):
    if request.method == "POST":
        form = AdquirentesForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('listar_adquirentes')
    else:
        form = AdquirentesForm()
    return render(request, "cadastrar_adquirente.html", {'form': form})



# Listagem de Adquirentes

def listar_adquirente(request):
    List = Adquirentes.objects.all()

    return render(request, 'listar_adquirentes.html', {'List': list})
