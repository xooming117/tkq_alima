from utils import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_account_header():
    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'pub.alimama.com',
        'Pragma': 'no-cache',
        'Referer': 'http://pub.alimama.com/myunion.htm?spm=a219t.7900221/10.1998910419.dab027959.150650b17Lg2MB',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    return header

def get_search_headers():
    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': '',
        'Host': 'pub.alimama.com',
        # 'Referer': get_search_referer(url),
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    return header

