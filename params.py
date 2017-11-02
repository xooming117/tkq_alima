#coding=utf-8
from utils import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 根据url获取商品信息
def get_search(g_url, yxjh, tbToken):
    return {'q': g_url,
            '_t': get_t(),
            'toPage': 1,
            'auctionTag': '',
            'perPageSize': 40,
            'shopTag': yxjh,
            't': get_t(),
            'pvid': get_pvid('10'),
            '_tb_token_': tbToken
            }

# 根据商家id获取计划
def get_campaign_by_userNumberId(userNumberId, tbToken):
    return {'oriMemberId': userNumberId,
            't': get_t(),
            'pvid': get_pvid('53'),
            '_tb_token_': tbToken,
            '_input_charset': 'utf-8'
            }

# 根据商品id获取计划
def get_common_campaign_by_itemId(g_url, tbToken):
    return {'itemId': get_url_params(g_url)['id'],
            't': get_t(),
            '_tb_token_': tbToken,
            'pvid': get_pvid('10')
            }

def get_apply_common_campaign(campId, keeperid, applyreason, tbToken):
    return {'campId': campId,
            'keeperid': keeperid,
            'applyreason': applyreason,
            't': get_t(),
            '_tb_token_': tbToken,
            'pvid': get_pvid('10')
            }

# 根据计划id获取其中的所有商品
def get_goods(campaignId, shopkeeperId, userNumberId, pvid, tbToken, pageNo):
    return {'spm': 'a219t.7900221/10.1998910419.dab027959.7b6ba29fFWsZEy',
            'campaignId': campaignId,
            'shopkeeperId': shopkeeperId,
            'userNumberId': userNumberId,
            'tab': 2,
            'omid': userNumberId,
            'toPage': pageNo,
            'perPagesize': 10,
            't': get_t(),
            'pvid': pvid,
            '_tb_token_': tbToken,
            '_input_charset': 'utf-8'
            }

# 根据userNumberId获取keeperId
def get_keeper(userNumberId, tbToken):
    return {'oriMemberId': userNumberId,
            't': get_t(),
            'pvid': get_pvid('53'),
            '_tb_token_': tbToken,
            '_input_charset': 'utf-8'
            }

# 获取推广链接，长链接，短连接，二维码，淘口令
def get_tg_link(auctionid, adzoneid, siteid, tbToken):
    return {'auctionid': auctionid,
            'adzoneid': adzoneid,
            'siteid': siteid,
            'scenes': 1,
            't': get_t(),
            '_tb_token_': tbToken,
            'pvid' : get_pvid('10')
            }

