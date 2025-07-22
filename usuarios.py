class Usuario:
    def __init__(self, usuario_id, nombre, email):
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"ID: {self.usuario_id} | Nombre: {self.nombre} | Email: {self.email}"

class GestionUsuarios:
    def __init__(self):
        self._usuarios = []

    def registrarUsuario(self, usuario):
        self._usuarios.append(usuario)

    def eliminarUsuario(self, usuario_id):
        original = len(self._usuarios)
        self._usuarios = [u for u in self._usuarios if u.usuario_id != usuario_id]
        return len(self._usuarios) < original

    def buscarUsuario(self, criterio):
        # Busca por nombre o ID (parcial)
        return [u for u in self._usuarios if criterio.lower() in u.nombre.lower() or criterio == str(u.usuario_id)]

    def actualizarUsuario(self, usuario_id, nombre=None, email=None):
        for u in self._usuarios:
            if u.usuario_id == usuario_id:
                if nombre:
                    u.nombre = nombre
                if email:
                    u.email = email
                return True
        return False

    def listarUsuarios(self):
        return self._usuarios