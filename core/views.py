from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Pessoa, 
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
)
from .forms import (
    PessoaForm, 
    VeiculoForm, 
    MovRotativoForm, 
    MensalistaForm,
    MovMensalistaForm
)

@login_required
def home(request):
    context = {'mensagem':"Ola mundo"}
    return render(request,'core/index.html',context)


### PESSOAS
@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    #return render(request, 'lista_pessoas.html') ## pasta template do dir principal
    data = {'pessoas':pessoas, 'form':form}
    return render(request, 'core/lista_pessoas.html', data) ## pasta template/core do dir core


@login_required
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


@login_required
def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


@login_required
def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':pessoa})


### VEICULOS
@login_required
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos':veiculos, 'form':form}
    return render(request, 'core/lista_veiculos.html', data) ## pasta template/core do dir core


@login_required
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


@login_required
def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)


@login_required
def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':veiculo})


## MOVIMENTOS ROTATIVOS
@login_required
def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'mov_rot':mov_rot, 'form':form}
    return render(
        request, 'core/lista_movrotativos.html', data) ## pasta template/core do dir core


@login_required
def movrotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')


@login_required
def movrotativo_update(request, id):
    data = {}
    mov = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=mov)
    data['movrotativo'] = mov
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/update_movrotativo.html', data)


@login_required
def movrotativo_delete(request, id):
    mov = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        mov.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':mov})


## MENSALISTAS
@login_required
def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas':mensalistas, 'form':form}
    return render(request, 'core/lista_mensalistas.html', data) ## pasta template/core do dir core


@login_required
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')


@login_required
def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/update_mensalista.html', data)


@login_required
def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':mensalista})


## MOVIMENTO MENSALISTAS
@login_required
def lista_movmensalistas(request):
    mov_mensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'mov_mensalistas':mov_mensalistas, 'form':form}
    return render(request, 'core/lista_movmensalistas.html', data) ## pasta template/core do dir core


@login_required
def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalista')


@login_required
def movmensalista_update(request, id):
    data = {}
    mov = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=mov)
    data['movmensalista'] = mov
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalista')
    else:
        return render(request, 'core/update_movmensalista.html', data)


@login_required
def movmensalista_delete(request, id):
    mov = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        mov.delete()
        return redirect('core_lista_movmensalista')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':mov})