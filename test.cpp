
#include "aux.cpp"
#include "c.cpp"
#include "890.find-and-replace-pattern.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vs words = {"abc","deq","mee","aqq","dkd","ccc"}; 
	string pattern = "abb"; 
	vs res = s.findAndReplacePattern(words, pattern); 
	say(res);
	return 0;
}

