def mostrar_tabla_de_multiplicar():
    while True:
        try:
            # Pedir al usuario que ingrese un número entre 1 y 10
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            
            # Verificar si el número está en el rango válido
            if 1 <= n <= 10:
                try:
                    # Intentar abrir y leer el archivo correspondiente
                    with open(f'tabla_{n}.txt', 'r') as archivo:
                        contenido = archivo.read()
                    print(f"Contenido de tabla_{n}.txt: ")
                    print(contenido)
                    exit()  # Salir del programa
                except FileNotFoundError:
                    print(f"El archivo tabla_{n}.txt no existe.")
            else:
                print("El número ingresado no está en el rango válido (1-10).")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

# Llamar a la función
mostrar_tabla_de_multiplicar()
