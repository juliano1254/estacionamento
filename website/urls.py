from django.urls import path, include
from website.views import (
    home,
    contato
)

urlpatterns = [
    path('', home, name='website_home'),
    path('contato/', contato, name='website_contato'),
]
