#!/usr/bin/python3
# @Time    : 2025-02-22
# @Author  : Kevin Kong (kfx2007@163.com)

from datetime import datetime
import uuid
from hashlib import sha1
import hmac
import base64
import urllib.parse
import json
import requests

URL = "https://dysmsapi.aliyuncs.com"


class Core(object):
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def _get_data(self, signature=None, timestamp=None):
        """
        获取参数
        """
        data = {
            "AccessKeyId": self.key,
            "Format": "JSON",
            "RegionId": "cn-qingdao",
            "SignatureMethod": "HMAC-SHA1",
            "SignatureNonce": signature if signature else str(uuid.uuid1()),
            "SignatureVersion": "1.0",
            "Timestamp": timestamp
            if timestamp
            else datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%SZ"),
            "Version": "2017-05-25",
        }

        return data

    def get_to_sign(self, data):
        return "&".join(
            "{}={}".format(key, urllib.parse.quote(data[key].encode("utf-8"), safe=""))
            for key in sorted(data.keys())
            if data[key]
        )

    def sign(self, data):
        """
        签名算法
        """
        ss = "GET&{}&{}".format(
            urllib.parse.quote("/",safe=""), urllib.parse.quote(self.get_to_sign(data), safe="")
        )
        hashstr = hmac.new(
            "{}&".format(self.secret).encode("utf-8"), ss.encode("utf-8"), sha1
        ).digest()
        return base64.b64encode(hashstr).decode("utf-8")

    def get(self, data):
        """
        发送请求
        """
        signature = self.get_to_sign(data)
        sign = self.sign(data)
        data["Signature"] = sign
        url = URL + "/?" + urllib.parse.urlencode(data)
        # 使用http get发送请求
        url = "{}/?Signature={}&{}".format(URL, urllib.parse.quote(sign), signature)
        res = requests.get(url).json()
        return res
