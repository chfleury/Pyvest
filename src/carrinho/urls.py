from . import views
from django.urls import path

urlpatterns =[
    path('carrinho',views.Listacarrinho),
]
