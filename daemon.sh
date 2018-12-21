#!/bin/bash

st=$1
: ${st:=1800} # Default sleep time is 30 minutes 
while :; do
	echo "" > nohup.out
	nohup python3 daily_submit.py &
	pid=$!
	sleep $st
	kill -9 $pid 
done

# bash test.sh &
# pid=$!
# echo $!

# sleep_time=$1
# : ${sleep_time:=3}
# sleep $sleep_time

# echo $pid
