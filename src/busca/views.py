from django.shortcuts import render, redirect
from sys import argv
import csv
from django.http import HttpResponse
import requests 
import json 
import os


class Node:
    def __init__(self, name, key):
        self.name = name
        self.key = key
        self.next = None
hash_table = []
# Lista formada por nodes de palavras e chaves de cada ação
class LinkedList:
    def __init__(self):
        self.head = None
        

    def append(self, word, key):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(word, key)
        else:
            self.head = Node(word, key)
    
    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.name) + "----" + str(pointer.key) + "->"
            pointer = pointer.next
        r = r + "None"
        return r

    def __str__(self):
        return self.__repr__()
    

    def search(self, palavra):
        lista = []
        pointer = self.head
        while(pointer):
            if palavra.lower() in pointer.name.lower():
                lista.append(pointer.key)
                print(pointer.key)
            pointer = pointer.next
        return lista


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

        print(url)
        dados = requests.get(url)
        test = json.loads(dados.text)
        price = test['results'][i]['market_cap']
        listaDados.append(test['results'][i])

        print('-----------------------')
    return listaDados
#
# Pilha (lista) do carrinho temp

# blz testa ai vc a busca ver se ta funcionando direito 
#blz
# quer ir discord? to lá
# eai
# ta dando um  Not Found: /favicon.ico]
# sabe oq e iso?


#TODO: fazer o carrinho pilha
#joga aqui pae
class NodePilha:
    def __init__(self, symbol, name, region, currency, time_open, time_close, timezone, market_cap, price, change_percent, updated_at):
        self.symbol = symbol
        self.name = name
        self.region = region
        self.currency = currency
        self.open = time_open
        self.close = time_close
        self.timezone = timezone
        self.market_cap = market_cap
        self.price = price
        self.change_percent = change_percent
        self.updated_at = updated_at
        self.next = None

class Pilha:
    #construtor
    def __init__(self):
        self.top = None
        self._size = 0
    

    #insere um elemento na pilha
    def push(self, symbol, name, region, currency, time_open, time_close, timezone, market_cap, price, change_percent, updated_at):
        node = NodePilha(symbol, name, region, currency, time_open, time_close, timezone, market_cap, price, change_percent, updated_at)
        node.next = self.top
        self.top = node
        self._size += 1


   #remove o elemento do topo da pilha
    def pop(self):
        if self._size > 0:
            node = self.top
            self.top = node.next
            node.next = None
            self._size -= 1
            return node
        raise IndexError("a pilha esta vazia")
    
    
    #retorna o topo sem remover
    def peek(self):
        if self._size > 0:
            return self.top.data
        raise IndexError("a pilha esta vazia")

    
    # retorna o tamanha da lista
    def __len__(self):
        return self._size
    
    #representação de como enxergar a pilha 
    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r +str(pointer.name) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

carrinho_temp = Pilha()


#------------------------------------------
""" def adicionar_carrinho_temp(acao):
    carrinho_temp.append(acao)

def remover_carrinho_temp():
    if len(carrinho_temp) > 0:
        carrinho_temp.pop(-1)
 """
# teste_requisicao('ITSA3', '3eafa921')
# Create your views here.
context = {}

def busca(request):
    path = os.path.join(
      '..', 'templates', 'busca.html')
    print(carrinho_temp)

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

            context['acoes'] = request_api(symbolList, 'dc9e7785')
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
                #TODO: alterar..
                carrinho_temp.pop()
                print(carrinho_temp)
                return render(request, path, contextDesfazer)

            else:
            # Caso ele não tenha desfeito, significa que esse POST
            # foi utilizado para adicionar uma ação ao carrinho (Caso 3)
            # temporário, o que é feito a seguir
                contextCarrinho = {}
                contextCarrinho['acoes'] = context['acoes']
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
                '''
                acao = {} 
                acao['market_time'] = {}
                acao['symbol'] = request.POST.get('symbol'),
                acao['name'] = request.POST.get('name'),
                acao['region'] = request.POST.get('region'),
                acao['currency'] = request.POST.get('currency'),
                acao['market_time']['open'] = request.POST.get('open'),
                acao['market_time']['close'] = request.POST.get('close'),
                acao['market_time']['timezone'] = request.POST.get('timezone'),
                acao['market_cap'] = request.POST.get('market_cap'),
                acao['price'] = request.POST.get('price'),
                acao['change_percent'] = request.POST.get('change_percent'),
                acao['updated_at'] = request.POST.get('updated_at'),
                
                print(acao)
                #TODO: alterar...
                carrinho_temp.push(acao)
                '''
                print(carrinho_temp)

                print(contextCarrinho)
                return render(request, path, contextCarrinho)
    else:
        return render(request, path)
# TODO:fazer com que o contextCarrinho seja passado tbm para essa funcao

def redirectcarrinho(request):
    if request.method == 'GET':
        return redirect('/carrinho')



