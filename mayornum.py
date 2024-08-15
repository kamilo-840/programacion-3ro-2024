def encontrarmayornumero():
    mayor_numero = 0  # Inicializamos el mayor número en 0
    while True:
        numero = int(input("Ingresa un número entero positivo (0 para terminar): "))
        if numero == 0:
            break  # Salimos del bucle si el usuario ingresa 0
        elif numero < 0:
            print("Por favor, ingresa solo números enteros positivos.")
        else:
            if numero > mayor_numero:
                mayor_numero = numero  # Actualizamos el mayor número si es necesario

    if mayor_numero > 0:
        print(f"El mayor número ingresado fue: {mayor_numero}")
    else:
        print("No se ingresaron números positivos.")

# Llamamos a la función
encontrarmayornumero()
