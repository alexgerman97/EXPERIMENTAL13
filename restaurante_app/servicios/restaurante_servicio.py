from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

    def __init__(
        self,
        archivo_servicio: ArchivoServicio
    ) -> None:

        self.archivo_servicio = archivo_servicio

        self.productos = self._cargar_productos()
        self.usuarios = self._cargar_usuarios()

    def _cargar_productos(
        self
    ) -> list[Producto]:

        datos = (
            self.archivo_servicio
            .cargar_productos()
        )

        productos = []

        for producto in datos:

            productos.append(
                Producto(
                    producto["codigo"],
                    producto["nombre"],
                    producto["categoria"],
                    producto["precio"],
                    producto["stock"]
                )
            )

        return productos

    def _cargar_usuarios(
        self
    ) -> list[Usuario]:

        datos = (
            self.archivo_servicio
            .cargar_usuarios()
        )

        usuarios = []

        for usuario in datos:

            usuarios.append(
                Usuario(
                    usuario["identificacion"],
                    usuario["nombre"],
                    usuario["correo"]
                )
            )

        return usuarios

    def validar_login(
        self,
        usuario: str,
        contrasena: str
    ) -> bool:

        return (
            usuario == "admin"
            and
            contrasena == "1234"
        )

    def obtener_productos(
        self
    ) -> list[Producto]:

        return self.productos

    def obtener_usuarios(
        self
    ) -> list[Usuario]:

        return self.usuarios