from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')

def servicos(request):
    return render(request, 'website/servicos.html')

def contato(request):
    return render(request, 'website/contato.html')

def sobre(request):
    return render(request, 'website/sobre.html')

def planos(request):
    return render(request, 'website/planos.html')