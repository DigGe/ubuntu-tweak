import os
import json
import urllib
from ubuntutweak.conf import settings

class Parser(dict):
    def __init__(self, file, key):
        try:
            self.__data = json.loads(open(file).read())
            self.init_items(key)
        except:
            self.is_available = False
        else:
            self.is_available = True

    def init_items(self, key):
        for item in self.__data:
            item['fields']['id'] = item['pk']
            self[item['fields'][key]] = item['fields']

    def get_by_lang(self, key, field):
        value = self[key][field]
        if settings.LANG in value.keys():
            return value[settings.LANG]
        else:
            return value['raw']
