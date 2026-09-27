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
            text="PANEL PRINCIPAL DEL RESTAURANTE",
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
            .listar_productos()
        )

        self.texto.insert(
            tk.END,
            "=== PRODUCTOS REGISTRADOS ===\n\n"
        )

        for producto in productos:

            self.texto.insert(
                tk.END,
                f"Código: {producto.codigo}\n"
                f"Nombre: {producto.nombre}\n"
                f"Categoría: {producto.categoria}\n"
                f"Precio: ${producto.precio}\n"
                f"Stock: {producto.stock}\n\n"
            )

    def mostrar_usuarios(self) -> None:

        self.texto.delete(
            "1.0",
            tk.END
        )

        usuarios = (
            self.restaurante_servicio
            .listar_usuarios()
        )

        self.texto.insert(
            tk.END,
            "=== USUARIOS REGISTRADOS ===\n\n"
        )

        for usuario in usuarios:

            self.texto.insert(
                tk.END,
                f"Usuario: {usuario.usuario}\n"
                f"Nombre: {usuario.nombre}\n\n"
            )

    def cerrar_sesion(self) -> None:

        respuesta = messagebox.askyesno(
            "Cerrar sesión",
            "¿Desea cerrar sesión?"
        )

        if respuesta:

            self.frame.destroy()

            self.volver_login()