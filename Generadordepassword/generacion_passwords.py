import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from turtle import width

ventana = tk.Tk()
ventana.title("Generador de password")
ventana.config(width=300, height=300)

def generador():
    minus = " abcdefghijklmnopqrstuvwxyz "
    mayus = minus.upper()
    numeros = " 0123456789 "
    simbolos = " a()[]{}*,;/-_¿?¡!$#>6+% "
    base = minus+mayus+numeros+simbolos
    temp_log = int(caja_log.get())
    muestra = random.sample(base , temp_log  )
    password = "".join(muestra)
    etiqueta_resultado.config(text=f"Password:  {password}")

log = ttk.Label(text="Ingresar la longitud de la contraseña: :")
log.place(x=20, y=20)

caja_log = ttk.Entry()
caja_log.place(x=220, y=20, width=60)

boton_pass = ttk.Button( text="Password" , command=generador)
boton_pass.place(x=20, y=60)

etiqueta_resultado = ttk.Label(text="Password: ")
etiqueta_resultado.place(x=20, y=120)

ventana.mainloop()



