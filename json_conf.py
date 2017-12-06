#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
json配置文件类，调用方法
data_dict = {"a":"1", "b":"2"}
JsonConf.set(data_dict)
即可在当前目录下生成json文件：config.json
'''
import json
import os


class JsonConf:
    """
    json配置文件类
    """
    json_data = {}

    @staticmethod
    def store2(file_name, datas):
        with open(file_name, 'w', encoding="utf-8") as json_file:
            tmp = json.dumps(datas, ensure_ascii=False, indent=4)
            json_file.write(tmp)

    @staticmethod
    def store(file_name):
        JsonConf.store2(file_name, JsonConf.json_data)

    @staticmethod
    def load(file_name):
        if not os.path.exists(file_name):
            with open(file_name, 'w', encoding="utf-8") as json_file:
                pass
        with open(file_name, encoding="utf-8") as json_file:
            try:
                JsonConf.json_data = json.load(json_file)
            except:
                JsonConf.json_data = {}
            return JsonConf.json_data

    @staticmethod
    def set(file_name, data_dict):
        json_obj = JsonConf.load(file_name)
        for key in data_dict:
            json_obj[key] = data_dict[key]
        JsonConf.store2(file_name, json_obj)
        print(json.dumps(json_obj, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    # data = {"a": " 1", "f": "100", "b": "3000"}
    # JsonConf.set("mytest.json", data)
    pass
