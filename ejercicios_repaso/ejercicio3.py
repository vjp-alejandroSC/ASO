def eliminar_alumno():
    alumno = input("Ingrese el nombre del alumno que quiere eliminar: ")

    with open("ejercicios_repaso/alumnos.txt", "w+") as archivo:
        
        leer_archivo = archivo.readlines()
            
        if alumno in leer_archivo:
            leer_archivo[alumno].remove
            print("El nombre ha sido eliminado.")

eliminar_alumno()            