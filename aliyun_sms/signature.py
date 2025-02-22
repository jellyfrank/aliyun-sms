#!/usr/bin/python3
# @Time    : 2025-02-22
# @Author  : Kevin Kong (kfx2007@163.com)

from .core import Core
from datetime import datetime


class Signature(Core):
    def getSiginatureList(self, index=0, size=10):
        """
        获取签名
        """
        data = {
            "AccessKeyId": self.key,
            "Action": "QuerySmsSignList",
            # "SignatureMethod": "HMAC-SHA1",
            "Timestamp": datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%SZ"),
            "SignatureVersion": "1.0",
            "Version": "2017-05-25",
        }
        return self.get(data)
