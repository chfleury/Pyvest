from . import views
from django.urls import path
from busca import views as busca_views

urlpatterns =[
    path('carrinho',views.Listacarrinho, name = "carrinho view"),
    path('carrinho/entrar', busca_views.logout_view)
]
