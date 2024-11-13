# NOMBRE: ANDREA VALENTINA CAMPAÑA INTRIAGO
# FECHA: 29 de octubre de 2024
# Clase 3 - Estructura de Datos II

## LISTA ENLAZADA SIMPLE ##

class Nodo:
    def __init__(self, dato):
        self.dato = dato # dato del nodo
        self.siguiente = None # referencia o puntero de la estructura nodo

class ListaPorDescubrir:
    def __init__(self):
        self.primero = None # referencia al primer nodo de la lista
        self.ultimo = None # referencia al ultimo nodo de la lista

    def estaVacia(self):
        return self.primero == None # si el primer nodo no existe (None), la lista está vacía

    def agregarUltimo(self, dato):
        if self.estaVacia(): # verificar si está vacía
            self.primero = self.ultimo = Nodo(dato) # si está vacía, el nuevo nodo es el primero y el último
        else:
            auxiliar = self.ultimo # variable auxiliar es el actual último nodo
            self.ultimo = auxiliar.siguiente = Nodo(dato) # último (ahora penúltimo) nodo conectado al nuevo nodo mediante la referencia siguiente del penúltimo

    def eliminarUltimo(self):
        if self.estaVacia():
            print("La lista está vacía.")
            return
        if self.primero == self.ultimo: # si el primer nodo también es el último
            self.primero = self.ultimo = None # se le asigna none a ese nodo, eliminandolo y la lista queda vacía
        else:
            auxiliar = self.primero # variable auxiliar que comienza desde el primer nodo 
            while auxiliar.siguiente != self.ultimo: # mientras la referencia siguiente del primer nodo no sea el último nodo
                auxiliar = auxiliar.siguiente # recorre hasta el pen
            auxiliar.siguiente = None # elimina el enlace al último nodo
            self.ultimo = auxiliar # actualiza el ultimo

    def agregarInicio(self, dato):
        if self.estaVacia():
            self.primero = self.ultimo = Nodo(dato) # si está vacía, el nuevo nodo es el primero y el último
        else:
            auxiliar = Nodo(dato) # crear nuevo nodo
            auxiliar.siguiente = self.primero # enlazar el nuevo nodo al primer nodo actual
            self.primero = auxiliar # actualizar primero

    def eliminarInicio(self):
        if self.estaVacia():
            print("La lista está vacía.")
            return
        self.primero = self.primero.siguiente # darle el primero al siguiente nodo
        if self.primero is None: # si la lista queda vacía
            self.ultimo = None # el último se actualiza también

    def recorrerLista(self):
        auxiliar = self.primero # variable auxiliar para recorrer la lista
        if auxiliar is None: # si está vacía
            print("La lista está vacía.")
            return
        print("Lista: ")
        while auxiliar:
            print(f"{auxiliar.dato} -> ", end="") # imprime cada dato de los nodos de la lista
            auxiliar = auxiliar.siguiente
        print("None") # fin de la lista 


if __name__ == "__main__":
    lista = ListaPorDescubrir()
    opcion = 0

    while opcion != 7:
        print("\n---Lista por descubrir 1---\n1. ¿Está vacía la lista?\n2. Agregar último nodo.\n3. Eliminar último nodo.\n4. Agregar nodo inicial.\n5. Eliminar nodo inicial.\n6. Mostrar la lista.\n7. Salir\n")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            print("Sí, la lista está vacía\n" if lista.estaVacia() else "No, la lista contiene datos.\n")

        elif opcion == 2:
            dato = int(input("Ingrese un dato para agregarlo al último: "))
            lista.agregarUltimo(dato)
            lista.recorrerLista()

        elif opcion == 3:
            lista.eliminarUltimo()
            lista.recorrerLista()

        elif opcion == 4:
            dato = int(input("Ingrese un dato para agregarlo al inicio: "))
            lista.agregarInicio(dato)
            lista.recorrerLista()

        elif opcion == 5:
            lista.eliminarInicio()
            lista.recorrerLista()

        elif opcion == 6:
            lista.recorrerLista()

        elif opcion == 7:
            print("Gracias por usar el programa.")
            break

        else:
            print("Opción inválida.\n")
