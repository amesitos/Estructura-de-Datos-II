# NOMBRE: ANDREA VALENTINA CAMPAÑA INTRIAGO
# FECHA: 29 de octubre de 2024
# Clase 3 - Estructura de Datos II

class Cola:
    def __init__(self):
        self.cola = []
        self.tamanio = 0

# Función: Agregar datos
    def agregarDatos(self, dato):
        self.cola.append(dato)  
        self.tamanio += 1

# Función: Eliminar dato
    def eliminarDatos(self):
        if self.estaVacia():
            print("La cola está vacía.")
        else:
            dato_eliminado = self.cola[0]  
            del self.cola[0] 
            self.tamanio -= 1
            print(f"El dato {dato_eliminado} ha sido eliminado.")

# Función: ¿hay elementos?
    def estaVacia(self):
        return len(self.cola) == 0 

# Función: Mostrar cola con índice
    def mostrarColaConIndice(self):
        if self.estaVacia():
            print("La cola está vacía.")
        else:
            for indice in range(self.tamanio):
                print(f"[{indice}] => {self.cola[indice]}")  

# Función: Mostrar primer elemento de la cola
    def mostrarPrimerElemento(self):
        if self.estaVacia():
            print("La cola está vacía.")
        else:
            primer_elemento = self.cola.pop(0)  
            print(f"El primer elemento de la cola es: {primer_elemento}")

# Función: Mostrar último elemento de la cola
    def mostrarUltimoElemento(self):
        if self.estaVacia():
            print("La cola está vacía.")
        else:
            print(f"El último elemento de la cola es: {self.cola[-1]}")  


if __name__ == "__main__":
    cola = Cola()

    while True:
        try:
            print("\n---Colas---\n1. Agregar datos\n2. Eliminar datos\n3. ¿Está vacía la cola?\n4. Mostrar la cola con índices\n5. Mostrar primer elemento\n6. Mostrar último elemento\n7. Salir.")
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
        except Exception as e:
            print(f"Error: {e}")
