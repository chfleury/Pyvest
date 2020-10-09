from django.shortcuts import render
import json
from .models import Plot_Chart

import requests

url = "https://api.hgbrasil.com/finance/stock_price?key=68df2e2f&symbol=CIEL3"

payload = {}
headers = {
  'Cookie': '__cfduid=dcad4a377fb91994eb56d1a27bb7fbeca1598974673'
}

response = requests.request("GET", url, headers=headers, data = payload)



def products(response):

    #recebe os dados do banco de dados
    queryset = Plot_Chart.objects.all()
    names = [obj.name for obj in queryset]
    prices = [int(obj.price) for obj in queryset]
    market_caps = [int(obj.market_cap) for obj in queryset]

    context = {
        #transforma o objeto python em uma string JSON
        'names': json.dumps(names),
        'prices': json.dumps(prices),
        'market_caps': json.dumps(market_caps)
    }

    #renderiza o template com o contexto do dicionário dado, nesse caso é o 'context'
    return render(response, 'plot_chart/products.html', context)