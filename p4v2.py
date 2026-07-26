personas = ["Ana", "Luis", "Sofia"]

for persona in personas:

    while True:
        try:
            horas = int(input(f"{persona}, cuantas horas dormiste? "))

            if horas < 0:
                print("Coloca un numero mayor a 0")
                continue
            elif horas > 24:
                print("Coloca un numero por debajo de 24")
                continue
        except ValueError:
            print("Coloca exclusivamente numeros")
            continue

        break

    if horas < 6:
        print(f"{persona} durmio poco")
    elif horas <= 9:
        print(f"{persona} durmio lo adecuado")
    elif horas > 9:
        print(f"{persona} durmio de mas")