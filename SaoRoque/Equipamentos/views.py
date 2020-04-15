import post
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *


# Create your views here.

# View de Login
def login(request):
    return redirect('login')

# Views de Cadastro
# Cadastro de Adquirente
@login_required()
def cadastrar_adquirente(request):
    if request.method == "POST":
        form = AdquirentesForm(request.POST)
        if form.is_valid():
            form = form.save()
            form.save()
            return redirect('listar_adquirentes')
    else:
        form = AdquirentesForm()
    return render(request, "cadastrar_adquirente.html", {'form': form})


# Cadastro de Colaborador
@login_required()
def cadastrar_colaborador(request):
    if request.method == "POST":
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form = form.save()
            form.save()
            return redirect('listar_colaborador')
    else:
        form = ColaboradorForm()
    return render(request, "cadastrar_colaborador.html", {'form': form})


# Cadastro de Computador
@login_required()
def cadastrar_computador(request):
    if request.method == "POST":
        form = ComputadorForm(request.POST)
        if form.is_valid():
            form = form.save()
            form.save()
            return redirect('listar_computador')
    else:
        form = ComputadorForm()
    return render(request, "cadastrar_computador.html", {'form': form})


# Cadastro de Dispositivo
@login_required()
def cadastrar_dispositivo(request):
    if request.method == "POST":
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form = form.save()
            form.save()
            return redirect('listar_dispositivo')
    else:
        form = DispositivoForm()
    return render(request, "cadastrar_dispositivo.html", {'form': form})


# Cadastro de Estabelecimento
@login_required()
def cadastrar_estabelecimento(request):
    if request.method == "POST":
        form = EstabelecimentoForm(request.POST)
        if form.is_valid():
            form = form.save()
            form.save()
            return redirect('listar_estabelecimento')
    else:
        form = EstabelecimentoForm()
    return render(request, "cadastrar_estabelecimento.html", {'form': form})


# Cadastro de Maquininhas
@login_required()
def cadastrar_maquininha(request):
    if request.method == "POST":
        form = MaquininhaForm(request.POST)
        if form.is_valid():
            form = form.save()
            form.save()
            return redirect('listar_maquininha')
    else:
        form = MaquininhaForm()
    return render(request, "cadastrar_maquininha.html", {'form': form})


# Views de Listagem
# Listagem de Adquirentes
@login_required()
def listar_adquirente(request, template_name="listar_adquirente.html"):
    query = request.GET.get("busca")
    if query:
        adquirente = Adquirentes.objects.filter(adquirente_icontains=query)
    else:
        adquirente = Adquirentes.objects.all()
    adquirentes = {'lista': adquirente}
    return render(request, template_name, adquirentes)


# Listagem de Colaborador
@login_required()
def listar_colaborador(request, template_name="listar_colaborador.html"):
    query = request.GET.get("busca")
    if query:
        colaborador = Colaborador.objects.filter(colaborador_icontains=query)
    else:
        colaborador = Colaborador.objects.all()
    colaboradores = {'lista': colaborador}
    return render(request, template_name, colaboradores)


# Listagem de Computador
@login_required()
def listar_computador(request, template_name="listar_computador.html"):
    query = request.GET.get("busca")
    if query:
        computador = Computador.objects.filter(computador_icontains=query)
    else:
        computador = Computador.objects.all()
    computadores = {'lista': computador}
    return render(request, template_name, computadores)


# Listagem de Dispositivo
@login_required()
def listar_dispositivo(request, template_name="listar_dispositivo.html"):
    query = request.GET.get("busca")
    if query:
        dispositivo = Dispositivos.objects.filter(dispositivos_icontains=query)
    else:
        dispositivo = Dispositivos.objects.all()
    dispositivos = {'lista': dispositivo}
    return render(request, template_name, dispositivos)


# Listagem de Estabelecimento
@login_required()
def listar_estabelecimento(request, template_name="listar_estabelecimento.html"):
    query = request.GET.get("busca")
    if query:
        estabelecimento = Estabelecimento.objects.filter(estabelecimento_icontains=query)
    else:
        estabelecimento = Estabelecimento.objects.all()
    estabelecimento = {'lista': estabelecimento}
    return render(request, template_name, estabelecimento)


# Listagem de Maquininhas
@login_required()
def listar_maquininha(request, template_name="listar_maquininha.html"):
    query = request.GET.get("busca")
    if query:
        maquininha = Maquininha.objects.filter(maquininha_icontains=query)
    else:
        maquininha = Maquininha.objects.all()
    maquininha = {'lista': maquininha}
    return render(request, template_name, maquininha)


# Views de Edição
# Edição de Adquirentes
@login_required()
def editar_adquirente(request, pk, template_name="cadastrar_adquirente.html"):
    adquirente = get_object_or_404(Adquirentes, pk=pk)
    if request.method == "POST":
        form = AdquirentesForm(request.POST, instance=adquirente)
        if form.is_valid():
            form.save()
            return redirect('listar_adquirentes')
    else:
        form = AdquirentesForm(instance=adquirente)
    return render(request, template_name, {'form': form})


# Edição de Colaborador
@login_required()
def editar_colaborador(request, pk, template_name="cadastrar_colaborador.html"):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == "POST":
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            return redirect('listar_colaborador')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, template_name, {'form': form})


# Edição de Computador
@login_required()
def editar_computador(request, pk, template_name="cadastrar_computador.html"):
    computador = get_object_or_404(Computador, pk=pk)
    if request.method == "POST":
        form = ComputadorForm(request.POST, instance=computador)
        if form.is_valid():
            form.save()
            return redirect('listar_computador')
    else:
        form = ComputadorForm(instance=computador)
    return render(request, template_name, {'form': form})


# Edição de Dispositivo
@login_required()
def editar_dispositivo(request, pk, template_name="cadastrar_dispositivo.html"):
    dispositivo = get_object_or_404(Dispositivos, pk=pk)
    if request.method == "POST":
        form = DispositivoForm(request.POST, instance=dispositivo)
        if form.is_valid():
            form.save()
            return redirect('listar_dispositivo')
    else:
        form = DispositivoForm(instance=dispositivo)
    return render(request, template_name, {'form': form})


# Edição de Estabelecimento
@login_required()
def editar_estabelecimento(request, pk, template_name="cadastrar_estabelecimento.html"):
    estabelecimento = get_object_or_404(Estabelecimento, pk=pk)
    if request.method == "POST":
        form = EstabelecimentoForm(request.POST, instance=estabelecimento)
        if form.is_valid():
            form.save()
            return redirect('listar_estabelecimento')
    else:
        form = EstabelecimentoForm(instance=estabelecimento)
    return render(request, template_name, {'form': form})


# Edição de Maquininha
@login_required()
def editar_maquininha(request, pk, template_name="cadastrar_maquininha.html"):
    maquininha = get_object_or_404(Maquininha, pk=pk)
    if request.method == "POST":
        form = MaquininhaForm(request.POST, instance=maquininha)
        if form.is_valid():
            form.save()
            return redirect('listar_maquininha')
    else:
        form = MaquininhaForm(instance=maquininha)
    return render(request, template_name, {'form': form})



# Views de Exclusões
# Exclusão de Adquirente
@login_required()
def remover_adquirente(request, pk, template_name="remover_adquirente.html"):
    adquirente = Adquirentes.objects.get(pk=pk)
    if request.method == 'POST':
        adquirente.delete()
        return redirect('listar_adquirentes')
    return render(request, template_name, {'adquirente': adquirente})


# Exclusão de Colaborador
@login_required()
def remover_colaborador(request, pk, template_name="remover_colaborador.html"):
    colaborador = Colaborador.objects.get(pk=pk)
    if request.method == 'POST':
        colaborador.delete()
        return redirect('listar_colaborador')
    return render(request, template_name, {'colaborador': colaborador})


# Exclusão de Computador
@login_required()
def remover_computador(request, pk, template_name="remover_computador.html"):
    computador = Computador.objects.get(pk=pk)
    if request.method == 'POST':
        computador.delete()
        return redirect('listar_computador')
    return render(request, template_name, {'computador': computador})


# Exclusão de Dispositivo
@login_required()
def remover_dispositivo(request, pk, template_name="remover_dispositivo.html"):
    dispositivo = Dispositivos.objects.get(pk=pk)
    if request.method == 'POST':
        dispositivo.delete()
        return redirect('listar_dispositivo')
    return render(request, template_name, {'dispositivo': dispositivo})


# Exclusão de Estabelecimento
@login_required()
def remover_estabelecimento(request, pk, template_name="remover_estabelecimento.html"):
    estabelecimento = Estabelecimento.objects.get(pk=pk)
    if request.method == 'POST':
        estabelecimento.delete()
        return redirect('listar_estabelecimento')
    return render(request, template_name, {'estabelecimento': estabelecimento})


# Exclusão de Maquininha
@login_required()
def remover_maquininha(request, pk, template_name="remover_maquininha.html"):
    maquininha = Maquininha.objects.get(pk=pk)
    if request.method == 'POST':
        maquininha.delete()
        return redirect('listar_maquininha')
    return render(request, template_name, {'maquininha': maquininha})
