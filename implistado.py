def mostrar_menu():
    print("\nMenú:")
    print("1 - Comenzar programa")
    print("2 - Imprimir listado")
    print("3 - Finalizar programa")

def comenzar_programa():
    print("Programa comenzado...")

def imprimir_listado():
    print("Listado impreso...")

def main():
    while True:
        mostrar_menu()
        
        # Leer la opción del usuario
        opcion = input("Selecciona una opción (1, 2, 3): ")
        
        if opcion == '1':
            comenzar_programa()
        elif opcion == '2':
            imprimir_listado()
        elif opcion == '3':
            print("Finalizando el programa...")
            break
        else:
            print("Opción incorrecta. Por favor, selecciona 1, 2 o 3.")

if __name__ == "__main__":
    main()