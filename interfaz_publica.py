# Tipo de dato abstracto: Pila (Stack) con interfaz pública

class Pila:
    def __init__(self):
        # Inicializa la pila como una lista vacía
        self.elementos = []

    def apilar(self, elemento):
        # Agrega un elemento al tope de la pila
        self.elementos.append(elemento)

    def desapilar(self):
        # Elimina y retorna el elemento del tope de la pila
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            print("La pila está vacía.")
            return None

    def cima(self):
        # Retorna el elemento del tope sin eliminarlo
        if not self.esta_vacia():
            return self.elementos[-1]
        else:
            print("La pila está vacía.")
            return None

    def esta_vacia(self):
        # Verifica si la pila está vacía
        return len(self.elementos) == 0

    def mostrar(self):
        # Muestra todos los elementos de la pila
        print("Pila:", self.elementos)

def mostrar_menu():
    # Muestra el menú de opciones al usuario
    print("\n--- Menú de Pila ---")
    print("1. Apilar elemento")
    print("2. Desapilar elemento")
    print("3. Ver cima")
    print("4. Mostrar pila")
    print("5. Salir")

def main():
    # Crea una instancia de la pila
    pila = Pila()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            # Apila un elemento ingresado por el usuario
            elemento = input("Introduce el elemento a apilar: ")
            pila.apilar(elemento)
        elif opcion == "2":
            # Desapila el elemento del tope y lo muestra
            desapilado = pila.desapilar()
            if desapilado is not None:
                print(f"Elemento desapilado: {desapilado}")
        elif opcion == "3":
            # Muestra el elemento en la cima de la pila
            cima = pila.cima()
            if cima is not None:
                print(f"Cima de la pila: {cima}")
        elif opcion == "4":
            # Muestra todos los elementos de la pila
            pila.mostrar()
        elif opcion == "5":
            # Sale del programa
            print("¡Programa finalizado!")
            break
        else:
            # Informa si la opción no es válida
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()