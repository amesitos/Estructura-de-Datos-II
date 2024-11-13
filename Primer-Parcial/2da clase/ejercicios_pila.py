
"""def invertir_cadena(cadena):
    pila = []
    for caracter in cadena:
        pila.append(caracter)
    cadena_invertida = ""
    while pila:
        cadena_invertida += pila.pop()
    return cadena_invertida

cadena = input("Ingresa una cadena: ")
print(f"Cadena invertida: {invertir_cadena(cadena)}")

def verificar_balance(expresion):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}
    for simbolo in expresion:
        if simbolo in "([{":
            pila.append(simbolo)
        elif simbolo in ")]}":
            if not pila or pila.pop() != pares[simbolo]:
                return False
    return len(pila) == 0

expresion = input("Ingresa una expresión: ")
if verificar_balance(expresion):
    print("Los paréntesis están balanceados.")
else:
    print("Los paréntesis no están balanceados.")"""

texto = ""
pila_deshacer = []
pila_rehacer = []

def insertar_texto(nuevo_texto):
    global texto
    pila_deshacer.append(texto)
    texto += nuevo_texto

def deshacer():
    global texto
    if pila_deshacer:
        pila_rehacer.append(texto)
        texto = pila_deshacer.pop()
    else:
        print("Nada que deshacer.")

def rehacer():
    global texto
    if pila_rehacer:
        pila_deshacer.append(texto)
        texto = pila_rehacer.pop()
    else:
        print("Nada que rehacer.")

insertar_texto("Hola")
insertar_texto(" Mundo")
print("Texto actual:", texto)
deshacer()
print("Después de deshacer:", texto)
rehacer()
print("Después de rehacer:", texto)
