#coding=utf-8
from operator import itemgetter, attrgetter

import params
import utils
from mongodb import *
from j_request import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Goods:
    def __init__(self, campaignID, jd):
        #营销计划ｉｄ
        self.campaignID = campaignID
        #拍卖id
        self.auctionId = jd['auctionId']
        self.auctionUrl = jd['auctionUrl']
        self.title = jd['title']
        self.pictUrl = jd['pictUrl']
        #折扣价
        self.zkPrice = jd['zkPrice']
        #折扣比
        self.zkRate = jd['zkRate']
        #活动类型
        self.zkType = jd['zkType']
        #评论数量
        self.commentCount = jd['commentCount']
        #用户类型
        self.userType = jd['userType']
        #佣金比例
        self.commissionRate = jd['commissionRate']
        #佣金金额
        self.calCommission = jd['calCommission']
        #30天销量
        self.biz30day = jd['biz30day']
        #30天推广量
        self.totalNum = jd['totalNum']
        #30天支付佣金
        self.totalFee = jd['totalFee']
        #掌柜id
        self.userNumberId = jd['userNumberId']
        #掌柜昵称
        self.nick = jd['nick']

    def __repr__(self):
        return '%s %d %d %d %s %s %s ' \
               '%f %d %s %s %d %d ' \
               '%f %d %d %d ' % \
               (self.nick, self.userNumberId, self.campaignID, self.auctionId, self.auctionUrl, self.title, self.pictUrl,
                self.zkPrice, self.zkRate, self.zkType, self.commentCount, self.userType, self.commissionRate,
                self.calCommission, self.biz30day, self.totalNum, self.totalFee)


class Campaign:
    def __init__(self, campaignId, shopKeeperId, campaignName, campaignComments, properties, campaignType, avgCommission, thirtyCmSettleNum, thirtyCmCommisionAmt, ninetyPubNum,
                 createTime, startTime, updateTime, endTime):
        # 活动ID
        self.campaignId = campaignId
        #
        self.shopKeeperId = shopKeeperId
        # 活动名称
        self.campaignName = campaignName
        # 活动描述
        self.campaignComments = campaignComments
        # 是否审核, 1不需要，３需要
        self.properties = properties
        # 推广类型, 1是通用，２是定向
        self.campaignType = campaignType
        # 推广佣金比例
        self.avgCommission = avgCommission
        # 30天推广量
        self.thirtyCmSettleNum = thirtyCmSettleNum
        # 30天支出的佣金
        self.thirtyCmCommisionAmt = thirtyCmCommisionAmt
        # 参与淘客数量
        self.ninetyPubNum = ninetyPubNum
        # 活动创建时间
        self.createTime = createTime
        # 活动开始时间
        self.startTime = startTime
        # 活动更新时间
        self.updateTime = updateTime
        # 活动结束时间
        self.endTime = endTime

    def __repr__(self):
        return '%d %d %s %s\n %d %d %d %d %d %d %s %s %s %s' % \
               (self.campaignId, self.shopKeeperId, self.campaignName, self.campaignComments, self.properties, self.campaignType,
                self.avgCommission, self.thirtyCmSettleNum, self.thirtyCmCommisionAmt, self.ninetyPubNum,
                self.createTime, self.startTime, self.updateTime, self.endTime)

# 根据商家id获取计划，一个商家可能对应多个计划 ok
def getCampaignByUserNumberId(driver, userNumberId):
    _tb_token_ = driver.get_cookie('_tb_token_')['value']
    params1 = params.get_campaign_by_userNumberId(userNumberId, _tb_token_)
    return j_req(driver, 'GET', 'http://pub.alimama.com/shopdetail/campaigns.json', params1)

# 根据商家id获取店铺详情 ok
def getShopInfo(driver, userNumberId):
    _tb_token_ = driver.get_cookie('_tb_token_')['value']
    params1 = params.get_keeper(userNumberId, _tb_token_)
    return j_req(driver, 'GET', 'http://pub.alimama.com/shopdetail/shopinfo.json', params1)

# 根据商家id获取计划，一个商品可能对应多个计划 ok
def getCommonCampaignByItemId(driver, g_url):
    _tb_token_ = driver.get_cookie('_tb_token_')['value']
    params1 = params.get_common_campaign_by_itemId(g_url, _tb_token_)
    return j_req(driver, 'GET', 'https://pub.alimama.com/pubauc/getCommonCampaignByItemId.json', params1)

# 申请定向计划 ok
def applyForCommonCampaign(driver, campId, keeperid, applyreason):
    _tb_token_ = driver.get_cookie('_tb_token_')['value']
    data1 = params.get_apply_common_campaign(campId, keeperid, applyreason, _tb_token_)
    return j_req(driver, 'POST', 'http://pub.alimama.com/pubauc/applyForCommonCampaign.json', data1)

# 获取推广链接，长链接，短连接，二维码，淘口令 ok
def getAuctionCode(driver, g_url, pid):
    tbToken = driver.get_cookie('_tb_token_')['value']
    adzoneid, siteid = utils.get_pid_by_mmid(pid)
    ps = utils.get_url_params(g_url)
    auctionid = ps['id']
    params1 = params.get_tg_link(auctionid, adzoneid, siteid, tbToken)
    return j_req(driver, 'GET', 'https://pub.alimama.com/common/code/getAuctionCode.json', params1)

