from usuarios import Usuario, GestionUsuarios

def mostrar_menu():
    print("\n--- Gestión de Usuarios ---")
    print("1. Registrar usuario")
    print("2. Buscar usuario por nombre o ID")
    print("3. Eliminar usuario por ID")
    print("4. Actualizar usuario")
    print("5. Listar todos los usuarios")
    print("6. Salir")

def main():
    gestion = GestionUsuarios()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            usuario_id = input("ID de usuario: ")
            nombre = input("Nombre: ")
            email = input("Email: ")
            gestion.registrarUsuario(Usuario(usuario_id, nombre, email))
            print("Usuario registrado.")
        elif opcion == "2":
            criterio = input("Nombre o ID a buscar: ")
            resultados = gestion.buscarUsuario(criterio)
            if resultados:
                for usuario in resultados:
                    print(usuario)
            else:
                print("No se encontraron usuarios.")
        elif opcion == "3":
            usuario_id = input("ID de usuario a eliminar: ")
            if gestion.eliminarUsuario(usuario_id):
                print("Usuario eliminado.")
            else:
                print("No se encontró el usuario con ese ID.")
        elif opcion == "4":
            usuario_id = input("ID de usuario a actualizar: ")
            nombre = input("Nuevo nombre (deja vacío para no cambiar): ")
            email = input("Nuevo email (deja vacío para no cambiar): ")
            if gestion.actualizarUsuario(usuario_id, nombre if nombre else None, email if email else None):
                print("Usuario actualizado.")
            else:
                print("No se encontró el usuario con ese ID.")
        elif opcion == "5":
            usuarios = gestion.listarUsuarios()
            if usuarios:
                for usuario in usuarios:
                    print(usuario)
            else:
                print("No hay usuarios registrados.")
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()