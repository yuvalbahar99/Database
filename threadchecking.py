from filedatabase import FileDatabase
from syncdatabase import SyncDatabase
from threading import Thread
import logging

FILENAME = "newfile"
MODE = "threading"


def reader(sync, value, database):
    for i in range(100000):
        assert value == database.get_value(value)


def writer(sync, key, value, database):
    for i in range(100000):
        assert database.set_value(key,value)


def main():
    #  checks the access of writing and reading without compitition
    database = SyncDatabase(MODE, FileDatabase(FILENAME))


if __name__ == "__main__":
    main()