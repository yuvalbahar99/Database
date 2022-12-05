from filedatabase import FileDatabase
from syncdatabase import SyncDatabase
from threading import Thread
import logging

FILENAME = "newfile"
MODE = "threading"
READER_NUM

def reader(database):
    logging.debug("reader joined")
    for i in range(100000):
        assert i == database.get_value(i)
    logging.debug("reader left")


def writer(database):
    logging.debug("writer joined")
    for i in range(100000):
        assert database.set_value(i,i)
    logging.debug("writer left")


def main():
    #  checks the access of writing and reading without compitition
    # צריך להדפיס כל פעם שלקוח מקבל גישהלכתוב או לקרוא, וכל פעם שהוא משחרר את הגישה
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')
    database = SyncDatabase(MODE, FileDatabase(FILENAME))
    # הרשאת כתיבה כאשר אין תחרות
    logging.debug("----- no competition -----")
    writer(database)
    reader(database)
    # הרשאת כתיבה כאשר יש תחרות
    logging.debug("----- with competition -----")
    all_threads = []
    for i in range(0, 10):
        thread = Thread(target=writer, args=(database, ))
        all_threads.append(thread)
        thread.start()
    for i in all_threads:
        i.join()
    for i in range(0, 50):
        thread = Thread(target=reader, args=(database, ))
        all_threads.append(thread)
        thread.start()
    for i in all_threads:
        i.join()

if __name__ == "__main__":
    main()
    
