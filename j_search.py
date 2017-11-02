# coding=utf-8

from selenium.common.exceptions import NoSuchElementException

from utils import *
from j_request import *
import params
from browser import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getUserNumberId(driver, g_url):
    # 跳转到超级搜索
    driver.get('http://pub.alimama.com/promo/search/index.htm')
    time.sleep(1)

    campaign_type = '0'
    userNumberId = ''

    # 搜索某一商品
    try:
        txt_search = driver.find_element_by_xpath('//*[@id="q"]')
        bt_search = driver.find_element_by_xpath('//*[@id="magix_vf_header"]/div/div/div[2]/div[2]/button')
        txt_search.send_keys(g_url)
        bt_search.click()
        time.sleep(1)
        check_yx = driver.find_element_by_xpath('//*[@id="J_sort_filter"]/div/div[2]/span[2]/label')
        check_yx.click()
        time.sleep(1)
    except NoSuchElementException as e:
        print '输入商品时，未找到输入网页元素'
        print e


    try:
        ele = driver.find_element_by_xpath('//*[@id="J_search_results"]/div/div/div[3]/div[1]/span/a')
        url = ele.get_attribute('href')
        print url
        userNumberId = get_user_number_id(url)
    except NoSuchElementException as e:
        campaign_type = '9'
        print '确认搜索后，网页未找到商品，请确认url是否正确: '
        print g_url
        print e

    try:
        ele = driver.find_element_by_xpath('//*[@id="J_search_results"]/div/div/div[3]/div[2]/a')
        title = ele.get_attribute('title')
        if title and title.find('营销计划')>0:
            campaign_type = '1'
        elif title and title.find('定向计划')>0:
            campaign_type = '2'

    except NoSuchElementException as e:
        print '网页未找营销: '
        print g_url
        print e

    # 跳转到商品的店铺
    # shop = driver.find_element_by_xpath('//*[@id="J_search_results"]/div/div/div[3]/div[1]')
    # shop.click()
    # time.sleep(1)

    return userNumberId, campaign_type

def getGoodsById(driver, g_url, shopTag):
    tbToken = driver.get_cookie('_tb_token_')['value']
    params1 = params.get_search(g_url, shopTag, tbToken)
    return j_req(driver, 'GET', 'http://pub.alimama.com/items/search.json', params1)

# getGoodsById(get_chrome_browser(),'https://detail.tmall.com/item.htm?id=560101611168','')