numero = input("Introduce un número entero positivo: ")

# Verificar si el número es positivo
if not numero.isdigit():
    print("El valor introducido no es un número entero positivo.")
else:
    # Convertir el número a una lista de dígitos y sumarlos
    suma_digitos = sum(int(digito) for digito in numero)
    
    # Imprimir la suma de los dígitos
    print(f"La suma de los dígitos es: {suma_digitos}")
