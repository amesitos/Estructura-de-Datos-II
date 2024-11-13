class Cola:

	def __init__(self):
		self.elementos = []

	def vacio(self):
		if len(self.elementos) == 0:
			return True
		else:
			return False

	def insertar(self,nodo): #Encolar
		self.elementos.append(nodo)
		print("El elemento fue añadido")

	def eliminar(self): #Desencolar
		if self.vacio():
			print("La estructura está vacía")
		else:
			eliminado = self.elementos.pop(0)
			print("Elemento eliminado : "+str(eliminado))

	def consultar(self):
		if self.vacio():
			print("La cola no tiene elementos")
		else:
			print(self.elementos)

	def sumar(self):
		if self.vacio():
			print("No hay nada que sumar")
		else:
			total = 0
			for nodo in self.elementos:
				total = total + int(nodo)
			print("El total es: " + str(total))

obj = Cola()
while True:
	print("1.- Insertar (Encolar)")
	print("2.- Consultar")
	print("3.- Eliminar (Desencolar)")
	print("4.- Sumar")
	print("5.- Salir")
	opcion = int(input("Escribe tu opcion:"))
	if opcion==1:
		nodo = input("Escribe el nuevo elemento: ")
		obj.insertar(nodo)
	elif opcion==2:
		obj.consultar()
	elif opcion==3:
		obj.eliminar()
	elif opcion==4:
		obj.sumar()
	elif opcion==5:
		break
	else:
		print("No existe esa opción")