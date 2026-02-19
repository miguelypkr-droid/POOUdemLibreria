from main import Libro, Usuario, Biblioteca


# crear biblioteca y usuario

nombre_biblioteca = input("Nombre de la biblioteca: ")
biblioteca = Biblioteca(nombre_biblioteca)

nombre_usuario = input("Nombre del usuario: ")
usuario = Usuario(nombre_usuario)


while True:

    print("\n--- MENÚ ---")
    print("1. Agregar libro")
    print("2. Mostrar libros disponibles")
    print("3. Tomar libro prestado")
    print("4. Mostrar libros prestados")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")


    # AGREGAR LIBRO
    if opcion == "1":

        titulo = input("Titulo: ")
        autor = input("Autor: ")
        año = int(input("Año: "))

        libro = Libro(titulo, autor, año)

        biblioteca.agregar_libro(libro)

        print("Libro agregado correctamente.")


    # MOSTRAR LIBROS DISPONIBLES (CORREGIDO)
    elif opcion == "2":

        if not biblioteca.libros:

            print("No hay libros disponibles.")

        else:

            print("\nLibros disponibles:")

            for libro in biblioteca.libros:

                print(libro.mostrar_info())


    # TOMAR LIBRO PRESTADO
    elif opcion == "3":

        titulo = input("Titulo del libro a prestar: ")

        encontrado = None

        for libro in biblioteca.libros:

            if libro.titulo == titulo:

                encontrado = libro
                break


        if encontrado:

            usuario.tomar_prestado(encontrado)

            biblioteca.libros.remove(encontrado)

            print("Libro prestado correctamente.")

        else:

            print("Libro no encontrado.")


    # MOSTRAR LIBROS PRESTADOS (CORREGIDO)
    elif opcion == "4":

        libros = usuario.mostrar_libros()

        if not libros:

            print("No tienes libros prestados.")

        else:

            print("\nLibros prestados:")

            for libro in libros:

                print(libro.mostrar_info())


    # SALIR
    elif opcion == "5":

        print("Programa finalizado.")

        break


    else:

        print("Opción inválida.")
