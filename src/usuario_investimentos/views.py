from django.shortcuts import render, redirect
from carrinho.models import Investimento
from plot_chart.views import products
from eda.Linked_List import *
# criar um botão para cada investimento com o código e o nome de cada um
# usar a API pra pegar o dado do dia daquele investimento
context = {}
context['acoes'] = []

def meus_investimentos(request):
  
    context['acoes'] = []
    lista_investimentos = Linked_List_Investimentos()

    userId = 0
    if request.user.is_authenticated:
        userId = request.user.id
    else:
        print('redicisadmsaks')
        return redirect('/entrar') 
              
    investimentos = Investimento.objects.all().filter(userId= userId)

    for i in investimentos:
        lista_investimentos.append(i.symbol, i.name, i.price, i.id)

        
    context['acoes'] = lista_investimentos.load_context()
    
    if request.method == 'POST':

        x = request.POST.get('symbol')
        y = request.POST.get('id')
        n = request.POST.get('name')
        if x != None:
          print(x)
          return products(request, x, n)
        else:
            investimentos = Investimento.objects.all().filter(id= y).delete()
        
            context['acoes'] = []
            lista_investimentos = Linked_List_Investimentos()
                    
            investimentos = Investimento.objects.all().filter(userId= userId)

            for i in investimentos:
                lista_investimentos.append(i.symbol, i.name, i.price, i.id)

            context['acoes'] = lista_investimentos.load_context()

            return render(request, 'investimentos_do_usuario.html', context)
    else:
      
            
        return render(request, 'investimentos_do_usuario.html', context)
  
 