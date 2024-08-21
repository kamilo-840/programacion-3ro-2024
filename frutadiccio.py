precios_frutas = {
    'manzana': 2000,  # Precio por kilo en euros
    'banana': 2500,
    'naranja': 2800,
    'pera': 3200,
    'uva': 4000
}

# Función principal
def calcular_precio():
    # Solicitar al usuario la fruta y el número de kilos
    fruta = input("Ingrese el nombre de la fruta: ").lower()
    try:
        kilos = float(input("Ingrese el número de kilos: "))
    except ValueError:
        print("Por favor, ingrese un número válido para los kilos.")
        return

    # Verificar si la fruta está en el diccionario
    if fruta in precios_frutas:
        precio_por_kilo = precios_frutas[fruta]
        precio_total = precio_por_kilo * kilos
        print(f"El precio de {kilos} kilos de {fruta} es {precio_total:.2f} pesos.")
    else:
        print(f"La fruta '{fruta}' no está en el diccionario.")

# Ejecutar la función principal
calcular_precio()
