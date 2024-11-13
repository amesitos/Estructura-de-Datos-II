
# CREAR CLASE NODO 
class Nodo:
    def __init__(self, dato):
        self.dato = dato # dato que almacena el nodo
        self.siguiente = None # referencia al nodo siguiente de la lista
        self.anterior = None # referencia al nodo anterior de la lista

# CONSTRUCTOR DE LA CLASE
class ListaDoble:
    def __init__(self):
        self.head = None # inicio de la lista comienza vacío

# Agregar un nodo al final de la lista
    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato) # creación de nuevo nodo con su dato
        if not self.head: # si la lista está vacía
            self.head = nuevo_nodo # se asigna el nuevo nodo a la cabeza
            return # devuelve el valor de la función si se cumple la condicional
        ultimo = self.head # empezar con la cabeza
        while ultimo.siguiente: # ciclo while para recorrer la lista hasta el último
            ultimo = ultimo.siguiente 
        ultimo.siguiente = nuevo_nodo # el último nodo apunta al nuevo nodo 
        nuevo_nodo.anterior = ultimo # el nuevo nodo apunta al nodo anterior
    
# Mostrar los nodos de la lista en orden
    def mostrar(self):
        nodo_actual = self.head # comenzar desde la cabeza
        while nodo_actual: # recorrer la lista hasta el final
            print(nodo_actual.dato, end=' <=> ') # imprime el dato del nodo actual
            nodo_actual = nodo_actual.siguiente
        print('None') # indicar el final de la lista

# Mostrar los nodos de la lista en orden inverso
    def mostrar_invertido(self):
        nodo_actual = self.head # empezar en la cabeza
        if not nodo_actual: # si la lista está vacía
            return # la función termina
        while nodo_actual.siguiente: # se recorre la lista hasta el último nodo
            nodo_actual = nodo_actual.siguiente 
        while nodo_actual: # recorrer la lista de forma inversa
            print(nodo_actual.dato, end=' <=> ') # mostrar el nodo actual
            nodo_actual = nodo_actual.anterior # retroceder al nodo anterior
        print('None') # indicar el final de la lista

# Agregar un nodo al inicio de la lista
    def agregar_al_inicio(self, dato): 
        nuevo_nodo = Nodo(dato) # crear nuevo nodo
        if not self.head: # si la lista está vacía
            self.head = nuevo_nodo # se asigna el nuevo nodo a la cabeza
            return # se culmina la función
        nuevo_nodo.siguiente = self.head # el nuevo nodo apunta a la cabeza
        self.head.anterior = nuevo_nodo # el anterior nodo apunta al nuevo nodo
        self.head = nuevo_nodo # el nuevo nodo ahora es la cabeza

    # Eliminar un nodo de la lista que contenga un dato específico
    def eliminar_nodo(self, dato):
        nodo_actual = self.head          # Empezamos desde la cabeza
        while nodo_actual:               # Recorremos la lista
            if nodo_actual.dato == dato:  # Si encontramos el nodo con el dato buscado
                if nodo_actual.anterior:  # Si no es el primer nodo
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente  # Enlazamos el nodo anterior con el siguiente
                if nodo_actual.siguiente:  # Si no es el último nodo
                    nodo_actual.siguiente.anterior = nodo_actual.anterior  # Enlazamos el nodo siguiente con el anterior
                if nodo_actual == self.head:  # Si es el nodo cabeza
                    self.head = nodo_actual.siguiente  # Actualizamos la cabeza de la lista
                return  # Salimos después de eliminar el nodo
            nodo_actual = nodo_actual.siguiente  # Avanzamos al siguiente nodo

    # Método para buscar un nodo por su dato
    def buscar(self, dato):
        nodo_actual = self.head           # Empezamos desde la cabeza
        while nodo_actual:                # Recorremos la lista
            if nodo_actual.dato == dato:  # Si encontramos el nodo con el dato buscado
                return nodo_actual        # Retornamos el nodo encontrado
            nodo_actual = nodo_actual.siguiente  # Avanzamos al siguiente nodo
        return None                       # Si no se encuentra, retornamos None

    # Método para contar la cantidad de nodos en la lista
    def contar_nodos(self):
        contador = 0                      # Inicializamos el contador en 0
        nodo_actual = self.head           # Comenzamos desde la cabeza
        while nodo_actual:                # Recorremos la lista
            contador += 1                 # Incrementamos el contador por cada nodo
            nodo_actual = nodo_actual.siguiente  # Avanzamos al siguiente nodo
        return contador                   # Retornamos el número total de nodos

    # Método para insertar un nodo después de un nodo existente
    def insertar_despues(self, nodo_existente, dato):
        if not nodo_existente:            # Verificamos que el nodo existente no sea None
            print("El nodo existente no puede ser None.")
            return
        nuevo_nodo = Nodo(dato)           # Creamos un nuevo nodo
        nuevo_nodo.siguiente = nodo_existente.siguiente  # El nuevo nodo apunta al siguiente del nodo existente
        nodo_existente.siguiente = nuevo_nodo            # El nodo existente apunta al nuevo nodo
        nuevo_nodo.anterior = nodo_existente             # El nuevo nodo apunta al nodo existente como anterior
        if nuevo_nodo.siguiente:         # Si el nuevo nodo no es el último
            nuevo_nodo.siguiente.anterior = nuevo_nodo   # El nodo siguiente al nuevo nodo lo reconoce como su anterior

    # Método para eliminar el último nodo de la lista
    def eliminar_ultimo(self):
        if not self.head:                # Si la lista está vacía, no hacemos nada
            return
        nodo_actual = self.head          # Comenzamos desde la cabeza
        while nodo_actual.siguiente:     # Recorremos hasta el último nodo
            nodo_actual = nodo_actual.siguiente
        if nodo_actual.anterior:         # Si no es el único nodo
            nodo_actual.anterior.siguiente = None  # Eliminamos la referencia al último nodo
        else:
            self.head = None  # Si solo había un nodo, la lista queda vacía

    # Método para buscar un nodo por su índice en la lista
    def buscar_por_indice(self, indice):
        if indice < 0:                   # Si el índice es negativo, retornamos None
            return None
        nodo_actual = self.head           # Comenzamos desde la cabeza
        for i in range(indice):           # Recorremos la lista hasta el índice deseado
            if nodo_actual is None:
                return None               # Si llegamos al final antes del índice, retornamos None
            nodo_actual = nodo_actual.siguiente
        return nodo_actual                # Retornamos el nodo en la posición deseada

    # Método para eliminar un nodo por su índice
    def eliminar_por_indice(self, indice):
        if indice < 0:                    # Si el índice es negativo, no hacemos nada
            return
        nodo_a_eliminar = self.buscar_por_indice(indice)  # Buscamos el nodo por índice
        if nodo_a_eliminar:
            if nodo_a_eliminar.anterior:  # Si no es el primer nodo
                nodo_a_eliminar.anterior.siguiente = nodo_a_eliminar.siguiente
            if nodo_a_eliminar.siguiente: # Si no es el último nodo
                nodo_a_eliminar.siguiente.anterior = nodo_a_eliminar.anterior
            if nodo_a_eliminar == self.head:  # Si es el nodo cabeza
                self.head = nodo_a_eliminar.siguiente  # Actualizamos la cabeza

    # Método para modificar el dato de un nodo por su índice
    def modificar_por_indice(self, indice, nuevo_dato):
        nodo_a_modificar = self.buscar_por_indice(indice)  # Buscamos el nodo por índice
        if nodo_a_modificar:
            nodo_a_modificar.dato = nuevo_dato  # Modificamos el dato del nodo

# Ejemplo de uso
lista = ListaDoble()
lista.agregar_al_final(1)
lista.agregar_al_final(2)
lista.agregar_al_final(3)

print("Lista normal:")
lista.mostrar()

print("Lista invertida:")
lista.mostrar_invertido()

# Agregar al inicio
lista.agregar_al_inicio(0)
print("Lista después de agregar 0 al inicio:")
lista.mostrar()

# Eliminar un nodo
lista.eliminar_nodo(2)
print("Lista después de eliminar el nodo con valor 2:")
lista.mostrar()

# Buscar un nodo
nodo_buscado = lista.buscar(3)
if nodo_buscado:
    print(f"Nodo encontrado: {nodo_buscado.dato}")
else:
    print("Nodo no encontrado.")

# Contar nodos
cantidad_nodos = lista.contar_nodos()
print(f"Número de nodos en la lista: {cantidad_nodos}")

# Insertar después de un nodo existente
nodo_existente = lista.buscar(1)
lista.insertar_despues(nodo_existente, 1.5)
print("Lista después de insertar 1.5 después de 1:")
lista.mostrar()

# Eliminar el último nodo
lista.eliminar_ultimo()
print("Lista después de eliminar el último nodo:")
lista.mostrar()

# Buscar por índice
indice = 1
nodo_por_indice = lista.buscar_por_indice(indice)
if nodo_por_indice:
    print(f"Nodo en índice {indice}: {nodo_por_indice.dato}")
else:
    print(f"No hay nodo en el índice {indice}.")

# Eliminar por índice
lista.eliminar_por_indice(0)
print("Lista después de eliminar el nodo en índice 0:")
lista.mostrar()

# Modificar por índice
lista.modificar_por_indice(1, 5)
print("Lista después de modificar el nodo en índice 1 a 5:")
lista.mostrar()
