#!usr/bin/python3
# -*- encoding: utf-8 -*-
import uuid

class Util(object):
    def __init__(self):
        pass

    @classmethod
    def uuid_str(cls):
        """
        创建uuid,返回uuid字符串，类似如下字符串: "ebd56479-b39f-5a51-ad94-43fbc81f36be"
        :return:
        """
        return uuid.uuid1().__str__()
