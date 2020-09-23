#!/bin/bash 
comments=$@
echo '*' `date +"%a %D/%T":` $comments | tee -a c.log 
readme='/dev/null'

echo '
README
============================== 
存放leetcode(www.leetcode.com) 上的问题解法代码，主力语言Ruby, 偶而使用C++, Python。 

***** 
|Author|@GaoangLiu|
|:---  |:---
|E-mail|GaoangLau@gmail.com

### Log: 
```' > $readme

cat c.log >> $readme
echo '```' >> $readme 

# auto update README.md
python3 scripts/auto_add_log.py 

git add .
git commit -m "$comments"
git push 