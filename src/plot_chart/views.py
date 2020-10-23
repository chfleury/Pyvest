from django.shortcuts import render
import json
from .models import Plot_Chart
import requests

def fazerRequisicao(symbol, key, nome_do_campo):

    url = f'https://api.hgbrasil.com/finance/stock_price?&key={key}&symbol={symbol}&fields={nome_do_campo}'

    dados = requests.get(url)

    resposta_geral = dados.json()
    somente_resultados = resposta_geral["results"]
    valor_do_campo_desejado = somente_resultados["PETR4"]
    print(json.dumps(valor_do_campo_desejado))

    return valor_do_campo_desejado
for_chart = float(fazerRequisicao('PETR4', 'dc9e7785', 'price'))
print(for_chart)
def products(request):

    #context = {
        #transforma o objeto python em uma string JSON
        #'names': json.dumps(names),
        #'prices': json.dumps(prices),
    #    'for_chart' : for_chart,
    #}

    #renderiza o template com o contexto do dicionário dado, nesse caso é o 'context'
    return render(request, 'plot_chart/products.html', {
      'for_chart': for_chart,
    })