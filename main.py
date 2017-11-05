# coding=utf-8

import sys
import schedule
import threading
from Queue import Queue

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from account import *
from conf import *
from task import *


# 开启采集营销计划任务
def start_get_campaign_task():
    t = threading.Thread(target=get_campaigns, args=())
    t.setDaemon(True)
    t.start()


def init1():
    d = login()
    if d:
        put_driver(d)


def init():
    init1()
    schedule.every(10).minutes.do(init1)


def start():
    start_get_campaign_task()


def main():
    init()
    start()
    while True:
        schedule.run_pending()
        time.sleep(3)


if __name__ == '__main__':
    main()
