class Pila:
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.tope = 0
        self.pila = []
        
    def estaVacia(self):
        return self.tope == 0
    
    def apilar(self, dato):
        if self.tope < self.tamanio:
            self.lista.append(dato)
            self.tope += 1
        else:
            self.tamanio += 5
            self.lista.append(dato)
            self.tope += 1
            
    def desapilar(self):
        if self.estaVacia():
            return "La pila está vacía, no hay ningún dato que desapilar."
        else:
            print(f"El dato eliminado es {self.lista.pop()}")
            self.tope=-1
            print(f"La lista actual es: {self.lista}")
            
            
    try:
        pila
        opcion = 0
        while opcion != 10:
            print("|| PILA - LIFO (last in first out)")
            print("1. ¿Está vacía la pila?")
            print("2. Apilar dato.")
            print("3. Desapilar dato.")
            print("4. Mostrar pila sin índices.")
            print("5. Mostrar pila con índices.")
            print("6. Buscar dato según índice.")
            opcion = int(input("Ingrese una opción: "))
            
        
            