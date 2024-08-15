prod=[]
rta="si"
while rta=="si":
    option=input("seleccione una opcion \n 1. agregar productos a la lista \n 2. mostrar productos de la lista \n 3. salir  \n")
    if option=="1":
        prodagre=input("ingrese el producto que quiere agregar")
        prod.append(prodagre)
    elif option=="2":
        print("los productos eb la lista son:\n") 
        for p in prod:
            print (p)
    elif option=="3":
        mta=input("esta segurp que quiere salir del sistema si/no ")
        if rta=="si" or rta=="Si" or rta=="SI":
            print ("salio del sistema")
            break
        else:
            print("se lo reingresara al sistema")