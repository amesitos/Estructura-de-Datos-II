class Nodo:
    def __init__(self, dato: str): # se impone el dato de tipo string
        super().__init__()
        self.dato: str = dato  # dato del nodo
        self.siguiente: Nodo = None # puntero al siguiente nodo, inicialmente null
        self.anterior: Nodo = None  # puntero al nodo anterior, inicialmente null

class ListaPorDescubrir3:
    def __init__(self):
        # inicializa una lista doblemente enlazada con la cabeza como null
        self.cabeza: Nodo = None  # apunta al primer nodo de la lista, inicialmente null

    def agregarDato(self, dato: str):
        nuevoNodo = Nodo(dato)
        if self.cabeza is None:
            nuevoNodo.siguiente = nuevoNodo
            nuevoNodo.anterior = nuevoNodo
            self.cabeza = nuevoNodo
        else:
            ultimo = self.cabeza.anterior  # Encuentra el último nodo
            ultimo.siguiente = nuevoNodo
            nuevoNodo.anterior = ultimo
            nuevoNodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevoNodo

if __name__ == "__main__":  
    lista = ListaPorDescubrir3()  

    lista.agregarDato("k")
    lista.agregarDato("y")
    lista.agregarDato("m")
    lista.agregarDato("a")
    lista.agregarDato("n")
    lista.agregarDato("c")
    lista.agregarDato("a")
    lista.agregarDato("n")
    lista.agregarDato("o")
    lista.agregarDato("n")

    auxiliar = lista.cabeza  # comienza desde la cabeza de la lista
    contador = 0
    while contador < 10:           
        print(str(contador), " ", auxiliar.dato)  # imprime el índice y el dato del nodo actual
        auxiliar = auxiliar.anterior  # retrocede al nodo anterior
        contador += 1