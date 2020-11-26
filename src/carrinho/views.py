from django.shortcuts import render,redirect
from .models import Investimento

def Listacarrinho(request):
    if request.user.is_authenticated:
        userId = request.user.id
    else:
        return redirect('/entrar') 

    context ={}
    try:
        listaInvestimentos = []
        listaInvestimentos = request.session['acoes']
        context['acoes'] = listaInvestimentos
    except:
        context['vazio'] = True
        

    if request.method == 'POST':
        if request.POST.get('investir') == 'investir':
            userId = 0
            if request.user.is_authenticated:
                userId = request.user.id
            
            for i in listaInvestimentos:
                Investimento(
                    symbol = i['symbol'],
                    name= i['name'],
                    region = i['region'],
                    currency = i['currency'],
                    timeOpen= i['time_open'],
                    timeClose= i['time_close'],
                    timeZone= i['timezone'],
                    marketCap=i['market_cap'],
                    price= i['price'],
                    changePercent= i['change_percent'],
                    data= i['updated_at'],
                    userId = userId,
                ).save()
            request.session['acoes'] = []
            
            return render(request, 'index_carrinho.html' )
        elif request.POST.get('excluir') == 'excluir':
            request.session['acoes'] = []
            
            return render(request, 'index_carrinho.html')
        return render(request, 'index_carrinho.html', context )
    else: 
        return render(request, 'index_carrinho.html', context )

    
