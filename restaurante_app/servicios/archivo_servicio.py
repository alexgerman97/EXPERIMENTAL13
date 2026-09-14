import json


class ArchivoServicio:

    def __init__(self) -> None:

        self.archivo_productos = (
            "restaurante_app/datos/productos.json"
        )

        self.archivo_usuarios = (
            "restaurante_app/datos/usuarios.json"
        )

    def cargar_productos(self) -> list:

        try:

            with open(
                self.archivo_productos,
                "r",
                encoding="utf-8"
            ) as archivo:

                return json.load(archivo)

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            return []

    def cargar_usuarios(self) -> list:

        try:

            with open(
                self.archivo_usuarios,
                "r",
                encoding="utf-8"
            ) as archivo:

                return json.load(archivo)

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            return []