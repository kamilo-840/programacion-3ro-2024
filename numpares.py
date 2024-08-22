cantidad_pares = 0

while True:
    # Leer un número entero desde el teclado
    numero_str = input("Introduce un número entero positivo (-1 para terminar): ")
    
    # Verificar si el usuario quiere terminar
    if numero_str == "-1":
        break
    
    # Verificar si el número es un entero positivo
    if not numero_str.isdigit():
        print("El valor introducido no es un número entero positivo.")
        continue
    
    # Convertir el número a entero
    numero = int(numero_str)
    
    # Calcular la suma de los dígitos
    suma_digitos = sum(int(digito) for digito in numero_str)
    
    # Imprimir la suma de los dígitos
    print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
    
    # Verificar si el número es par y contar
    if numero % 2 == 0:
        cantidad_pares += 1

# Mostrar cuántos números pares se ingresaron
print(f"Se ingresaron {cantidad_pares} números pares.")
