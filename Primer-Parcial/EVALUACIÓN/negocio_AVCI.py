# NOMBRE: ANDREA VALENTINA CAMPAÑA INTRIAGO
# FECHA: 12 de noviembre de 2024
# Evaluación Primer Parcial - Estructura de Datos II

class Registro_AVCI:
    def __init__(self, nombres, apellidos, descripcion, valUnitario, cantidad):
        self.nombres = nombres
        self.apellidos = apellidos
        self.descripcion = descripcion
        self.valUnitario = valUnitario
        self.cantidad = cantidad
        self.total = valUnitario * cantidad
        self.siguiente = None
        self.anterior = None

class Ventas_AVCI:
    def __init__(self):
        self.primero = None 
        self.ultimo = None 
        # self.tamanio = 0 

    def estaVacia(self):
        return self.primero == None
    
    def registrarVenta(self, nombres, apellidos, descripcion, valUnitario, cantidad):
        nuevoRegistro = Registro_AVCI(nombres, apellidos, descripcion, valUnitario, cantidad)
        if self.estaVacia():
            self.primero = self.ultimo = nuevoRegistro
        else:
            nuevoRegistro.anterior = self.ultimo 
            self.ultimo.siguiente = nuevoRegistro
            self.ultimo = nuevoRegistro
        # self.tamanio += 1  

    def eliminarVenta(self, reciclaje):
        if self.estaVacia():
            print("No existen registros que eliminar.")
            return
        elif self.primero.siguiente == None:
            ventaEliminada = self.primero
            reciclaje.agregarRegistroEliminado(ventaEliminada)
            self.primero = self.ultimo = None
            print("Última venta eliminada.")
        else:
            ventaEliminada = self.ultimo
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            reciclaje.agregarRegistroEliminado(ventaEliminada)
            print("Última venta eliminada.")

            
    def verVentas(self):
        if self.estaVacia():
            print("No existen registros de venta.")
        else:
            venta = self.ultimo
            print("\n---------------------VENTAS DE NEGOCIO AVCI------------------------")
            while venta:
                print(f"{venta.nombres} {venta.apellidos} | {venta.descripcion} | ${venta.valUnitario} | {venta.cantidad} | ${venta.total}")
                venta = venta.anterior

    def reportePorCliente(self):
        if self.estaVacia():
            print("Reporte vacío. Realice un registro de venta.")
        else:
            reporte = {}
            auxiliar = self.primero
            print("\n-------------REPORTE DE VENTAS POR CLIENTE--------------")
            while auxiliar:
                nombreCompleto = f"{auxiliar.nombres} {auxiliar.apellidos}"
                if nombreCompleto in reporte:
                    reporte[nombreCompleto] += auxiliar.total
                else:
                    reporte[nombreCompleto] = auxiliar.total
                auxiliar = auxiliar.siguiente
            for cliente, total in reporte.items():
                print(f"{cliente} => TOTAL: {total}")

class Reciclaje_AVCI:
    def __init__(self):
        self.cola = []
            
    def agregarRegistroEliminado(self, registro):
        self.cola.append(registro)

    def verColaReciclaje(self):
        if not self.cola:
            print("No hay registros en el reciclaje.")
            return
        else:
            print("\n-------------------REGISTROS ELIMINADOS------------------------")
            for registro in self.cola:
                print(f"{registro.nombres} {registro.apellidos} | {registro.descripcion} | {registro.cantidad}")

if __name__ == "__main__":
    avci = Ventas_AVCI()
    papelera = Reciclaje_AVCI()
    opcion = 0

    while True:
        try:
            print("\n--- Menú de Gestión de Ventas ---")
            print("1. Verificar si existen registro de ventas.")
            print("2. Registrar nueva venta.")
            print("3. Eliminar la última venta registrada")
            print("4. Mostrar todas las ventas registradas")
            print("5. Visualizar el reciclaje de ventas eliminadas")
            print("6. Generar reporte de total de ventas por cliente")
            print("7. Salir")
            
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                if avci.estaVacia():
                    print("\nNo existen registros de ventas.")
                else:
                    print("\nSí existen registros de ventas.")
                    
            elif opcion == 2:
                nombres = input("\nIngrese los nombres del cliente: ")
                apellidos = input("Ingrese los apellidos del cliente: ")
                descripcion = input("Ingrese la descripción del producto: ")
                valorUnitario = float(input("Ingrese el valor unitario: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                avci.registrarVenta(nombres, apellidos, descripcion, valorUnitario, cantidad)
                print("¡Venta registrada!\n")
                
            elif opcion == 3:
                avci.eliminarVenta(papelera)
                
            elif opcion == 4:
                avci.verVentas()
                
            elif opcion == 5:
                papelera.verColaReciclaje()
                
            elif opcion == 6:
                avci.reportePorCliente()
                
            elif opcion == 7:
                print("Saliendo...")
                break
                
            else:
                print("Opción inválida.")
                
        except Exception as e:
            print(f"Error: {e}")
