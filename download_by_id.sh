#!/bin/bash 

leetcode show $1 -gx -l cpp
leetcode show $1 -gx -l ruby
leetcode show $1 -gx -l python3
leetcode show $1 -gx -l javascript

cppFile=$(ls | grep cpp | grep -v 'aux')

echo "static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();

int main(int argc, char const *argv[]) {
	Solution s;
	return 0;
}
" >> $cppFile
