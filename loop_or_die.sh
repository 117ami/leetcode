#!/bin/bash

submit() {
	random_file=$(ls solutions | gshuf -n 1)
	tmp=$random_file
	random_file=${random_file/\_/\.}
	cp solutions/$tmp /tmp/$random_file
	leetcode submit /tmp/$random_file
}

while :; 
do 
	submit()
	sleep $(($RANDOM % 5+1))
done

