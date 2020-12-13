# -*- coding: utf-8 -*-

"""
    ! Clase que hace la conexión con la BD y ejecuta algunas consultas al ser necesitadas
        * Inserta datos
        * Obtiene datos
        * Actualiza datos ya existentes
        * Otro tipo de consultas
    @author: Ángel
    @date: dd / mm / aaaa

"""

import MySQLEngine
import ConnectionConfig
import readIni
import json

class Connection:
    def __init__(self, id):
        self.id = id
        self.reader = readIni.ReadINI() # Se crea el objeto que apunta a la clase que obtiene los datos de config.ini
        # Las siguiente 5 líneas obtienen los datos para hacer la conexión a la base de datos
        self.db_host = self.reader.get_db_host()
        self.db_name = self.reader.get_db_name()
        self.db_port = self.reader.get_db_port()
        self.db_user = self.reader.get_db_user()
        self.db_password = self.reader.get_db_password()
        self.validar_credenciales() # Se hace la conexión

    def validar_credenciales(self):
        #Esto hay que mejorarlo, no maneja las excepciones 
        try:
            self.try_connect()
            # print("Conexion Exitosa")
        except IndexError:
            print("Conexion fallida")

    def try_connect(self):
        self.config = ConnectionConfig.ConnectionConfig(
            self.db_host,
            int(self.db_port),
            self.db_user,
            self.db_password,
            self.db_name
        )
        self.engine = MySQLEngine.MySQLEngine(self.config)

    # Cada método hace literalmente lo que su nombre especifica
    
    def set_user(self, values):    
        self.engine.set_user("REGISTRAR_USUARIO", values)
        # self.engine.select("CALL REGISTRAR_USUARIO('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8]))

    def update_user(self, values):
        self.engine.update_user("ACTUALIZAR_USUARIOS", values)

    def remove_user(self, id):
        # self.engine.select("DELETE FROM Usuario WHERE id='%s'" % id)
        # self.engine.select("CALL ELIMINAR_USUARIO(%s)" % id)
        self.engine.remove_user(id)

    def logout(self, values):
        self.engine.logout("Logout", values)

    def get_name(self):
        usuario = self.engine.select("SELECT username FROM Usuario WHERE id ='%s'" %(self.id))
        return usuario[0][0]

    def get_user_type(self):
        user_type = self.engine.select("SELECT tipo_usuario_id FROM Usuario WHERE id ='%s'" %(self.id))
        return "Administrador" if user_type[0][0] == 1 else "Operador"

    def get_fill_color(self):
        fill_color = self.engine.select("SELECT f_color FROM Usuario WHERE id = '%s'" % self.id)
        return fill_color[0][0]

    def get_pen_color(self):
        pen_color = self.engine.select("SELECT p_color FROM Usuario WHERE id = '%s'" % self.id)
        return pen_color[0][0]

    def login(self, values):
        self.engine.procedureLogin("Login", values)

    def get_user_data(self):
        user_data = self.engine.select("SELECT * FROM DatosUser")
        return user_data

    def get_user_pictures(self):
        user_pics = self.engine.select("Select * From DatosDibujo WHERE `Usuario`.`id` = '%s'" % self.id)
        return user_pics

    # Obtiene los dibujos de un usuario a través de un inner join de 3 tablas
    def get_user_pics(self):
        user_pics = self.engine.select("""SELECT 
	        Dibujo.id, Dibujo.var_nombre, Dibujo.tim_creacion, Usuario.id
	        FROM Usuario INNER JOIN Repositorio ON Usuario.id = Repositorio.usuario_id
            INNER JOIN Dibujo ON Dibujo.repositorio_id = Repositorio.id WHERE Usuario.id= '%s'""" % self.id)
        return user_pics

    # Obtiene un dibujo en específico
    def get_draw(self, id):
        draw = self.engine.select("SELECT json_dibujo FROM Dibujo WHERE id = '%s'" % id)
        return draw

    def get_user_info(self, id):
        user_info = self.engine.select("SELECT * FROM Usuario WHERE id = '%s'" % id)
        return user_info

    # Añade un dibujo a ambas bases de datos
    def insert_draw(self, name, draw, draw2):
        values = (name, draw, self.id, draw2)
        self.engine.insert_draw(values)
        # self.engine.insert_draw("INSERT INTO Dibujo (`var_nombre`, `json_dibujo`, `repositorio_id`) VALUES ('%s', '%s', %s);" % (name, draw, 1))
        # self.engine.select("INSERT INTO Dibujo (var_nombre, json_dibujo, repositorio_id) VALUES ('" + name + "', '" + str(json.loads(draw))  + "', " + str(1))
    
    def remove_draw(self, id):
        self.engine.remove_draw(id)