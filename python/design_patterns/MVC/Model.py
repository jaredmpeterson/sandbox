import json


class Person(object):
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last

    def name(self):
        return f'{self.first} {self.last}'

    @classmethod
    def get_all(self):
        with open('db.json', 'r') as db:
            data = json.load(db)
        result = []
        for item in data:
            # item = json.load(item)
            person = Person(item['first'], item['last'])
            result.append(person)
        return result
