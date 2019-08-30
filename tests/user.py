from wework.CorpApi import CorpApi, CORP_API_TYPE
from wework.AbstractApi import ApiException
from .conf import *

api = CorpApi(TestConf['CORP_ID'], TestConf['CONTACT_SYNC_SECRET'])

try:
    response = api.httpCall(
        CORP_API_TYPE['USER_CREATE'],
        {
            'userid': 'zhangsan',
            'name': 'zhangsanfeng',
            'mobile': '131488888888',
            'email': 'zhangsan@ipp.cas.cn',
            'department': 1,
        })
    print(response)
    response = api.httpCall(
        CORP_API_TYPE['USER_GET'],
        {
            'userid': 'zhangsan',
        })
    print(response)
    response = api.httpCall(
        CORP_API_TYPE['USER_DELETE'],
        {
            'userid': 'zhangsan',
        })
    print(response)

except ApiException as e:
    print(e.errCode, e.errMsg)
    response = api.httpCall(
        CORP_API_TYPE['USER_DELETE'],
        {
            'userid': 'zhangsan',
        })
    print(response)
