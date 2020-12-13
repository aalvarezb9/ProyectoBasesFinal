#importamos libreria tkinter
from tkinter import *
#importamos libreria ttk para poder usar el sistema de tablas
from tkinter import ttk
#importamos libreria messagebox para motrar mensajes de alerta
from tkinter import messagebox
import tkinter as tk

import Connection
import createUser

class RemoveUser:
    #creamos nueva instancia de la clase Tk
    def __init__(self):
        self.removeUser = Tk()
    #definimos tamaño de la ventana
        self.removeUser.geometry("800x320")
    #definimos titulo de la ventana
        self.removeUser.title("Eliminar Usuario")
    #bloqueamos la opcion de que el usuario cambie el tamaño de la ventana
        self.removeUser.resizable(False,False)
    #damos color de fondo a nuestra ventana
        self.removeUser.config(background="#ccd9cf")
    #creamos un titulo para el formulario
        self.removeUser_label = Label(self.removeUser, text="Elminar Usuario", font=("Arial", 20), bg="#9bc0b9", fg="#0b1828", width="550", height="2")
        #self.removeUser_label.pack()
        self.current = None
        self.table=ttk.Treeview(self.removeUser)
        self.table.bind("<<TreeviewSelect>>", self._on_tree_select)

        self.table["columns"]=("#1", "#2", "#3", "#4" ,"#5")#,"#6")
        self.table.column("#0", width=100, minwidth=100)
        self.table.column("#1", width=100, minwidth=100)
        self.table.column("#2", width=100, minwidth=100)
        self.table.column("#3", width=100, minwidth=100)
        self.table.column("#4", width=100, minwidth=100)
        self.table.column("#5", width=100, minwidth=100)
       # self.table.column("#6", width=100, minwidth=100)

        self.selectCheck = ttk.Checkbutton(self.removeUser)

        self.table.heading("#0", text="id", anchor=tk.W)
        self.table.heading("#1", text="Nombre de Usuario", anchor=tk.W)
        self.table.heading("#2", text="Primer Nombre", anchor=tk.W)
        self.table.heading("#3", text="Segundo Nombre", anchor=tk.W)
        self.table.heading("#4", text="Primer Apellido", anchor=tk.W)
        self.table.heading("#5", text="Segundo Apellido", anchor=tk.W)
        #self.table.heading("#6", text="Seleccionar", anchor=tk.W)

        self.table.pack(side=tk.TOP,fill=tk.X)
        self.message = Label(self.removeUser, text="", font=("Arial", 12), bg="#ccd9cf", fg="red")
        self.message.place(x=365, y=230)

        self.editUser_btn = Button(self.removeUser, text="Editar Usuario", font=("Arial", 10), width="15", height="1", bg="#0b1828", fg="#ccd9cf", command=self.editar)
        self.editUser_btn.place(x=260, y=260)

        self.removeUser_btn = Button(self.removeUser, command=self.deleteUser, text="Eliminar Usuario", font=("Arial", 10), width="15", height="1", bg="#0b1828", fg="#ccd9cf")
        self.removeUser_btn.place(x=400, y=260)

        self.users = Connection.Connection(None).get_user_data()
        # print("self.users ---->")
        # print(self.users)

        # self.test = [(1,'usuario1','alejandro','fernado','herrera','dias'),(2,'usuario2','alejandro','fernado','herrera','dias'), (3,'usuario3','alejandro','fernado','herrera','dias')]
        self.getUsers()

    def getUsers(self):       
        records = self.table.get_children()
        for element in records:
            self.table.delete(element)        
        for row in self.users:
            #print(row)
            self.table.insert('',0, text=row[0], values=(row[1], row[2], row[3],row[4], row[5]))   

    def update_user(self):
        self.users = Connection.Connection(None).get_user_data()

    def deleteUser(self):
        # Connection.Connection(None).remove_user(int(self.current['text']))
        Connection.Connection(None).remove_user(int(self.current['text']))
        self.removeUser.destroy()
        # try:
        #     self.table.item(self.table.selection())['text']
        # except IndexError as e:
        #     self.message['text']= 'Por favor seleccione un registro'
        #     return
        # user = self.table.item(self.table.selection())['text']
        # #imprimimos en consola id de usuario a eliminar
        # print('Usuario a elimnar: ' +str(user)) 
        # self.update_user()
        # self.getUsers()          

    def editar(self):
        if self.current == None:
            self.error("Debe seleccionar algún campo")
        else:
            editarUser = createUser.createUser("put")
            editarUser.set_default_data(int(self.current['text']))
            editarUser.start()        
            self.update_user()
            self.getUsers()

    def _on_tree_select(self, event):
        self.current = self.table.focus()
        if not self.current:
            return
        self.current = self.table.item(self.current)
        # print(data)

    def error(self, text):
        messagebox.showerror("Error", text)

    def start(self):
        self.removeUser.mainloop()   
    


# ventana = RemoveUser()
# ventana.start()
