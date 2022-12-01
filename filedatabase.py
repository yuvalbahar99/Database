from database import Database
import pickle


class FileDatabase(Database):

    def __init__(self, file):
        super().__init__()
        self.file = file
        try:
            f = open(self.file, "x")
        except:
            pass

    def dump_file(self):
        pickle.dump(self.dict, open(self.file, "wb"))

    def load_file(self):
        try:
            self.dict = pickle.load(open(self.file, "rb"))
        except:
            pass

    def get_value(self, key):
        self.load_file()
        return super().get_value(key)

    def set_value(self, key, val):
        self.load_file()
        flag = super().set_value(key, val)
        self.dump_file()
        return flag

    def delete_value(self, key):
        self.load_file()
        flag = super().delete_value()
        self.dump_file()
        return flag
