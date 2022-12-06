"""
author: Yuval Bahar
date: 6/12/2022
description: checks the synchronization while mode is processing
"""

#  ----------------- IMPORTS -----------------

from filedatabase import FileDatabase
from syncdatabase import SyncDatabase
from multiprocessing import Process
import logging

# ----------------- CONSTANTS - ----------------

FILENAME = "new_file"
MODE = 'processing'
READER_NUM = 50
WRITER_NUM = 10
FORMAT = '%(asctime)s %(levelname)s %(threadName)s %(message)s'
FILENAMELOG = 'logging_process.text'

# ----------------- FUNCTIONS - ----------------


def reader(database):
    """
    reader is trying to get an access to read the value from the dictionary
    :param database: an object that one of his feature is a dictionary
    :return: None
    """
    logging.debug("reader started")
    for i in range(100):
        flag = database.get_value(i) == i or database.get_value(i) is None
        assert flag
    logging.debug("reader left")


def writer(database):
    """
    writer is trying to get an access to write the value from the dictionary
    :param database: an object that one of his feature is a dictionary
    :return: None
    """
    logging.debug("writer started")
    for i in range(100):
        assert database.set_value(i, i)
    for i in range(100):
        flag = database.delete_value(i) == i or database.delete_value(i) is None
        assert flag
    logging.debug("writer left")


def main():
    """
    combine the running of the writers and the readers by multiprocessing
    :return: None
    """
    #  checks the access of writing and reading without competition
    # צריך להדפיס כל פעם שלקוח מקבל גישהלכתוב או לקרוא, וכל פעם שהוא משחרר את הגישה
    logging.basicConfig(filename=FILENAMELOG, level=logging.DEBUG, format=FORMAT)
    database = SyncDatabase(MODE, FileDatabase(FILENAME))
    # הרשאת כתיבה כאשר יש תחרות
    all_processes = []
    for i in range(0, READER_NUM):
        proc = Process(target=reader, args=(database, ))
        all_processes.append(proc)
    for i in range(0, WRITER_NUM):
        proc = Process(target=writer, args=(database, ))
        all_processes.append(proc)
    for i in all_processes:
        i.start()
    for i in all_processes:
        i.join()


if __name__ == "__main__":
    main()
