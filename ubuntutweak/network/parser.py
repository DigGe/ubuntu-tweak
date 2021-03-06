import os
import json
import urllib

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

if __name__ == '__main__':
    file = os.path.expanduser('~/.ubuntu-tweak/apps/data/apps.json')
    parser = Parser(file, 'package')
    import pdb
    pdb.set_trace()
