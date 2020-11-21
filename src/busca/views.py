from django.shortcuts import render, redirect
from sys import argv
import csv
from django.http import HttpResponse
import requests 
import json 
import os

from eda.HashTable import *
from eda.Pilha import *

hash_table = []

# Lista formada por nodes de palavras e chaves de cada ação

# Retornará o índice em que a palavra deve ser colocada dentro da hashtable
def get_key(palavra):
    return ord(palavra[0].lower()) - 97
# Inicia os valores da lista com o objeto LinkedList

def hash_init():
    for i in range(23):
        hash_table.append(LinkedList())

# Lista os itens no arquivo csv
def get_stock():
    with open('static/csv/acoes_api.csv', encoding="utf8") as entrada:
        acoes = list(csv.reader(entrada))
    return acoes


# Carrega a hash table
def load_hash(acoes):
    row = 0
    for i in acoes:
        key = get_key(acoes[row][0])
        hash_table[key].append(acoes[row][0], acoes[row][1])
        row += 1 

def request_api(symbolList, key):
    listaDados = []
    for i in symbolList:
        url = f'https://api.hgbrasil.com/finance/stock_price?key={key}&symbol={i}'

        dados = requests.get(url)
        test = json.loads(dados.text)
        listaDados.append(test['results'][i])
  
    return listaDados

context = {}

def busca(request):
    if request.user.is_authenticated:
        userId = request.user.id
    else:
        return redirect('/entrar') 
    acoesSession = []
    carrinho_temp = Pilha()

    try:
        acoesSession = request.session['acoes']
    except:
        acoesSession = []
  
    print('Carrinho:')
    print(carrinho_temp)

    print('Acoes session')
    print(acoesSession)
    path = os.path.join(
      '..', 'templates', 'busca.html')

    if request.method == 'POST':
        busca = request.POST.get('busca')
        # Nessa view temos 3 situações de POST:
        # 1: Se o usuário fez uma busca
        # 2: Se o usuário desfez a ultima adição do carrinho 
        # 3: Se o usuário adicionou alguma ação ao carrinho temporário

        # Nesse if verificamos se ele tentou fazer busca ou não
        if busca is not None:
        # Caso ele tenha feito uma busca, executamos o códico da busca (Caso 1)
            acoes = get_stock()
            
            hash_init()
            load_hash(acoes) 

            key = get_key(busca)

            if key > 22:
                print("Nenhum valor com esta letra.")
                return render(request, path, {})

            symbolList = set(hash_table[key].search(busca))

            context['acoes'] = request_api(symbolList, '0d9862ec')
            return render(request, path, context)
        else:
        # Caso contrário, ele ainda pode ter ou adicionado ao carrinho,
        # ou desfeito a ação
            desfazer = request.POST.get('desfazer')

            # Checa se usuario desfez a ação, se sim, entramos no caso 2
            # e executamos o códico de desfazer a ação
            if desfazer is not None and desfazer:
                contextDesfazer = {}
                contextDesfazer['acoes'] = context['acoes']
                contextDesfazer['desfeito'] = True
                
                l = []
                try:
                    l = request.session['acoes']

                except:
                    l = []

                for i in l:
                    carrinho_temp.push(
                        i['symbol'],
                        i['name'],
                        i['region'],
                        i['currency'],
                        i['time_open'],
                        i['time_close'],
                        i['timezone'],
                        i['market_cap'],
                        i['price'],
                        i['change_percent'],
                        i['updated_at'])
#
                carrinho_temp.pop()
                
                request.session['acoes'] = carrinho_temp.listar()

                return render(request, path, contextDesfazer)

            else:
            # Caso ele não tenha desfeito, significa que esse POST
            # foi utilizado para adicionar uma ação ao carrinho (Caso 3)
            # temporário, o que é feito a seguir
                adicionar = request.POST.get('adicionar')

                if adicionar is not None and adicionar:

                    contextCarrinho = {}
                    try:
                        contextCarrinho['acoes'] = context['acoes']
                    except:
                        contextCarrinho['acoes'] = []

                    contextCarrinho['snack'] = True
                    
                    # pega os respectivos valores e utiliza como parametro
                    carrinho_temp.push(
                        request.POST.get('symbol'),
                        request.POST.get('name'),
                        request.POST.get('region'),
                        request.POST.get('currency'),
                        request.POST.get('open'),
                        request.POST.get('close'),
                        request.POST.get('timezone'),
                        request.POST.get('market_cap'),
                        request.POST.get('price'),
                        request.POST.get('change_percent'),
                        request.POST.get('updated_at')
                    )
                    l = []
                    try:
                        l = request.session['acoes']

                    except:
                        l = []
                    request.session['acoes'] = carrinho_temp.listar() + l
     
                    return render(request, path, contextCarrinho)
                else:
                    return render(request, path)

    else:
        return render(request, path)

def redirectcarrinho(request):
    if request.method == 'GET':
        return redirect('/carrinho')



