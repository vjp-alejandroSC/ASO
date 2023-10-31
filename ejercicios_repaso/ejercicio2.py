def contar_alumnos():
        
    with open("ejercicios_repaso/alumnos.txt", "r") as archivo:
        lineas = archivo.readlines()
        numero_de_alumnos = len(lineas)
        print(f"\nEl número de alumnos es: {numero_de_alumnos}")

# Llamar a la función y mostrar el resultado
contar_alumnos()
