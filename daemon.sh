#!/bin/bash

while :; do
	echo "" > nohup.out
	nohup python3 daily_submit.py &
	pid=$!
	sleep 1800
	kill -9 $pid 
done

# bash test.sh &
# pid=$!
# echo $!
# sleep 1
# echo $pid
