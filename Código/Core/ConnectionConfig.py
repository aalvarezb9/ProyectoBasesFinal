# -*- coding: utf-8 -*-


"""
    ! Hace la conexión con la BD con los parámetros en config.ini
       

    @author: Ángel
    @date: 13 \ 12 \ 2020 

"""

class ConnectionConfig:

    def __init__(self,server,port,user,password,database):
        self.server = server
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        
