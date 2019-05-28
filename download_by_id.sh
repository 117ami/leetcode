#!/bin/bash 

leetcode show $1 -gx -l cpp
leetcode show $1 -gx -l ruby
leetcode show $1 -gx -l python3
leetcode show $1 -gx -l javascript

js_file=$(ls -t *.js | head -n 1)
python_file=$(ls -t *.py | head -n 1)
cpp_file=$(ls -t *.cpp | head -n 1)

# echo -e "
# var print = function(a) {
# 	console.log(a);
# } " | tee -a $js_file
cat aux.js | tee -a $js_file

echo -e "\n\n
s = Solution()\n\n" | tee -a $python_file

# echo -e "\n\n
# static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();" | tee -a $cpp_file

echo "
#include \"aux.cpp\"
#include \"c.cpp\"
#include \"$cpp_file\"

int main(int argc, char const *argv[]) {
	Solution s;
	return 0;
}
" | tee test.cpp
