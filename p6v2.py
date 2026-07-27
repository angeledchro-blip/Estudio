def obtener_precio(producto):
  while True:
     try:
        precio = int(input(f"{producto} Precio: " ))
        if precio <0:
          print("Coloca un numero mayor a 0")
          continue
        elif precio >10000:
          print("Coloca un numero menor a 10000")     
          continue
        break
     except ValueError:
      print("Coloca un numero valido")
      continue
  return precio

def clasificar_precio(precios):
  if precios <100:
    return "Economico"
  elif precios <=500:
    return "Precio moderado"
  else:
    return "Caro"

productos = ["USB", "Monster", "Bacardi"]
for producto in productos:
  obtener = obtener_precio(producto)
  clasificar = clasificar_precio(obtener)  
  print(f"{producto}: {clasificar}")