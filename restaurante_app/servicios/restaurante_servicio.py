from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:

    def __init__(self, productos_data, usuarios_data):

        self.productos = []
        self.usuarios = []

        self.cargar_productos(productos_data)
        self.cargar_usuarios(usuarios_data)

    def cargar_productos(self, datos):

        for producto in datos:

          self.productos.append(
            Producto(
                producto["codigo"],
                producto["nombre"],
                producto["categoria"],
                producto["precio"],
                producto["stock"]
            )
        )

    def cargar_usuarios(self, datos):

        for usuario in datos:

            self.usuarios.append(
                Usuario(
                    usuario["usuario"],
                    usuario["password"],
                    usuario["nombre"]
                )
            )

    def validar_login(self, usuario, contrasena):

        for u in self.usuarios:

            if (
                u.usuario == usuario and
                u.password == contrasena
            ):
                return True

        return False

    def listar_productos(self):
        return self.productos

    def listar_usuarios(self):
        return self.usuarios