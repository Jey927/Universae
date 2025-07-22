from prestamos import GestionPrestamos

def mostrar_menu():
    print("\n--- Gestión de Préstamos ---")
    print("1. Realizar préstamo")
    print("2. Devolver libro")
    print("3. Buscar préstamos por usuario")
    print("4. Generar informe de préstamos")
    print("5. Salir")

def main():
    gestion = GestionPrestamos()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            usuario_id = input("ID de usuario: ")
            libro_isbn = input("ISBN del libro: ")
            if gestion.realizarPrestamo(usuario_id, libro_isbn):
                print("Préstamo realizado.")
            else:
                print("El libro ya está prestado y no ha sido devuelto.")
        elif opcion == "2":
            libro_isbn = input("ISBN del libro a devolver: ")
            if gestion.devolverLibro(libro_isbn):
                print("Libro devuelto correctamente.")
            else:
                print("No se encontró un préstamo activo para ese libro.")
        elif opcion == "3":
            usuario_id = input("ID de usuario: ")
            prestamos = gestion.buscarPrestamosPorUsuario(usuario_id)
            if prestamos:
                for p in prestamos:
                    print(p)
            else:
                print("No se encontraron préstamos para ese usuario.")
        elif opcion == "4":
            informe = gestion.generarInformePrestamos()
            if informe:
                for p in informe:
                    print(p)
            else:
                print("No hay préstamos registrados.")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()