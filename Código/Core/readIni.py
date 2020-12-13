# -*- coding: utf-8 -*-

"""
    ! Se obtienen los valores establecidos en el config.ini
        * Con esto se evita problemas de compatibilidad entre computadoras

    @author: Ángel
    @date: 13 \ 12 \ 2020 

"""

import configparser

class ReadINI:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('./config.ini')
        self.db_host = self.config['DEFAULT']['DB_HOST']
        self.db_name = self.config['DEFAULT']['DB_NAME']
        self.db_port = self.config['DEFAULT']['DB_PORT']
        self.db_user = self.config['DEFAULT']['DB_USER']
        self.db_password = self.config['DEFAULT']['DB_PASSWORD']

    def get_db_host(self):
        return self.db_host
        
    def get_db_name(self):
        return self.db_name

    def get_db_port(self):
        return self.db_port

    def get_db_user(self):
        return self.db_user

    def get_db_password(self):
        return self.db_password
