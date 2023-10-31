def eliminar_alumno(nombre):
    try:
        with open("ejercicios_repaso/alumnos.txt", "r") as archivo:
            lineas = archivo.readlines()
        encontrado = False

        with open ("ejercicios_repaso/alumnos.txt", "w") as archivo:
            for linea in lineas:
                if nombre not in linea:
                    archivo.write(linea)
                else:
                    encontrado = True
            if encontrado:
                print(f"El alumno {nombre} ha sido borrado.")
            else:
                print(f"El alumno {nombre} no fue encontrado en el archivo.")
    except FileNotFoundError:
        print("El fichero 'alumnos.txt' no existe")

nombre_eliminar = input("Introduce el nombre del alumno que deseas eliminar: ")

eliminar_alumno(nombre_eliminar)
            