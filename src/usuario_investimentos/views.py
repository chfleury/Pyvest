from django.shortcuts import render

# criar um botão para cada investimento com o código e o nome de cada um
# usar a API pra pegar o dado do dia daquele investimento

class Node_Investimentos:
    #construtor
    def __init__(self, symbol, name):
        "constructor to initiate this object"
        
        # guarda os dados
        self.symbol = symbol
        self.name = name

        # guarda a referência (next item)
        self.next = None

class Linked_List_Investimentos:
    #construtor
    def __init__(self):
        self.head = None
        self.tail = None

    def output_list(self):
        "outputs the list (the value of the node, actually)"
        current_node = self.head
        
        while current_node is not None:
            print(current_node.symbol)
            
            # jump to the linked node
            current_node = current_node.next
            
        return current_node


def meus_investimentos(request):

    






    return render(request, 'investimentos_do_usuario.html', {})