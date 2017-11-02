#coding=utf-8

import pymongo
from pymongo import MongoClient
from pymongo import errors

import sys
import datetime
from match_nodejs import *


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 连接mongodb数据库
client = MongoClient('mongodb://mongodb:27017/')
# 指定数据库名称
db = client.tbk_database
# 获取非系统的集合
db.collection_names(include_system_collections=False)
print db.collection_names()


def get_one_cai():
    cai = db.cai
    return cai.find_one_and_update({'status': 0}, {'$set': {'status': 1}})

def set_cai_status(data):
    cai = db.cai
    return cai.update({'_id': data['_id']}, {'$set': {'status': 2}})

def get_cai_by_id(_id):
    cai = db.cai
    return cai.find({'_id': _id})

def insert_many_goods(gs):
    goods = db.goods
    for g in gs:
        result = goods.update({'auctionId': g['auctionId']}, g, upsert=True)
        print result

def insert_many_campaign(oriMemberId, data_campaign):
    campaign = db.campaign
    for item in data_campaign:
        item['oriMemberId'] = oriMemberId
        result_set = campaign.find({'oriMemberId': oriMemberId, 'campaignId': item['campaignId']})
        print 'campaign.find item count: ' + str(result_set.count())
        # 存在则更新，需要用到oriMemberId和campaignId唯一标示一条记录
        result = None
        print '准备插入的数据记录：' + str(item)
        if result_set.count() > 0:
            result = campaign.update({'oriMemberId': oriMemberId, 'campaignId': item['campaignId']}, item)
        # 不存在则插入
        else:
            result = campaign.insert(item)

        result_set.close()
        print result

def save_keeper(data_keeper):
    keeper = db.keeper
    # 存在则更新，不存在则插入
    print '准备插入的数据记录：' + str(data_keeper)
    result = keeper.update({'oriMemberId': keeper['oriMemberId']}, data_keeper, upsert=True)
    print result

def save_goods(data):
    goods = db.goods
    data['_id'] = get_good_seq_id()
    data['isDelete'] = False
    data['createAt'] = datetime.datetime.now()
    data['updateAt'] = datetime.datetime.now()

    print 'auctionId'
    print data['auctionId']
    print str(data)

    try:
        result = goods.update({'auctionId': data['auctionId']}, data, upsert=True)
        print 'save goods result:'
        print str(result)
    except errors.WriteError as e:
        print e

# c = get_one_cai()
# _id = c['_id']
# print c
# c['status'] = 2
# set_cai_status(c)
# print str(get_cai_by_id(_id))

# gs = [{'name':'xx1', 'age': 10},{'name':'xx2'},{'name':'xx3'}]
# insert_many(gs)
#
# goods = db.goods
# result = goods.find()
# for re in result:
#     print(re)