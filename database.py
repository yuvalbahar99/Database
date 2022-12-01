class Database:

    def __init__(self):
        self.dict = {None:None}

    def set_value(self, key, val):
        self.dict.update({key: val})
        return True

    def get_value(self, key):
        if key in self.dict.keys():
            return self.dict[key]
        return None

    def delete_value(self, key):
        if key in self.dict.keys():
            return self.dict.pop(key)
        return None
