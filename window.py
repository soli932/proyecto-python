from cProfile import label
from tkinter import *
from ip import IP


class Window:

    def __init__(self, window):

        window.title("Obtener Private y Public IP")

        window.geometry('400x200')

        lbl = Label(window, text="Hola \n Obtener una IP privada y una IP pública desde el dispositivo que lo ejecuta.")

        lbl.grid(column=1, row=1)

        btn = Button(window, text="Obtener IP", command=lambda: self.clicked(window))

        btn.grid(column=1, row=2)

    def clicked(self, window):
        
        ip = IP()
        private = StringVar()
        #private ip
        private = Label(window, text="Private IP: "+ip.lan_ip)
        private.grid(column=1, row=3)
        
        #public ip
        private = Label(window, text="Public IP: "+ip.wan_ip)
        private.grid(column=1, row=4)
        