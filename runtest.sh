#!/usr/local/bin/bash 

file=$1
if [[ "$file" == *. ]]; then 
    file="${file}py"
fi 

pythonTemp="temp.py"

echo "
from aux import * 
import collections
import functools
import bisect
" > $pythonTemp

cat $file >> $pythonTemp

/usr/local/bin/python3 $pythonTemp
