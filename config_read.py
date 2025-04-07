import json


class RJson:
    @staticmethod
    def readjson(path):
        with open(path) as file:
            data = json.load(file)
            return data
