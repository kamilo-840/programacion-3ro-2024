rta="si"
contador=0
while rta=="si":
    contra=("sapallo")
    usuario=("camilo")
    usuarioing=input("ingrese el usuario: ")
    contraing=input("ingrese la contraseña: ")
    contador=contador+1
    if contraing==contra and usuarioing==usuario and contador<4:
        print("ha ingresado al sistema op hagoto la cantidad de intentos")
        break
    else:
        print("la contraseña o el usuario es incorrecta, ingreselos de nuevo")