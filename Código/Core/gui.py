# -*- coding: utf-8 -*-

import os
import turtle
import tkinter.colorchooser
import tkinter.filedialog
import json
import Connection
import userControl
import GetId
import repository
from os import remove
from tkinter import Tk, Label, Entry, Button, StringVar
import Blob
import ManejoArchivos

datos = ''



class GoToCommand:
    def __init__(self, x, y, width=1, color="black"):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x, self.y)

    def __str__(self):
        return '{"Command": "GoTo", "x":"' + str(self.x) + '", "y":"' + \
             str(self.y) + '", "width":"' + str(self.width) + '", "color": "' + str(self.color) + '"}'

class CircleCommand:
    def __init__(self, radius, width=1, color="black"):
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.circle(self.radius)

    def __str__(self):
        return '{"Command": "Circle", "radius": "' + str(self.radius) + '", "width":"' + str(self.width) + '", "color":"' + str(self.color) + '"}'


class BeginFillCommand:
    def __init__(self, color):
        self.color = color

    def draw(self, turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()

    def __str__(self):
        return '{"Command":"BeginFill", "color":"' + str(self.color) +  '"}'

class EndFillCommand:
    def __init__(self):
        pass
    
    def draw (self, turtle):
        turtle.end_fill()

    def __str__(self):
        return '{"Command":"EndFill"}' 

class PenUpCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.penup()

    def __str__(self):
        return '{"Command":"PenUp"}'

class PenDownCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.pendown()

    def __str__(self):
        return '{"Command":"PenDown"}'

class PyList:
    def __init__(self):
        self.gcList = []

    def append(self, item):
        self.gcList = self.gcList + [item]

    def removeLast(self):
        self.gcList = self.gcList[:-1]

    def __iter__(self):
        for c in self.gcList:
            yield c

    def __len__(self):
        return len(self.gcList)


class DrawingApplication(tkinter.Frame): #DrawingApplication(tkinter.Frame)
    def __init__(self, master=None): 
        super().__init__(master)
        # print(datos)
        self.master = master
        # self.id = self.get_id()
        self.id = GetId.GetId().get_id()
        self.user = Connection.Connection(self.id).get_name()
        self.user_type = Connection.Connection(self.id).get_user_type()
        self.fill_color = Connection.Connection(self.id).get_fill_color()
        self.pen_color = Connection.Connection(self.id).get_pen_color()
        self.info = {}
        self.pack()
        # self.master.pack()
        self.buildWindow()
        self.graphicsCommands = PyList()

    def buildWindow(self):

        self.master.title("Bienvenido, %s (%s)" % (self.user, self.user_type))
        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar, tearoff=0)

        def newWindow():
            theTurtle.pen()
            theTurtle.penup()
            theTurtle.goto(0, 0)
            theTurtle.pendown()
            screen.update()
            screen.listen()
            self.graphicsCommands = PyList()

        fileMenu.add_command(label="New", command=newWindow)

        def parse(filename):

            with open(filename) as f:
                dictionary = json.load(f)

            for i in range(len(dictionary)):
                command = dictionary[i]["Command"]
                element = dictionary[i]
                if command == "GoTo":
                    x = float(element["x"])
                    y = float(element["y"])
                    width = float(element["width"])
                    color = element["color"].strip()
                    cmd = GoToCommand(x, y, width, color)
                elif command == "Circle":
                    radius = float(element["radius"])
                    width = float(element["width"])
                    color = element["color"].strip()
                    cmd = CircleCommand(radius, width, color)
                elif command == "BeginFill":
                    color = element["color"].strip()
                    cmd = BeginFillCommand(color)
                elif command == "EndFill":
                    cmd = EndFillCommand()
                elif command == "PenUp":
                    cmd = PenUpCommand()
                elif command == "PenDown":
                    cmd = PenDownCommand()
                else:
                    raise RuntimeError("Comando desconocido " + command)


                self.graphicsCommands.append(cmd)
            os.remove('drawCookie')
                

        def loadFile():
            # filename = tkinter.filedialog.askopenfilename(title="Selecciona una")
            # newWindow()
            draw = repository.Repository().start()
            # parse('drawCookie')
            self.graphicsCommands = PyList()

            # print(draw)
            # print(type(draw))
            parse('drawCookie')
            # parse('drawCookie')

            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)

            screen.update()


        fileMenu.add_command(label="Cargar...", command=loadFile)

        def write(filename):
            filename = filename+'.json'
            contador = 0
            file = open(filename, "w")
            file.write("[")

            for cmd in self.graphicsCommands:
                contador += 1
                if contador == len(self.graphicsCommands):
                    file.write('    ' + str(cmd) + "\n")
                else:
                    file.write('    ' + str(cmd) + "," + "\n")

            file.write("]")
            file.close()

            # with open(filename) as f:
                # draw = json.load(f)

            file = open(filename, "r")
            draw = file.read()
            file.close()


            with open(filename) as f:
                json_file = json.load(f)

            str_file = json.dumps(json_file, sort_keys=True)
            archivoBLOB = ManejoArchivos.Manejo(filename).comprimir(str_file)

            Connection.Connection(self.id).insert_draw(filename, draw, archivoBLOB)


            remove(filename)
            remove(filename+'.gz')


        def saveFile():
            # filename = tkinter.filedialog.asksaveasfilename(title="Guardar imagen como...")
            window = Tk()

            filename = StringVar(window)
            window.title("Selecciona el nombre de tu dibujo")

            window.geometry('350x200')

            lbl = Label(window, text="Nombre del dibujo")

            lbl.grid(column=0, row=0)

            txt = Entry(window,width=10, textvariable=filename)

            txt.grid(column=1, row=0)

            def clicked():
                write(filename.get())
                window.destroy()

            btn = Button(window, text="Guardar", command=clicked)

            btn.grid(column=2, row=0)

            window.mainloop()

        fileMenu.add_command(label="Guardar como...", command=saveFile)

        fileMenu.add_command(label="Descargar")

        def goConfig():
            # self.master.iconify()
            userControl.userControl().start()

        fileMenu.add_command(label="Configurar", command=goConfig) if self.user_type == "Administrador" else False
        

        fileMenu.add_command(label="Salir", command=self.master.quit)

        bar.add_cascade(label="Archivo", menu=fileMenu)

        self.master.config(menu=bar)

        canvas = tkinter.Canvas(self, width=600, height=600)
        canvas.pack(side=tkinter.LEFT)

        theTurtle = turtle.RawTurtle(canvas)

        theTurtle.shape("circle")
        screen = theTurtle.getscreen()

        screen.tracer(0)

        sideBar = tkinter.Frame(self, padx=5, pady=5)
        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        pointLabel = tkinter.Label(sideBar, text="Width")
        pointLabel.pack()

        widthSize = tkinter.StringVar()
        widthEntry = tkinter.Entry(sideBar, textvariable=widthSize)
        widthEntry.pack()
        widthSize.set(str(1))

        radiusLabel = tkinter.Label(sideBar, text="Radius")
        radiusLabel.pack()
        radiusSize = tkinter.StringVar()
        radiusEntry = tkinter.Entry(sideBar, textvariable=radiusSize)
        radiusSize.set(str(10))
        radiusEntry.pack()

        def circleHandler():
            cmd = CircleCommand(float(radiusSize.get()), float(widthSize.get()), penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

            screen.update()
            screen.listen()

        circleButton = tkinter.Button(sideBar, text="Dibujar círculo", command=circleHandler)
        circleButton.pack(fill=tkinter.BOTH)

        screen.colormode(255)
        penLabel = tkinter.Label(sideBar, text="Color del lápiz")
        penLabel.pack()
        penColor = tkinter.StringVar()
        penEntry = tkinter.Entry(sideBar, textvariable=penColor)
        penEntry.pack()

        penColor.set(self.pen_color)

        def getPenColor():
            color = tkinter.colorchooser.askcolor()
            if color != None:
                penColor.set(str(color)[-9:-2])

        penColorButton = tkinter.Button(sideBar, text="Selecciona un color", command=getPenColor)
        penColorButton.pack(fill=tkinter.BOTH)
        fillLabel = tkinter.Label(sideBar, text="Llenar color")
        fillLabel.pack()
        fillColor = tkinter.StringVar()
        fillEntry = tkinter.Entry(sideBar, textvariable=fillColor)
        fillEntry.pack()
        fillColor.set(self.fill_color)

        def getFillColor():
            color = tkinter.colorchooser.askcolor()
            if color != None:
                fillColor.set(str(color)[-9:-2])
            
        fillColorButton = \
            tkinter.Button(sideBar, text="Escoja color de relleno", command=getFillColor)
        fillColorButton.pack(fill=tkinter.BOTH)

        def beginFillHandler():
            cmd = BeginFillCommand(fillColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

        beginFillButton = tkinter.Button(sideBar, text="Inicio relleno", command=beginFillHandler)
        beginFillButton.pack(fill=tkinter.BOTH)

        def endFillHandler():
            cmd = EndFillCommand()
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
        
        endFillButton = tkinter.Button(sideBar, text="Terminar relleno", command=endFillHandler)
        endFillButton.pack(fill=tkinter.BOTH)

        penLabel = tkinter.Label(sideBar, text="Lápiz abajo")
        penLabel.pack()

        def penUpHandler():
            cmd = PenUpCommand()
            cmd.draw(theTurtle)
            penLabel.configure(text="Lápiz arriba")
            self.graphicsCommands.append(cmd)

        penUpButton = tkinter.Button(sideBar, text="Lápiz arriba", command=penUpHandler)
        penUpButton.pack(fill=tkinter.BOTH)

        def penDownHandler():
            cmd = PenDownCommand()
            cmd.draw(theTurtle)
            penLabel.configure(text="Lápiz abajo")
            self.graphicsCommands.append(cmd)

        penDownButton = tkinter.Button(sideBar, text="Lápiz abajo", command=penDownHandler)
        penDownButton.pack(fill=tkinter.BOTH)

        def clickHandler(x, y):
            cmd = GoToCommand(x, y, float(widthSize.get()), penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()

        screen.onclick(clickHandler)

        def dragHandler(x, y):
            cmd = GoToCommand(x, y, float(widthSize.get()), penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()

        theTurtle.ondrag(dragHandler)

        def undoHandler():
            if len(self.graphicsCommands) > 0:
                self.graphicsCommands.removeLast()
                theTurtle.clear()
                theTurtle.penup()
                theTurtle.goto(0, 0)
                theTurtle.pendown()
                for cmd in self.graphicsCommands:
                    cmd.draw(theTurtle)
                screen.update()
                screen.listen()

        screen.onkeypress(undoHandler, "u")
        screen.listen()

    # def screen_update(self):
    #     self.graphicsCommands = PyList()

    #     parse(filename)

    #     for cmd in self.graphicsCommands:
    #         cmd.draw(theTurtle)

    #     screen.update()






    