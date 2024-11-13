# NOMBRE: ANDREA VALENTINA CAMPAÑA INTRIAGO
# FECHA: 22 de octubre de 2024
# Clase 2 - Estructura de Datos II

# lista 1
lista1 = []
print("\n---LISTA 1---")
respuesta = input("¿Desea agregar elementos en la lista 1? (Y/N): ")

while respuesta.lower() == "y" or respuesta.lower() == "s":
    elemento = input("Ingrese un elemento o nombre: -> ")
    lista1.append(elemento)
    respuesta = input("¿Desea agregar más elementos? (Y/N): ")

print(f"\nLos elementos que ha ingresado en la lista 1 son: {lista1}")

# lista 2
print("\n---LISTA 2---")
lista2 = []
respuesta = input("¿Desea agregar elementos en la lista 2? (Y/N): ")

while respuesta.lower() == "y" or respuesta.lower() == "s":
  elemento = input("Ingrese un elemento o nombre: -> ")
  lista2.append(elemento)

  respuesta = input("¿Desea agregar más elementos? (Y/N): ")
print(f"\nLos elementos que ha ingresado en la lista 2 son: {lista2}")

# Unir listas
union = list(set(lista1) | set(lista2))
union.sort()
print(f"\nLa unión de las listas es: {union}")

# Solo elementos que están lista 1
solo_lista1 = list(set(lista1) - set(lista2))
print(f"\nLos elementos que están en la lista 1 pero no en la lista 2 son: {solo_lista1}")

# Solo lista 2
solo_lista2 = list(set(lista2) - set(lista1))
print(f"\nLos elementos que están en la lista 2 pero no en la lista 1 son: {solo_lista2}")

# Intersección
lista_unida = list(set(lista1) & set(lista2))
print(f"\nLos elementos de ambas listas son: {lista_unida}")
