# 2017-11-23 
当前可在网页上完成协议测试，修改并保存（但不可额外增加数据并保存）
增加bin目录，其中start.sh,status.sh,stop.sh可完成程序启动，停止，检测状态
在/etc/rc.d/rc.local中加入以下语句：
export KDS_MOBILE_STOCK_HOME=/opt/kds/mobile-stock    
su - kds -c $KDS_MOBILE_STOCK_HOME/UnitTestServer/bin/start.sh    
即可在系统启动时使用kds用户启动此web程序



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




