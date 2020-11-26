from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def entrar(request):
    context = {}
    context['error'] = '0'

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            return redirect('/busca')
        else:
            messages.error(request, 'Usuário e/ou senha incorretos.')

            return redirect('/entrar') 
    else:
        return render(request, '../templates/entrar.html', context)


def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/entrar')
    else:
        form = UserCreationForm()
    return render(request, '../templates/registrar.html', {'form': form})


