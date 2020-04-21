import json
from datetime import datetime

import requests

from test_requests.test_wework.api.base_api import BaseApi


class WeWork(BaseApi):
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "ww1a31c218ee50b1a9"
    token = dict()
    token_time = dict()
    secret = "P4xQ_fcopeWhEP-MSYn_7rj_rwKX2AIzl4M4Itznm7E"

    @classmethod
    def get_token(cls, secret=secret):
        # todo
        if secret is None:
            # todo:token制度发生辩护，在这个地方决定是否重新获取
            return cls.token[secret]
        # 避免重复请求，提高速度
        if secret not in cls.token.keys():
            r = cls.get_access_token(secret)
            cls.token[secret] = r["access_token"]
            cls.token_time[secret] = datetime.now()
        return cls.token[secret]

    @classmethod
    def get_access_token(cls, secret):
        r = requests.get(cls.token_url,
                         params={
                             "corpid": cls.corpid,
                             "corpsecret": secret
                         })
        cls.format(r)
        assert r.json()["errcode"] == 0
        return r.json()


