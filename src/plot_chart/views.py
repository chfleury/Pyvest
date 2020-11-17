from django.shortcuts import render
import json
from .models import Plot_Chart
import requests
from carrinho.models import Investimento

# Requisição feita na API
def fazerRequisicao(symbol, key):
    
    #maior queda
    url1 = f'https://api.hgbrasil.com/finance/stock_price?&key={key}&symbol=get-low'
    
    #dados da ação desejada
    url2 = f'https://api.hgbrasil.com/finance/stock_price?&key={key}&symbol={symbol}'
    
    #maior alta
    url3 = f'https://api.hgbrasil.com/finance/stock_price?&key={key}&symbol=get-high'

    #guarda os dados dos requests
    dados1 = requests.get(url1)
    dados2 = requests.get(url2)
    dados3 = requests.get(url3)

    #trabalha os dados da maior queda para retornar o 'price', 'change_percent' e 'market_cap'
    resposta_min = dados1.json()
    somente_resultados1 = resposta_min["results"]
    lista_min = list(somente_resultados1.keys())
    symbol_min = lista_min[0]
    price_for_chart1 = (somente_resultados1[symbol_min])["price"]
    change_for_chart1 = (somente_resultados1[symbol_min])["change_percent"]
    market_for_chart1 = (somente_resultados1[symbol_min])["market_cap"]
    
    #trabalha os dados do investimento do usuário para retornar o 'price', 'change_percent' e 'market_cap'
    resposta_geral = dados2.json() 
    somente_resultados2 = resposta_geral["results"]
    price_for_chart2 = (somente_resultados2[symbol])["price"]
    change_for_chart2 = (somente_resultados2[symbol])["change_percent"]
    market_for_chart2 = (somente_resultados2[symbol])["market_cap"]

    #trabalha os dados da maior alta para retornar o 'price', 'change_percent' e 'market_cap'
    resposta_max = dados3.json()
    somente_resultados3 = resposta_max["results"]
    lista_max = list(somente_resultados3.keys())
    symbol_max = lista_max[0]
    price_for_chart3 = (somente_resultados3[symbol_max])["price"]
    change_for_chart3 = (somente_resultados3[symbol_max])["change_percent"]
    market_for_chart3 = (somente_resultados3[symbol_max])["market_cap"]

    return price_for_chart1, price_for_chart2, price_for_chart3, change_for_chart1, change_for_chart2, change_for_chart3, market_for_chart1, market_for_chart2, market_for_chart3, symbol_min, symbol, symbol_max

# Dados usado no gráfico    
#price_for_chart1, price_for_chart2, price_for_chart3, change_for_chart1, change_for_chart2, change_for_chart3, market_for_chart1, market_for_chart2, market_for_chart3, label_for_chart1, label_for_chart2, label_for_chart3 = fazerRequisicao('PETR4', '3eafa921')
#label_for_chart1 = json.dumps(label_for_chart1)
#label_for_chart2 = json.dumps(label_for_chart2)
#label_for_chart3 = json.dumps(label_for_chart3)

def products(request, symbol, name):
    if request.user.is_authenticated:
        userId = request.user.id
    else:
        return redirect('/entrar') 
      
    print(symbol)

    price_for_chart1, price_for_chart2, price_for_chart3, change_for_chart1, change_for_chart2, change_for_chart3, market_for_chart1, market_for_chart2, market_for_chart3, label_for_chart1, label_for_chart2, label_for_chart3 = fazerRequisicao(symbol, '3eafa921')
    label_for_chart1 = json.dumps(label_for_chart1)
    label_for_chart2 = json.dumps(label_for_chart2)
    label_for_chart3 = json.dumps(label_for_chart3)


    # fazerRequisicao()
    #renderiza o template com o contexto do dicionário dado, nesse caso é o 'context'
    return render(request, 'plot_chart/products.html', {
      'price_for_chart1': price_for_chart1,
      'price_for_chart2': price_for_chart2,
      'price_for_chart3': price_for_chart3,
      'change_for_chart1': change_for_chart1,
      'change_for_chart2': change_for_chart2,
      'change_for_chart3': change_for_chart3,
      'market_for_chart1': market_for_chart1,
      'market_for_chart2': market_for_chart2,
      'market_for_chart3': market_for_chart3,
      'label_for_chart1': label_for_chart1,
      'label_for_chart2': label_for_chart2,
      'label_for_chart3': label_for_chart3,
      'acao': {'symbol': symbol, 'name': name}
    })