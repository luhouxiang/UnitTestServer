# UnitTestServer
单元测试服务器    
python3.5.3 + django1.11.5    
在原协议测试服务器的基础上进行的开发，本服务器遵循简单粗暴法则，快速生成要测试内容。后期再考虑将成果合并到协议测试服务器中

# 创建步骤
python -m django --version
django-admin startproject UnitTestServer
cd UnitTestServer
python manage.py startapp autotrade
