from django.urls import path
from . import views

urlpatterns = [
    path('entrar', views.entrar),
    path('registrar', views.registrar)
]
