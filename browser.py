# -*- coding: utf-8 -*-

from seleniumrequests import Chrome

def get_chrome_browser():
    b = Chrome()
    b.set_window_size(1440, 1000)
    return b
