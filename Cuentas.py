import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Cuentas:
    """
    dibuja la ventana de las cuentas,
    que al serr clickeado el boton mostrara un popup con la data de las cuentas
    """
    def __init__ (self):
        self.ventana_cuentas=tk.Tk()
        self.ventana_cuentas.geometry("500x500")
        self.crear_cuentas = ttk.Button(self.ventana_cuentas,text="Nueva Cuenta",command=self.dibuja_creacuentas)
        self.crear_cuentas.grid(column=0,row=0)
        self.ventana_cuentas.mainloop()

    def dibuja_creacuentas(self):
        self.cuenta = Creacioncuentas(self.ventana_cuentas)
        return self.cuenta

class Creacioncuentas:    
    def __init__(self,ventanaprincipal):
        """
        ventana para crear cuentas nuevas
        """
        self.ventana_crear_cuentas=tk.Toplevel(ventanaprincipal)
        self.ventana_crear_cuentas.title("Registrar nueva cuenta")
        self.ventana_crear_cuentas.geometry("300x300")
        self.nombre_sitio = ttk.Label(self.ventana_crear_cuentas,text="Nombre sitio:")
        self.nombre_sitio.grid(column=0,row=0)
        self.registra_sitio = tk.StringVar()
        self.entrada_sitio = ttk.Entry(self.ventana_crear_cuentas,width=25,textvariable=self.registra_sitio)
        self.entrada_sitio.grid(column=1,row=0)
        self.url_sitio = ttk.Label(self.ventana_crear_cuentas,text="URL sitio:")
        self.url_sitio.grid(column=0,row=1)
        self.registra_url = tk.StringVar()
        self.entrada_url = ttk.Entry(self.ventana_crear_cuentas,width=25,textvariable=self.registra_url)
        self.entrada_url.grid(column=1,row=1)
        self.login = ttk.Label(self.ventana_crear_cuentas,text="Usuario/Mail:")
        self.login.grid(column=0,row=2)
        self.registra_login = tk.StringVar()
        self.entrada_login = ttk.Entry(self.ventana_crear_cuentas,width=25,textvariable=self.registra_login)
        self.entrada_login.grid(column=1,row=2)
        self.pwwd = ttk.Label(self.ventana_crear_cuentas,text="Contraseña:")
        self.pwwd.grid(column=0,row=3)
        self.registra_pwwd = tk.StringVar()
        self.entrada_pwwd = ttk.Entry(self.ventana_crear_cuentas,width=25,textvariable=self.registra_pwwd)
        self.entrada_pwwd.grid(column=1,row=3)
        self.confirma_pwwd = ttk.Label(self.ventana_crear_cuentas,text="Confirmar contraseña:")
        self.confirma_pwwd.grid(column=0,row=4)
        self.registra_confirma_pwwd = tk.StringVar()
        self.entrada_confirma_pwwd = ttk.Entry(self.ventana_crear_cuentas,width=25,textvariable=self.registra_confirma_pwwd)
        self.entrada_confirma_pwwd.grid(column=1,row=4)
        self.boton_cancelar = ttk.Button(self.ventana_crear_cuentas,text="Cancelar", command=self.ventana_crear_cuentas.destroy)
        self.boton_cancelar.grid(column=0,row=5)
        self.boton_aceptar = ttk.Button(self.ventana_crear_cuentas,text="Aceptar", command=self.verifica_contra)
        self.boton_aceptar.grid(column=1,row=5)
        self.ventana_crear_cuentas.mainloop()

    def verifica_contra(self):
        pwwd = str(self.registra_pwwd.get())
        confirma_pwwd = str(self.registra_confirma_pwwd.get())
        if pwwd == confirma_pwwd:
            self.mensaje_exito = messagebox.showinfo(title="resultado", message="¡las contraseñas coinciden!",parent=self.ventana_crear_cuentas)
        else:
            self.mensaje_exito = messagebox.showwarning(title="resultado", message="¡las contraseñas no coinciden!",parent=self.ventana_crear_cuentas)
app1 = Cuentas()