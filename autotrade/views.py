from django.http import HttpResponse
from django.shortcuts import render
from web_json import WebJson
from account_info import AccountInfo

def index(request):
    return render(request, 'index.html')

def send(request):
    """
    数据发送模块
    :param request:
    :return:
    """
    if request.method == 'POST':
        web = WebJson()
        url = request.POST.get('inputurl')
        print("打印send: ", url)
        method = request.POST.get('method')
        if 'GET' == method:
            data = web.get(url)
        else:
            postdata = request.POST.get('postdata')
            data = web.post(url, postdata)
        return HttpResponse(data)

def login(request):
    """
    用户登录
    :param request:
    :return:
    """
    web = WebJson()
    url = request.POST.get('inputurl')
    postdata = request.POST.get('postdata')
    data = bytes(postdata, 'utf8')
    json = web.get_url_json(url, data)
    try:
        AccountInfo.zjzh = json["dlxx"][0]["zjzh"]
        AccountInfo.hkdm = json["dlxx"][0]["khdm"]
        AccountInfo.yybdm = json["dlxx"][0]["yybdm"]
        for item in json["gdlb"]:
            gddm = dict()
            gddm["gddm"] = item["gddm"]
            gddm["jysdm"] = item["jysdm"]
            AccountInfo.gdlb[item["jysdm"]] = gddm
    except Exception as err:
        print(err)
    finally:
        return HttpResponse(web.parse_json(json))




