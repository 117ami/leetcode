#!/bin/bash 

leetcode show $1 -gx -l cpp
leetcode show $1 -gx -l ruby
leetcode show $1 -gx -l python3
leetcode show $1 -gx -l javascript

pythonFile=$(ls -t *.py | head -n 1)
cppFile=$(ls -t *.cpp | head -n 1)

echo -e "\n\n
s = Solution()\n\n" | tee -a $pythonFile

echo -e "\n\n
static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();" | tee -a $cppFile

echo "
#include \"aux.cpp\"
#include \"$cppFile\"

int main(int argc, char const *argv[]) {
	Solution s;
	return 0;
}
" | tee test.cpp
