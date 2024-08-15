provincias={"cordoba":"cordoba","buenos aires":"la plata","rio negro":"viedma","la pampa":"santa rosa","chubut":"rawson","santa cruz":"rio gallegos","tierra del fuego":"ushuaia","neuquen":"neuquen","mendoza":"mendoza","san juan":"san juan","la rioja":"la rioja","catamarca":"san fernando","tucuman":"san miguel","salta":"salta","jujuy":"san salvador","formosa":"formosa","chaco":"resistencia","misiones":"posadas","corrientes":"corrientes","santa fe":"santa fe","entre rios":"parana","san luis":"san luis","santiago del estero":"santiago del estero"}


pciaBuscarValorCapital=input("Ingresar provincia a buscar capital: ")
#Buscamos el valor por clave, en este caso capital ingresando provincia
x = provincias[pciaBuscarValorCapital]
print("su capital es:",x)
print("_______________________")
for p, c in provincias.items():
    print(p, "-", c)
