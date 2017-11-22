#!/bin/bash

pid=`netstat -nlpt | grep 8000 | awk '{print $7}' | awk -F"/" '{print $1}'`
kill -9 $pid >/dev/null 2>log &
