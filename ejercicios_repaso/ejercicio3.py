def eliminar_alumno(nombre):
    try:
        with open("ejercicios_repaso/alumnos.txt", "r") as archivo:
            lineas = archivo.readlines()
        encontrado = False

        with open ("ejercicios_repaso/alumnos.txt", "w") as archivo:
            for linea in lineas: # Recorre cada línea del fichero buscando el nombre
                if nombre not in linea: 
                    archivo.write(linea) # Si el nombre no se encuentra, escribe la línea completa
                else:
                    encontrado = True # Si lo encuentra, borrará la línea completa
            if encontrado:
                print(f"El alumno {nombre} ha sido borrado.")
            else:
                print(f"El alumno {nombre} no fue encontrado en el archivo.")
    except FileNotFoundError:
        print("El fichero 'alumnos.txt' no existe")

nombre_eliminar = input("Introduce el nombre del alumno que deseas eliminar: ")

eliminar_alumno(nombre_eliminar)
            