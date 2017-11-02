#coding=utf-8

import pymongo
from pymongo import MongoClient
import sys

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 连接mongodb数据库
client = MongoClient('mongodb://mongodb:27017/')
# 指定数据库名称
db = client.home
# 获取非系统的集合
db.collection_names(include_system_collections=False)
print db.collection_names()

def get_good_seq_id():
    cc = db.seq
    results = cc.find_one_and_update({'_id': 'goods'}, {'$inc': {'seq': 1}});
    if not results:
        cc.insert({'_id': 'goods', 'seq': 1})
        results = cc.find_one_and_update({'_id': 'goods'}, {'$inc': {'seq': 1}});
    return results['seq']
