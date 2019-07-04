#!/bin/bash

submit() {
	random_file=$(ls solutions | shuf -n 1)
	tmp=$random_file
	random_file=${random_file/\_/\.}
	cp solutions/$tmp /tmp/$random_file
	leetcode submit /tmp/$random_file
}

while :; 
do 
	submit()
	sleep $(($RANDOM % 180+1))
done

