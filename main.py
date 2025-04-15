from contacto_modelo import Contacto

def mostrar_menu():
    print("\nGestión de Contactos")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Actualizar contacto")
    print("5. Mostrar todos")
    print("6. Salir")

def main():
    agenda = Contacto()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo electrónico: ")
            telefono = input("Teléfono: ")
            agenda.agregar_contacto(nombre, apellido, correo, telefono)

        elif opcion == "2":
            codigo = int(input("Código del contacto a eliminar: "))
            agenda.eliminar_contacto(codigo)

        elif opcion == "3":
            termino = input("Nombre o correo: ")
            resultados = agenda.buscar_contacto(termino)
            for c in resultados:
                print(c)

        elif opcion == "4":
            codigo = int(input("Código del contacto a actualizar: "))
            nombre = input("Nuevo nombre: ")
            apellido = input("Nuevo apellido: ")
            correo = input("Nuevo correo: ")
            telefono = input("Nuevo teléfono: ")
            agenda.actualizar_contacto(codigo, nombre, apellido, correo, telefono)

        elif opcion == "5":
            for c in agenda.obtener_todos():
                print(c)

        elif opcion == "6":
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
