def preguntar_horas(persona):
    while True:
        try:
            horas = int(input(f"{persona} Cuantas horas dormiste? "))
            if horas <0:
                print("Coloca un numero mayor a 0")
                continue
            elif horas >24:
                print("Coloca un numero menor a 24")
                continue
            break
        except ValueError:
            print("Coloca un numero valido")   
            continue
    if horas <6:
     print("Dormiste poco")     
    elif horas <=9:
        print("Dormiste lo adecuado")    
    else:
        print("Dormiste de mas")    
nombres = ["Diego", "Ezra", "Edmundo"] 
for nombre in nombres:
    preguntar_horas(nombre)
           
             



