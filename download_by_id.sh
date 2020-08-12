#!/bin/bash 

prepro() {
    op=$(proxychains4 leetcode show $1 -gx -l python3)	
    if [[ $op =~ "ERROR" ]]; then 
    	echo $op
		echo "Refreshing cache may help resolving this problem [leetcode cache -d]."
	fi 
	# proxychains4 leetcode show $1 -gx -l python3
	proxychains4 leetcode show $1 -gx -l cpp
}

prepro $@

# rust_file=$(ls -t *.rs | head -n 1)
# js_file=$(ls -t *.js | head -n 1)
python_file=$(ls -t *.py | head -n 1)
# ruby_file=$(ls -t *.rb | head -n 1)
cpp_file=$(ls -t *.cpp | head -n 1)

# echo -e "
# var print = function(a) {
# 	console.log(a);
# } " | tee -a $js_file
# cat aux.js | tee -a $js_file

# cat aux.js > tmpjs
# cat $js_file >> tmpjs
# mv tmpjs $js_file
# ================================================================= Python soluton file
echo -e "
sol = Solution()\n\n" | tee -a $python_file

/usr/local/bin/gsed -ie '1i from collections import Counter, defaultdict, OrderedDict, deque\
from bisect import bisect_left, bisect_right \
from functools import reduce, lru_cache \
from typing import List \
import itertools \
import math \
import heapq \
import string\
true = True\
false = False\
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007' $python_file

proxychains4 leetcode show $1 > tmp.file 
python3 scripts/add_inputs_to_solution_file.py $python_file >> $python_file
rm tmp.file 

# ================================================================= Rust soluton file
# cp $rust_file question.rs 
# echo -e "\n\npub struct Solution; " >> question.rs 
# cat aux.rs >> question.rs 

# method=$(cat $rust_file | grep fn | head -n 1 | awk '{print $3}' | cut -d "(" -f 1)
# echo "
# mod question; 

# // let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

# fn main(){
# 	println!(\"{:?}\", question::Solution::$method());
# }
# " > main.rs 


# ================================================================= C++ soluton file
# cat cpp/helper.cpp > tmpcpp
# cat $cpp_file >> tmpcpp
# mv tmpcpp $cpp_file

echo -e "\n\n
static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();" | tee -a $cpp_file


echo "
#include \"aux.cpp\"
#include \"$cpp_file\"

int main(int argc, char const *argv[]) {
	Solution s;
	return 0;
}
" | tee test.cpp

rm *.pye 

