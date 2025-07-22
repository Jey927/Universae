class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} - {self.autor} (ISBN: {self.isbn})"

class GestionLibros:
    def __init__(self):
        self._catalogo = []

    def agregar_libro(self, libro):
        self._catalogo.append(libro)

    def buscar_libro(self, titulo):
        return [libro for libro in self._catalogo if titulo.lower() in libro.titulo.lower()]

    def eliminar_libro(self, isbn):
        original = len(self._catalogo)
        self._catalogo = [libro for libro in self._catalogo if libro.isbn != isbn]
        return len(self._catalogo) < original

    def listar_libros(self):
        return self._catalogo