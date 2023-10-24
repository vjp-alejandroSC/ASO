# Función para limpiar la pantalla
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para añadir un contacto a la agenda
def agregar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    apellidos = input("Ingrese los apellidos del contacto: ")
    telefono = input("Ingrese el número de teléfono del contacto: ")
    instagram = input("Ingrese su instagram: ")
    while instagram[0] != "@":
        instagram = input("Tiene que empezar por @. Introdúcelo de nuevo: ")
    
    profesion = input("Ingrese su profesión: ")

    contacto = {"Nombre": nombre, "Apellidos": apellidos, "Teléfono": telefono, "Instagram": instagram, "Profesión": profesion}
    agenda.append(contacto)
    print("Contacto agregado exitosamente.")


# Función para buscar un contacto en la agenda
def buscar_contacto(agenda, nombre_buscar):
    for i, contacto in enumerate(agenda):
        if contacto["Nombre"] == nombre_buscar:
            print(f"El contacto '{nombre_buscar}' se encuentra en la posición {i + 1}.")
            return
    print(f"El contacto '{nombre_buscar}' no se encuentra en la agenda.")

# Función para borrar un contacto de la agenda
def borrar_contacto(agenda, nombre_borrar):
    for contacto in agenda:
        if contacto["Nombre"] == nombre_borrar:
            agenda.remove(contacto)
            print(f"Contacto '{nombre_borrar}' borrado exitosamente.")
            return
    print(f"El contacto '{nombre_borrar}' no se encuentra en la agenda.")
    input("Presiona cualquier tecla para continuar...")

# Función para mostrar la lista completa de contactos
def mostrar_lista_contactos(agenda):
    if not agenda:
        print("La agenda está vacía.")
    else:
        print("Lista de Contactos:")
        for i, contacto in enumerate(agenda):
            print(f"Contacto {i + 1}:")
            print(f"Nombre: {contacto['Nombre']}")
            print(f"Apellidos: {contacto['Apellidos']}")
            print(f"Teléfono: {contacto['Teléfono']}")
            print(f"Instagram: {contacto['Instagram']}")
            print(f"Profesión: {contacto['Profesión']}")
            print("-" * 30)

# Función para mostrar el tamaño de la agenda
def mostrar_tamaño_agenda(agenda):
    print(f"La agenda contiene {len(agenda)} contactos.")

# Función para mostrar los contactos con la misma profesión
def mostrar_por_profesión(agenda, trabajo):
    print("Estos son los contactos que comparten la profesión:")

    for contacto in agenda:
        if contacto['Profesión'] == trabajo:        
            print(f"Nombre: {contacto['Nombre']}")
            print(f"Profesión: {contacto['Profesión']}")
            print("-" * 30)

# Función para cambiar la profesión

def cambiar_profesión (agenda, nombre_contacto):
    for contacto in agenda:
        if contacto["Nombre"] == nombre_contacto:
            contacto["Profesión"] = input("Introduce la nueva profesión: ")
        else:
            print("Este contacto no existe en la agenda.")            


# Función principal del programa
def main():
    agenda = []
    while True:
        limpiar_pantalla()
        print("Agenda de Contactos")
        print("1. Añadir contacto")
        print("2. Buscar contacto")
        print("3. Borrar contacto")
        print("4. Mostrar Lista completa de Contactos")
        print("5. Tamaño de la agenda")
        print("6. Buscar profesión")
        print("7. Cambiar profesión")
        print("8. Salir de la agenda")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_contacto(agenda)
            input("Presione cualquier tecla para continuar...")
        elif opcion == "2":
            nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
            buscar_contacto(agenda, nombre_buscar)
            input("Presione cualquier tecla para continuar...")
        elif opcion == "3":
            nombre_borrar = input("Ingrese el nombre del contacto a borrar: ")
            borrar_contacto(agenda, nombre_borrar)
            input("Presione cualquier tecla para continuar...")
        elif opcion == "4":
            print("\n")
            mostrar_lista_contactos(agenda)
            input("Presione cualquier tecla para continuar...")
        elif opcion == "5":
            mostrar_tamaño_agenda(agenda)
            input("Presione cualquier tecla para continuar...")
        elif opcion == "6":
            trabajo = input("Introduce la profesión que quieres buscar: ")
            mostrar_por_profesión(agenda, trabajo)
            input("Presiona cualquier tecla para continuar...")
        elif opcion == "7":
            nombre_contacto = input("Introduce el nombre del contacto: ")
            cambiar_profesión(agenda, nombre_contacto)
            input("Presiona cualquier tecla para continuar...")
        elif opcion == "8":
            print("¡Hasta luego!")
            exit()
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presiona cualquier tecla para continuar...")

if __name__ == "__main__":
    main()