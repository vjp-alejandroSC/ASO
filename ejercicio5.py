def buscar_palabra_en_archivo():
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    palabra = input("Ingrese la palabra a buscar: ")

    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            cantidad = contenido.count(palabra)
            posiciones = [i for i, word in enumerate(contenido.split()) if word == palabra]

            if cantidad > 0:
                print(f"La palabra '{palabra}' aparece {cantidad} veces en el archivo.")
                print(f"Posiciones de la palabra '{palabra}': {posiciones}")
            else:
                print(f"La palabra '{palabra}' no se encontró en el archivo.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

# Llamar a la función
buscar_palabra_en_archivo()
