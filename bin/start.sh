#!/bin/bash
# export PYTHON_HOME=/opt/kds/anaconda3/envs/python3.5.3
# export SERVER_HOME=/opt/kds/mobile-stock/UnitTestServer
nohup python ../manage.py runserver 0.0.0.0:8000 >/dev/null 2>log  &
PIDS=$!
echo $PIDS > UnitTestServer.pid

if [ `ps -fP $PIDS | wc -l` -gt 1 ]
then echo "UnitTestServer: 服务已启动"
else echo "UnitTestServer: 服务启动失败"
fi
