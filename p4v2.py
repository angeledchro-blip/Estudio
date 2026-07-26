nombres = ["Ezra", "Diego", "Edmundo"]
for nombre in nombres:
    while True:
     try:
        horas = int(input(f"{nombre} Cuantas horas dormiste?"))
        if horas <0:
         print("Coloca un numero mayor a 0")
         continue
        elif horas >24:
         print("Coloca un numero menor a 24") 
         continue
     except ValueError:
         print("Coloca un numero valido")   
         continue
     break   
    if horas <6:
     print(f"{nombre} Dormiste poco")
    elif horas <9:
     print(f"{nombre} Dormiste lo adecuado")
    else:
     print(f"{nombre} Dormiste de mas")      