from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')

def servicos(request):
    return render(request, 'website/servicos.html')

def contato(request):
    #import pdb; pdb.set_trace()
    contato = {}
    contato['nome'] = request.POST.get('nome')
    contato['email'] = request.POST.get('email')
    contato['telefone'] = request.POST.get('telefone')
    contato['mensagem'] = request.POST.get('mensagem')
    return render(request, 'website/contato.html')

def sobre(request):
    return render(request, 'website/sobre.html')

def planos(request):
    return render(request, 'website/planos.html')