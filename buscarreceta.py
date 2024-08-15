recetas={"milanesa":{"carne":"200 gm","pan rallado":"300 gm","huevo":"3"},"empanadas de carne":{"tapa de empanada":"10","carne molida":"300 gm","cebolla":"3"},"pure de papa":{"papa":"750 gm","crema":"2  cucharadas","condimentos":"sal, pimienta, nuez moscada"}}
print("las recetas que tenemos son: milanesa, empanadas de carne, pure de papa")
buscarreceta=input("ingrese la receta que quiere conocer: ")
x = recetas[buscarreceta]
print("la receta es:",x)