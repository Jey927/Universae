from datetime import datetime

class Prestamo:
    def __init__(self, usuario_id, libro_isbn, fecha_prestamo=None, fecha_devolucion=None):
        self.usuario_id = usuario_id
        self.libro_isbn = libro_isbn
        self.fecha_prestamo = fecha_prestamo or datetime.now()
        self.fecha_devolucion = fecha_devolucion

    def __str__(self):
        estado = "Devuelto" if self.fecha_devolucion else "En préstamo"
        fecha_dev = self.fecha_devolucion.strftime("%Y-%m-%d %H:%M") if self.fecha_devolucion else "Pendiente"
        return (f"Usuario: {self.usuario_id} | Libro: {self.libro_isbn} | "
                f"Fecha préstamo: {self.fecha_prestamo.strftime('%Y-%m-%d %H:%M')} | "
                f"Fecha devolución: {fecha_dev} | Estado: {estado}")

class GestionPrestamos:
    def __init__(self):
        self._prestamos = []

    def realizarPrestamo(self, usuario_id, libro_isbn):
        # Verifica si el libro ya está prestado y no devuelto
        for p in self._prestamos:
            if p.libro_isbn == libro_isbn and p.fecha_devolucion is None:
                return False  # Libro ya prestado
        prestamo = Prestamo(usuario_id, libro_isbn)
        self._prestamos.append(prestamo)
        return True

    def devolverLibro(self, libro_isbn):
        for p in self._prestamos:
            if p.libro_isbn == libro_isbn and p.fecha_devolucion is None:
                p.fecha_devolucion = datetime.now()
                return True
        return False  # No se encontró préstamo activo

    def buscarPrestamosPorUsuario(self, usuario_id):
        return [p for p in self._prestamos if p.usuario_id == usuario_id]

    def generarInformePrestamos(self):
        return self._prestamos