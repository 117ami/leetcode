#!/bin/bash
 cat file.txt | tr -s ' ' '\n' | sort | uniq -c | sort | awk '{print $2, $1}'
