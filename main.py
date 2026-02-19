class Libro:

    def __init__(self, titulo: str, autor: str, año: int):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def mostrar_info(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}"

class Usuario:

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros_prestados = []

    def tomar_prestado(self, libro: Libro):
        self.libros_prestados.append(libro) # la clase Libro se agarra y se pone como una variable llamada libro, que se agrega a la lista libros_prestados

    def mostrar_libros(self):
        return self.libros_prestados

class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        print(f"Libros disponibles {self.libros}")