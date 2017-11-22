#!/bin/bash

pid=`cat UnitTestServer.pid`
ps -ef | grep -v grep | grep $pid
