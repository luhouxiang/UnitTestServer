##########
二、智能逆回购
##########

* 智能逆回购定制::
请求:        
	URL：http://192.168.5.252:31800/api/autotrade/order

包体:: 以上请求包体数据采用json格式，具体如下：  

+------------+------------+-----------+------------+-------------------------------------------+
| Header 1   | Header 2   | Header 3  |  Header 4  |           Header 5                        |
+============+============+===========+============+===========================================|
| body row 1 | column 2   | column 3  |   column 4 |           column 5                        |
+------------+------------+-----------+------------+-------------------------------------------+


作者：seayxu
链接：http://www.jianshu.com/p/1885d5570b37
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。





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

