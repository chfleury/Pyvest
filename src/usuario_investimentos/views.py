from django.shortcuts import render


def meus_investimentos(request):
    return render(request, 'investimentos_do_usuario.html', {})