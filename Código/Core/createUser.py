#importamos libreria tkinter
from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu, messagebox
import Connection
import tkinter.colorchooser
class createUser:
    #creamos nueva instancia de la clase Tk
    def __init__(self, action):
        self.action = action
        self.createUser = Tk()
        self.id = 0
    #definimos tamaño de la ventana
        self.createUser.geometry("650x550")
    #definimos titulo de la ventana
        self.createUser.title("Formulario de Registro") if action == 'post' else self.createUser.title("Editar usuario")
    #bloqueamos la opcion de que el usuario cambie el tamaño de la ventana
        self.createUser.resizable(False,False)
    #damos color de fondo a nuestra ventana
        self.createUser.config(background="#ccd9cf")
    #creamos un titulo para el formulario, depende del tipo de petición
        if action == 'post':
            self.createUser_label = Label(self.createUser, text="Crear Usuario", font=("Arial", 20), bg="#9bc0b9", fg="#0b1828", width="550", height="2")
        else:
            self.info = []
            self.createUser_label = Label(self.createUser, text="Editar Usuario", font=("Arial", 20), bg="#9bc0b9", fg="#0b1828", width="550", height="2")
        self.createUser_label.pack()

    #se crean las variables en las que se almacenará lo escrito en los campos de texto
        self.userNameS = StringVar(self.createUser)
        self.firstNameS = StringVar(self.createUser)
        self.secondNameS = StringVar(self.createUser)
        self.firstLastNameS = StringVar(self.createUser)
        self.secondLastNameS = StringVar(self.createUser)
        self.passwordS = StringVar(self.createUser)
        self.typeUserS = StringVar(self.createUser)
        self.confirmPassword = StringVar(self.createUser)
        self.typeUserS.set("Operador")

    #definimos todos los elementos para obtener el nombre de usuario
        self.userName_label = Label(self.createUser, text="Nombre de Usuario ", font=("Arial", 12), bg="#ccd9cf", fg="#0b1828")
        self.userName_label.place(x=20,y=80)
        self.userName_entry = Entry(self.createUser, width="50", font=("Arial", 12), textvariable=self.userNameS)
        self.userName_entry.place(x=170,y=80)

    #definimos todos los elemntos para obtener el primer nombre del nuevo usuario
        self.firstName_label = Label(self.createUser, text="Primer Nombre", font=("Arial", 12), bg="#ccd9cf", fg="#0b1828")
        self.firstName_label.place(x=20,y=120)
        self.firstName_entry = Entry(self.createUser, textvariable=self.firstNameS, width="50", font=("Arial", 12))
        self.firstName_entry.place(x=170,y=120)

    #definimos todos los elemntos para obtener el segundo nombre del nuevo usuario
        self.secondName_label = Label(self.createUser, text="Segundo Nombre", font=("Arial", 12), bg="#ccd9cf", fg="#0b1828")
        self.secondName_label.place(x=20,y=160)
        self.secondName_entry = Entry(self.createUser, textvariable=self.secondNameS, width="50", font=("Arial", 12))
        self.secondName_entry.place(x=170,y=160)

    #definimos todos los elemntos para obtener el primer apellido del nuevo usuario
        self.firstLastName_label = Label(self.createUser, text="Primer Apellido", font=("Arial", 12), bg="#ccd9cf", fg="#0b1828")
        self.firstLastName_label.place(x=20,y=200)
        self.firstLastName_entry = Entry(self.createUser, textvariable=self.firstLastNameS, width="50", font=("Arial", 12))
        self.firstLastName_entry.place(x=170,y=200)

    #definimos todos los elemntos para obtener el segundo apellido del nuevo usuario
        self.secondLastName_label = Label(self.createUser, text="Segundo Apellido", font=("Arial", 12), bg="#ccd9cf", fg="#0b1828")
        self.secondLastName_label.place(x=20,y=240)
        self.secondLastName_entry = Entry(self.createUser, textvariable=self.secondLastNameS, width="50", font=("Arial", 12))
        self.secondLastName_entry.place(x=170,y=240)

    #definimos elementos para obtener la contraseña
        self.password_label = Label(self.createUser, text="Contraseña", font=("Arial", 12), bg="#ccd9cf", fg="#0b1828")
        self.password_label.place(x=20,y=280)
        self.password_entry = Entry(self.createUser, textvariable=self.passwordS, width="50", show="*", font=("Arial", 12))
        self.password_entry.place(x=170,y=280)

    #definimos elementos para obtener confirmacion de la contraseña        
        self.password_label2 = Label(self.createUser, text="Corfirmación Contraseña", font=("Arial", 12), bg="#ccd9cf", fg="#0b1828")
        self.password_label2.place(x=20,y=320)
        self.password_entry2 = Entry(self.createUser, textvariable=self.confirmPassword, width="50", show="*", font=("Arial", 12))
        self.password_entry2.place(x=170,y=320)

    #definimos elementos para obtener el tipo de usuario que se creara
        self.typeUser_label = Label(self.createUser, text="Tipo de Usuario", font=("Arial", 12), bg="#ccd9cf", fg="#0b1828")
        self.typeUser_label.place(x=20,y=360)
        self.typeUser_option = OptionMenu(self.createUser, self.typeUserS, "Administrador", "Operador")
        self.typeUser_option.place(x=170, y=360)

    #definimos elementos para el boton que guardara nuestros datos
        self.saveDataUser_button = Button(self.createUser, text="Guardar", font=("Arial", 13), width="20", height="2", bg="#0b1828", fg="#ccd9cf", command=self.save_user)
        self.saveDataUser_button.place(x=235, y=490)

    #metodo para obtener el color del lapiz que el usuario tendra por defecto
        def getPenColor():
                color = tkinter.colorchooser.askcolor()
                if color != None:
                    self.penColor.set(str(color)[-9:-2])

    #definimos elementos para obtener color de lapiz
        self.penLabel = Label(self.createUser, text="Pen color", font=("Arial", 12), bg="#ccd9cf", fg="#0b1828")
        self.penLabel.place(x=20 ,y=400)
        #self.penLabel.pack()
        self.penColorButton = Button(self.createUser, text="Selecciona un color",font=("Arial", 8), width="18", height="1", bg="#0b1828", fg="#ccd9cf", command=getPenColor)
        self.penColorButton.place(x=170, y=400)
        #self.penColorButton.pack(pen=BOTH)
        
        self.penColor = StringVar(self.createUser)
        self.penEntry = Entry(self.createUser, textvariable=self.penColor, width="8", font=("Arial", 12))
        self.penEntry.place(x=300 ,y=400)
        #self.penEntry.pack()
        self.penColor.set("#000000")


    #metodo para obtener el color del lapiz que el usuario tendra por defecto
        def getFillColor():
                color = tkinter.colorchooser.askcolor()
                if color != None:
                    self.fillColor.set(str(color)[-9:-2])

    #definimos elementos para obtener color de lapiz
        self.fillLabel = Label(self.createUser, text="Fill color", font=("Arial", 12), bg="#ccd9cf", fg="#0b1828")
        self.fillLabel.place(x=20 ,y=440)
        #self.fillLabel.pack()
        self.fillColorButton = Button(self.createUser, text="Selecciona un color",font=("Arial", 8), width="18", height="1", bg="#0b1828", fg="#ccd9cf", command=getFillColor)
        self.fillColorButton.place(x=170, y=440)
        #self.fillColorButton.pack(fill=BOTH)
        
        self.fillColor = StringVar(self.createUser)
        self.fillEntry = Entry(self.createUser, textvariable=self.fillColor, width="8", font=("Arial", 12))
        self.fillEntry.place(x=300 ,y=440)
        #self.fillEntry.pack()
        self.fillColor.set("#000000")

    
    # Método que registra al usuario en la BD
    def save_user(self):
        username = self.userNameS.get()  
        fname = self.firstNameS.get()  
        sname = self.secondNameS.get()  
        flastn = self.firstLastNameS.get()  
        slastn = self.secondLastNameS.get()  
        passw = self.passwordS.get()
        passw2 = self.confirmPassword.get()
        typeuser = 1 if self.typeUserS.get() == "Administrador" else 2
        fillcolor = self.fillColor.get()
        pencolor = self.penColor.get()

        # Aquí comienzan las validaciones
        if (
            username == '' or
            fname == '' or
            sname == '' or
            flastn == '' or
            slastn == '' or
            passw == '' or
            passw2 == ''
        ):
            self.error("Debe llenar todos los campos")
        else:
            if(passw != passw2):
                self.error("Contraseñas no coinciden")
            else:
                if self.action == 'post':
                    values = (
                        fname,
                        sname,
                        flastn,
                        slastn,
                        username,
                        passw,
                        typeuser, 
                        pencolor,
                        fillcolor
                    )
                    Connection.Connection(None).set_user(values)
                    self.createUser.destroy()
                else:
                    values = (
                        self.id,
                        fname,
                        sname,
                        flastn,
                        slastn,
                        username,
                        passw,
                        typeuser, 
                        pencolor,
                        fillcolor
                    )
                    Connection.Connection(self.id).update_user(values)
                    self.createUser.destroy()

    def set_default_data(self, id):
        self.id = id
        self.info = Connection.Connection(id).get_user_info(id)
          
    def error(self, text):
        messagebox.showerror("Error", text)

    def start(self):
        self.firstNameS.set(self.info[0][1]) if self.action == 'put' else False
        self.secondNameS.set(self.info[0][2]) if self.action == 'put' else False
        self.firstLastNameS.set(self.info[0][3]) if self.action == 'put' else False
        self.secondLastNameS.set(self.info[0][4]) if self.action == 'put' else False
        self.userNameS.set(self.info[0][5]) if self.action == 'put' else False    
        self.typeUserS.set("Administrador") if self.action == 'put' and self.info[0][7] == 1 else self.typeUserS.set("Operador")
        self.penColor.set(self.info[0][-2]) if self.action == 'put' else False
        self.fillColor.set(self.info[0][-1]) if self.action == 'put' else False
        self.createUser.mainloop()

# ventana = createUser()
# ventana.start()