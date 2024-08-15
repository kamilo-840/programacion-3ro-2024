def sumarnumerospositivos():
    suma = 0
    while True:
        numero = int(input("Ingresa un número entero (0 para terminar): "))
        if numero == 0:
            break
        if numero > 0:
            suma += numero
    print(f"La sumatoria de los números positivos ingresados es: {suma}")

sumarnumerospositivos()