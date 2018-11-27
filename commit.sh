#!/bin/bash 
comments=$1
echo '*' `date +"%a %D/%T":` $comments | tee -a c.log 
readme='README.md'

echo '
README
============================== 
存放leetcode(www.leetcode.com) 上的问题解法代码，主力语言Ruby, 偶而使用C++, Python。 

***** 
|Author|@ssrzz|
|:---  |:---
|E-mail|ssrzz@pm.me

### Log: 
```' > $readme

cat c.log >> $readme
echo '```' >> $readme 

git add .
git commit -m "$comments"
git push 