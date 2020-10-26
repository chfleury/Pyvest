from . import views
from django.urls import path

urlpatterns =[
    path('busca',views.busca,name='busca'),
    path('busca/redirect',views.redirectcarrinho)
]
