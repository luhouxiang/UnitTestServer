#!/bin/bash
export PYTHON_HOME=/opt/kds/anaconda3/envs/python3.5.3
export SERVER_HOME=/opt/kds/mobile-stock/UnitTestServer
nohup $PYTHON_HOME/bin/python $SERVER_HOME/manage.py runserver 0.0.0.0:8000 >/dev/null 2>log  &
PIDS=$!
echo $PIDS
echo $PIDS > $SERVER_HOME/bin/UnitTestServer.pid
