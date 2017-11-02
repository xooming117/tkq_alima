#!/usr/bin/python
# coding:utf-8

import requests

import sys

print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

while True:
    url = 'http://pub.alimama.com/items/search.json?q=https://detail.tmall.com/item.htm?id=560101611168'
    r = requests.get(url)
    r.encoding = 'utf-8'
    print('abc')
    print('中文')
    print(r.content)