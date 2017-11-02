#coding=utf-8
import thread

driver = None
is_new = False

lock = thread.allocate_lock()

def put_driver(d):
    global driver
    global is_new
    lock.acquire()
    driver = d
    is_new = True
    lock.release()

def get_driver():
    driver1 = None
    is_new1 = False
    global is_new
    lock.acquire()
    driver1 = driver
    is_new1 = is_new
    is_new = False
    lock.release()
    return driver1, is_new1
