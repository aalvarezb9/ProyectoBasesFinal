# importamos libreria tkinter
from tkinter import Tk, Label, Button
from createUser import createUser
from removeUser import RemoveUser


class userControl:
    def __init__(self):
        # creamos nueva instancia de la clase Tk
        self.controlUser = Tk()
        # definimos tamaño de la ventana
        self.controlUser.geometry("650x300")
# definimos titulo de la ventana
        self.controlUser.title("Control de Usuarios")
# bloqueamos la opcion de que el usuario cambie el tamaño de la ventana
        self.controlUser.resizable(False, False)
# damos color de fondo a nuestra ventana
        self.controlUser.config(background="#ccd9cf")
# creamos un titulo para el formulario
        self.main_title = Label(self.controlUser, text="Control de Usuarios", font=(
            "Arial", 20), bg="#9bc0b9", fg="#0b1828", width="550", height="2")
        self.main_title.pack()
# usamos etiqueta para definir el boton de crear nuevo usuario
        self.createUser_label = Label(self.controlUser, text="Presione este boton si desea crear un usuario nuevo", font=(
            "Arial", 14), bg="#ccd9cf", fg="#0b1828")
        self.createUser_label.place(x=110, y=80)

        def get_form():
            ventana_createUser = createUser("post")
            ventana_createUser.start()

        def get_removeUser():
            ventana_removeUser = RemoveUser()    
            ventana_removeUser.start()
                

# creamos un boton el cual nos abrira el formulario de registro para crear el nuevo usuario
        self.goToCreateUser_btn = Button(self.controlUser, command=get_form, text="Crear Usuario", font=(
            "Arial", 15), width="30", height="2", bg="#0b1828", fg="#ccd9cf")
        self.goToCreateUser_btn.place(x=160, y=110)
# usamos etiqueta para definir el boton de editar usuario
        self.upDateUser_label = Label(self.controlUser ,text="Presione este boton si desea editar o eliminar un usuario existente", font=("Arial", 14), bg="#ccd9cf", fg="#0b1828")
        self.upDateUser_label.place(x=60, y=180)
# creamos un boton el cual nos abrira el formulario para editar datos de usuario
        self.goToUpDateUser_btn = Button(self.controlUser, command=get_removeUser, text="Editar Usuario", font=(
            "Arial", 15), width="30", height="2", bg="#0b1828", fg="#ccd9cf")
        self.goToUpDateUser_btn.place(x=160, y=210)

# usamos etiqueta para definir el boton de eliminar usuario
#        self.removeUser_label = Label(self.controlUser, text="Presione este boton si desea editar o eliminar un usuario existente", font=(
#            "Arial", 14), bg="#ccd9cf", fg="#0b1828")
#        self.removeUser_label.place(x=110, y=280)
# creamos un boton el cual nos abrira el formulario de registro para eliminar un usuario
#        self.goToRemoveUser_btn = Button(self.controlUser, text="Eliminar Usuario", font=(
#            "Arial", 15), width="30", height="2", bg="#0b1828", fg="#ccd9cf")
#        self.goToRemoveUser_btn.place(x=160, y=310)



    def start(self):
        self.controlUser.mainloop()

# ventana = userControl()
# ventana.start()
