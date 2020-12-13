# -*- coding: utf-8 -*-

import gui

import tkinter
from tkinter import Tk, StringVar, LabelFrame, Entry, Button, messagebox
import os

import readIni
import MySQLEngine
import ConnectionConfig
import Connection


class Login:
    def __init__(self, root):
        self.info = {}
        self.reader = readIni.ReadINI()
        self.db_host = self.reader.get_db_host()
        self.db_name = self.reader.get_db_name()
        self.db_port = self.reader.get_db_port()
        self.db_user = self.reader.get_db_user()
        self.db_password = self.reader.get_db_password()
        self.cin = StringVar()
        self.string_login = StringVar() #Este es nuevo###########
        self.string_password = StringVar() #Este tambien##############3
        self.root = root
        self.root.title("Login")
        self.root.geometry("650x420")
        self.frame = LabelFrame(root, text="Inicie sesión", font="arial-14", padx=6, pady=6)
        self.frame.pack(padx=100, pady=100)
        self.login = Entry(self.frame, width=40, borderwidth=5, textvariable=self.string_login)
        self.password = Entry(self.frame, show="*", width=40, borderwidth=5, textvariable=self.string_password)
        # self.login.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        # self.password.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.login.pack()
        self.password.pack()

        self.button = Button(self.frame, text="Iniciar sesión", command=self.validar_credenciales)
        # self.button.grid(row=3, column=1)
        self.button.pack(pady=20)
    
    # Crea un json que simula a una cookie
    def make_cookie(self, id):
        file = open(os.getcwd() + '/Core/cookie', 'w')
        file.write('{"id":"%s"}' % id)
        # file.write( '{"%s": "%s", "%s": "%s"}' % ("username", info["username"], "password", info["password"]) )
        file.close()
        
        self.root.destroy()
        self.open_home()

    # Se abre la interfaz principal
    def open_home(self):
        root = tkinter.Tk()
        # otroObjeto = gui.GettingData(info)
        gui.DrawingApplication(root)

    # Se valida que los campos no estén vacíos
    def validar_credenciales(self):
        self.username = self.string_login.get()
        self.password = self.string_password.get()
        if self.username == '' or self.password == '':
            self.error("Llene los campos para iniciar sesión")
        else:
            status, idd = None, None
            values = (self.username, self.password, status, idd)
            self.try_connect(values)
        

    def try_connect(self, values):
        self.config = ConnectionConfig.ConnectionConfig(
            self.db_host,
            int(self.db_port),
            self.db_user,
            self.db_password,
            self.db_name
        )
        self.engine = MySQLEngine.MySQLEngine(self.config)
        self.obtener_usuario(values)

    # Se manda a crear la cookie siempre y cuando el result de la query no sea nulo
    def obtener_usuario(self, values):
        id = self.engine.procedureLogin("Login", values)
        self.make_cookie(id[-1]) if id[-1] != None else self.error("Credenciales inválidas")

    def error(self, text):
        messagebox.showerror("Error", text)
        
    def start(self):
        self.root.mainloop()


