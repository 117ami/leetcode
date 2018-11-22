#!/bin/bash 
account=($(awk '{print $1}' /usr/local/info/credential.dat))

expect -c "set timeout 3
spawn leetcode user -l 
expect \"login:\"
send \"${account[0]}\r\"
expect \"pass:\"
send \"${account[1]}\r\"
interact
"

