from django.shortcuts import render

def Listacarrinho(request):
    context = {}
    try:
        # ta funcionando
        # 
        context['acoes'] = request.session['acoes']
        print('---------carrinho------------')
        print(request.session['acoes'])
        print('----------carrinho-----------')

    except:
        context['vazio'] = True
        print('erro')
   

    return render(request, 'index_carrinho.html', context )

    
