# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:zdhpython
# File_name:dingding.py
# Author: gl
# Time:2020年09月04日
import json
import requests

def message(link=1):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=0e064544823d1a0efd0e4126fefff6d82c4b30516cb5052aa1d880e7c5dce488'
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": "：%s " % ('巴啦啦能量')
        },
        "at":{
            "atMobiles":[
                "17739023982"       #需要填写自己的手机号，钉钉通过手机号@对应人
            ],
            "isAtAll": False     #是否@所有人，默认否
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(url, data=json.dumps(pagrem), headers=headers)

if __name__ == "__main__":
    message()









