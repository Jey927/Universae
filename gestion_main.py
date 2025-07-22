from libros import Libro, GestionLibros

def mostrar_menu():
    print("\n--- Gestión de Libros ---")
    print("1. Agregar libro")
    print("2. Buscar libro por título")
    print("3. Eliminar libro por ISBN")
    print("4. Listar todos los libros")
    print("5. Salir")

def main():
    gestion = GestionLibros()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            gestion.agregar_libro(Libro(titulo, autor, isbn))
            print("Libro agregado.")
        elif opcion == "2":
            titulo = input("Título a buscar: ")
            resultados = gestion.buscar_libro(titulo)
            if resultados:
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros.")
        elif opcion == "3":
            isbn = input("ISBN a eliminar: ")
            if gestion.eliminar_libro(isbn):
                print("Libro eliminado.")
            else:
                print("No se encontró el libro con ese ISBN.")
        elif opcion == "4":
            libros = gestion.listar_libros()
            if libros:
                for libro in libros:
                    print(libro)
            else:
                print("No hay libros en el catálogo.")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()