import heapq

class ColaPrioridad:
    def __init__(self):
        self.cola = []

    def enqueue(self, elemento, prioridad):
        # heapq usa min-heap, así que invertimos la prioridad para que 1 sea la más alta
        heapq.heappush(self.cola, (prioridad, elemento))

    def dequeue(self):
        if not self.is_empty():
            prioridad, elemento = heapq.heappop(self.cola)
            return elemento
        else:
            print("La cola de prioridad está vacía.")
            return None

    def mostrar(self):
        print("Elementos en la cola de prioridad (menor número = mayor prioridad):")
        for prioridad, elemento in sorted(self.cola):
            print(f"Elemento: {elemento}, Prioridad: {prioridad}")

    def is_empty(self):
        return len(self.cola) == 0

def menu():
    cola = ColaPrioridad()
    while True:
        print("\nMenú Cola de Prioridad:")
        print("1. Enqueue (agregar elemento con prioridad)")
        print("2. Dequeue (eliminar elemento de mayor prioridad)")
        print("3. Mostrar cola de prioridad")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            elemento = input("Ingresa el elemento: ")
            prioridad = int(input("Ingresa la prioridad (número, menor = mayor prioridad): "))
            cola.enqueue(elemento, prioridad)
        elif opcion == "2":
            eliminado = cola.dequeue()
            if eliminado is not None:
                print("Elemento eliminado:", eliminado)
        elif opcion == "3":
            cola.mostrar()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()