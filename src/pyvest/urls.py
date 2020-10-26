"""pyvest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import index
from django.urls import include


#importa o arquivo 'views' da aplicação 'chart'
from plot_chart import views

from usuario_investimentos import views as inv_views

from usuario_investimentos_lista import views as inv_lista_views

# 'urlpatterns' será utilizado para encontrar a URL desejada em ordem de busca sequencial 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('',include('busca.urls')),
    path('',include('carrinho.urls')),
]

