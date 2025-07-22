class PilaVaciaError(Exception):
    """Excepción personalizada para pila vacía."""
    pass

class Pila:
    def __init__(self, limite=None):
        # Inicializa la pila y opcionalmente un límite de elementos
        self._elementos = []
        self._limite = limite

    def apilar(self, elemento):
        # Agrega un elemento al tope de la pila, verifica el límite
        if self._limite is not None and len(self._elementos) >= self._limite:
            print("La pila está llena. No se puede apilar más elementos.")
        else:
            self._elementos.append(elemento)

    def desapilar(self):
        # Elimina y retorna el elemento del tope, lanza excepción si está vacía
        if self.esta_vacia():
            raise PilaVaciaError("No se puede desapilar: la pila está vacía.")
        return self._elementos.pop()

    def cima(self):
        # Retorna el elemento del tope sin eliminarlo
        if self.esta_vacia():
            raise PilaVaciaError("No se puede consultar la cima: la pila está vacía.")
        return self._elementos[-1]

    def esta_vacia(self):
        # Verifica si la pila está vacía
        return len(self._elementos) == 0

    def mostrar(self):
        # Muestra todos los elementos de la pila
        print("Pila:", self._elementos)

def mostrar_menu():
    print("\n--- Menú de Pila Avanzada ---")
    print("1. Apilar elemento")
    print("2. Desapilar elemento")
    print("3. Ver cima")
    print("4. Mostrar pila")
    print("5. Salir")

def main():
    limite = input("¿Deseas establecer un límite de elementos en la pila? (deja vacío para ilimitada): ")
    pila = Pila(int(limite) if limite.isdigit() else None)
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            elemento = input("Introduce el elemento a apilar: ")
            pila.apilar(elemento)
        elif opcion == "2":
            try:
                desapilado = pila.desapilar()
                print(f"Elemento desapilado: {desapilado}")
            except PilaVaciaError as e:
                print(e)
        elif opcion == "3":
            try:
                cima = pila.cima()
                print(f"Cima de la pila: {cima}")
            except PilaVaciaError as e:
                print(e)
        elif opcion == "4":
            pila.mostrar()
        elif opcion == "5":
            print("¡Programa finalizado!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()