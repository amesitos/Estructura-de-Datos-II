class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        
class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        
    def estaVacia(self):
        if self.cabeza == None:
            return True
       
    def insertarInicio(self, dato):
        nuevoNodo = Nodo(dato)
        if self.cabeza:
            self.cabeza.siguiente = nuevoNodo
            self.cabeza = nuevoNodo 
        else:
            self.cabeza = self.cola = nuevoNodo
        
    def insertarFinal(self, dato):
        nuevoNodo = Nodo(dato)
        if self.cabeza:
            self.cola.siguiente = nuevoNodo
            self.cola = nuevoNodo
        else:
            self.cabeza = self.cola = nuevoNodo
       
    def buscarDato(self, dato):
        if self.estaVacia():
            return "La lista está vacía."
        else:
            actualNodo = self.cabeza
            while actualNodo:
                if actualNodo.dato == dato:
                    return True
                else:
                    actualNodo = actualNodo.siguiente
            return False