# -*- coding: utf-8 -*-

import os
import json

class GetId:
    def __init__(self):
        pass

    def get_id(self):
        with open(os.getcwd() + '/Core/cookie') as f:
            userInfo = json.load(f)

        return userInfo["id"]