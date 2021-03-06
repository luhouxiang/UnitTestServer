#!/usr/bin/evn python3
# -*- encoding: utf-8 -*-

# 针对web端json协议的通信库，通信协议为json,传出的data为json格式，接收的数据也是json格式
# 外界调用时可先初始化web_json类，如下所示：
# get调用
# web = WebJson("http://baidu.com/")
# params = "abcd/select/100000?userID=1234&groupID=79"
# web.get(params)
# 
# post调用
# web = WebJson("http://baidu.com/")
# params = "abcd/select/100000"
# data = '{"name": "jack", "id": "1"}'
# web.post(params, data)

# from urllib.request import urlopen
import json
import ssl
import requests

class WebJson(object):
    def __init__(self):
        pass

    @classmethod
    def get_url_json(cls, url, data, method):
        ssl._create_default_https_context = ssl._create_unverified_context # 解决https的认证问题
        response = None
        if method == "GET":
            response = requests.get(url)
        else:
            response = requests.post(url, data)

        print(url)
        print("status: ", response.status_code)
        res_text = response.content.decode()
        json_data = None
        try:
            json_data = json.loads(res_text)
        except:
            json_data = res_text
        # web = urlopen(url, data)
        # print(web.url)
        # print("status: ", web.status)
        # raw_text = web.read()
        # json_data = json.loads(raw_text.decode('utf8'))
        return json_data

    @classmethod
    def parse_json(cls, json_data):
        json_text = json.dumps(json_data, sort_keys=False, ensure_ascii=False, indent=2)
        return json_text

    @classmethod
    def get_url_data(cls, url, data, method):
        """
        :param url:
        :param data:
        :return:
        """
        json_data = cls.get_url_json(url, data, method)
        json_text = cls.parse_json(json_data)
        print(json_text)
        return json_text

    @classmethod
    def get(cls, url):
        return cls.get_url_data(url, None, "GET")
    
    @classmethod
    def post(cls, url, data):
        data = bytes(data, 'utf8')
        return cls.get_url_data(url, data, "POST")


if __name__ == '__main__':
    rawtext = '{"name":"jack", "value":"1"}'
    json_str = json.loads(rawtext) 
    str_list = []
    str_data = None
    if isinstance(json_str, dict):
        for item in json_str:
            str_list.append(item+"="+json_str[item])
            print("key:", item,", value:" ,json_str[item])
    if len(str_list) != 0:
        str_data = "&".join(str_list)
    print(str_data)
    print(len(str_data))
    # print(len(None))
