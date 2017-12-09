#!usr/bin/python3
# -*- encoding: utf-8 -*-
import uuid
import time

class Util(object):
    def __init__(self):
        pass

    @classmethod
    def new_uuid_str(cls):
        """
        创建uuid,返回uuid字符串，类似如下字符串: "ebd56479-b39f-5a51-ad94-43fbc81f36be"
        :return:
        """
        return uuid.uuid1().__str__()

    @classmethod
    def new_request_item(cls):
        item = dict()
        item["preRequestScript"] = None
        item["currentHelper"] = "normal"
        item["data"] = []
        item["time"] = str(int(time.time()))
        item["pathVariables"] = dict()
        item["tests"] = None
        item["headers"] = "Content-Type: application/json\n",
        item["queryParams"] = []
        item["responses"] = ""
        item["dataMode"] = "raw"
        item["helperAttributes"] = dict()
        item["headerData"] = []
        item["pathVariableData"] = []

        # 以下内容应该是由客户端上传与之合并
        item["id"] = Util.new_uuid_str()  # 生成新的uuid
        item["name"] = ""
        item["method"] = ""
        item["url"] = ""
        item["rawModeData"] = ""
        item["description"] = ""
        item["folder"] = ""
        item["collectionId"] = ""
        return item

    @classmethod
    def new_folder_item(cls):
        item = dict()
        # 以下内容应该是由客户端上传与之合并
        item["id"] = Util.new_uuid_str()  # 生成新的uuid
        item["owner"] = ""
        item["order"] = []
        item["folders_order"] = []
        item["description"] = ""
        item["name"] = ""
        item["collectionId"] = ""
        return item









