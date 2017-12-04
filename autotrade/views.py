#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from web_json import WebJson
from json_conf import JsonConf
from django.conf import settings
import json

def index(request):
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
        print("打印send: ", url)
        method = request.POST.get('method')
        if 'GET' == method:
            data = web.get(url)
        else:
            raw_mode_data = request.POST.get('rawModeData')
            data = web.post(url, raw_mode_data)
        return HttpResponse(data)

def save(request):
    """
    数据保存模块
    :param request:
    :return:
    """
    if request.method == 'POST':
        web = WebJson()
        id = request.POST.get('id')
        name = request.POST.get('name')
        url = request.POST.get('url')
        raw_mode_data = request.POST.get('rawModeData')
        print("打印send: ", url)
        method = request.POST.get('method')
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




