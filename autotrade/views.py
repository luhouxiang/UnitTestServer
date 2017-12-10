#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from web_json import WebJson
from json_conf import JsonConf
from util import Util
from django.conf import settings
import json
from user_logbook import user_log as logger

def index(request):
    logger.info("index: 初始化文件：" + settings.INIT_DATA)
    print(settings.INIT_DATA)
    json_data = JsonConf.load(settings.INIT_DATA)
    return render(request, 'index.html', {'Dict': json.dumps(json_data)})

def send(request):
    """
    数据发送模块
    :param request:
    :return:
    """
    if request.method == 'POST':
        web = WebJson()
        url = request.POST.get('url')
        method = request.POST.get('method')
        raw_mode_data = request.POST.get('rawModeData')
        logger.info("send: " + "url: " + url + ", method: " + method + ", data: " + raw_mode_data)
        if 'GET' == method:
            data = web.get(url)
        else:
            data = web.post(url, raw_mode_data)
        return HttpResponse(data)


def save_new_item(request):
    """
    保存新增项
    算法：新生成item项，生成item的uuid,然后将uuid加入到对应folder的order列表中
    :param request:
    :return:
    """
    if request.method != 'POST':
        return HttpResponse("数据异常.")

    str_data = request.POST.get('jsons')
    logger.info("new_item: " + str_data)
    jsons = json.loads(str_data)
    name = jsons['name']
    method = jsons['method']
    folder = jsons['folder']
    collection_id = jsons['collectionId']

    item = Util.new_request_item()
    item["folder"] = folder
    item["collectionId"] = collection_id
    item["method"] = method
    item["name"] = name
    request_list = JsonConf.json_data['requests']
    request_list.append(item)

    folder_list = JsonConf.json_data['folders']
    for fd in folder_list:
        if fd["id"] == folder:
            fd["order"].append(item["id"])
            break
    JsonConf.store(settings.INIT_DATA)
    return HttpResponse("保存成功.")

def save_change_item(request):
    """
    保存改变项
    算法：在rquest_list中查找对应的uuid,找到后将数据更新其中
    :param request:
    :return:
    """
    if request.method != 'POST':
        return HttpResponse("数据异常.")

    str_data = request.POST.get('jsons')
    logger.info("change_item: " + str_data)
    jsons = json.loads(str_data)
    id = jsons['id']
    name = jsons['name']
    url = jsons['url']
    raw_mode_data = jsons['rawModeData']
    method = jsons['method']
    print("打印send: ", url)

    request_list = JsonConf.json_data['requests']

    for item in request_list:
        if id == item["id"]:
            item["method"] = method
            item["rawModeData"] = raw_mode_data
            item["name"] = name
            item["url"] = url
            break
    JsonConf.store(settings.INIT_DATA)

    return HttpResponse("保存成功.")

def save_new_folder(request):
    """
    保存新增文件夹
    算法：新生成文件夹，生成文件夹的uuid,然后将uuid加入到对应folder的folders_order列表中
    :param request:
    :return:
    """
    if request.method != 'POST':
        return HttpResponse("数据异常.")

    str_data = request.POST.get('jsons')
    logger.info("new_folder: " + str_data)
    jsons = json.loads(str_data)
    owner = jsons['owner']
    folder_id = jsons['folder']
    collection_id = jsons['collectionId']
    name = jsons['name']

    folder_list = JsonConf.json_data['folders']

    item = Util.new_folder_item()
    item["owner"] = owner
    item["collectionId"] = collection_id
    item["name"] = name
    folder_list.append(item)


    folder_list = JsonConf.json_data['folders']
    for fd in folder_list:
        if fd["id"] == folder_id:
            fd["folders_order"].append(item["id"])
            break

    JsonConf.store(settings.INIT_DATA)
    return HttpResponse(item["id"])

def save_change_folder(request):
    if request.method != 'POST':
        return HttpResponse("数据异常.")

    str_data = request.POST.get('jsons')
    logger.info("change_folder: " + str_data)
    jsons = json.loads(str_data)
    owner = jsons['owner']
    folder_id = jsons['folder']
    collection_id = jsons['collectionId']
    name = jsons['name']

    folder_list = JsonConf.json_data['folders']
    for item in folder_list:
        if item["id"] == folder_id:
            item["owner"] = owner
            item["collectionId"] = collection_id
            item["name"] = name
            break

    JsonConf.store(settings.INIT_DATA)
    return HttpResponse("保存成功.")

def save(request):
    """
    数据保存模块
    :param request:
    :return:
    """
    if request.method == 'POST':
        # web = WebJson()
        str_data = request.POST.get('jsons')
        jsons = json.loads(str_data)
        id = jsons['id']
        name = jsons['name']
        url = jsons['url']
        raw_mode_data = jsons['rawModeData']
        method = jsons['method']
        folder = jsons['folder']
        collection_id = jsons['collectionId']
        print("打印send: ", url)

        request_list = JsonConf.json_data['requests']
        folder_list = JsonConf.json_data['folders']

        if id == '':
            item = Util.new_request_item()
            item["folder"] = folder
            item["collectionId"] = collection_id
            item["method"] = method
            item["rawModeData"] = raw_mode_data
            item["name"] = name
            item["url"] = url
            request_list.append(item)
            for fd in folder_list:
                if fd["id"] == folder:
                    fd["order"].append(item["id"])
                    break
        else:
            for item in request_list:
                if id == item["id"]:
                    item["method"] = method
                    item["rawModeData"] = raw_mode_data
                    item["name"] = name
                    item["url"] = url
                    break
        JsonConf.store(settings.INIT_DATA)

    return HttpResponse("保存成功.")




