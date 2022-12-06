"""
author: Yuval Bahar
date: 6/12/2022
description: get, set and deletes values from the dictionary
using the file
"""

#  ----------------- IMPORTS -----------------

from database import Database
import pickle


# ----------------- FUNCTIONS - ----------------


class FileDatabase(Database):

    def __init__(self, file):
        """
        initialize new class that has a dictionary in a file
        :param file: name of the file that the dictionary will be written in
        """
        super().__init__()
        self.file = file
        try:
            f = open(self.file, "x")
        except:
            pass

    def dump_file(self):
        """
        write in the file
        :return: None
        """
        pickle.dump(self.dict, open(self.file, "wb"))

    def load_file(self):
        """
        read from the file
        :return: None
        """
        try:
            self.dict = pickle.load(open(self.file, "rb"))
        except:
            pass

    def get_value(self, key):
        """
        returns the value of the value of the key in the dictionary
        :param key: key of the dictionary
        :return: the value of the value of the key's dictionary
        """
        self.load_file()
        return super().get_value(key)

    def set_value(self, key, val):
        """
        changes the value of the value of the key in the dictionary
        :param key: key of the dictionary
        :param val: value to put in the dictionary
        :return: True/ False (if it was successful)
        """
        self.load_file()
        flag = super().set_value(key, val)
        self.dump_file()
        return flag

    def delete_value(self, key):
        """
        deletes the value of the value of the key in the dictionary
        :param key: key of the dictionary
        :return: the value that was deleted
        """
        self.load_file()
        flag = super().delete_value(key)
        self.dump_file()
        return flag
