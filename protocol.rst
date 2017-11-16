=========
智能逆回购
=========

********
1、智能逆回购定制
********
* 请求方式: post
* URL：http://192.168.5.252:31800/api/autotrade/order
* 参数说明

===============  ================  ==========  =========  ===========================================
     标识              名称          类型       是否必要      备注
===============  ================  ==========  =========  ===========================================
identifier       用户标识符         string      Y          客户号
appType          手机类型           string      Y    
orderChannel     渠道号             string      Y
orderType        订阅类型           string      Y          1:订阅，2：暂停，3：修改，4：恢复
serviceId        服务类型           string      Y          8002：表示国债逆回购
yybdm            营业部代码         string      Y          
lhxx             留痕信息           string      Y          auto.***
zjzh             资金账号           stirng      Y
order            订阅数据           数组          
---------------  ----------------  ----------  ---------  -------------------------------------------
gddm             股东代码           string
marketId         市场代码           string
orderDate        订阅日期           string                 2017-11-14
orderStartTime   开始时段           string                 14:30:00
orderEndTime     结束时段           string                 22:00:00
stockCode        代码              string                
stockName        名称              string
discription      中文说明          string
price            利率              string
orderAmount      金额              string
endDate          截止日期           string                 2017-11-14
===============  ================  ==========  =========  ===========================================

* 定制
::
 
 http://172.16.239.239:21800/api/autotrade/reverse_order
 {
   "identifier" : "101500000010",
   "appType" : "1",
   "orderChannel" : "1",
   "orderType" : "1",
   "serviceId" : "8002",
   "yybdm" : "1031",
   "lhxx" : "auto.lhxx",
   "zjzh" : "101500000010",
   "order" : [
      {
         "gddm" : "A231941760",
         "marketId" : "0",
         "orderDate" : "2017-11-14",
         "orderStartTime" : "14:30:00",
         "orderEndTime" : "22:00:00",
         "stockCode" : "131810",
         "stockName" : "R－001",
         "discription":"一天期",
         "price" : "0.01",
         "orderAmount" : "10000.00",
         "endDate" : "2017-11-30"
      }
   ]
}





********
Features
********

* hierarchical pages
* extensive built-in support for multilingual websites
* multi-site support
* draft/publish workflows
* version control
* a sophisticated publishing architecture, that's also usable in your own applications
* frontend content editing
* a hierarchical content structure for nested plugins
* an extensible navigation system that your own applications can hook into
* SEO-friendly URLs
* designed to integrate thoroughly into other applications


***********
Quick Start
***********

You can use the `django CMS installer <https://djangocms-installer.readthedocs.io>`_::

    $ pip install --upgrade virtualenv
    $ virtualenv env
    $ source env/bin/activate
    (env) $ pip install djangocms-installer
    (env) $ mkdir myproject && cd myproject
    (env) $ djangocms -f -p . my_demo
    (env) $ python manage.py


************
Getting Help
************

Please head over to our IRC channel, #django-cms, on irc.freenode.net or write
to our `mailing list <https://groups.google.com/forum/#!forum/django-cms>`_.

