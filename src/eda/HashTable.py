class Node:
    def __init__(self, name, key):
        self.name = name
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        

    def append(self, word, key):
        if self.head:
            pointer = Node(word, key)
            pointer.next = self.head
            self.head = pointer
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

# é so isso manos, ai importa ela, comenta a outra lá e vê se dá bom