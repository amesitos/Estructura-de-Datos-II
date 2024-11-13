# NOMBRE: ANDREA VALENTINA CAMPAÑA INTRIAGO
# FECHA: 29 de octubre de 2024
# Clase 3 - Estructura de Datos II

class Pila: 

  def __init__(self, tamanio):
    self.lista = [] 
    self.tope = 0 
    self.tamanio = tamanio 

# Función: Agregar datos
  def agregarDatos (self, dato): 
    if self.tope < self.tamanio:
      self.lista.append(dato)
    else: 
      self.tamanio += 1
      self.lista.append(dato)
    self.tope+=1 

# Función: Eliminar dato
  def eliminarDato(self):
    if self.estaVacia():
        print("La pila está vacía.")
    else:
        self.tope -=1
        print(f"Dato eliminado: {self.lista.pop()}")
        print(f"La pila actual es: {self.lista}")

# Función: ¿hay elementos?
  def estaVacia (self):
    return len(self.lista) == 0

# Función: Mostrar lista con índice
  def mostrarPilaConIndice(self):
    if self.estaVacia():
        print("La pila está vacía.")
    else:
        for indice, elemento in enumerate(self.lista):
            print(f"[{indice}] => {elemento}")

# Función: Mostrar lista sin índices
  def mostrarPila(self):
    if self.estaVacia():
       print("La pila está vacía.") 
    else: 
        print(f"Pila: {self.lista}")

# Función: Mostrar cima
  def mostrarCima(self):
    if self.estaVacia():
        print("La pila está vacía.") 
    else:
        cima = self.lista.copy().pop()  
        print(f"La cima de la pila es: {cima}")


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