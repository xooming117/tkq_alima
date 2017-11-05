#coding=utf-8

from conf import *
from j_campaign import *
from j_search import *
from mongodb import *
import types

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_campaigns(goods):
    driver_old = None

    while True:
        # 判断是否新开Chrome，并且Driver处于登录状态
        driver1, is_new1 = get_driver()
        print 'is_new1:'+str(is_new1)
        if not driver1:
            print '账号未登录，get_campaigns采集暂停'
            time.sleep(5)
            continue

        # 已处于登录状态，如果有新的Chrome打开，关闭旧的
        if is_new1:
            if driver_old:
                driver_old.close()
            driver_old = driver1

        # 获取一条采集信息，无则休眠
        cai = get_one_cai()
        print 'cai:'+str(cai)
        if not cai:
            time.sleep(10)
            continue

        g_url = cai['good_url']
        # g_url = 'https://detail.tmall.com/item.htm?id=539918019609'
        print 'read g_url: ' + g_url

        # 获取商品的userNumberId ok
        userNumberId, yxjh = getUserNumberId(driver1, g_url)
        print 'userNumberId:' + userNumberId
        print 'yxjh: ' + yxjh
        if userNumberId == '':
            print '无商品userNumberId, 请求下一个'
            continue

        # 获取商品信息
        r = getGoodsById(driver1, g_url, '')
        if len(r) == 0:
            continue

        print r['pageList'][0]
        r['pageList'][0]['yxjh'] = int(yxjh)
        r['pageList'][0]['userNumberId'] = int(userNumberId)


        # 获取商品推广链接 ok
        pid = 'mm_124124492_38596292_143034784'
        r1 = getAuctionCode(driver1, g_url, pid)
        print type(r1)
        print '获取商品推广链接结果：' + str(r1)

        try:
            if r1 and len(r1) > 1:
                r['pageList'][0]['taoToken'] = r1.get('taoToken', '')
                r['pageList'][0]['clickUrl'] = r1.get('clickUrl', '')
                r['pageList'][0]['shortLinkUrl'] = r1.get('shortLinkUrl', '')
                r['pageList'][0]['couponLinkTaoToken'] = r1.get('couponLinkTaoToken', '')
                r['pageList'][0]['couponShortLinkUrl'] = r1.get('couponShortLinkUrl', '')
                r['pageList'][0]['qrCodeUrl'] = r1.get('qrCodeUrl', '')
                r['pageList'][0]['couponLink'] = r1.get('couponLink', '')

                print str(r['pageList'][0])
                save_goods(r['pageList'][0])

        except KeyError as e:
            print '数据解析错误１'
            print e
        except TypeError as e:
            print '数据解析错误２'
            print e


        #

        # 获取商家的所有计划 ok
        # r = getCampaignByUserNumberId(driver1, userNumberId)
        # print '结果：' + str(r)
        #
        # # 获取店铺信息 ok
        # r = getShopInfo(driver1, userNumberId)
        # print '结果：' + str(r)

        # 获取商品的计划　ok
        # cams = getCommonCampaignByItemId(driver1, g_url)
        # print '结果：' + str(cams)


        # 申请定向计划
        # for c in cams:
        #     print c['CampaignType'] + c['CampaignName'] + str(c['CampaignID'])
        #     if c['CampaignType'] == '定向推广计划':
        #         applyreason = '淘客圈(taokequan.com)，帮您推广，谢谢！'
        #         # ok
        #         r = applyForCommonCampaign(driver1, c['CampaignID'], c['ShopKeeperID'], applyreason)
        #         print '结果：' + str(r)
        #         time.sleep(10)
        # continue

        # 获取店铺信息
        # keeper = get_shopdetail(driver1, userNumberId)
        # save_keeper(keeper)

        # 获取商品的所有推广计划
        # cs = get_top_campaign_by_userNumberId(driver1, userNumberId)
        # print str(cs)
        # insert_many_campaign(userNumberId, cs)

        # 获取推广计划里面的所有商品
        # for c in cs:
        #     print 'one c:' + str(c)
        #     save_goods_by_campaignId(driver1, c['campaignId'], c['shopKeeperId'], userNumberId)

        # 设置采集状态，２为完成状态
        cai['status'] = 2
        set_cai_status(cai)
