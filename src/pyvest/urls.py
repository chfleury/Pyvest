from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import index
from django.urls import include
from django.urls import path, include
from .views import index
from .views import home
from .views import sobre
from busca import views as busca_views
from plot_chart import views
from usuario_investimentos import views as inv_views

# 'urlpatterns' será utilizado para encontrar a URL desejada em ordem de busca sequencial 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('',include('busca.urls')),
    path('',include('carrinho.urls')),
    path('meus_investimentos/', inv_views.meus_investimentos),
    path('meus_investimentos/grafico/', views.products),
    path('meus_investimentos/entrar', busca_views.logout_view),
    path('meus_investimentos/grafico/entrar', busca_views.logout_view),
    path('home', home),
    path('sobre', sobre),
    path('', include('entrar_registrar.urls')),
]

