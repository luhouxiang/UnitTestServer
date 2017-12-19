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
    folder_id = jsons['folder']
    collection_id = jsons['collectionId']

    item = Util.new_request_item()
    item["folder"] = folder_id
    item["collectionId"] = collection_id
    item["method"] = method
    item["name"] = name
    request_list = JsonConf.json_data['requests']
    request_list.append(item)

    if collection_id == folder_id:
        JsonConf.json_data["order"].append(item["id"])
    else:
        folder_list = JsonConf.json_data['folders']
        for fd in folder_list:
            if fd["id"] == folder_id:
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
    parent_folder_id = jsons['parent_folderId']
    collection_id = jsons['collectionId']
    name = jsons['name']

    folder_list = JsonConf.json_data['folders']

    item = Util.new_folder_item()
    item["owner"] = owner
    item["collectionId"] = collection_id
    item["name"] = name
    folder_list.append(item)

    if collection_id == parent_folder_id:
        JsonConf.json_data["folders_order"].append(item["id"])
    else:
        for fd in folder_list:
            if fd["id"] == parent_folder_id:
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


def save_tree_state(request):
    """
    数据树状态
    :param request:
    :return:
    """
    if request.method == 'POST':
        # web = WebJson()
        is_folder = request.POST.get('is_folder')
        item_id = request.POST.get('id')
        expand = request.POST.get('expand')

        if is_folder == "1":
            folder_list = JsonConf.json_data['folders']
            if JsonConf.json_data['id'] == item_id:
                JsonConf.json_data["expand"] = expand
            else:
                for item in folder_list:
                    if item["id"] == item_id:
                        item["expand"] = expand
                        break
        else:
            request_list = JsonConf.json_data['requests']
            for item in request_list:
                if item["id"] == item_id:
                    item["expand"] = expand
                    break
        JsonConf.store(settings.INIT_DATA)
    return HttpResponse("保存成功.")


def save_tree_title(request):
    """
    数据树标题
    :param request:
    :return:
    """
    if request.method == 'POST':
        # web = WebJson()
        is_folder = request.POST.get('is_folder')
        item_id = request.POST.get('item_id')
        name = request.POST.get('title')

        if is_folder == "1":
            folder_list = JsonConf.json_data['folders']
            if JsonConf.json_data['id'] == item_id:
                JsonConf.json_data["name"] = name
            else:
                for item in folder_list:
                    if item["id"] == item_id:
                        item["name"] = name
                        break
        else:
            request_list = JsonConf.json_data['requests']
            for item in request_list:
                if item["id"] == item_id:
                    item["name"] = name
                    break
        JsonConf.store(settings.INIT_DATA)
    return HttpResponse("保存成功.")


def delete_item(request):
    """
    删除项目
    :param request:
    :return:
    """
    if request.method == 'POST':
        item_id = request.POST.get('itemId')
        folder_id = request.POST.get("folderId")
        collection_id = request.POST.get("collectionId")
        request_list = JsonConf.json_data['requests']
        # 删除request_list中的具体项
        for i, item in enumerate(request_list):
            if item["id"] == item_id:
                del request_list[i]
                break

        # 删除最顶端的Id
        if folder_id == collection_id:
            items = JsonConf.json_data["order"]
            for i, item in enumerate(items):
                if item == item_id:
                    del items[i]
        else:   # 删除对应文件夹中的Id
            items1 = JsonConf.json_data["folders"]
            for index1, item1 in enumerate(items1):
                if folder_id == item1["id"]:
                    items2 = item1["order"]
                    for index2, item2 in enumerate(items2):
                        if item2 == item_id:
                            del items2[index2]
        JsonConf.store(settings.INIT_DATA)
    return HttpResponse("删除项目成功.")

def collect_list(folder_id, folder_list, item_list):
    folders = JsonConf.json_data['folders']
    for fd in folders:
        if folder_id == fd["id"]:
            folder_list.append(folder_id)
            item_list.extend(fd["order"])
            for item in fd["folders_order"]:
                collect_list(item, folder_list, item_list)

def delete_folder(request):
    """
    删除项目
    :param request:
    :return:
    """
    if request.method != 'POST':
        return HttpResponse("数据异常.")

    folder_id = request.POST.get("folderId")
    folder_list = []
    item_list = []
    collect_list(folder_id, folder_list, item_list)

    data_list = JsonConf.json_data['folders_order']
    for fd1 in reversed(folder_list):
        for fd2 in reversed(data_list):
            if fd1 == fd2:
                folder_list.remove(fd1)
                data_list.remove(fd2)

    data_list = JsonConf.json_data['folders']
    for fd1 in reversed(folder_list):
        for fd2 in reversed(data_list):
            if fd1 == fd2["id"]:
                folder_list.remove(fd1)
                data_list.remove(fd2)

    data_list = JsonConf.json_data['order']
    for it1 in reversed(item_list):
        for it2 in reversed(data_list):
            if it1 == it2:
                item_list.remove(it1)
                data_list.remove(it2)

    data_list = JsonConf.json_data['requests']
    for it1 in reversed(item_list):
        for it2 in reversed(data_list):
            if it1 == it2["id"]:
                item_list.remove(it1)
                data_list.remove(it2)
    JsonConf.store(settings.INIT_DATA)
    return HttpResponse("保存成功.")
