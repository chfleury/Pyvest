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
        # esse price ja ta no test a gente ja manda ele pra listaDados pode
        # price = test['results'][i]['market_cap']
        listaDados.append(test['results'][i])
        print(listaDados)
        print('-----------------------')
    return listaDados


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

acoesSession = []
class Pilha:
    #construtor
    def __init__(self):
        self.top = None
        self._size = 0
    
    
    #insere um elemento na pilha
    def push(self, request, symbol, name, region, currency, time_open, time_close, timezone, market_cap, price, change_percent, updated_at):
        node = NodePilha(symbol, name, region, currency, time_open, time_close, timezone, market_cap, price, change_percent, updated_at)
        node.next = self.top
        self.top = node
        self._size += 1
        
        # a gente 
        acoesSession.append({
            'symbol': node.symbol,
            'name' : node.name,
            'region' : node.region,
            'currency' : node.currency,
            'time_open' : node.open,
            'time_close' : node.close,
            'timezone' : node.timezone,
            'market_cap' : node.market_cap,
            'price' : node.price,
            'change_percent' : node.change_percent,
            'updated_at' : node.updated_at})
        
        # acoesSession[-1]['symbol'] = node.symbol
        # acoesSession[-1]['name'] = node.name
        # acoesSession[-1]['region'] = node.region
        # acoesSession[-1]['currency'] = node.currency
        # acoesSession[-1]['time_open'] = node.open
        # acoesSession[-1]['time_close'] = node.close
        # acoesSession[-1]['timezone'] = node.timezone
        # acoesSession[-1]['market_cap'] = node.market_cap
        # acoesSession[-1]['price'] = node.price
        # acoesSession[-1]['change_percent'] = node.change_percent
        # acoesSession[-1]['updated_at'] = node.updated_at
        
        request.session['acoes'] = acoesSession
        # for attr, value in node.__dict__.items():
        #     acoesSession[-1][attr] = value

        # too pensando
        # agr tem q ver se ta la mesmo armazenado
        # acoesSession.append(json.dumps(node))
        # la na parte da busca

        # request.session['acoes'] = acoesSession
        request.session['testes'] = [{'teste1': 14}, {'teste':12}]
        #pera ai vou ver no site como e q esqueci ss
        # nao da pra botar nosso node direto na session parece
        # tem que ser uma lista de dicionarios
        #sei nem o q é isso,
        # na hora de inserir o node na session
    
   #remove o elemento do topo da pilha
    def pop(self, request):
        if self._size > 0:
            node = self.top
            self.top = node.next
            node.next = None
            self._size -= 1
            # roda ai gayzao
            acoesSession.pop()
            request.session['acoes'] = acoesSession

            return node
        #bora tentar so o push primeiro
        
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

context = {}

def busca(request):
    try:
        # ta funcionando
        # 

        print('---------------------')
        print(request.session['acoes'])
        print('---------------------')

    except:
        print('erro')
    #botei pra printar  bora rodar agr

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

            context['acoes'] = request_api(symbolList, '34a625c3')
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
                carrinho_temp.pop(request)
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
                    request,
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

                #print(contextCarrinho)
                return render(request, path, contextCarrinho)
    else:
        return render(request, path)
# TODO:fazer com que o contextCarrinho seja passado tbm para essa funcao

def redirectcarrinho(request):
    if request.method == 'GET':
        return redirect('/carrinho')



