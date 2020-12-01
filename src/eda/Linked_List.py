class Node_Investimentos:
    #construtor
    def __init__(self, symbol, name, price, idAcao):
        # guarda os dados
        self.symbol = symbol
        self.name = name
        self.price = price
        self.idAcao = idAcao
        # guarda a referência (next item)
        self.next = None

class Linked_List_Investimentos:
    #construtor
    def __init__(self):
        self.head = None
        self.tail = None

    def output_list(self):
        current_node = self.head
        
        while current_node is not None:
            print(current_node.symbol)
            
            # jump to the linked node
            current_node = current_node.next
            
        return current_node
    
    # O(N)
    # Adicionado ao final da lista
    def append(self, symbol, name, price, idAcao):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node_Investimentos(symbol, name, price, idAcao)
        else:
            self.head = Node_Investimentos(symbol, name, price, idAcao)
    
    def pop_search(self, name):
        pointer = self.head
        while(pointer.name != name): 
            q = pointer
            pointer = pointer.next
        q.next = pointer.next
        pointer.next = None
        
        # 1 2 3
        # |---|

    # O(N)
    def load_context(self):
        pointer = self.head
        context = []
        while(pointer):
            context.append({
                    'name' : pointer.name, 
                    'symbol': pointer.symbol,
                    'price': pointer.price,
                    'id': pointer.idAcao
                    })
            pointer = pointer.next
        return context


    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.name) + "----" + str(pointer.idAcao) + "->"
            pointer = pointer.next
        r = r + "None"
        return r
        
     
    def __str__(self):
        return self.__repr__()
            