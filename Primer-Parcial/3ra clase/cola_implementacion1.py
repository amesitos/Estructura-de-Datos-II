# NOMBRE: ANDREA VALENTINA CAMPAÑA INTRIAGO
# FECHA: 29 de octubre de 2024
# Clase 3 - Estructura de Datos II

class Cola:
    def __init__(self):
        self.cola = []
        self.tamanio = 0

# Función: Agregar datos
    def agregarDatos(self, dato):
        self.cola.insert(self.tamanio, dato)
        self.tamanio += 1

# Función: Eliminar dato
    def eliminarDatos(self):
        if not self.cola:
            print("La cola está vacía.")
        else:
            self.cola.pop(0)
            self.tamanio -= 1
            print("El dato ha sido eliminado.")

# Función: ¿hay elementos?
    def estaVacia(self):
        if self.cola == []:
            return True
        else:
            return False

# Función: Mostrar cola con índice
    def mostrarColaConIndice(self):
        if self.estaVacia():
            print("La cola está vacía.")
        else:
            for indice, valor in enumerate(self.cola[::-1]):
                print(f"[{len(self.cola) - 1 - indice}] => {valor}")

# Función: Mostrar primer elemento
    def mostrarPrimerElemento(self):
        if self.estaVacia():
            print("La cola está vacía.")
        else:
            print(f"El primer elemento de la cola es: {next(iter(self.cola))}")

# Función: Mostrar último elemento
    def mostrarUltimoElemento(self):
        if self.estaVacia():
            print("La cola está vacía.")
        else:
            ultimo_elemento = next(iter(reversed(self.cola)))
            print(f"El último elemento de la cola es: {ultimo_elemento}")


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
