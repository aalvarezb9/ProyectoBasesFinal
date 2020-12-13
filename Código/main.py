# -*- coding: utf-8 -*-

"""
    ! Programa con interfaz gráfica (tkinter) hecho en Python 3.x
        * Crear dibujos
        * Guardar dichos dibujos
        * Cargar dibujos
        * Administrar usuarios (en caso de que el usuario tenga los privilegios)
        * Acceso a un repositorio
        * Etc

    @author: Ángel
    @date: dd / mm / aaaa 

"""

import os
from os import remove
import sys
sys.path.append(os.getcwd() + '/Core/')

import tkinter
import Core.login as login
import Core.GetId as getid
import Core.Connection as con

def main():
    root = tkinter.Tk() # Se crea el objeto tk, que servirá de parámetro para enviarlo a la clase Login
    drawingApp = login.Login(root)  # Se manda el objeto previamente creado
    drawingApp.start()  # Se llama al método 'start' de la clase 'Login'; se ejecuta el mainloop

    print("Ejecución completada")   # Ejecución del programa ya terminado
    archivo_cookie = os.getcwd() + '/Core/cookie'   # Se hace referencia al archivo 'cookie', se explicará en las demás clases su función
    # id = getid.GetId().get_id()
    # values = (id, 0)
    # con.Connection(id).logout(values)
    remove(archivo_cookie) if os.path.isfile(archivo_cookie) else False # Se borra el archivo 'cookie' en caso de que exista


if __name__ == "__main__":
    main()



