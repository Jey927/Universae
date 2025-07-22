# Este programa crea un árbol binario de búsqueda (BST) y permite al usuario insertar valores.
# Luego muestra el recorrido en orden (in-order), que imprime los valores de menor a mayor.

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None  # Hijo izquierdo
        self.derecho = None    # Hijo derecho

# Función para insertar un nuevo valor en el árbol
def insertar(raiz, dato):
    if raiz is None:
        return Nodo(dato)  # Si el árbol está vacío, crea la raíz
    if dato < raiz.dato:
        raiz.izquierdo = insertar(raiz.izquierdo, dato)  # Inserta en el subárbol izquierdo
    else:
        raiz.derecho = insertar(raiz.derecho, dato)      # Inserta en el subárbol derecho
    return raiz

# Recorrido en orden: primero izquierdo, luego raíz, luego derecho
def imprimir_en_orden(raiz):
    if raiz is not None:
        imprimir_en_orden(raiz.izquierdo)
        print(raiz.dato, end=" ")
        imprimir_en_orden(raiz.derecho)

if __name__ == "__main__":
    raiz = None
    print("Introduce valores para el árbol binario (separados por espacio):")
    # El usuario ingresa los valores, por ejemplo: 5 3 8 1 4
    valores = input().split()
    for v in valores:
        raiz = insertar(raiz, int(v))  # Inserta cada valor en el árbol

    print("\nRecorrido en orden (de menor a mayor):")
    imprimir_en_orden(raiz)
    print("\n\n¡Árbol creado y recorrido mostrado!")

# Al ejecutar el programa, el usuario verá cómo se construye el árbol y cómo se imprimen los valores ordenados.