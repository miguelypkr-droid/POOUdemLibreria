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
        self.libros_prestados.append(libro) # agarra libro
        self