# UnitTestServer
单元测试服务器    
python3.5.3 + django1.11.5    
在原协议测试服务器的基础上进行的开发，本服务器遵循简单粗暴法则，快速生成要测试内容。后期再考虑将成果合并到协议测试服务器中

# 创建步骤
python -m django --version
django-admin startproject UnitTestServer
cd UnitTestServer
python manage.py startapp autotrade

# 完成内容：
v0.01 读取json配置文件（此json文件兼容postman导出的配置文件），生成访问列表。

# 计划
生成一张规则配置表，在基础配置的基础上完成关联测试。
关联规则是个难点，还要构思中




