while True:
    try:
        edad = int(input("¿Cuántos años tienes? "))
        if edad <= 0:
            print("Ingresa un número mayor que 0")
            continue   # vuelve al inicio del while, sin llegar al break
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

if edad >= 18:
    print("Eres mayor de edad, puede votar.")
else:
    print("Eres menor de edad, no puede votar.")