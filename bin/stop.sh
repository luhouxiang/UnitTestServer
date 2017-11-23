#!/bin/bash

pid=`cat UnitTestServer.pid` 

for p_pid in `ps -ef |grep $pid|grep -v grep | awk '{print $2}'`
do
	pkill -9 -P $p_pid
done

if [ `ps -fP $pid | wc -l` -gt 1 ]
then echo "UnitTestServer: 服务停止失败"
else echo "UnitTestServer: 服务已停止"                                                                                           
fi
