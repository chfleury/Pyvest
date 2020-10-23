from django.shortcuts import render, redirect
from sys import argv
import csv
from django.http import HttpResponse
import requests 
import json 

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
  # blz
    listaDados = []
    for i in symbolList:
        url = f'https://api.hgbrasil.com/finance/stock_price?key={key}&symbol={i}'

        print(url)
        dados = requests.get(url)
        listaDados.append(dados)
        print(dados.text)
        test = json.loads(dados.text)
        price = test['results'][i]['market_cap']
        print(price)
        print('-----------------------')
    return listaDados

# teste_requisicao('ITSA3', '3eafa921')
# Create your views here.
def busca(request):
    if request.method == 'POST':
        busca = request.POST['busca']
        # ta igual eu acho
        print(busca)
        print('1')
        acoes = get_stock()
        print('2')
        hash_init()
        print('3')
        load_hash(acoes) 
        print('4')

        key = get_key(busca)
        print('5')

        if key > 22:
            print("Nenhum valor com esta letra.")
            exit()  
        print('6')
        symbolList = hash_table[key].search(busca)

        request_api(symbolList, '3eafa921')
        
        return redirect('/busca')
    else:
        return render(request, '../templates/busca.html')
 
    
    # return render(request,'busca.html')
    """  context = [acoes] """
    '''
    return HttpResponse(hash_table)
    '''

""" 
if __name__ == "__main__":
    acoes = get_stock()
    hash_init()
    load_hash(acoes) 
    pesquisa = input("Digite o nome a ser pesquisado: ") 
    key = get_key(pesquisa)
    if key > 22:
        print("Nenhum valor com esta letra.")
        exit()  
    hash_table[key].search(pesquisa)  """