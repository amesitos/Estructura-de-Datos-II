# NOMBRE: ANDREA VALENTINA CAMPAÑA INTRIAGO
# FECHA: 5 de noviembre de 2024
# Clase 4 - Estructura de Datos II

## LISTA ENLAZADA SIMPLE ##

class Nodo:
    def __init__(self, dato):
        self.dato = dato # dato del nodo
        self.siguiente = None # referencia o puntero de la estructura nodo

class ListaSimple:
    def __init__(self):
        self.primero = None # referencia al primer nodo de la lista
        self.ultimo = None # referencia al ultimo nodo de la lista
        
# Función: ¿contiene datos?
    def estaVacia(self):
        return self.primero == None # si el primer nodo no existe (None), la lista está vacía

# Función: Agregar dato al final de la lista simple
    def agregarUltimo(self, dato):
        if self.estaVacia(): # verificar si la lista está vacía
            self.primero = self.ultimo = Nodo(dato) # si está vacía, el nuevo nodo es el primero y el último
        else:
            auxiliar = self.ultimo # variable auxiliar que tendrá el último nodo
            self.ultimo = auxiliar.siguiente = Nodo(dato) # último (ahora penúltimo) nodo conectado al nuevo nodo mediante la referencia siguiente del penúltimo

# Función: Eliminar dato al final de la lista simple
    def eliminarUltimo(self):
        if self.estaVacia(): # verifica si la lista está vacía antes de eliminar
            print("La lista está vacía.")
            return # culmina la función
        if self.primero == self.ultimo: # si el primer nodo también es el último, es decir, solo tiene un nodo
            self.primero = self.ultimo = None # se le asigna none a ese nodo, eliminandolo y la lista queda vacía
        else:
            auxiliar = self.primero # variable auxiliar que comienza desde el primer nodo 
            while auxiliar.siguiente != self.ultimo: # mientras la referencia siguiente de los nodos que se recorrerán no sea el último nodo
                auxiliar = auxiliar.siguiente # la variable irá yendo por cada referencia siguiente
            auxiliar.siguiente = None # el enlace del ultimo nodo será null
            self.ultimo = auxiliar # el auxiliar ahora es el último nodo

# Función: Agregar dato al inicio de la lista simple
    def agregarInicio(self, dato):
        if self.estaVacia(): # verifica si la lista está vacía
            self.primero = self.ultimo = Nodo(dato) # si está vacía, el nuevo nodo es el primero y el último
        else:
            auxiliar = Nodo(dato) # crear nuevo nodo y se lo almacena en auxiliar
            auxiliar.siguiente = self.primero # la referencia siguiente del nuevo nodo ahora irá al que fue el primer nodo
            self.primero = auxiliar # se actualiza el nodo auxiliar como primero

# Función: Eliminar dato al inicio de la lista simple
    def eliminarInicio(self):
        if self.estaVacia(): # verifica si la lista está vacía
            print("La lista está vacía.")
            return # termina la función
        self.primero = self.primero.siguiente # declarar el siguiente nodo como primero
        if self.primero is None: # si la lista es de un solo nodo y queda vacía
            self.ultimo = None # se declara el nodo como primero y último, dejando el último como vacío

# Función: Eliminar dato de la lista simple mediante índice
    def eliminarPorIndice(self):
        if self.estaVacia(): # verifica si la lista está vacía
            print("La lista está vacía.")
            return # termina la función
        indice = int(input("Ingrese el índice a eliminar de la lista: ")) # ingreso de datos para el índice a eliminar
        if indice == 0: # si el índice es el 0
            self.eliminarInicio() # se llama la función de eliminar nodo inicial
            return # termina la función
        auxiliar = self.primero # variable auxiliar que apunta al primer nodo de la lista
        for i in range(indice -1): # recorrer la lista hasta llegar la nodo anterior que se quiere eliminar
            if auxiliar == None:  # si el indice ingresado no existe en la lista
                print("Error. Índice fuera de rango.")
                return # termina la función
            auxiliar = auxiliar.siguiente # mueve auxiliar al siguiente nodo de la lista
            
        if auxiliar.siguiente == None: # si el indice está fuera de rango
            print("Error. Índice fuera de rango.")
            return
        
         # actualiza el enlace siguiente del nodo en auxiliar para que salte el nodo que se desea eliminar
         # el nodo siguiente al auxiliar (nodo que queremos eliminar) es omitido, apuntando en su lugar al nodo después de él
        auxiliar.siguiente = auxiliar.siguiente.siguiente # se desconecta el nodo que se desea eliminar de la lista

        if auxiliar.siguiente is None: # si el nodo eliminado era el último de la lista
            self.ultimo = auxiliar # ahora self ultimo apunta auxiliar que es el nuevo último nodo de la lista
        print(f"Nodo en índice {indice} eliminado.")

# Función: Recorrer lista simple
    def recorrerLista(self):
        auxiliar = self.primero # variable auxiliar para recorrer la lista
        if auxiliar is None: # si la lista está vacía
            print("La lista está vacía.")
            return # termina la función
        print("Lista: ")
        while auxiliar: # mientras haya nodos en la lista
            print(f"{auxiliar.dato} -> ", end="") # imprime cada dato de los nodos de la lista
            auxiliar = auxiliar.siguiente # irá yendo de nodo a nodo
        print("None") # fin de la lista 


if __name__ == "__main__":
    lista = ListaSimple()
    opcion = 0

    while opcion != 8:
        print("\n---Lista simple enlazada---\n1. ¿Está vacía la lista?\n2. Agregar último nodo.\n3. Eliminar último nodo.\n4. Agregar nodo inicial.\n5. Eliminar nodo inicial.\n6. Eliminar dato por índice.\n7. Mostrar la lista.\n8. Salir\n")
        
        try:
            opcion = int(input("Ingrese una opción: "))

            if opcion == 1:
                print("Sí, la lista está vacía.\n" if lista.estaVacia() else "No, la lista contiene datos.\n")

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
                try:
                    lista.eliminarPorIndice()
                    lista.recorrerLista()
                except ValueError:
                    print("Error: el índice debe ser un número entero.")

            elif opcion == 7:
                lista.recorrerLista()

            elif opcion == 8:
                print("Gracias por usar el programa.")
                break

            else:
                print("Opción inválida.\n")

        except ValueError:
            print("Error: por favor, ingrese un número entero válido para la opción.")
