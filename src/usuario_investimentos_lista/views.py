from django.shortcuts import render


def meus_investimentos_lista(request):
    return render(request, 'investimentos_do_usuario_lista.html', {})