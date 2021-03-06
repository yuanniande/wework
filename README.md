
# About

wework 是为了简化开发者对企业微信API接口的使用而设计的，API调用库系列之 python 版本    

[官方文档](https://work.weixin.qq.com/api/doc)

# Install & Update

```
pip install -U wework
```

# A Simple Example

```python
from wework.CorpApi import CorpApi, CORP_API_TYPE
api = CorpApi(TestConf['CORP_ID'], TestConf['APPROVAL_APP_SECRET'])
params = {"starttime": 1566871220, "endtime": 1566874224}
response = api.httpCall(CORP_API_TYPE['GET_APPROVAL_DATA'], params)
```

详细使用方法参考examples路径下的样例

# 关于token的缓存

token是需要缓存的，不能每次调用都去获取token，[否者会中频率限制](https://work.weixin.qq.com/api/doc#10013/%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%BC%93%E5%AD%98%E5%92%8C%E5%88%B7%E6%96%B0access_token)  
在本库的设计里，token是以类里的一个变量缓存的
比如api/src/CorpApi.py 里的access_token变量
在类的生命周期里，这个accessToken都是存在的， 当且仅当发现token过期，CorpAPI类会自动刷新token
刷新机制在 api/src/AbstractApi.py
所以，使用时，只需要全局实例化一个CorpAPI类，不要析构它，就可一直用它调函数，不用关心 token  
```
api = CorpAPI(corpid, corpsecret);
api.dosomething()
api.dosomething()
api.dosomething()
....
```
当然，如果要更严格的做的话，建议自行修改，全局缓存token，比如存redis、存文件等，失效周期设置为2小时。

# 注意事项

1. WXBizMsgCrypt.py文件封装了WXBizMsgCrypt接口类，提供了用户接入企业微信的三个接口，Sample.py文件提供了如何使用这三个接口的示例，ierror.py提供了错误码。
2. WXBizMsgCrypt封装了VerifyURL, DecryptMsg, EncryptMsg三个接口，分别用于开发者验证回调url，收到用户回复消息的解密以及开发者回复消息的加密过程。使用方法可以参考Sample.py文件。
3. 加解密协议请参考企业微信官方文档。
4. 本代码用到了pycrypto第三方库，请开发者自行安装此库再使用。

# 其它语言的库推荐

* python : https://github.com/sbzhu/weworkapi_python  abelzhu@tencent.com(企业微信团队)
* ruby : https://github.com/mycolorway/wework  MyColorway(个人开发者)
* php : https://github.com/sbzhu/weworkapi_php  abelzhu@tencent.com(企业微信团队)
* golang : https://github.com/sbzhu/weworkapi_golang  ryanjelin@tencent.com(企业微信团队)
* golang : https://github.com/doubliekill/EnterpriseWechatSDK  1006401052yh@gmail.com(个人开发者)


# Contact us
abelzhu@tencent.com
