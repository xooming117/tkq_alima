# coding=utf-8

from selenium.common.exceptions import TimeoutException
from requests import ConnectionError
import requests
from header import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def j_req(driver, method, j_url, params1):
    my_data = []
    print '原始请求参数--method: %s, url: %s' % (method, j_url)
    print '原始请求参数--params: %s' % (params1)
    try:
        if method.upper() == 'GET':
            r = driver.request(method, j_url, params=params1)
            r.encoding = 'utf-8'
        else:
            r = driver.request(method, j_url, data=params1)
            r.encoding = 'utf-8'
        print '原始请求结果:'
        print r.content
        my_data = r.json()['data']
    except ConnectionError as c:
        print '连接异常：'
        print c
    except TimeoutException as t:
        print '读取超时异常：'
        print t
    else:
        pass
    finally:
        if not my_data or len(my_data) == 0:
            print '计划为空，未请求到数据，返回'
        print '转换成data数据:'
        print str(my_data)
        return my_data

def j_req2(driver, method, j_url, params1):
    print '原始请求参数--method: %s, url: %s' % (method, j_url)
    print '原始请求参数--params: %s' % (params1)
    headers1 = get_search_headers()
    my_data = []
    if method.upper() == 'GET':
        r = requests.get(url=j_url, params=params1, headers=headers1)
        r.encoding = 'utf-8'
        print(r.status_code)
        print(r.url)
        print '原始请求结果:'
        print(r.content)
        my_data = r.json()['data']
        print '转换成data数据:'
        print str(my_data)

    elif method.upper() == 'POST':
        r = requests.post(url=j_url, data=params1)
        print(r.status_code)
        print(r.url)
        print '原始请求结果:'
        print(r.content)
        my_data = r.json()['data']
        print '转换成data数据:'
        print str(my_data)

    return my_data

