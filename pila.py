class PilaVaciaError(Exception):
    pass

class Pila:
    def __init__(self):
        self._elementos = []

    def apilar(self, elemento):
        self._elementos.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")
        return self._elementos.pop()

    def cima(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")
        return self._elementos[-1]

    def esta_vacia(self):
        return len(self._elementos) == 0

    def limpiar(self):
        self._elementos.clear()