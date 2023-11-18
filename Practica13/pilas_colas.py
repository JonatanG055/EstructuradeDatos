class Pila:
    def  __init__(self):
        self.items=[]

    def IsEmpty_Pila(self):
        return  len(self.items)==0

    def push_pila(self,elemento):
        self.items.append(elemento)
    def pop_pila(self):
        if not self.IsEmpty_Pila():
            return self.items.pop()
        return None
    def peek_pila(self):
        if not self.IsEmpty_Pila():
            return self.items[-1]
        return None

class Cola:
    def __init__(self):
        
        self.items=[]

    def IsEmpty_cola(self):
        return len (self.items)==0

    def enqueue_cola(self,elemento):
        self.items.append(elemento)

    def dequeue_cola(self):
        if not self.IsEmpty_cola():
            return self.items.pop(0)
        return None

    def peek_cola(self):
        if not self.IsEmpty_cola():
            return self.items[0]
        return None