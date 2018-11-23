#!/bin/bash 
cred=/usr/local/info/credential.dat 
if [ ! -f $cred ]; then 
	echo "File not found: $cred"
	exit
fi

account=($(awk '{print $1}' $cred))

expect -c "set timeout 3
spawn leetcode user -l 
expect \"login:\"
send \"${account[0]}\r\"
expect \"pass:\"
send \"${account[1]}\r\"
interact
"

