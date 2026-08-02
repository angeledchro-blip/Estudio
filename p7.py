pelicula = {"titulo": "Spiderman", "Año": 2008}
calificacion = int(input("Califica " f"{pelicula["titulo"]} - {pelicula["Año"]}: "))
if calificacion <5:
    print("No recomendada")
elif calificacion <=9:
    print("Recomendada")    
else:
    print("Excelente")    
 
