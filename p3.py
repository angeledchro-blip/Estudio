while True:
    try:     
         horas = int(input("Cuantas horas dormiste? "))

         if horas <0:
            print("Coloca un numero mayor a 0")
            continue
         elif horas >24:
            print("Coloca un numero por debajo de 24")   
            continue
    except ValueError:
        print("Coloca exclusivamente numeros")
        continue
    
    break

if horas <6:
    print("Dormiste poco")
elif horas <=9:
    print("Dormiste lo adecuado")
elif horas >9:
    print("Dormiste de mas")    
