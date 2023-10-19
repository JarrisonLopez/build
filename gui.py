import os
from pathlib import Path
from tkinter import Tk, Canvas, Text, Button, PhotoImage

CURRENT_PATH = Path(__file__).parent
ASSETS_PATH = CURRENT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


class Menu:
    def __init__(self):
        self.window = None
        self.canvas = None

        self.button_image_1 = None

        self.button_image_2 = None

        self.button_image_3 = None

        self.button_image_4 = None

        self.button_image_5 = None

        self.button_image_6 = None

        self.button_image_7 = None

        self.button_image_8 = None

        self.button_image_9 = None

        self.image_image_2 = None

        self.image_image_1 = None

        self.registrar_usuario = None

        self.crear_producto = None

        self.agregar_cantidad_de_producto = None

        self.modificar_producto = None

        self.eliminar_producto = None

        self.registrar_venta = None

        self.mostrar_producto = None

        self.mostrar_usuario = None

        self.cerrar_sesion = None

    def crear_ventana(self):
        self.window = Tk()
        self.window.geometry("360x800")
        self.window.configure(bg="#58A76E")

    def configurar_canvas(self):
        self.canvas = Canvas(
            self.window,
            bg="#58A76E",
            height=800,
            width=360,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            61.999999999999886,
            360.0,
            799.9999999999999,
            fill="#FFFFFF",
            outline="")

    def boton_registrar_usuario(self):
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.registrar_usuario = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.registrar_usuario.place(
            x=12.0,
            y=698.9999999999999,
            width=336.0,
            height=64.0
        )

    def boton_crear_producto(self):
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))

        self.crear_producto = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.crear_producto.place(
            x=12.0,
            y=614.9999999999999,
            width=336.0,
            height=67.0
        )

    def boton_agregar_cantidad_de_producto(self):
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))

        self.agregar_cantidad_de_producto = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.agregar_cantidad_de_producto.place(
            x=13.0,
            y=533.9999999999999,
            width=336.0,
            height=70.0
        )

    def boton_modificar_producto(self):
        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.modificar_producto = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.modificar_producto.place(
            x=15.0,
            y=458.9999999999999,
            width=336.0,
            height=70.0
        )

    def boton_eliminar_producto(self):
        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.eliminar_producto = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.eliminar_producto.place(
            x=6.0,
            y=381.9999999999999,
            width=345.0,
            height=67.0
        )

    def boton_registrar_venta(self):
        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.registrar_venta = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        self.registrar_venta.place(
            x=13.0,
            y=302.9999999999999,
            width=336.0,
            height=72.0
        )

    def boton_mostrar_producto(self):
        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.mostrar_producto = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        self.mostrar_producto.place(
            x=12.0,
            y=225.9999999999999,
            width=336.0,
            height=72.0
        )

    def boton_mostrar_usuario(self):
        self.button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.mostrar_usuario = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        self.mostrar_usuario.place(
            x=6.0,
            y=153.9999999999999,
            width=342.0,
            height=75.0
        )

    def boton_cerrar_sesion(self):
        self.button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png"))
        self.cerrar_sesion = Button(
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        self.cerrar_sesion.place(
            x=9.0,
            y=73.99999999999989,
            width=340.0,
            height=80.0
        )

    def logo(self):
        self.canvas.create_text(
            70.0,
            15.999999999999886,
            anchor="nw",
            text="ADMINISTRADOR",
            fill="#000000",
            font=("Inter", 25 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            43.744140625,
            34.80435180664051,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            43.937477111816406,
            26.874999999999886,
            image=self.image_image_2
        )

    def iniciar_ventana(self):
        self.window.resizable(False, False)
        self.window.mainloop()

    def iniciar_menu_admin(self):

        self.crear_ventana()
        self.configurar_canvas()
        self.boton_registrar_usuario()
        self.boton_crear_producto()
        self.boton_agregar_cantidad_de_producto()
        self.boton_modificar_producto()
        self.boton_eliminar_producto()
        self.boton_registrar_venta()
        self.boton_mostrar_producto()
        self.boton_mostrar_usuario()
        self.boton_cerrar_sesion()
        self.logo()
        self.iniciar_ventana()


ventana = Menu()
ventana.iniciar_menu_admin()
