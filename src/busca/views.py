from django.shortcuts import render
from sys import argv
import csv
from django.http import HttpResponse

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
        pointer = self.head
        while(pointer):
            if palavra.lower() in pointer.name.lower():
                print(pointer.key)
            pointer = pointer.next


# Retornará o índice em que a palavra deve ser colocada dentro da hashtable
def get_key(palavra):
    return ord(palavra[0].lower()) - 97

# Inicia os valores da lista com o objeto LinkedList
def hash_init():
    for i in range(23):
        hash_table.append(LinkedList())

# Lista os itens no arquivo csv
def get_stock():
    with open('static/csv/acoes_api.csv') as entrada:
        acoes = list(csv.reader(entrada))
    return acoes


# Carrega a hash table
def load_hash(acoes):
    row = 0
    for i in acoes:
        key = get_key(acoes[row][0])
        hash_table[key].append(acoes[row][0], acoes[row][1])
        row += 1 
        
# Create your views here.
def busca(request):
    acoes = get_stock()
    hash_init()
    load_hash(acoes)
    # print(hash_table[21])
    
    return render(request,'busca.html')
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