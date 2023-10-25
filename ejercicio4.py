def mostrar_linea_de_tabla():
    try:
        # Pedir al usuario que ingrese dos números entre 1 y 10
        n = int(input("Ingrese un número entero entre 1 y 10 (n): "))
        m = int(input("Ingrese otro número entero entre 1 y 10 (m): "))
        
        # Verificar si los números están en el rango válido
        if 1 <= n <= 10 and 1 <= m <= 10:
            try:
                # Intentar abrir y leer el archivo correspondiente
                with open(f'tabla_{n}.txt', 'r') as archivo:
                    lineas = archivo.readlines()
                if 1 <= m <= len(lineas):
                    # Mostrar la línea m del archivo (se resta 1 para acceder a la línea correcta en la lista)
                    print(lineas[m - 1])
                else:
                    print("El valor de m está fuera del rango válido.")
            except FileNotFoundError:
                print(f"El archivo tabla_{n}.txt no existe.")
        else:
            print("Los números ingresados no están en el rango válido (1-10).")
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")

# Llamar a la función
mostrar_linea_de_tabla()
