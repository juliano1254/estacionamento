from django.urls import path, include
from django.contrib import admin
from core.views import (
    home, 
    lista_pessoas, 
    lista_veiculos, 
    lista_movrotativos,
    lista_mensalistas,
    lista_movmensalistas,
    pessoa_novo,
    veiculo_novo,
    movrotativo_novo,
    mensalista_novo,
    movmensalista_novo,
    pessoa_update,
    veiculo_update,
    movrotativo_update,
    mensalista_update,
    movmensalista_update,
    pessoa_delete,
    veiculo_delete,
    movrotativo_delete,
    mensalista_delete,
    movmensalista_delete
)

urlpatterns = [
    path('', include('website.urls')),
    path('sistema/', home, name='core_home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    ## PESSOAS
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa-novo/', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa-update/(?P<id>\d+)/', pessoa_update, name='core_pessoa_update'),
    path('pessoa-delete/(?P<id>\d+)/', pessoa_delete, name='core_pessoa_delete'),

    ## VEICULOS
    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo-novo/', veiculo_novo, name='core_veiculo_novo'),
    path('veiculo-update/(?P<id>\d+)/', veiculo_update, name='core_veiculo_update'),
    path('veiculo-delete/(?P<id>\d+)/', veiculo_delete, name='core_veiculo_delete'),

    ## MOVIMENTACAO ROTATIVOS
    path('mov-rot/', lista_movrotativos, name='core_lista_movrotativos'),
    path('mov-rot-novo/', movrotativo_novo, name='core_movrotativo_novo'),
    path('mov-rot-update/(?P<id>\d+)/', movrotativo_update, name='core_movrotativo_update'),
    path('mov-rot-delete/(?P<id>\d+)/', movrotativo_delete, name='core_movrotativo_delete'),

    ## MENSALISTAS
    path('mensalistas/', lista_mensalistas, name='core_lista_mensalista'),
    path('mensalista-novo/', mensalista_novo, name='core_mensalista_novo'),
    path('mensalista-update/(?P<id>\d+)/', mensalista_update, name='core_mensalista_update'),
    path('mensalista-delete/(?P<id>\d+)/', mensalista_delete, name='core_mensalista_delete'),

    ## MOVIMENTACAO MENSALISTAS
    path('mov-mensal/', lista_movmensalistas, name='core_lista_movmensalista'),
    path('mov-mensal-novo/', movmensalista_novo, name='core_movmensalista_novo'),
    path('mov-mensal-update/(?P<id>\d+)/', movmensalista_update, name='core_movmensalista_update'),
    path('mov-mensal-delete/(?P<id>\d+)/', movmensalista_delete, name='core_movmensalista_delete'),
]
