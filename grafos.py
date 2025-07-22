# Programa básico para comprender el concepto de grafo dirigido

class Grafo:
    def __init__(self):
        self.nodos = set()
        self.aristas = []

    def agregar_nodo(self, nodo):
        self.nodos.add(nodo)

    def agregar_arista(self, origen, destino):
        self.aristas.append((origen, destino))
        self.nodos.add(origen)
        self.nodos.add(destino)

    def mostrar(self):
        print("Nodos:", self.nodos)
        print("Aristas:", self.aristas)

def mostrar_menu():
    print("\n--- Menú de Grafo ---")
    print("1. Agregar nodo")
    print("2. Agregar arista")
    print("3. Mostrar nodos y aristas")
    print("4. Salir")

def main():
    grafo = Grafo()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            nodo = input("Introduce el nombre del nodo: ")
            grafo.agregar_nodo(nodo)
            print(f"Nodo '{nodo}' agregado.")
        elif opcion == "2":
            origen = input("Nodo origen: ")
            destino = input("Nodo destino: ")
            grafo.agregar_arista(origen, destino)
            print(f"Arista '{origen}' - '{destino}' agregada.")
        elif opcion == "3":
            grafo.mostrar()
        elif opcion == "4":
            print("¡Programa finalizado!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()