def es_palindromo(palabra):
    pila = Pila(len(palabra))
    for letra in palabra:
        pila.push(letra)
    
    palabra_inversa = ""
    while not pila.empty():
        palabra_inversa += pila.top()
        pila.pop()
    
    return palabra == palabra_inversa

palabra = input("Ingresa una palabra: ")
print("Es un palíndromo" if es_palindromo(palabra) else "No es un palíndromo")

def parentesis_balanceados(expresion):
    pila = Pila(len(expresion))
    for caracter in expresion:
        if caracter == "(":
            pila.push(caracter)
        elif caracter == ")":
            if pila.empty():
                return False
            pila.pop()
    
    return pila.empty()

expresion = input("Ingresa una expresión: ")
print("Paréntesis balanceados" if parentesis_balanceados(expresion) else "Paréntesis no balanceados")

def decimal_a_binario(numero):
    pila = Pila(20)
    while numero > 0:
        residuo = numero % 2
        pila.push(residuo)
        numero //= 2
    
    binario = ""
    while not pila.empty():
        binario += str(pila.top())
        pila.pop()
    
    return binario

numero = int(input("Ingresa un número decimal: "))
print("Binario:", decimal_a_binario(numero))


def invertir_cadena(cadena):
    pila = Pila(len(cadena))
    for letra in cadena:
        pila.push(letra)
    
    cadena_invertida = ""
    while not pila.empty():
        cadena_invertida += pila.top()
        pila.pop()
    
    return cadena_invertida

cadena = input("Ingresa una cadena: ")
print("Cadena invertida:", invertir_cadena(cadena))


def eliminar_pares(pila):
    pila_aux = Pila(pila.size)
    
    while not pila.empty():
        if pila.top() % 2 != 0:
            pila_aux.push(pila.top())
        pila.pop()
    
    while not pila_aux.empty():
        pila.push(pila_aux.top())
        pila_aux.pop()

pila = Pila(10)
for i in range(10):
    pila.push(i)
print("Pila original:")
pila.show()

eliminar_pares(pila)
print("Pila sin pares:")
pila.show()


def deshacer_ultimo(pila):
    if not pila.empty():
        print("Acción deshecha:", pila.top())
        pila.pop()
    else:
        print("Nada que deshacer")

pila = Pila(10)
while True:
    accion = input("Ingresa una acción (o 'deshacer' para deshacer): ")
    if accion == "deshacer":
        deshacer_ultimo(pila)
    else:
        pila.push(accion)
        print(f"Acción '{accion}' agregada.")
