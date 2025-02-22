#!/usr/bin/python3
# @Time    : 2019-09-26
# @Author  : Kevin Kong (kfx2007@163.com)

from .core import Core
import json


class Sms(Core):

    def sendSms(self, phone, sign, code, params, outid=None, extendcode=None, signature=None, timestamp=None):
        """
        发送短信
        """

        data = self._get_data(signature=signature, timestamp=timestamp)
        data.update({
            "PhoneNumbers": phone,
            "SignName": sign,
            "TemplateCode": code,
            "TemplateParam": json.dumps(params, separators=(',', ':')),
            "AccessKeyId": self.key,
            "OutId": outid,
            "SmsUpExtendCode": extendcode,
            "Action": "SendSms"
        })
        
        return self.get(data)