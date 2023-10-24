def pedir_numero():
    n = input("del 1 al 10: ")

    if 1 < n > 10:
        print("El número debe estar comprendido entre el 1 y el 10")

print(pedir_numero())