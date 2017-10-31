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

    @staticmethod
    def store(file_name, data):
        with open(file_name, 'w') as json_file:
            json_file.write(json.dumps(data, indent=4))

    @staticmethod
    def load(file_name):
        if not os.path.exists(file_name):
            with open(file_name, 'w', encoding="utf-8") as json_file:
                pass
        with open(file_name, encoding="utf-8") as json_file:
            try:
                data = json.load(json_file)
            except:
                data = {}
            return data

    @staticmethod
    def set(file_name, data_dict):
        json_obj = JsonConf.load()
        for key in data_dict:
            json_obj[key] = data_dict[key]
        JsonConf.store(file_name, json_obj)
        print(json.dumps(json_obj, indent=4))


if __name__ == "__main__":
    data = {"a": " 1", "f": "100", "b": "3000"}
    JsonConf.set(data)