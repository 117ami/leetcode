
#include "aux.cpp"
#include "76.minimum-window-substring.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string ss = "ADOBECODEBANC", t = "ABC"; 
	ss = "abc", t = "cba";
	say(s.minWindow(ss, t));
	return 0;
}

