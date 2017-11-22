#!/bin/bash
netstat -nlpt > a.dmeo

#pid=`cat a.dmeo |grep 8000|awk '{print $7}'|awk -F"/" '{print $1}' >/dev/null 2>log&`
#kill -9 $pid >/dev/null 2>log &
#rm -rf a.dmeo
