#!/bin/bash
echo python协议测试UnitTestServer服务：
pid=`cat UnitTestServer.pid`
ps -ef | grep -v grep | grep $pid
