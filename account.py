# coding=utf-8

import time

import sys
from browser import *
from qemail import *
from selenium.common.exceptions import NoSuchElementException

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Account:
    def __init__(self, memberid, mmNick, tkMemberRank, ip):
        self.memberid = memberid
        self.mmNick = mmNick
        self.tkMemberRank = tkMemberRank
        self.ip = ip

    def __repr__(self):
        return '%d %s %d %s' % (self.memberid, self.mmNick, self.tkMemberRank, self.ip)

def er_login(driver):
    status = 0
    try:
        er_url = driver.find_element_by_xpath('//*[@id="J_QRCodeImg"]/img').get_attribute('src')
        print '获取二维码url:'
        print er_url
        send_email('淘宝客', er_url)
        status = 1
    except NoSuchElementException as e:
        status = 2
        print e
    return status

def input_login(driver):
    status = 0
    try:
        driver.find_element_by_id("TPL_username_1").send_keys("xoming117")
        time.sleep(1)
        driver.find_element_by_id("TPL_password_1").send_keys("xoming036146")
        time.sleep(1)
        driver.find_element_by_id("J_SubmitStatic").click()
        time.sleep(5)
        status = 1
    except NoSuchElementException as e:
        status = 2
        print e
    return status

def do_login(driver):
    is_login = False
    re = er_login(driver)
    if re == 1:
        is_login = True
    elif re == 2:
        input_login(driver)
    else:
        pass
    return is_login

def login():
    wait_timeout = [0, 180, 360, 540, 720]
    wait_num = 0
    start_time = int(time.time())
    print 'start time:'+str(start_time)
    is_send = False
    b = get_chrome_browser()
    # 登录
    # b.get('https://login.taobao.com/member/login.jhtml?style=mini&newMini2=true&css_style=alimama&from=alimama&redirectURL=http%3A%2F%2Fwww.alimama.com&full_redirect=true&disableQuickLogin=true')
    b.get('https://login.taobao.com/member/login.jhtml?style=mini&newMini2=true&from=alimama&redirectURL=http%3A%2F%2Flogin.taobao.com%2Fmember%2Ftaobaoke%2Flogin.htm%3Fis_login%3d1&full_redirect=true&disableQuickLogin=true')
    while b.current_url != 'https://www.alimama.com/index.htm':
        cur = int(time.time())
        print 'time cha:' + str((cur-start_time)) + '-' + str(wait_timeout[wait_num])

        if (cur-start_time) > wait_timeout[wait_num]:
            print '请抓紧输入账号密码！！！'
            b.refresh()
            time.sleep(3)
            re = do_login(b)

            wait_num += 1
            print 'wait_num:' + str(wait_num)

            # 所有等待超时
            if wait_num == len(wait_timeout):
                b.close()
                b = None
                print '所有等待超时，耐心等待下一次调度'
                break
        else:
            time.sleep(3)
            print 'ssss'
    return b
