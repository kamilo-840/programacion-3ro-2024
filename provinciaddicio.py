provincia={"cordoba":"cordoba","buenos aires":"la plata","rio negro":"viedma","la pampa":"santa rosa","chubut":"rawson","santa cruz":"rio gallegos","tierra del fuego":"ushuaia","neuquen":"neuquen","mendoza":"mendoza","san juan":"san juan","la rioja":"la rioja","catamarca":"san fernando","tucuman":"san miguel","salta":"salta","jujuy":"san salvador","formosa":"formosa","chaco":"resistencia","misiones":"posadas","corrientes":"corrientes","santa fe":"santa fe","entre rios":"parana","san luis":"san luis","santiago del estero":"santiago del estero"}
print(provincia)
print("___________")
for c,v in provincia.itens():#uso el for para mostrarlo prolijo
    print(c, ":",v ) 
    print("__________")#imprimo esto para separalos
