# -*- coding: utf-8 -*-

from ConnectionConfig import ConnectionConfig
from MySQLEngine import MySQLEngine
from tkinter import *
import tkinter.ttk
from tkinter.ttk import * 
import json

import Connection
import GetId


class Repository:
    # DEFINIMOS EL CONSTRUCTOR Y TOMAMOS EL PARAMETRO QUE NOS ESTAN PASANDO AL INICIAR LA VENTANA
    def __init__(self):

        # CREAR PROPIEDAD U OBJETO PARA ALMACENAR LA VENTANA QUE ESTA RECIBIENDO EL CONSTRUCTOR
        self.win = Tk()
        self.win.title('Repositorio')
        self.contEditar = 0

        self.id = GetId.GetId().get_id()
        # TABLA
        frame2 = LabelFrame(self.win, text=' LISTA DE DIBUJOS POR USUARIO: ')
        frame2.grid(row = 7, column = 0, columnspan = 3, padx = 20, pady = 15)

        self.tree = tkinter.ttk.Treeview(frame2, height = 10, columns=("#1", "#2"))
        self.tree.grid(row = 7, column = 0, columnspan = 2, padx = 20, pady = 10)
        self.tree.heading("#0", text="Dibujo", anchor = CENTER)         
        self.tree.heading("#1", text="Fecha de creación", anchor = CENTER)
        self.tree.heading("#2", text="Nombre", anchor = CENTER)

        # SCROLL VERTICAL TREEVIEW
        scrolvert = Scrollbar(frame2, command = self.tree.yview)
        scrolvert.grid(row=7, column=2, sticky="nsew")
        self.tree.config(yscrollcommand=scrolvert.set)

         # SCROLL HORIZONTAL TREEVIEW
        scrolhoriz = Scrollbar(frame2, command = self.tree.xview, orient='horizontal')
        scrolhoriz.grid(row=12, column=0, columnspan=2, sticky="news")
        self.tree.config(xscrollcommand=scrolhoriz.set)

        # BOTONES
        # tkinter.ttk.Button(text='Aceptar', command=self.Aceptar).grid(row = 13, column = 0, columnspan=2, ipadx = 50, pady = 10)
        # tkinter.ttk.Button(text='Aceptar', command=self.Aceptar).pack()
        boton = Button(self.win, text='Aceptar', command=self.Aceptar)
        boton.grid(row = 13, column = 0, columnspan=2, ipadx = 50, pady = 10)
        boton2 = Button(self.win, text="Eliminar", command=self.eliminar)
        boton2.grid(row = 13, column = 4, columnspan=2, ipadx=50, pady = 10)
        # boton.pack()
        #Obtenemos los registros del dibujo seleccionado
        self.tree.bind("<<TreeviewSelect>>", self._on_tree_select)  # <<<<<<<<<
        self.get_data()

    def eliminar(self):
        # print(self.id_dibujo)
        Connection.Connection(None).remove_draw(int(self.data['text']))
        self.win.destroy()

    # CREACION INTERFAZ GRAFICA
    def _on_tree_select(self, event):
        current_item = self.tree.focus()
        if not current_item:
            return
        self.data = self.tree.item(current_item)
        # nombre = data["text"]
        # month, count = data["values"]
        # print(nombre)
        # print(month)
        # print(count)

    # Insertar datos en la tabla treeviw.
    def get_data(self):
        #Conectando a base de datos.
        # config = ConnectionConfig("localhost", "3306","Angel","Administr@dor_069","ProgramaDeDibujoBD")
        # engine = MySQLEngine(config)
        #Obteniendo datos de la view.
        # result = engine.select("SELECT var_nombre, tim_creacion, repositorio_id FROM Dibujo WHERE repositorio_id = 1")
        result = Connection.Connection(self.id).get_user_pics()

        for id_dibujo, tim_creacion, repositorio_id, user in result:
            # self.id_dibujo = id_dibujo
            self.tree.insert('', 0, text = id_dibujo, values = (repositorio_id, tim_creacion))
            # self.tree.insert('', 0, text = 'aa', values = (var_nombre, tim_creacion))

    # Funcion de boton aceptar.
    def Aceptar(self):
        # print(self.data)
        self.contEditar += 1
        draw = Connection.Connection(self.id).get_draw(self.data['text'])
        bytes_draw = draw[0][0]
        # print(bytes_draw)
        # print(bytes_draw)
        # print(type(bytes_draw))
        # normal_json = bytes_draw.decode('utf8').replace("'", '"')
        
        # self.win.destroy()
        # json_draw = json.loads(normal_json)
        
        
        # data = json.loads(normal_json)
        # self.final = data 
        # final_json = json.dumps(data, sort_keys=True)
        self.final = bytes_draw
        file = open('drawCookie', 'w')
        file.write(self.final)
        # print(data)
        file.close()
        self.win.destroy()
        
        
        # app = tkinter.Tk()
        # mylabel = Label(app, text="Volvemos a la interfaz principal")
        # mylabel.pack()

    def start(self):
        self.win.mainloop()
        return self.final if self.contEditar > 0 else False

# if __name__ == "__main__":
#     window = Tk()
#     aplication = Repository(window)
#     window.mainloop()
