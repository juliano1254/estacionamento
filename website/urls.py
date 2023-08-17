from django.urls import path, include
from website.views import (
    home,
)

urlpatterns = [
    path('', home, name='website_home'),
]
