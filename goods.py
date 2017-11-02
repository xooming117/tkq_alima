#coding=utf-8

import sys
from operator import itemgetter, attrgetter
from seleniumrequests import Chrome

from driver import *
from utils import *
from j_campaign import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# driver = get_normal_driver()

driver = Chrome()
driver.set_window_size(1440, 1000)

def location_page(driver):
    print driver

# 登录
driver.get('https://www.alimama.com/member/login.htm')
while driver.current_url != 'https://www.alimama.com/index.htm':
    time.sleep(1)

# 跳转到超级搜索
driver.get('http://pub.alimama.com/promo/search/index.htm')
time.sleep(1)

# 搜索某一商品
txt_search = driver.find_element_by_xpath('//*[@id="q"]')
bt_search = driver.find_element_by_xpath('//*[@id="magix_vf_header"]/div/div/div[2]/div[2]/button')
txt_search.send_keys('https://detail.tmall.com/item.htm?id=538096499721')
bt_search.click()
time.sleep(3)

# 跳转到商品的店铺
shop = driver.find_element_by_xpath('//*[@id="J_search_results"]/div/div/div[3]/div[1]')
shop.click()
time.sleep(5)

# 获取userNumberId
print driver.current_url
print driver.current_window_handle

ele = driver.find_element_by_xpath('//*[@id="J_search_results"]/div/div/div[3]/div[1]/span/a')
url = ele.get_attribute('href')
print url
userNumberId = get_user_number_id(url)
print userNumberId

# 获取店铺的所有营销计划
t1 = str(datetime.datetime.now().microsecond)
t2 = time.sleep(0.1)
params1 = {
    'oriMemberId': userNumberId,
    't': get_t(),
    'pvid': get_pvid('53'),
    '_tb_token_':driver.get_cookie('_tb_token_'),
    '_input_charset': 'utf-8'
}

print params1

r = driver.request('GET', 'http://pub.alimama.com/shopdetail/campaigns.json', params=params1)
print r.text
my_data = r.json()['data']['campaignList']
campaigns = []
for c in my_data:
    campaigns.append(Campaign(c['campaignId'], c['shopKeeperId'], c['campaignName'], c['campaignComments'], c['properties'], c['campaignType'],
                              c['avgCommission'], c['rptCpsShCampaign30d']['thirtyCmSettleNum'],
                              c['rptCpsShCampaign30d']['thirtyCmCommisionAmt'],
                              c['rptCpsShCampaign30d']['ninetyPubNum'],
                              c['createTime'], c['startTime'], c['updateTime'], c['endTime']))

campaigns = sorted(campaigns, key=attrgetter('avgCommission'), reverse=True)

for c in campaigns:
    print c

c = campaigns[0]
# 获取某个佣金计划里面的所有商品
t1 = str(datetime.datetime.now().microsecond)
params1 = {
    'spm': 'a219t.7900221/10.1998910419.dab027959.7b6ba29fFWsZEy',
    'campaignId': c.campaignId,
    'shopkeeperId': c.shopKeeperId,
    'userNumberId': userNumberId,
    'tab': 2,
    'omid': userNumberId,
    'toPage': 1,
    'perPagesize': 10,
    't': t1,
    'pvid': '',
    '_tb_token_': driver.get_cookie('_tb_token_'),
    '_input_charset': 'utf-8'
}


