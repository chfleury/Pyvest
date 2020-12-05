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
    
    
    # Insere um elemento na pilha
    # O(1)
    # Adicionado no início da pilha
    def push(self, symbol, name, region, currency, time_open, time_close, timezone, market_cap, price, change_percent, updated_at):
        node = NodePilha(symbol, name, region, currency, time_open, time_close, timezone, market_cap, price, change_percent, updated_at)
        node.next = self.top
        self.top = node
        self._size += 1
    # O(N)
    def listar(self):
        lista = []
        if self.top:
            pointer = self.top
            while(pointer):
                lista.insert(0, {
                'symbol': pointer.symbol,
                'name' : pointer.name,
                'region' : pointer.region,
                'currency' : pointer.currency,
                'time_open' : pointer.open,
                'time_close' : pointer.close,
                'timezone' : pointer.timezone,
                'market_cap' : pointer.market_cap,
                'price' : pointer.price,
                'change_percent' : pointer.change_percent,
                'updated_at' : pointer.updated_at})
                pointer = pointer.next
            return lista
        return []

   #remove o elemento do topo da pilha
    # O(1)

    def pop(self):
        if self.top:
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

