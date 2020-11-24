import tkinter as tk
from tkinter import Grid, ttk
from tkinter import messagebox
from Cuentas import cuenta
from Cifrado import Cifrado


class index:
    """
    dibuja la ventana de las cuentas,
    que al serr clickeado el boton mostrara un popup con la data de las cuentas
    """
    def __init__(
                self,
                id_usuario,
                password,
                nom_usu):
        self.id_usuario = id_usuario
        self.master_password = password
        self.nombre_usuario = nom_usu
        self.data_cuenta = []
        self.boton_cuentas = {}
        self.ventana_cuentas = tk.Tk()
        self.titulo = "Cuentas de " + self.nombre_usuario
        self.ventana_cuentas.title(self.titulo)
        self.ventana_cuentas.geometry("300x400")
        self.frame_ops = ttk.Frame()
        self.frame_ops.grid(column=0, row=0)
        self.labelframe_operaciones = ttk.LabelFrame(self.frame_ops)
        self.labelframe_operaciones.grid(column=1, row=0)
        self.crear_cuentas = ttk.Button(self.labelframe_operaciones,
                                        text="Nueva Cuenta",
                                        command=self.dibuja_creacuentas)
        self.crear_cuentas.grid(column=0, row=0)
        self.actualizar = ttk.Button(self.labelframe_operaciones,
                                        text="Actualizar Ventana",
                                        command=self.refresh)
        self.actualizar.grid(column=1, row=0)
        self.dibuja_botones()
        
        self.ventana_cuentas.mainloop()

    def dibuja_botones(self):
        """
        dibuja dinamicamente los botones de las cuentas
        """
        self.master_password = str(self.master_password)
        self.id_usuario = str(self.id_usuario)
        self.test_var = cuenta(
                                master_password=self.master_password,
                                id_usuario=self.id_usuario).verificar_cuentas()
        for row in self.test_var:
            sal = row[4]
            self.cifrado = Cifrado(self.master_password)
            cifrado_pass = self.cifrado.verificar_cifrado(sal)
            self.data_cuenta.append(self.cifrado.descifrado_suave(
                                                                row[0],
                                                                row[1],
                                                                row[2],
                                                                row[3],
                                                                cifrado_pass))
        self.info_cuentas = self.data_cuenta
        self.i = 1
        self.j = 0
        self.frame = ttk.Frame(self.ventana_cuentas)
        self.frame.grid(column=0, row=1)
        if self.info_cuentas is not None:
            for row in self.info_cuentas:
                self.labelframe_cuentas = ttk.LabelFrame(self.frame)
                self.labelframe_cuentas.grid(column=self.j,row=self.i)
                self.boton_cuentas[row[self.i]] = ttk.Button(self.labelframe_cuentas,
                                                            text=row[0])
                self.boton_cuentas[row[self.i]].grid(column=0, row=0)
                self.j = self.j + 1
                if self.j > 2:
                    self.j = 0
                    self.i = self.i + 1
        else:
            pass
        self.data_cuenta.clear()
    def dibuja_creacuentas(self):
        self.cuenta = Creacioncuentas(
                                    self.ventana_cuentas,
                                    self.id_usuario,
                                    self.master_password)
        return self.cuenta

    def refresh(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.grid_forget()
        self.dibuja_botones()

class Creacioncuentas:
    def __init__(
                self,
                ventanaprincipal,
                id_usuario,
                password):
        """
        ventana para crear cuentas nuevas
        """
        self.id_usuario = id_usuario
        self.master_password = password
        self.ventana_crear_cuentas = tk.Toplevel(ventanaprincipal)
        self.ventana_crear_cuentas.title("Registrar nueva cuenta")
        self.ventana_crear_cuentas.geometry("300x300")
        self.nombre_sitio = ttk.Label(
                                    self.ventana_crear_cuentas,
                                    text="Nombre sitio:")
        self.nombre_sitio.grid(column=0, row=0)
        self.registra_sitio = tk.StringVar()
        self.entrada_sitio = ttk.Entry(
                                    self.ventana_crear_cuentas,
                                    width=25,
                                    textvariable=self.registra_sitio)
        self.entrada_sitio.grid(column=1, row=0)
        self.url_sitio = ttk.Label(
                                self.ventana_crear_cuentas,
                                text="URL sitio:")
        self.url_sitio.grid(column=0, row=1)
        self.registra_url = tk.StringVar()
        self.entrada_url = ttk.Entry(
                                    self.ventana_crear_cuentas,
                                    width=25,
                                    textvariable=self.registra_url)
        self.entrada_url.grid(column=1, row=1)
        self.login = ttk.Label(
                            self.ventana_crear_cuentas,
                            text="Usuario/Mail:")
        self.login.grid(column=0, row=2)
        self.registra_login = tk.StringVar()
        self.entrada_login = ttk.Entry(
                                    self.ventana_crear_cuentas,
                                    width=25,
                                    textvariable=self.registra_login)
        self.entrada_login.grid(column=1, row=2)
        self.pwwd = ttk.Label(
                            self.ventana_crear_cuentas,
                            text="Contraseña:")
        self.pwwd.grid(column=0, row=3)
        self.registra_pwwd = tk.StringVar()
        self.entrada_pwwd = ttk.Entry(
                                    self.ventana_crear_cuentas,
                                    width=25,
                                    show="*",
                                    textvariable=self.registra_pwwd)
        self.entrada_pwwd.grid(column=1, row=3)
        self.confirma_pwwd = ttk.Label(
                                    self.ventana_crear_cuentas,
                                    text="Confirmar contraseña:")
        self.confirma_pwwd.grid(column=0, row=4)
        self.registra_confirma_pwwd = tk.StringVar()
        self.entrada_confirma_pwwd = ttk.Entry(
                                            self.ventana_crear_cuentas,
                                            width=25,
                                            show="*",
                                            textvariable=self.registra_confirma_pwwd)
        self.entrada_confirma_pwwd.grid(column=1, row=4)
        self.boton_cancelar = ttk.Button(
                                        self.ventana_crear_cuentas,
                                        text="Cancelar",
                                        command=self.ventana_crear_cuentas.destroy)
        self.boton_cancelar.grid(column=0, row=5)
        self.boton_aceptar = ttk.Button(
                                        self.ventana_crear_cuentas,
                                        text="Aceptar",
                                        command=self.verifica_contra)
        self.boton_aceptar.grid(column=1, row=5)
        self.ventana_crear_cuentas.mainloop()

    def verifica_contra(self):
        registra_sitio = str(self.registra_sitio.get())
        registra_url = str(self.registra_url.get())
        registra_login = str(self.registra_login.get())
        registra_pwwd = str(self.registra_pwwd.get())
        confirma_pwwd = str(self.registra_confirma_pwwd.get())
        if registra_pwwd == confirma_pwwd:
            self.cuenta_nueva = cuenta(
                                    self.id_usuario,
                                    registra_sitio,
                                    registra_url,
                                    registra_login,
                                    registra_pwwd,
                                    self.master_password).crear_cuenta()
            self.mensaje_exito = messagebox.showinfo(
                                                    title="resultado",
                                                    message="¡Registro realizado con éxito! "+self.cuenta_nueva,
                                                    parent=self.ventana_crear_cuentas)
            self.ventana_crear_cuentas.destroy()
        else:
            self.mensaje_exito = messagebox.showwarning(
                                                    title="resultado",
                                                    message="¡las contraseñas no coinciden!",
                                                    parent=self.ventana_crear_cuentas)
