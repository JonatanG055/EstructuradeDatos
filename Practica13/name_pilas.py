import pilas_colas as pc


pila = pc.Pila()
pila.push_pila(1)
pila.push_pila(2)
pila.push_pila(3)
print ("Pila:",pila.items)
print("elemento retirado",pila.pop_pila())
print("Elemento en el tope:", pila.peek_pila())

cola = pc.Cola()
cola.enqueue_cola(1)
cola.enqueue_cola(2)
cola.enqueue_cola(3)
print ("Cola:",cola.items)
print("elemento retirado",cola.dequeue_cola())
print("Elemento en el tope:", cola.peek_cola())