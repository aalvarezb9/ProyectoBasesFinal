# -*- coding: utf-8 -*-

import mysql.connector

class MySQLEngine:

    def __init__(self, config):
        self.server = config.server
        self.port = config.port
        self.user = config.user
        self.password = config.password
        self.database = config.database

        self.start()

    def start(self):
        self.con = mysql.connector.connect(
            host = self.server,
            port = self.port,
            user = self.user,
            passwd = self.password,
            database = self.database
        )

        # print("con %s" % self.con)

        self.link = self.con.cursor()

    def select(self, query):
        # print(query)
        self.link.execute(query)
        # self.con.commit()
        return self.link.fetchall()

    def insert_draw(self, values):
        self.link.callproc("Dibujo", values)
        self.con.commit()

    def set_user(self, name, values):
        self.link.callproc("REGISTRAR_USUARIO", values)
        self.con.commit()

    def update_user(self, name, query):
        self.link.callproc(name, query)
        self.con.commit()
    
    def procedureLogin(self, name, values):
        au = self.link.callproc(name, values)
        self.con.commit()
        return au

    def logout(self, name, values):
        self.link.callproc(name, values)
        self.con.commit()

    def remove_user(self, id):
        values = (id, 1)
        self.link.callproc("ELIMINAR_USUARIO", values)
        self.con.commit()

    def remove_draw(self, id):
        values = (id, 1)
        self.link.callproc("EliminarDibujo", values)
        self.con.commit()

        
        
               