from django.shortcuts import render

def Listacarrinho(request):
    return render(request, 'index_carrinho.html')
