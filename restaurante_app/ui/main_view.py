import tkinter as tk
from tkinter import messagebox


class MainView:

    def __init__(
        self,
        root,
        restaurante_servicio,
        volver_login
    ) -> None:

        self.root = root
        self.restaurante_servicio = (
            restaurante_servicio
        )
        self.volver_login = volver_login

        self.frame = tk.Frame(root)
        self.frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        tk.Label(
            self.frame,
            text="PANEL PRINCIPAL",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        tk.Button(
            self.frame,
            text="Mostrar Productos",
            command=self.mostrar_productos
        ).pack(pady=5)

        tk.Button(
            self.frame,
            text="Mostrar Usuarios",
            command=self.mostrar_usuarios
        ).pack(pady=5)

        tk.Button(
            self.frame,
            text="Ventas (Pendiente)"
        ).pack(pady=5)

        tk.Button(
            self.frame,
            text="Cerrar Sesión",
            command=self.cerrar_sesion
        ).pack(pady=15)

        self.texto = tk.Text(
            self.frame,
            width=70,
            height=15
        )

        self.texto.pack(pady=10)

    def mostrar_productos(self) -> None:

        self.texto.delete(
            "1.0",
            tk.END
        )

        productos = (
            self.restaurante_servicio
            .obtener_productos()
        )

        for producto in productos:

            self.texto.insert(
                tk.END,
                f"{producto.codigo} - "
                f"{producto.nombre} - "
                f"Stock: {producto.stock}\n"
            )

    def mostrar_usuarios(self) -> None:

        self.texto.delete(
            "1.0",
            tk.END
        )

        usuarios = (
            self.restaurante_servicio
            .obtener_usuarios()
        )

        for usuario in usuarios:

            self.texto.insert(
                tk.END,
                f"{usuario.identificacion} - "
                f"{usuario.nombre}\n"
            )

    def cerrar_sesion(self) -> None:

        self.frame.destroy()

        self.volver_login()