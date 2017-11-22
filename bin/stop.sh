#!/bin/bash

#`./.stop.sh > /dev/null 2> log`
pid=`cat UnitTestServer.pid` 
echo $pid

for p_pid in `ps -ef |grep $pid|grep -v grep | awk '{print $2}'`
do
	echo $p_pid
	pkill -9 -P $p_pid
done
