import json
import copy

from pprint import pprint


class Convert():
    def __init__(self, gm_value):
        self.gm_value = gm_value
        
    def convert_quantity(self, value, quantity):
        value.update({'quantity': quantity * self.gm_value})
        return value


    def get_child(self, value):
        if isinstance(value, dict):
            if value.get('quantity') is not None:
                quantity = value.get('quantity')
                mydict = self.convert_quantity(value, quantity)
                return mydict

            new_dict = dict()
            for k, v in value.items():
                new_dict.update({k: self.get_child(value.get(k))})        #   Recursive Call
            return new_dict

        if isinstance(value, list):
            return [self.get_child(i) for i in value]        #   Recursive Call


    def read_data(self):
        jsondata = json.load(open('data.json'))
        gm_100 = jsondata.get('data').get('100gm')
        return self.get_child(gm_100)


pprint(Convert(0.23).read_data())
pprint(Convert(0.50).read_data())
pprint(Convert(2.60).read_data())
