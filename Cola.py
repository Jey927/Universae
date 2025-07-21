class Cola:
    def __init__(self):
        self.elementos = []

    def enqueue(self, elemento):
        self.elementos.append(elemento)  # Agrega el elemento al final de la cola

    def dequeue(self):
        if not self.is_empty():
            return self.elementos.pop(0)  # Elimina y retorna el primer elemento (frente)
        else:
            print("La cola está vacía.")
            return None

    def mostrar(self):
        print("Elementos en la cola:", self.elementos)

    def is_empty(self):
        return len(self.elementos) == 0

def menu():
    cola = Cola()
    while True:
        print("\nMenú:")
        print("1. Enqueue (agregar elemento)")
        print("2. Dequeue (eliminar elemento frente)")
        print("3. Mostrar cola")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            elemento = input("Ingresa el elemento: ")
            cola.enqueue(elemento)  # Agrega el elemento al final de la cola
        elif opcion == "2":
            eliminado = cola.dequeue()  # Elimina el elemento del frente
            if eliminado is not None:
                print("Elemento eliminado:", eliminado)
        elif opcion == "3":
            cola.mostrar()  # Muestra todos los elementos de la cola
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
    
