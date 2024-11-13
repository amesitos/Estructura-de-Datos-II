# NOMBRE: ANDREA VALENTINA CAMPAÑA INTRIAGO
# FECHA: 22 de octubre de 2024
# Clase 2 - Estructura de Datos II

class Pila: # clase PiLa

  def __init__(self, tamanio):
    self.lista = [] # lista vacía para los datos de la pila
    self.tope = 0 # cantidad de elementos actuales de la pila
    self.tamanio = tamanio # tamaño máximo de la pila

# Función: Agregar datos
  def agregarDatos (self, dato): # parámetro de dato
    if self.tope < self.tamanio: # si la cantidad de datos es menor al tamaño actual
      self.lista += [dato] # solo se agrega a la pila el dato (.append)
      self.tope+=1
    else: # si el tope sobrepasa el tamaño definido
      self.tamanio+=5 # se le da 5 espacios nuevos al tamaño dinámicamente
      self.lista += [dato] # el dato se almacena en la pila
      self.tope+=1 # contador que incrementa a 1 la cantidad de datos

# Función: Eliminar dato
  def eliminarDato(self):
    if self.estaVacia(): # si la cantidad de datos de la pila es 0
        print("No se puede eliminar un dato porque la lista está vacía.") # mensaje
    else: # si el tope es distinto a 0
        print(f"Dato eliminado: {self.lista.pop()}") # se saca un elemento de la pila
        self.tope -= 1  # el tope resta a 1 porque hay un dato menos
        print(f"La pila actual es: {[self.lista[i] for i in range(self.tope)]}") # recorre los datos de la pila mediante el índice

# Función: ¿hay elementos?
  def estaVacia (self):
    if self.tope == 0: # si la cantidad de elementos es 0
      return True # retorna verdadero
    else:
      return False # retorna falso

# Función: Mostrar lista con índice
  def mostrarPilaConIndice(self):
    if self.estaVacia(): # uso del método estaVacia
       print("La pila está vacía.") # si es True, entonces imprime 
    else: # si la pila no está vacía
        auxiliar = self.tope -1 # variable auxiliar que empieza desde el tope de la pila
        while auxiliar > -1: # recorre desde el tope hasta el fondo
            print(f"[{auxiliar}] => {self.lista[auxiliar]}") # imprime los índices y su dato 
            auxiliar -=1 # decrementa el índice auxiliar para moverse hacia abajo en la pila

# Función: Mostrar lista sin índices
  def mostrarPila(self):
    if self.estaVacia(): # verifica si la pila está vacía
       print("La pila está vacía.") # imprime
    else: # si la pila no está vacía
        for auxiliar in self.lista[::-1]: # variable auxiliar que recorrerá la pila de forma inversa
            print(auxiliar) # imprime los datos

# Función: Mostrar cima
  def mostrarCima(self):
    if self.estaVacia(): # si el tope es 0
      print("La pila está vacía.") # imprime
    else: # si hay datos en la pila
      print(f"La cima de la pila es: {self.lista[-1]}") # imprimirá el índice -1 de la pila, es decir el último

while True:
    opcion = 0
    try:
        if __name__ == "__main__":
            
            # Definir pila con un tamaño de 5 espacios
            pila = Pila(5)
            
            # MENÚ CON WHILE
            while opcion != 7:

                print("\n---Pilas---\n1. Agregar datos\n2. Eliminar datos\n3. ¿Está vacía la pila?\n4. Mostrar la pila con índice\n5. Mostrar la pila sin índice\n6. Mostrar la cima\n7. Salir\n")
                opcion = int(input("Ingrese una opción: "))

                if opcion == 1:
                    dato = int(input("Ingrese un dato: "))
                    pila.agregarDatos(dato)
                    print(f"El dato {dato} ha sido agregado.\n")

                elif opcion == 2:
                    pila.eliminarDato()

                elif opcion == 3:
                    print("Sí, la pila está vacía.\n" if pila.estaVacia() else "No, la pila contiene datos.\n")

                elif opcion == 4:
                    pila.mostrarPilaConIndice()
      
                elif opcion == 5:
                    pila.mostrarPila()

                elif opcion == 6:
                    pila.mostrarCima()

                elif opcion == 7:
                    print("Gracias por usar el programa.")
                    break        

                else:
                    print("Opción inválida.\n")
            break
    except Exception as e:
        print(f"Error: {e}")