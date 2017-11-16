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
     标识              名称          类型        是否必要     备注
===============  ================  ==========  =========  ===========================================
identifier       用户标识符         string      Y          客户号
===============  ================  ==========  =========  ===========================================

* 定制(
::
 
 http://172.16.239.239:21800/api/autotrade/reverse_order
 {
   "appType" : "1",
   "identifier" : "101500000010",
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

