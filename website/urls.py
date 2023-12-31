from django.urls import path, include
from website.views import (
    home,
    servicos,
    contato,
    sobre,
    planos
)

urlpatterns = [
    path('', home, name='website_home'),
    path('contato/', contato, name='website_contato'),
    path('servicos/', servicos, name='website_servicos'),
    path('sobre/', sobre, name='website_sobre'),
    path('planos/', planos, name='website_planos'),
]
