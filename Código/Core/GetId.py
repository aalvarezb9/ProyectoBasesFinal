# -*- coding: utf-8 -*-


"""
    ! Obtiene el id del usuario activo que está guardado temporalmente en un archivo json
        

    @author: Ángel
    @date: 13 \ 12 \ 2020 

"""

import os
import json

class GetId:
    def __init__(self):
        pass

    def get_id(self):
        with open(os.getcwd() + '/Core/cookie') as f:
            userInfo = json.load(f)

        return userInfo["id"]
