# NOMBRE: ANDREA VALENTINA CAMPAÑA INTRIAGO
# FECHA: 29 de octubre de 2024
# Clase 3 - Estructura de Datos II

## LISTA CIRCULAR DOBLEMENTE ENLAZADA ##

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
        nuevoNodo = Nodo(dato)  # nuevo nodo con el dato dado
        auxiliar = self.cabeza  # variable auxiliar que apunta a la cabeza de la lista
        
        if auxiliar is None:
            # Si la lista está vacía, el nuevo nodo se conecta consigo mismo
            nuevoNodo.siguiente = nuevoNodo # se auto-apunta como siguiente
            nuevoNodo.anterior = nuevoNodo  # se auto-apunta como anterior
            self.cabeza = nuevoNodo   # el nuevo nodo se convierte en la cabeza de la lista
            return
        
        # inserción en una lista circular no vacía
        auxiliar = auxiliar.siguiente  # obtiene el nodo siguiente desde la cabeza
        auxiliar.anterior = nuevoNodo  # el nodo siguiente a la cabeza apunta al nuevo nodo como anterior
        nuevoNodo.anterior = auxiliar  # el nuevo nodo apunta al auxiliar como su anterior
        nuevoNodo.siguiente = self.cabeza  # el nuevo nodo apunta a la cabeza como su siguiente
        self.cabeza.anterior = nuevoNodo  # la cabeza apunta al nuevo nodo como su anterior

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
