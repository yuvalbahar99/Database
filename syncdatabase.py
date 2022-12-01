import threading
import multiprocessing
from filedatabase import FileDatabase

class Syncdatabase():

    def __init__(self, mode, database):
        super().__init__()
        self.mode = mode
        self.database = database
        if self.mode == 'threading':
            self.lock = threading.Lock()
            self.semaphore = threading.Semaphore(10)
        if self.mode == 'processing':
            self.lock = multiprocessing.Lock()
            self.semaphore = multiprocessing.Semaphore(10)

    def write_access(self):
        self.lock.acquire()
        for i in range(10): # אם לכותב הרשאת כתיבה לכל האחרים אין גם לקריאה
            self.semaphore.acquire()

    def write_release(self):
        for i in range(10):
            self.semaphore.release()
        self.lock.release()

    def read_access(self):
        self.semaphore.acquire()

    def read_release(self):
        self.semaphore.release()

    def get_value(self, key):
        self.read_access()
        flag = self.database.get_value(key)
        self.read_release()
        return flag

    def set_value(self, key, val):
        self.write_access()
        flag = self.database.set_value(key, val)
        self.write_release()
        return flag

    def delete_value(self, key):
        self.write_access()
        flag = self.database.delete_value(key)
        self.write_release()
        return flag
