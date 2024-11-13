# NOMBRE: ANDREA VALENTINA CAMPAÑA INTRIAGO
# FECHA: 22 de octubre de 2024
# Clase 2 - Estructura de Datos II

class Cola: # Clase Cola
  def __init__ (self):
    self.cola = [] # lista vacía para la cola
    self.tamanio = 0 # solo indica la cantidad de datos en la cola
    
    # Función: Agregar datos a la cola
  def agregarDatos(self, dato): # parámetro dato
    self.cola += [dato] # se le agrega el dato a la cola
    self.tamanio +=1 # el tamaño aumenta
    
    # Función: Eliminar datos de la cola
  def eliminarDatos(self):
    if self.estaVacia(): # verifica si está vacía antes de eliminar un dato
        print("La cola está vacía.") # imprime
    else: # si la cola no está vacía
        # crea una nueva lista eliminando el primer elemento (indice 0) y guarda el resto de los elementos
        self.cola = [self.cola[i] for i in range(1, self.tamanio)] 
        self.tamanio -= 1 # se reduce 1 en el tamaño
        print("El dato ha sido eliminado.") # mensaje de confirmación    

    # Función: ¿La cola está vacía?
  def estaVacia(self):
    return len(self.cola) == 0  # Retorna True si la longitud de la cola es 0, de lo contrario False

    # Función: Mostrar la cola
  def mostrarColaConIndice(self):
    if self.estaVacia():  # si la cola está vacía
        print("La cola está vacía.")  # imprime
    else:
        indice = self.tamanio -1
        while indice > -1:
            print(f"[{indice}] => {self.cola[indice]}")
            indice -=1

    # Función: Mostrar primer elemento de la cola
  def mostrarPrimerElemento(self):
    if self.estaVacia(): # verifica si la cola está vacía
        print("La cola está vacía.") # imprime
    else: # de lo contrario
        # imprime el dato de la cola posicionado en índice 0
        print(f"El primer elemento de la cola es: {self.cola[0]}") 

  # Función: Mostrar último elemento de la cola
  def mostrarUltimoElemento(self):
      if self.estaVacia(): # verifica si la cola está vacía
        print("La cola está vacía.") # imprima
      else:
        print(f"El último elemento de la cola es: {self.cola[-1]}") # imprime el último elemento de la cola con el índice -1


while True:
    opcion = 0
    try: 
        if __name__ == "__main__":
            cola = Cola()

        while opcion != 7:
            print("\n---Colas---\n1. Agregar datos\n2. Eliminar datos\n3. ¿Está vacía la cola?\n4. Mostrar la cola con índices\n5. Mostrar primer elemento\n6. Mostrar último elemento\n7.Salir.")
      
            opcion = int(input("Ingrese una opción: "))

            if opcion == 1:
                dato = int(input("Ingrese un dato: "))
                cola.agregarDatos(dato)
                print(f"El dato {dato} ha sido agregado.\n")

            elif opcion == 2:
                cola.eliminarDatos()

            elif opcion == 3:
                print("Sí, la cola está vacía.\n" if cola.estaVacia() else "No, la cola contiene datos.\n")

            elif opcion == 4:
                cola.mostrarColaConIndice()

            elif opcion == 5:
                cola.mostrarPrimerElemento()

            elif opcion == 6:
                cola.mostrarUltimoElemento()

            elif opcion == 7:
                print("Gracias por usar el programa.")
                break

            else:
                print("Opción inválida.\n")
        break

    except Exception as e:
        print(f"Error: {e}")