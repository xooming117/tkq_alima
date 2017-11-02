#coding=utf-8

import time
import datetime
import random
import urllib
import string
import json
import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_t():
    return str(int(round(time.time()*1000)))

def get_four():
    return str(random.randint(1000, 99999))

def get_pvid(s1):
    # 例子：10_223.208.12.179_36892_1508160081543
    s2 = '14.196.92.6'
    s3 = random.randint(1000, 99999)
    s4 = int(round(time.time()*1000))
    return '%s_%s_%d_%d' % (s1, s2, s3, s4)

def get_search_pvid():
    # 例子：10_223.208.12.179_36892_1508160081543
    return get_pvid('10')

def get_user_number_id(url):
    str = 'userNumberId'
    idx = url.find(str)
    idx += (len(str) + 1)
    return url[idx:]

# url = 'https://detail.tmall.com/item.htm?id=538096499721'
def convert(q, url):
    url = url.decode('gbk', 'replace')
    url = url.encode('utf-8', 'replace')
    return urllib.urlencode({q: url})

def get_search_referer(url):
    referer = 'http://pub.alimama.com/promo/search/index.htm?'
    referer += convert('q', url)
    referer += '&_t=' + str(int(round(time.time()*1000)))
    return referer

def dump_cookies(cookies):
    for c in cookies:
        if c['name'] == 'isg':
            print 'isg=%s' % c['value']
            break

def get_goods_url(url):
    urls = re.findall('http.+\r\n', url)
    if len(urls) == 2:
        urls[0].strip('\r\n')
        urls[1].strip('\r\n')
        return 1, urls
    else:
        return 0, urls

def get_url_params(url):
    values = url.split('?')[-1]
    params = values.split('&')
    result = {}
    for param in params:
        ps = param.split('=')
        if len(ps) == 2:
            result[ps[0]] = ps[1]
    return result

def get_pid_by_mmid(mm_id):
    # mm_124124492_38596292_143034784
    ids = mm_id.split('_')
    adzoneid = ids[3]
    siteid = ids[2]
    return adzoneid, siteid
