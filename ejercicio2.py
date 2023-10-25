def generar_tabla_de_multiplicar():
    try:
        # Pedir al usuario que ingrese un número entre 1 y 10
        n = int(input("Ingrese un número entero entre 1 y 10: "))
        
        # Verificar si el número está en el rango válido
        if 1 <= n <= 10:
            # Generar la tabla de multiplicar y guardarla en un archivo
            with open(f'tabla_{n}.txt', 'w') as archivo:
                for i in range(1, 11):
                    resultado = n * i
                    archivo.write(f"{n} x {i} = {resultado}\n")
            print(f"La tabla de multiplicar del {n} se ha guardado en tabla_{n}.txt")
            
            # Leer y mostrar el contenido del archivo
            with open(f'tabla_{n}.txt', 'r') as archivo:
                contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)
        else:
            print("El número ingresado no está en el rango válido (1-10).")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Llamar a la función
generar_tabla_de_multiplicar()