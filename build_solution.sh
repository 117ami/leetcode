#!/bin/bash
# using leetcode-cli to build solutions 
# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;36m'
PLAIN='\033[0m'

echo -e "${BLUE}USAGE: ./build-cli problem_id [language: c/cpp/ruby/python]${PLAIN}"
pid=$1
lan='ruby'
if [ $# -gt 1 ] ; then 
	lan=$2 
fi

# downloading file 
leetcode show $pid -g -l $lan 

# downloading description 
source=`ls -Art|tail -n 1`
echo "=begin" >> $source
leetcode show $pid >> $source
echo "=end" >> $source

# removing spaces 
sed -i "1irequire './aux.rb\'" $source
sed -i '/^\s*$/d' $source

