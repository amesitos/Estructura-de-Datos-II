# NOMBRE: ANDREA VALENTINA CAMPAÑA INTRIAGO
# FECHA: 5 de noviembre de 2024
# Trabajo autónomo 1 - Agenda de contactos

""" Se requiere realizar un programa que emule una agenda de contactos telefónicos en la que se almacene los nombres de la persona 
y su número telefónico mediante una lista enlazada simple. La agenda debe de tener las siguientes opciones:
-Ingreso de nombres y número de teléfono.
-Eliminación de contacto mediante coincidencia del número telefónico.
-Mostrar la agenda con las siguientes columnas (índice, nombres, teléfono)."""

# Clase Nodo que representa cada contacto en la agenda
class Nodo:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.siguiente = None # Puntero al siguiente contacto en la lista
        
# Clase AgendaContactos que representa la agenda de contactos
class AgendaContactos:
    def __init__ (self):
        self.primero = None # Puntero al primer contacto en la lista
        self.ultimo = None # Puntero al último contacto en la lista
        
# Función: ¿está vacía?
    def agendaVacia(self):
        if self.primero == None: # Verifica si hay un nodo en la lista
            return True
        else:
            return False

# Función: Ingresar contacto a la lista.
    def ingresarContacto(self, nombre, apellido, telefono):
        nuevoNodo = Nodo(nombre, apellido, telefono)  # Crea un nuevo nodo con los datos del contacto
        if self.agendaVacia(): # si la agenda está vacía
            self.primero = self.ultimo = nuevoNodo # pone el nuevo nodo como el primero y el último
        else: # si hay nodos en la lista
            self.ultimo.siguiente = nuevoNodo # el nuevo nodo se agrega al final de la lista por medio del puntero siguiente del que era último
            self.ultimo = nuevoNodo # actualiza el puntero al último nodo
        
# Función: Mostrar la agenda con las columnas (índice, nombres, teléfono)
    def eliminarContacto(self, telefono):
        if self.agendaVacia(): # verifica si la agenda está vacía
            print("La agenda está vacía.")
            return
        
        auxiliar = self.primero # variable auxiliar que empieza desde el primer nodo para recorrer la lista
        anterior = None # variable que guarda el nodo anterior al que se va a eliminar
        
        while auxiliar != None: # mientras que se encuentre el número en la lista
            if auxiliar.telefono == telefono: # si el número coincide con el que se está buscando
                if anterior == None: # si el nodo anterior no existe, es decir, si se ha eliminado el primer nodo
                    self.primero = auxiliar.siguiente # actualiza el puntero al primer nodo
                else:
                    anterior.siguiente = auxiliar.siguiente # actualiza el puntero al nodo anterior al que se va a eliminar
                if auxiliar == self.ultimo:  # si el nodo a eliminar es el último
                    self.ultimo = anterior # actualiza el puntero al último nodo
                print(f"Contacto con número {telefono} ha sido eliminado.")
                return
            anterior = auxiliar # actualiza el puntero al nodo anterior al que se está recorriendo
            auxiliar = auxiliar.siguiente # avanza al siguiente nodo en la lista
        print("Número no encontrado en la agenda.")

    def mostrarAgenda(self):
        if self.agendaVacia():
            print("La agenda está vacía.")
            return

        indice = 0
        contactos = self.primero
        
        print("\n-----------------------------------------------")
        print("|\t    | AGENDA DE CONTACTOS |\t       |")
        print("-----------------------------------------------")
        print(f"| {'ÍNDICE':^7} | {'NOMBRE':^18} | {'TELÉFONO':^13} |")
        print("|----------------------------------------------|")

        while contactos is not None:
            print(f"| {indice:^7} | {contactos.nombre + ' ' + contactos.apellido:^18} | {contactos.telefono:^13} |")
            contactos = contactos.siguiente
            indice += 1

        print("-----------------------------------------------")


if __name__ == "__main__":
    agenda = AgendaContactos()   
    opcion = 0
         
    try:
        while opcion != 4:
            print("\n-----------------------------------------------")
            print("|\t    | AGENDA DE CONTACTOS |\t      |")
            print("|---------------------------------------------|")
            print("|\t1. Agregar nuevo contacto.            |")
            print("|\t2. Eliminar contacto por teléfono.    |")
            print("|\t3. Mostrar contactos.                 |")
            print("|\t4. Salir                              |")
            print("|---------------------------------------------|")
            opcion = int(input(" Seleccione una opción: "))
            
            if opcion == 1:
                nombre = input("\nIngrese el nombre del contacto: ")
                apellido = input("Ingrese los apellidos del contacto: ")
                telefono = input("Ingrese el número de teléfono: ")
                agenda.ingresarContacto(nombre, apellido, telefono)
                print(f"El contacto {nombre} {apellido} con número {telefono} ha sido registrado.\n")
                
            elif opcion == 2:
                telefono = input("Ingrese el número de teléfono del contacto a eliminar: ")
                agenda.eliminarContacto(telefono)
            
            elif opcion == 3:
                agenda.mostrarAgenda()
                
            elif opcion == 4:
                print("Saliendo de la agenda...")
            else:
                print("Opción inválida.\n")
    
    except Exception as e:
        print(f"Error: {e}")

            
        