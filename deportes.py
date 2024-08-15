deportes={"d1":"futbol","d2":"voley","d3":"tenis"}

for c,v in deportes.items():
     print (c, ":", v)
     if "voley" in v:
          print("el deporte voley existe y tiene la clave:",c)