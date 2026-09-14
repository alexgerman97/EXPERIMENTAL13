import tkinter as tk

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


def main() -> None:

    root = tk.Tk()

    root.title("Restaurante App")
    root.geometry("700x500")

    archivo_servicio = ArchivoServicio()

    restaurante_servicio = RestauranteServicio(
        archivo_servicio
    )

    def mostrar_login() -> None:

        LoginView(
            root,
            restaurante_servicio,
            mostrar_main
        )

    def mostrar_main() -> None:

        MainView(
            root,
            restaurante_servicio,
            mostrar_login
        )

    mostrar_login()

    root.mainloop()


if __name__ == "__main__":
    main()