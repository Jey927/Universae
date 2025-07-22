class _Cola:
    def __init__(self):
        # La lista de elementos es privada (convención: guion bajo)
        self._elementos = []

    def _encolar(self, elemento):
        # Método privado para agregar un elemento al final de la cola
        self._elementos.append(elemento)

    def _desencolar(self):
        # Método privado para quitar y retornar el primer elemento de la cola
        if not self._esta_vacia():
            return self._elementos.pop(0)
        else:
            print("La cola está vacía.")
            return None

    def _esta_vacia(self):
        # Método privado para verificar si la cola está vacía
        return len(self._elementos) == 0

    def _mostrar(self):
        # Método privado para mostrar los elementos de la cola
        print("Cola:", self._elementos)

def main():
    cola = _Cola()
    # Interacción básica usando la interfaz privada (solo para ilustrar)
    cola._encolar("A")
    cola._encolar("B")
    cola._encolar("C")
    cola._mostrar()
    print("Desencolando:", cola._desencolar())
    cola._mostrar()

if __name__ == "__main__":
    main()