#!/bin/bash 

prepro() {
    op=$(leetcode show $1 -gx -l cpp)	
    if [[ $op =~ "ERROR" ]]; then 
    	echo $op
		echo "Refreshing cache may help resolving this problem [leetcode cache -d]."
		exit 1
    else
		leetcode show $1 -gx -l python3
		# leetcode show $1 -gx -l javascript
    fi
}

prepro $@

js_file=$(ls -t *.js | head -n 1)
python_file=$(ls -t *.py | head -n 1)
ruby_file=$(ls -t *.rb | head -n 1)
cpp_file=$(ls -t *.cpp | head -n 1)

# echo -e "
# var print = function(a) {
# 	console.log(a);
# } " | tee -a $js_file
# cat aux.js | tee -a $js_file

# cat aux.js > tmpjs
# cat $js_file >> tmpjs
# mv tmpjs $js_file

cat c.cpp > tmpcpp
cat $cpp_file >> tmpcpp
mv tmpcpp $cpp_file

# cat aux.py > tmppy
# cat $python_file >> tmppy
# mv tmppy $python_file

echo -e "
from collections import defaultdict, Counter, 
s = Solution()\n\n" | tee -a $python_file

echo -e "\n\n
static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();" | tee -a $cpp_file

# cat c.cpp > t.cpp
# cat $cpp_file >> t.cpp 
# mv t.cpp $cpp_file

echo "
#include \"aux.cpp\"
#include \"$cpp_file\"

int main(int argc, char const *argv[]) {
	Solution s;
	return 0;
}
" | tee test.cpp
