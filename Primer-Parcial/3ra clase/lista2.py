# NOMBRE: ANDREA VALENTINA CAMPAÑA INTRIAGO
# FECHA: 29 de octubre de 2024
# Clase 3 - Estructura de Datos II

## LISTA DOBLEMENTE ENLAZADA ##

class Nodo:
    def __init__(self, dato):
        self.dato = dato # almacena el dato del nodo
        self.siguiente = None # referencia o puntero al nodo siguiente
        self.anterior = None # referencia o puntero al nodo anterior

class ListaPorDescubrir2:
    def __init__(self):
        self.primero = None # referencia al primer nodo de la lista
        self.ultimo = None # referencia al ultimo nodo de la lista
        self.tamanio = 0 # nodos de la lista

    def estaVacia(self):
        return self.primero == None # si el primer nodo no existe, la lista está vacía

    def agregarFinal(self, dato):
        if self.estaVacia():
            self.primero = self.ultimo = Nodo(dato) # si está vacía, el nuevo nodo es el primero y el último
        else:
            auxiliar = Nodo(dato) # crea un nuevo nodo con el dato proporcionado
            auxiliar.anterior = self.ultimo # el nuevo nodo apunta al actual último nodo como anterior
            self.ultimo.siguiente = auxiliar # el actual último nodo apunta al nuevo nodo como siguiente
            self.ultimo = auxiliar # el nuevo nodo se convierte en el último nodo de la lista
        self.tamanio += 1 # crece el tamaño de la lista
        
    def eliminarFinal(self):
        if self.estaVacia():
            print("La lista está vacía.")
        elif self.primero.siguiente is None: # si solo hay un nodo en la lista
            self.primero = self.ultimo = None # elimina el nodo, dejando la lista vacía
            self.tamanio = 0 # el tamaño de la lista se vuelve 0 
        else: # si hay más de un nodo
            self.ultimo = self.ultimo.anterior # el penultimo nodo se convierte en el ultimo
            self.ultimo.siguiente = None # el nuevo ultimo nodo no tiene nodo siguiente
            self.tamanio -= 1 # decrece el tamaño de la lista

    def agregarInicio(self, dato):
        if self.estaVacia():
            self.primero = self.ultimo = Nodo(dato) # si está vacía, el nuevo nodo es el primero y el último
        else:
            auxiliar = Nodo(dato) # crea un nuevo nodo con el dato proporcionado
            auxiliar.siguiente = self.primero # el nuevo nodo apunta al actual primer nodo como siguiente
            self.primero.anterior = auxiliar # el actual primer nodo apunta al nuevo nodo como anterior
            self.primero = auxiliar # el nuevo nodo se convierte en el primer nodo de la lista
        self.tamanio += 1 # crece el tamaño de la lista

    def eliminarInicio(self):
        if self.estaVacia():
            print("La lista está vacía.")
        elif self.primero.siguiente is None: # si solo hay un nodo en la lista
            self.primero = self.ultimo = None # elimina el nodo, dejando la lista vacía
            self.tamanio = 0 # el tamaño de la lista se vuelve 0 
        else: # si hay más de un nodo
            self.primero = self.primero.siguiente # el segundo nodo se convierte en el primero
            self.primero.anterior = None # el nuevo primer nodo no tiene nodo anterior
            self.tamanio -= 1 # decrece el tamaño de la lista

    def recorrerInicio(self):
        auxiliar = self.primero # variable que inicia en el primer nodo
        if auxiliar is None: # si no hay primer nodo
            print("La lista está vacía.") # la lista está vacía
            return
        print("Lista desde el inicio:")
        while auxiliar is not None: # recorre cada nodo hasta llegar al final
            print(f"{auxiliar.dato} <-> ", end="") # imprime cada dato del nodo
            auxiliar = auxiliar.siguiente # avanza a cada nodo
        print("None") # fin de la lista

    def recorridoFinal(self):
        auxiliar = self.ultimo # variable que inicia en el último nodo
        if auxiliar is None: # si no hay primer o último nodo
            print("La lista está vacía.")
            return
        print("Lista desde el final:")
        while auxiliar is not None: # recorre cada nodo hasta llegar al inicio
            print(f"{auxiliar.dato} <-> ", end="") # imprime cada dato del nodo
            auxiliar = auxiliar.anterior # avanza a cada nodo
        print("None") # fin de la lista


if __name__ == "__main__":
    lista = ListaPorDescubrir2()
    opcion = 0

    while True:
        try:
            while opcion != 8:
                print("\n---Lista por descubrir 2---\n1. ¿Está vacía la lista?\n2. Agregar último nodo.\n3. Eliminar último nodo.\n4. Agregar nodo inicial.\n5. Eliminar nodo inicial.\n6. Mostrar la lista desde el inicio.\n7. Mostrar la lista desde el final.\n8. Salir.")
                opcion = int(input("Ingrese una opción: "))

                if opcion == 1:
                    print("Sí, la lista está vacía.\n" if lista.estaVacia() else "No, la lista contiene datos.\n")

                elif opcion == 2:
                    dato = int(input("Ingrese un dato para agregar al final: "))
                    lista.agregarFinal(dato)
                    lista.recorrerInicio()

                elif opcion == 3:
                    lista.eliminarFinal()
                    lista.recorrerInicio()

                elif opcion == 4:
                    dato = int(input("Ingrese un dato para agregar al inicio: "))
                    lista.agregarInicio(dato)
                    lista.recorrerInicio()

                elif opcion == 5:
                    lista.eliminarInicio()
                    lista.recorrerInicio()

                elif opcion == 6:
                    lista.recorrerInicio()
                
                elif opcion == 7:
                    lista.recorridoFinal()

                elif opcion == 8:
                    print("Gracias por usar el programa.")
                    break

                else:
                    print("Opción inválida.\n")
            break
        except Exception as e:
            print(f"Error: {e}")
